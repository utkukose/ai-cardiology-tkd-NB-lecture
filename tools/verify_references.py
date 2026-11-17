"""Compare the references of the course with Crossref, DataCite and OpenAlex.

Usage: python tools/verify_references.py references/references.json

For every entry with a digital object identifier (DOI), the script looks up
the DOI in Crossref (or in DataCite for data sets and software published with
DataCite DOIs) and in OpenAlex. It compares the title, the year and the family
names of all authors with the entry. An entry can record a year that the
registry is known to list instead of the print year (registry_year), with the
reason (registry_note); the script then prints the reason as a note. Entries
without a DOI are checked for a reachable web address. The script exits with
code 1 if any entry does not match or cannot be checked.
"""
import difflib
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

HEADERS = {"User-Agent": "ai-cardiology-tkd-NB-lecture reference check (mailto:utkukose@sdu.edu.tr)"}
DATACITE_PREFIXES = ("10.13026/", "10.24432/", "10.48550/")


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


def norm(text):
    text = unicodedata.normalize("NFKD", text or "")
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


def author_problems(entry, primary):
    """Authors of the record missing from the entry, and authors of the entry missing from the record."""
    mine = [norm(a["family"]) for a in entry["authors"] if "family" in a]
    groups = [norm(a["literal"]) for a in entry["authors"] if "literal" in a]
    theirs = [norm(name) for name in primary["authors"] if norm(name)]
    if not mine or not theirs:
        return []
    out = []
    if mine[0] not in theirs[:3]:
        out.append(f"first author differs: {primary['authors'][0]}")
    missing = [name for name in theirs if name not in mine and name not in groups]
    extra = [name for name in mine if name not in theirs]
    if missing:
        out.append("in the record but not in the entry: " + ", ".join(missing))
    if extra:
        out.append("in the entry but not in the record: " + ", ".join(extra))
    return out


def check(entry):
    problems = []
    doi = entry.get("doi")
    if not doi:
        try:
            status, _ = fetch(entry["url"])
        except RuntimeError as err:
            if "403" in str(err) or "429" in str(err):
                print(f"[note] {entry['key']}: the site refuses automated requests; check it by hand")
                return []
            raise
        return [] if status < 400 else [f"web address returns {status}"]
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
