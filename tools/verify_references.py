"""Compare the references of the course with Crossref, DataCite and OpenAlex.

Usage: python tools/verify_references.py references/references.json

For every entry with a digital object identifier (DOI), the script looks up
the DOI in Crossref (or in DataCite for data sets and software published with
DataCite DOIs) and in OpenAlex. It compares the title, the year and the family
names of all authors with the entry. An entry can record a year that the
registry is known to list instead of the print year (registry_year), with the
reason (registry_note); the script then prints the reason as a note. In the same
way, an entry can explain an author list that the registry is known to give
differently (registry_authors_note). Members of a group author that the record
lists one by one are reported as a note. Entries
without a DOI are checked for a reachable web address. An address that returns
404 or 410, or whose host cannot be found, is a problem. A site that refuses or
does not answer an automated request (for example HTTP 401, 403, 429 or a
server error, or a timeout) is reported as a note, because such refusals are
often temporary; the page is then checked by hand. The script exits with code 1
if any entry does not match or if a DOI cannot be checked.
"""
import difflib
import html
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

HEADERS = {"User-Agent": "ai-cardiology-tkd-NB-lecture reference check (mailto:utkukose@sdu.edu.tr)"}
DATACITE_PREFIXES = ("10.13026/", "10.24432/", "10.4230/", "10.48550/", "10.5281/")


def fetch(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.status, resp.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return 404, ""
            err = e
        except Exception as e:  # network errors are retried
            err = e
        time.sleep(2 * (i + 1))
    raise RuntimeError(f"{url}: {err}")


LETTERS = str.maketrans({"ø": "o", "Ø": "O", "æ": "ae", "Æ": "AE", "ß": "ss", "ł": "l", "Ł": "L", "đ": "d", "Đ": "D", "ı": "i"})


def norm(text):
    text = html.unescape(text or "").translate(LETTERS)
    text = re.sub("['\u2019\u02bc`\u00b4]", "", text)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def similar(a, b):
    a, b = norm(a), norm(b)
    if not a or not b:
        return False
    return a in b or b in a or difflib.SequenceMatcher(None, a, b).ratio() >= 0.85


def from_crossref(doi):
    status, body = fetch("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    if status == 404:
        return None
    m = json.loads(body)["message"]
    year = None
    for key in ("published-print", "published-online", "issued", "published"):
        parts = (m.get(key) or {}).get("date-parts") or [[None]]
        if parts[0] and parts[0][0]:
            year = parts[0][0]
            break
    authors = [a.get("family") or a.get("name", "") for a in m.get("author", [])]
    title = (m.get("title") or [""])[0]
    return dict(title=title, year=year, authors=authors)


def from_datacite(doi):
    status, body = fetch("https://api.datacite.org/dois/" + urllib.parse.quote(doi))
    if status == 404:
        return None
    a = json.loads(body)["data"]["attributes"]
    authors = [c.get("familyName") or c.get("name", "") for c in a.get("creators", [])]
    title = (a.get("titles") or [{}])[0].get("title", "")
    return dict(title=title, year=a.get("publicationYear"), authors=authors)


def from_openalex(doi):
    status, body = fetch("https://api.openalex.org/works/https://doi.org/" + doi)
    if status == 404:
        return None
    w = json.loads(body)
    authors = [a["author"]["display_name"].split()[-1] for a in w.get("authorships", []) if a.get("author")]
    return dict(title=w.get("title") or "", year=w.get("publication_year"), authors=authors)


def same_person(a, b):
    """Two normalised family names match when the words of one begin or end the words of the other."""
    wa, wb = a.split(), b.split()
    if not wa or not wb:
        return False
    short, long_ = (wa, wb) if len(wa) <= len(wb) else (wb, wa)
    return long_[:len(short)] == short or long_[-len(short):] == short


def author_problems(entry, primary):
    """Authors of the record missing from the entry, and authors of the entry missing from the record."""
    mine = [norm(a["family"]) for a in entry["authors"] if "family" in a]
    groups = [a["literal"] for a in entry["authors"] if "literal" in a]
    theirs = [norm(name) for name in primary["authors"] if norm(name)]
    if not mine or not theirs:
        return []
    found = lambda name, pool: any(same_person(name, other) for other in pool)
    out = []
    if not found(mine[0], theirs[:3]):
        out.append(f"first author differs: {primary['authors'][0]}")
    extra = [name for name in mine if not found(name, theirs)]
    missing = [name for name in theirs if not found(name, mine) and not found(name, [norm(g) for g in groups])]
    if missing and groups and not extra and not out:
        print(f"[note] {entry['key']}: the record also lists {len(missing)} members of the {groups[0]} as authors")
        missing = []
    if missing:
        out.append("in the record but not in the entry: " + ", ".join(missing))
    if extra:
        out.append("in the entry but not in the record: " + ", ".join(extra))
    if out and entry.get("registry_authors_note"):
        print(f"[note] {entry['key']}: {entry['registry_authors_note']}")
        return []
    return out


GONE = re.compile(r"HTTP Error 410")
NO_HOST = re.compile(r"Name or service not known|nodename nor servname|getaddrinfo failed|No address associated")


def check_page(entry):
    """A web page without a DOI: a missing page or host is a problem, a refused or unanswered request is a note."""
    try:
        status, _ = fetch(entry["url"])
    except RuntimeError as err:
        if GONE.search(str(err)):
            return ["web address returns 410"]
        if NO_HOST.search(str(err)):
            return ["the host of the web address cannot be found"]
        reason = str(err).split(": ", 1)[-1]
        print(f"[note] {entry['key']}: the site refused or did not answer the automated request ({reason}); check the page by hand")
        return []
    return [] if status < 400 else [f"web address returns {status}"]


def check(entry):
    problems = []
    doi = entry.get("doi")
    if not doi:
        return check_page(entry)
    primary = from_datacite(doi) if doi.startswith(DATACITE_PREFIXES) else from_crossref(doi)
    if primary is None:
        return ["DOI not found"]
    if entry.get("title") and not similar(entry["title"], primary["title"]):
        problems.append(f"title differs: '{primary['title']}'")
    if primary.get("year") and abs(int(primary["year"]) - int(entry["year"])) > 1:
        if str(primary["year"]) == entry.get("registry_year"):
            print(f"[note] {entry['key']}: {entry['registry_note']}")
        else:
            problems.append(f"year differs: {primary['year']}")
    problems += author_problems(entry, primary)
    try:
        oa = from_openalex(doi)
        if oa and entry.get("title") and not similar(entry["title"], oa["title"]):
            if doi.startswith(DATACITE_PREFIXES):
                # OpenAlex joins the versions of a record (Zenodo); the DataCite record of the DOI decides
                print(f"[note] {entry['key']}: OpenAlex gives the title '{oa['title']}', DataCite the title of the reference")
            else:
                problems.append(f"OpenAlex title differs: '{oa['title']}'")
    except RuntimeError as e:
        problems.append(f"OpenAlex not reachable ({e})")
    return problems


def main(path):
    entries = json.load(open(path, encoding="utf-8"))
    failed = 0
    for e in entries:
        try:
            problems = check(e)
        except RuntimeError as err:
            problems = [f"could not be checked: {err}"]
        if problems:
            failed += 1
            print(f"[problem] {e['key']}: " + "; ".join(problems))
        else:
            print(f"[ok] {e['key']}")
        time.sleep(0.3)
    print(f"{len(entries) - failed} of {len(entries)} references match.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "references/references.json"))
