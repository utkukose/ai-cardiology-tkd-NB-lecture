"""Synthetic discharge summaries of the virtual clinic, in Turkish and English.

The report archive of Week 6. Every patient of the registry gets a discharge
summary written from his or her data: the complaint, the history, the ECG,
the echocardiogram, the laboratory values, the course in hospital and the
drugs at discharge. The summaries carry no list of diagnoses: Six chronic
diagnoses have to be found in the narrative, where they appear as terms,
abbreviations, misspellings, negations, family history, drugs and
laboratory values.

Hospital A writes in full sentences, in Turkish and, for the same patients,
in English; every random choice is shared by the two languages, so that the
two texts say the same. Hospital B, the external test set, writes in the
telegraphic Turkish style with (+) and (-) that many clinics use. Every
mention of a diagnosis, a drug or a procedure is annotated with its
character span, and every diagnosis with its assertion: present, negated or
family. The truth of the six diagnoses comes from the registry, so that
every method can be checked against it. The texts are synthetic teaching
material and not clinical documents.
"""
import hashlib

import numpy as np
import pandas as pd

from .cohort import make_cohort
from .coronary import TERRITORIES, angiography, category

LABELS = ("HF", "AF", "CAD", "HT", "DM", "CKD")
NAMES = {"HF": ("heart failure", "kalp yetersizliği"), "AF": ("atrial fibrillation", "atriyal fibrilasyon"),
         "CAD": ("coronary artery disease", "koroner arter hastalığı"), "HT": ("hypertension", "hipertansiyon"),
         "DM": ("diabetes mellitus", "diyabetes mellitus"), "CKD": ("chronic kidney disease", "kronik böbrek hastalığı")}
ENTITY_TYPES = ("DIAG", "DRUG", "PROC")
SPLITS = (("training", 1800), ("validation", 600), ("test", 600), ("external", 600))

# Terms of the six diagnoses, Turkish and English. The first term is the standard one.
TERMS = {
    "HF": (["kalp yetersizliği", "KY", "konjestif kalp yetmezliği", "KKY", "kalp yetmezliği", "kalp yetmezligi"],
           ["heart failure", "HF", "congestive heart failure", "CHF", "cardiac failure", "heart failiure"]),
    "AF": (["atriyal fibrilasyon", "AF", "paroksismal AF", "atrial fibrilasyon", "AFib", "atriyal fibrilasyon (AF)"],
           ["atrial fibrillation", "AF", "paroxysmal AF", "atrial fibrilation", "AFib", "atrial fibrillation (AF)"]),
    "CAD": (["koroner arter hastalığı", "KAH", "iskemik kalp hastalığı", "koroner arter hastaligi"],
            ["coronary artery disease", "CAD", "ischaemic heart disease", "coronary artery diesase"]),
    "HT": (["hipertansiyon", "HT", "esansiyel hipertansiyon", "hipertansyon"],
           ["hypertension", "HTN", "essential hypertension", "hypertention"]),
    "DM": (["tip 2 diyabetes mellitus", "DM", "tip 2 DM", "diyabet", "diyebet"],
           ["type 2 diabetes mellitus", "DM", "T2DM", "diabetes", "diabetis"]),
    "CKD": (["kronik böbrek hastalığı", "KBH", "kronik böbrek yetmezliği", "KBY"],
            ["chronic kidney disease", "CKD", "chronic renal failure", "CRF"]),
}
FAMILY_TERMS = {"CAD": (["koroner arter hastalığı", "erken yaşta miyokard enfarktüsü"], ["coronary artery disease", "premature myocardial infarction"]),
                "DM": (["diyabet"], ["diabetes"]), "HT": (["hipertansiyon"], ["hypertension"])}
RELATIVES = (["Babasında", "Annesinde", "Erkek kardeşinde", "Kız kardeşinde"], ["father", "mother", "brother", "sister"])

# Drugs: (Turkish name, English name, dose)
LOOP = ("furosemid", "furosemide", "40 mg")
MRA = ("spironolakton", "spironolactone", "25 mg")
ARNI = ("sakubitril/valsartan", "sacubitril/valsartan", "49/51 mg")
SGLT2 = [("dapagliflozin", "dapagliflozin", "10 mg"), ("empagliflozin", "empagliflozin", "10 mg")]
BB = [("bisoprolol", "bisoprolol", "5 mg"), ("metoprolol süksinat", "metoprolol succinate", "50 mg"), ("karvedilol", "carvedilol", "6,25 mg")]
OAC = [("apiksaban", "apixaban", "5 mg"), ("rivaroksaban", "rivaroxaban", "20 mg"), ("edoksaban", "edoxaban", "60 mg"), ("dabigatran", "dabigatran", "150 mg")]
DIGOXIN = ("digoksin", "digoxin", "0,25 mg")
ASA = ("asetilsalisilik asit", "acetylsalicylic acid", "100 mg")
P2Y12 = [("klopidogrel", "clopidogrel", "75 mg"), ("tikagrelor", "ticagrelor", "90 mg")]
STATIN = [("atorvastatin", "atorvastatin", "40 mg"), ("rosuvastatin", "rosuvastatin", "20 mg")]
RAS = [("ramipril", "ramipril", "5 mg"), ("perindopril", "perindopril", "5 mg"), ("valsartan", "valsartan", "160 mg"), ("kandesartan", "candesartan", "8 mg")]
OTHER_HT = [("amlodipin", "amlodipine", "5 mg"), ("hidroklorotiyazid", "hydrochlorothiazide", "12,5 mg")]
GLUCOSE = [("metformin", "metformin", "1000 mg"), ("gliklazid", "gliclazide", "60 mg"), ("insülin glarjin", "insulin glargine", "20 IU"),
           ("sitagliptin", "sitagliptin", "100 mg")]
PROCS = {"PCI": ("perkütan koroner girişim (PKG)", "percutaneous coronary intervention (PCI)"),
         "CAG": ("koroner anjiyografi", "coronary angiography"),
         "CABG": ("koroner arter baypas greftleme (KABG)", "coronary artery bypass grafting (CABG)"),
         "DCCV": ("elektriksel kardiyoversiyon", "electrical cardioversion"),
         "TTE": ("transtorasik ekokardiyografi", "transthoracic echocardiography")}


class Choices:
    """Random choices of one patient that do not depend on the language: each
    choice is drawn from its own stream, named by a key."""

    def __init__(self, seed, i):
        self.seed, self.i = seed, i

    def _rng(self, key):
        h = int(hashlib.md5(f"{self.seed}:{self.i}:{key}".encode()).hexdigest()[:12], 16)
        return np.random.default_rng(h)

    def random(self, key):
        return float(self._rng(key).random())

    def index(self, key, n, weights=None):
        r = self._rng(key)
        if weights is None:
            return int(r.integers(n))
        w = np.asarray(weights, dtype=float)
        return int(r.choice(n, p=w / w.sum()))

    def uniform(self, key, a, b):
        return float(self._rng(key).uniform(a, b))


def tr_upper(text):
    """Upper case by the rules of Turkish: i becomes İ and ı becomes I."""
    return text.replace("i", "İ").replace("ı", "I").upper()


class Doc:
    """A text that is written piece by piece and remembers the span of every entity."""

    def __init__(self, transform=None):
        self.parts, self.n, self.entities = [], 0, []
        self.transform = transform

    def add(self, text, label=None, assertion=None, code=None):
        if self.transform:
            text = self.transform(text)
        if label:
            self.entities.append(dict(start=self.n, end=self.n + len(text), label=label, assertion=assertion, code=code, text=text))
        self.parts.append(text)
        self.n += len(text)
        return self

    def text(self):
        return "".join(self.parts)


def _num_tr(x, nd=0):
    s = f"{x:,.{nd}f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".")


def _cap(s, tr=True):
    """The first letter in capitals; in Turkish, i becomes İ and ı becomes I."""
    first = s[:1]
    if tr:
        first = {"i": "İ", "ı": "I"}.get(first, first.upper())
    else:
        first = first.upper()
    return first + s[1:]


def _term(ch, key, code, lang, abbreviation=False):
    terms = TERMS[code][0 if lang == "tr" else 1]
    if abbreviation:
        abbr = [t for t in terms if t.upper() == t and len(t) <= 4]
        return abbr[ch.index(key, len(abbr))]
    return terms[ch.index(key, len(terms), [6.0] + [1.4] * (len(terms) - 1))]


def _facts(row, ch):
    """The six diagnoses of a patient, which of them the history names, and the drugs at discharge."""
    hf = row["main_diagnosis"] in ("HFrEF", "HFpEF")
    truth = dict(HF=int(hf), AF=int(row["af"]), CAD=int(row["cad"]), HT=int(row["hypertension"]), DM=int(row["diabetes"]),
                 CKD=int(row["egfr"] < 60))
    share = {"HF": 0.8, "AF": 0.75, "CAD": 0.85, "HT": 0.8, "DM": 0.8, "CKD": 0.45}
    named = {k: bool(v and ch.random("named" + k) < share[k]) for k, v in truth.items()}
    drugs = []
    if truth["HF"]:
        drugs.append(LOOP)
        if ch.random("mra") < 0.6:
            drugs.append(MRA)
        if row["main_diagnosis"] == "HFrEF":
            drugs.append(ARNI if ch.random("arni") < 0.6 else RAS[ch.index("acei", 2)])
        if ch.random("sglt2") < 0.6:
            drugs.append(SGLT2[ch.index("sglt2kind", 2)])
    if truth["HF"] or (truth["AF"] and ch.random("bbaf") < 0.7) or (truth["CAD"] and ch.random("bbcad") < 0.5):
        drugs.append(BB[ch.index("bb", 3)])
    if truth["AF"]:
        drugs.append(OAC[ch.index("oac", 4)])
        if ch.random("dig") < 0.15:
            drugs.append(DIGOXIN)
    if truth["CAD"] or (truth["DM"] and ch.random("asaprimary") < 0.25):
        drugs.append(ASA)
    if truth["CAD"]:
        if row["main_diagnosis"] == "ACS" or ch.random("p2y12") < 0.3:
            drugs.append(P2Y12[ch.index("p2y12kind", 2)])
    if truth["CAD"] or ch.random("statin") < 0.25:
        drugs.append(STATIN[ch.index("statinkind", 2)])
    if truth["HT"]:
        if ARNI not in drugs and not any(d in drugs for d in RAS):
            drugs.append(RAS[ch.index("ras", 4)])
        if ch.random("ht2") < 0.4:
            drugs.append(OTHER_HT[ch.index("ht2kind", 2)])
    if truth["DM"]:
        drugs.append(GLUCOSE[ch.index("glucose", 4)])
        if ch.random("sglt2dm") < 0.4 and not any(d in drugs for d in SGLT2):
            drugs.append(SGLT2[1])
    order = np.argsort([ch.random("order" + d[0]) for d in drugs])
    return truth, named, [drugs[k] for k in order]


def _summary_a(row, lang, ch, truth, named, drugs, angio=None):
    """Hospital A: full sentences."""
    tr = lang == "tr"
    d = Doc()
    age, female, diag = int(row["age"]), row["sex"] == "F", row["main_diagnosis"]
    complaints = {"ACS": ("göğüs ağrısı", "chest pain"), "HFrEF": ("nefes darlığı ve bacaklarda şişlik", "breathlessness and leg swelling"),
                  "HFpEF": ("eforla gelen nefes darlığı", "breathlessness on exertion"), "CCS": ("eforla gelen göğüs ağrısı", "chest pain on exertion")}
    others = [("çarpıntı", "palpitations"), ("baş dönmesi", "dizziness"), ("atipik göğüs ağrısı", "atypical chest pain")]
    complaint = complaints.get(diag) or others[ch.index("complaint", 3)]
    place = ("acil servise", "the emergency department") if diag in ("ACS", "HFrEF") else ("kardiyoloji polikliniğine", "the cardiology clinic")
    if tr:
        d.add(f"Öykü: {age} yaşında {'kadın' if female else 'erkek'} hasta, {complaint[0]} yakınmasıyla {place[0]} başvurdu. ")
    else:
        article = "An" if str(age)[0] == "8" or age in (11, 18) else "A"
        d.add(f"Presentation: {article} {age}-year-old {'woman' if female else 'man'} came to {place[1]} with {complaint[1]}. ")

    # history
    d.add("Özgeçmiş: " if tr else "History: ")
    items = sorted([k for k in LABELS if named[k]], key=lambda k: ch.random("item" + k))
    if items:
        for i, k in enumerate(items):
            if i:
                d.add(", " if i < len(items) - 1 else (" ve " if tr else " and "))
            if k == "CAD" and ch.random("mi") < 0.3:
                year = 2010 + ch.index("miyear", 14)
                if tr:
                    d.add(f"{year} yılında geçirilmiş ").add("miyokard enfarktüsü", "DIAG", "present", "CAD")
                else:
                    d.add("A " if i == 0 else "a ").add("myocardial infarction", "DIAG", "present", "CAD").add(f" in {year}")
                continue
            term = _term(ch, "term" + k, k, lang)
            d.add(_cap(term, tr) if i == 0 else term, "DIAG", "present", k)
        d.add(" öyküsü var. " if tr else ". ")
    else:
        d.add("Bilinen kronik hastalığı yok. " if tr else "No known chronic disease. ")
    for k in ("DM", "AF", "CAD", "HT"):
        if not truth[k] and ch.random("neg" + k) < 0.18:
            term = _term(ch, "negterm" + k, k, lang)
            if tr:
                d.add(_cap(term, tr), "DIAG", "negated", k).add([" öyküsü yok. ", " tanımlamıyor. ", " yok. "][ch.index("negform" + k, 3)])
            else:
                d.add(["No history of ", "Denies ", "No "][ch.index("negform" + k, 3)]).add(term, "DIAG", "negated", k).add(". ")
    if row["family_history"] and ch.random("family") < 0.8:
        k = list(FAMILY_TERMS)[ch.index("familykind", 3)]
        rel = ch.index("relative", 4)
        terms = FAMILY_TERMS[k][0 if tr else 1]
        term = terms[ch.index("familyterm", len(terms))]
        if tr:
            d.add(RELATIVES[0][rel] + " ").add(term, "DIAG", "family", k).add(" öyküsü var. ")
        else:
            d.add(f"Family history: {RELATIVES[1][rel]} with ").add(term, "DIAG", "family", k).add(". ")
    if row["smoker"]:
        d.add("Aktif sigara içicisi. " if tr else "Current smoker. ")
    if not truth["DM"] and ch.random("prediabetes") < 0.1:
        d.add("Prediyabet nedeniyle diyet önerildi. " if tr else "Dietary advice was given for prediabetes. ")

    # examination
    irregular = row["ecg_rhythm"] == "AF"
    hr = int(round(row["ecg_hr"] + (25 if irregular else 0)))
    if tr:
        d.add(f"Fizik muayene: TA {int(row['sbp'])}/{int(row['dbp'])} mmHg, nabız {hr}/dk, {'düzensiz' if irregular else 'ritmik'}. ")
        if diag == "HFrEF" or (diag == "HFpEF" and ch.random("congestion") < 0.5):
            d.add("Bazallerde raller ve bilateral pretibial ödem mevcut. ")
    else:
        d.add(f"Examination: BP {int(row['sbp'])}/{int(row['dbp'])} mmHg, pulse {hr}/min, {'irregular' if irregular else 'regular'}. ")
        if diag == "HFrEF" or (diag == "HFpEF" and ch.random("congestion") < 0.5):
            d.add("Basal crackles and bilateral ankle oedema. ")

    # ECG
    d.add("EKG: " if tr else "ECG: ")
    if irregular:
        if tr:
            d.add(f"Ventrikül hızı {hr}/dk olan ").add("atriyal fibrilasyon", "DIAG", "present", "AF").add(". ")
        else:
            d.add("Atrial fibrillation", "DIAG", "present", "AF").add(f" with a ventricular rate of {hr}/min. ")
    else:
        d.add(f"Sinüs ritmi, {int(row['ecg_hr'])}/dk. " if tr else f"Sinus rhythm, {int(row['ecg_hr'])}/min. ")
        if truth["AF"] and ch.random("holter") < 0.5:
            if tr:
                d.add("Holter kaydında paroksismal ").add("atriyal fibrilasyon", "DIAG", "present", "AF").add(" atakları izlendi. ")
            else:
                d.add("Holter monitoring showed episodes of paroxysmal ").add("atrial fibrillation", "DIAG", "present", "AF").add(". ")
        elif not truth["AF"] and ch.random("noaf") < 0.3:
            if tr:
                d.add("Atriyal fibrilasyon", "DIAG", "negated", "AF").add(" izlenmedi. ")
            else:
                d.add("No ").add("atrial fibrillation", "DIAG", "negated", "AF").add(". ")
    if row["stemi_territory"] != "none":
        terr = {"anterior": ("Anterior", "anterior"), "inferior": ("İnferior", "inferior"), "lateral": ("Lateral", "lateral")}[row["stemi_territory"]]
        d.add(f"{terr[0]} derivasyonlarda ST yükselmesi. " if tr else f"ST elevation in the {terr[1]} leads. ")

    # echocardiography
    ef = int(row["lvef"])
    if ch.random("tte") < 0.15:
        d.add(_cap(PROCS["TTE"][0 if tr else 1], tr), "PROC", None, "TTE").add(": ")
    else:
        d.add("Ekokardiyografi: " if tr else "Echocardiography: ")
    grade = 0 if ef < 30 else (1 if ef < 40 else (2 if ef < 50 else 3))
    if tr:
        d.add(f"Sol ventrikül ejeksiyon fraksiyonu %{ef}; sistolik fonksiyonlar {['ileri derecede bozuk', 'orta derecede bozuk', 'hafif bozuk', 'normal'][grade]}. ")
        if diag == "HFpEF":
            d.add("Diyastolik disfonksiyon ve sol atriyal genişleme mevcut. ")
    else:
        d.add(f"Left ventricular ejection fraction {ef}%, {['severely reduced', 'moderately reduced', 'mildly reduced', 'normal'][grade]} systolic function. ")
        if diag == "HFpEF":
            d.add("Diastolic dysfunction and left atrial enlargement. ")

    # laboratory
    hba1c = ch.uniform("hba1c", 7.0, 9.5) if truth["DM"] and ch.random("hba1cshown") < 0.6 else None
    if tr:
        d.add(f"Laboratuvar: NT-proBNP {_num_tr(row['ntprobnp'])} pg/mL, troponin {_num_tr(row['troponin'])} ng/L, "
              f"kreatinin {_num_tr(row['creatinine'], 2)} mg/dL, eGFR {int(row['egfr'])} mL/dk/1,73 m²")
        d.add(f", HbA1c %{_num_tr(hba1c, 1)}" if hba1c else "").add(f", LDL {int(row['ldl'])} mg/dL. ")
    else:
        d.add(f"Laboratory: NT-proBNP {row['ntprobnp']:,.0f} pg/mL, troponin {row['troponin']:,.0f} ng/L, "
              f"creatinine {row['creatinine']:.2f} mg/dL, eGFR {int(row['egfr'])} mL/min/1.73 m²")
        d.add(f", HbA1c {hba1c:.1f}%" if hba1c else "").add(f", LDL {int(row['ldl'])} mg/dL. ")

    # course in hospital
    d.add("Seyir: " if tr else "Course: ")
    if diag == "ACS":
        if tr:
            d.add("Akut koroner sendrom", "DIAG", "present", "CAD").add(" tanısıyla yapılan ").add(PROCS["CAG"][0], "PROC", None, "CAG")
            d.add("da ciddi darlık saptandı ve ").add(PROCS["PCI"][0], "PROC", None, "PCI").add(" uygulandı. ")
        else:
            d.add("Coronary angiography", "PROC", None, "CAG").add(" for ").add("acute coronary syndrome", "DIAG", "present", "CAD")
            d.add(" showed a severe stenosis, treated by ").add(PROCS["PCI"][1], "PROC", None, "PCI").add(". ")
    elif diag in ("HFrEF", "HFpEF"):
        if tr:
            d.add("Dekompanse ").add(["kalp yetersizliği", "kalp yetmezliği"][ch.index("hfcourse", 2)], "DIAG", "present", "HF")
            d.add(" nedeniyle intravenöz diüretik tedavisi verildi; ödemleri geriledi. ")
        else:
            d.add("Treated with intravenous diuretics for decompensated ").add(["heart failure", "cardiac failure"][ch.index("hfcourse", 2)], "DIAG", "present", "HF")
            d.add("; the oedema resolved. ")
    elif diag == "CCS":
        treatment = angio["treatment"] if angio is not None else "medical"
        if tr:
            d.add("Elektif ").add(PROCS["CAG"][0], "PROC", None, "CAG")
            if treatment == "PCI":
                d.add(" yapıldı; ").add(PROCS["PCI"][0], "PROC", None, "PCI").add(" ile stent yerleştirildi. ")
            elif treatment == "CABG":
                d.add("da çok damar hastalığı saptandı ve hasta ").add(PROCS["CABG"][0], "PROC", None, "CABG").add(" için kalp ve damar cerrahisine yönlendirildi. ")
            else:
                d.add(" sonrasında medikal tedavisi düzenlendi. ")
        else:
            d.add("Elective ").add("coronary angiography", "PROC", None, "CAG")
            if treatment == "PCI":
                d.add(" was followed by ").add(PROCS["PCI"][1], "PROC", None, "PCI").add(". ")
            elif treatment == "CABG":
                d.add(" showed multivessel disease, and the patient was referred to cardiac surgery for ").add(PROCS["CABG"][1], "PROC", None, "CABG").add(". ")
            else:
                d.add(" was followed by optimised medical treatment. ")
    elif complaint[1] == "atypical chest pain":
        if tr:
            d.add("Akut koroner sendrom", "DIAG", "negated", "CAD").add(" seri troponin ölçümleriyle dışlandı. ")
        else:
            d.add("Serial troponins ruled out ").add("acute coronary syndrome", "DIAG", "negated", "CAD").add(". ")
    elif complaint[1] == "palpitations":
        if ch.random("possibleaf") < 0.5:
            if tr:
                d.add("Paroksismal ").add("AF", "DIAG", "possible", "AF").add(" şüphesiyle 24 saatlik Holter kaydı planlandı. ")
            else:
                d.add("A 24-hour Holter recording was planned for suspected paroxysmal ").add("AF", "DIAG", "possible", "AF").add(". ")
        else:
            d.add("Holter kaydında anlamlı aritmi izlenmedi. " if tr else "Holter monitoring showed no significant arrhythmia. ")
    else:
        d.add("Ortostatik hipotansiyon düşünüldü; yakınmaları sıvı tedavisiyle geriledi. " if tr else "Orthostatic hypotension was suspected; the symptoms resolved with fluids. ")
    if irregular and ch.random("dccv") < 0.2:
        d.add(_cap(PROCS["DCCV"][0 if tr else 1], tr), "PROC", None, "DCCV").add(" ile sinüs ritmi sağlandı. " if tr else " restored sinus rhythm. ")

    # drugs
    d.add("Taburcu tedavisi: " if tr else "Discharge medication: ")
    for i, (name_tr, name_en, dose) in enumerate(drugs):
        if i:
            d.add(", ")
        d.add(name_tr if tr else name_en, "DRUG").add(" " + (dose if tr else dose.replace(",", ".")))
    d.add(". " if drugs else ("yok. " if tr else "none. "))
    d.add("Kardiyoloji polikliniği kontrolü önerildi." if tr else "Follow-up in the cardiology clinic.")
    return d


def _summary_b(row, ch, truth, named, drugs, angio=None):
    """Hospital B: telegraphic Turkish with (+) and (-)."""
    d = Doc()
    d.add(f"{int(row['age'])} Y {'K' if row['sex'] == 'F' else 'E'}. ÖZGEÇMİŞ: ")
    first = True
    for k in LABELS:
        if not ((truth[k] and named[k]) or (not truth[k] and ch.random("bneg" + k) < 0.55)):
            continue
        if not first:
            d.add(" ")
        first = False
        d.add(_term(ch, "bterm" + k, k, "tr", abbreviation=True), "DIAG", "present" if truth[k] else "negated", k)
        d.add(" (+)" if truth[k] else " (-)")
    d.add("özellik yok. " if first else ". ")
    if row["family_history"] and ch.random("bfamily") < 0.6:
        d.add("SOYGEÇMİŞ: babada ").add("KAH", "DIAG", "family", "CAD").add(". ")
    irregular = row["ecg_rhythm"] == "AF"
    hr = int(round(row["ecg_hr"] + (25 if irregular else 0)))
    d.add("EKG: ")
    if irregular:
        d.add("AF", "DIAG", "present", "AF").add(f", VH {hr}/dk. ")
    else:
        d.add(f"NSR, {int(row['ecg_hr'])}/dk. ")
    d.add(f"EKO: EF %{int(row['lvef'])}. ")
    d.add(f"LAB: kre {_num_tr(row['creatinine'], 2)}, eGFR {int(row['egfr'])}, NT-proBNP {_num_tr(row['ntprobnp'])}, trop {_num_tr(row['troponin'])}. ")
    diag = row["main_diagnosis"]
    if diag == "ACS":
        d.add("SEYİR: AKS, ").add("KAG", "PROC", None, "CAG").add(" + ").add("PKG", "PROC", None, "PCI").add(". ")
    elif diag in ("HFrEF", "HFpEF"):
        d.add("SEYİR: dekompanse ").add("KY", "DIAG", "present", "HF").add(", IV diüretik. ")
    elif diag == "CCS":
        treatment = angio["treatment"] if angio is not None else "medical"
        d.add("SEYİR: elektif ").add("KAG", "PROC", None, "CAG")
        if treatment == "PCI":
            d.add(" + ").add("PKG", "PROC", None, "PCI").add(". ")
        elif treatment == "CABG":
            d.add(", çok damar hastalığı, ").add("KABG", "PROC", None, "CABG").add(" için KVC'ye yönlendirildi. ")
        else:
            d.add(", medikal tedavi. ")
    d.add("İLAÇLAR: ")
    for i, (name_tr, _, dose) in enumerate(drugs):
        if i:
            d.add(", ")
        d.add(name_tr, "DRUG").add(" " + dose)
    d.add("." if drugs else "yok.")
    return d


def archive(seed=2026):
    """The report archive: one discharge summary per patient, 3,600 patients.

    Returns a table with patient_id, split (training, validation and test
    from hospital A; external from hospital B), text_tr, text_en (empty for
    hospital B), entities_tr and entities_en (lists of dictionaries with
    start, end, label, assertion, code and text), and one column of 0 and 1
    for each of the six diagnoses in LABELS.
    """
    cohort, angio, _ = _registry(seed)
    rows, start = [], 0
    for split, k in SPLITS:
        for i in range(start, start + k):
            row = cohort.iloc[i]
            ch = Choices(seed, i)
            truth, named, drugs = _facts(row, ch)
            a = angio.get(row["patient_id"])
            if split == "external":
                b = _summary_b(row, ch, truth, named, drugs, a)
                text_tr, ent_tr, text_en, ent_en = b.text(), b.entities, "", []
            else:
                a_tr, a_en = _summary_a(row, "tr", ch, truth, named, drugs, a), _summary_a(row, "en", ch, truth, named, drugs, a)
                text_tr, ent_tr, text_en, ent_en = a_tr.text(), a_tr.entities, a_en.text(), a_en.entities
            rows.append(dict(patient_id=row["patient_id"], split=split, text_tr=text_tr, text_en=text_en,
                             entities_tr=ent_tr, entities_en=ent_en, **truth))
        start += k
    return pd.DataFrame(rows)


_CACHE = {}


def _registry(seed):
    """The registry of the archive and its angiographies, computed once per seed."""
    if seed not in _CACHE:
        n = sum(k for _, k in SPLITS)
        cohort = make_cohort(n)
        pats, lesions = angiography(cohort, seed)
        info = {}
        for p in pats.to_dict("records"):
            p["lesions"] = lesions[lesions["patient_id"] == p["patient_id"]].to_dict("records")
            info[p["patient_id"]] = p
        _CACHE[seed] = (cohort, info, (pats, lesions))
    return _CACHE[seed]


# Names of the arteries in the angiography reports: (Turkish variants, English variants)
VESSEL_NAMES = {
    "LM": (["Sol ana koroner arter (LMCA)", "LMCA", "Sol ana koroner arter"], ["Left main coronary artery (LMCA)", "LMCA", "Left main"]),
    "LAD": (["Sol ön inen arter (LAD)", "LAD", "Sol ön inen arter"], ["Left anterior descending artery (LAD)", "LAD", "Left anterior descending"]),
    "LCX": (["Sirkumfleks arter (Cx)", "Cx", "Sirkumfleks arter", "LCx"], ["Left circumflex artery (LCx)", "LCx", "Circumflex artery", "Cx"]),
    "RCA": (["Sağ koroner arter (RCA)", "RCA", "Sağ koroner arter"], ["Right coronary artery (RCA)", "RCA", "Right coronary artery"]),
    "D1": (["Birinci diyagonal dal (D1)", "D1", "1. diyagonal dal"], ["First diagonal branch (D1)", "D1", "First diagonal"]),
    "D2": (["İkinci diyagonal dal (D2)", "D2", "2. diyagonal dal"], ["Second diagonal branch (D2)", "D2", "Second diagonal"]),
    "OM1": (["Birinci obtus marjinal dal (OM1)", "OM1", "1. obtus marjinal dal"], ["First obtuse marginal branch (OM1)", "OM1", "First obtuse marginal"]),
    "OM2": (["İkinci obtus marjinal dal (OM2)", "OM2", "2. obtus marjinal dal"], ["Second obtuse marginal branch (OM2)", "OM2", "Second obtuse marginal"]),
    "PDA": (["Arka inen arter (PDA)", "PDA", "Posterior desendan arter (PDA)"], ["Posterior descending artery (PDA)", "PDA", "Posterior descending artery"]),
}
# Names written without Turkish letters or with a spelling error, used now and then by hospital A
VESSEL_TYPOS = {"LAD": "Sol on inen arter", "LCX": "Sirkumflex arter", "RCA": "Sag koroner arter"}
SHORT_B = {"LM": "LMCA", "LAD": "LAD", "LCX": "CX", "RCA": "RCA", "D1": "D1", "D2": "D2", "OM1": "OM1", "OM2": "OM2", "PDA": "PDA"}
SEGMENT_NAMES = {
    "ostial": (["ostiyumunda", "ostiyal kesimde"], ["at the ostium", "at the ostium"]),
    "proximal": (["proksimal segmentte", "proksimalde", "proksimal kesimde"], ["in the proximal segment", "in the proximal third"]),
    "mid": (["orta segmentte", "mid segmentte", "orta kesimde"], ["in the mid segment", "in the middle third"]),
    "distal": (["distal segmentte", "distalde", "distal kesimde"], ["in the distal segment", "in the distal third"]),
    "body": (["gövdesinde", "gövde kesiminde"], ["in the body", "in the body"]),
}
SEGMENT_B = {"ostial": "ostial", "proximal": "proksimal", "mid": "mid", "distal": "distal", "body": "gövde"}
RANGES = {50: "40-50", 60: "50-60", 70: "60-70", 80: "70-80", 90: "80-90", 95: "90-95", 99: "95-99"}


def _stenosis_words(ch, key, s, tr):
    """How a report writes a stenosis of s percent: a number, a range or words.

    A range ends at the true value, and words are used only inside one
    category: kritik for 90 to 99, ileri derecede for 70 to 89, orta
    derecede for 50 to 69 and plak or hafif for less than 50 percent.
    """
    r = ch.random(key)
    if s == 100:
        return (["total oklüzyon", "tam tıkanıklık", "%100 darlık"] if tr else ["total occlusion", "complete occlusion", "100% stenosis"])[ch.index(key + "w", 3)]
    if s == 99 and r < 0.4:
        return "subtotal darlık" if tr else "subtotal stenosis"
    if s >= 90 and r < 0.3:
        return "kritik darlık" if tr else "critical stenosis"
    if 70 <= s < 90 and r < 0.15:
        return "ileri derecede darlık" if tr else "severe stenosis"
    if 50 <= s < 70 and r < 0.15:
        return "orta derecede darlık" if tr else "moderate stenosis"
    if s < 50 and r < 0.3:
        return ("hafif darlık" if r < 0.15 else "plak") if tr else ("mild stenosis" if r < 0.15 else "plaque")
    if s in RANGES and r > 0.8:
        a, b = RANGES[s].split("-")
        return f"%{a}-{b} darlık" if tr else f"{a}-{b}% stenosis"
    noun = (["darlık", "darlık", "stenoz"] if tr else ["stenosis", "stenosis", "narrowing"])[ch.index(key + "n", 3)]
    if ch.random(key + "spelled") < 0.06:
        return f"yüzde {s} {noun}" if tr else f"{s} percent {noun}"
    return f"%{s} {noun}" if tr else f"{s}% {noun}"


def _vessel_sentence(d, ch, key, vessel, lesions, tr, dominance):
    """One sentence of hospital A about one artery."""
    lang = 0 if tr else 1
    names = VESSEL_NAMES[vessel][lang]
    name = names[ch.index(key + "name", len(names), [5] + [2] * (len(names) - 1))]
    if tr and vessel in VESSEL_TYPOS and ch.random(key + "typo") < 0.04:
        name = VESSEL_TYPOS[vessel]
    verbs = ["mevcut", "izlendi", "saptandı"]
    if not lesions:
        if vessel in ("D1", "D2", "OM1", "OM2", "PDA"):
            return
        d.add(name, "VESSEL", None, vessel).add(": ")
        if tr:
            d.add(["Normal.", "Doğal.", "Anlamlı darlık izlenmedi."][ch.index(key + "normal", 3)] + " ")
        else:
            d.add(["Normal.", "Normal.", "No significant stenosis."][ch.index(key + "normal", 3)] + " ")
        return
    coref = vessel == "RCA" and dominance == "right" and ch.random(key + "coref") < 0.15
    if coref:
        if tr:
            d.add(name, "VESSEL", None, vessel).add(" dominant ve iri. ")
            seg = lesions[0]["segment"]
            d.add(_cap({"ostial": "ostiyumunda", "proximal": "proksimal segmentinde", "mid": "orta segmentinde", "distal": "distal segmentinde"}[seg]),
                  "SEGMENT", None, seg).add(" ")
        else:
            d.add("The ").add(name if name[:2].isupper() else name[0].lower() + name[1:], "VESSEL", None, vessel).add(" is dominant and large. ")
            seg = lesions[0]["segment"]
            d.add("Its ").add({"ostial": "ostium", "proximal": "proximal segment", "mid": "mid segment", "distal": "distal segment"}[seg], "SEGMENT", None, seg)
            d.add(" has ")
        _lesion_words(d, ch, key + "l0", lesions[0], tr, after_segment=True)
        rest = lesions[1:]
        if rest:
            d.add(" " if tr else "; ")
            _lesion_list(d, ch, key + "rest", rest, tr)
        d.add(f" {verbs[ch.index(key + 'verb', 3)]}." if tr else ".")
        if lesions[0]["stenosis"] == 100:
            d.add(" Distal kısım kollaterallerle doluyor." if tr else " The distal vessel fills through collaterals.")
        d.add(" ")
        return
    d.add(name, "VESSEL", None, vessel).add(": ")
    if tr:
        _lesion_list(d, ch, key, lesions, tr, capital=True)
        stent_only = all(l["kind"] == "in-stent" and l["stenosis"] == 0 for l in lesions)
        d.add("." if stent_only else f" {verbs[ch.index(key + 'verb', 3)]}.")
    else:
        _lesion_list(d, ch, key, lesions, tr, capital=True)
        d.add(".")
    if any(l["stenosis"] == 100 for l in lesions):
        d.add(" Distal kısım kollaterallerle doluyor." if tr else " The distal vessel fills through collaterals.")
    d.add(" ")


def _lesion_words(d, ch, key, lesion, tr, after_segment=False):
    s, kind = lesion["stenosis"], lesion["kind"]
    if kind == "in-stent":
        if s == 0:
            d.add("stent açık" if tr else "a patent stent", "STENOSIS", None, 0)
        else:
            d.add(f"stent içi %{s} restenoz" if tr else f"{s}% in-stent restenosis", "STENOSIS", None, s)
        return
    d.add(_stenosis_words(ch, key, s, tr), "STENOSIS", None, s)


def _lesion_list(d, ch, key, lesions, tr, capital=False):
    """Lesions of one artery from the ostium to the distal end, joined by commas."""
    lang = 0 if tr else 1
    for j, l in enumerate(lesions):
        segs = SEGMENT_NAMES[l["segment"]][lang]
        seg = segs[ch.index(f"{key}seg{j}", len(segs))]
        if j:
            d.add(", " if j < len(lesions) - 1 else (" ve " if tr else " and "))
        if tr:
            if l["kind"] == "in-stent":
                stem = {"ostiyumunda": "ostiyumundaki", "ostiyal kesimde": "ostiyal kesimdeki"}.get(seg, seg + "ki")
                d.add(_cap(stem) if (capital and j == 0) else stem, "SEGMENT", None, l["segment"]).add(" ")
                if l["stenosis"] == 0:
                    d.add("stent açık", "STENOSIS", None, 0)
                else:
                    d.add(f"stentte %{l['stenosis']} restenoz", "STENOSIS", None, l["stenosis"])
                continue
            d.add(_cap(seg) if (capital and j == 0) else seg, "SEGMENT", None, l["segment"]).add(" ")
            _lesion_words(d, ch, f"{key}w{j}", l, tr)
        else:
            _lesion_words(d, ch, f"{key}w{j}", l, tr)
            if j == 0 and capital:
                d.parts[-1] = _cap(d.parts[-1], False)
                d.entities[-1]["text"] = d.parts[-1]
            d.add(" ").add(seg, "SEGMENT", None, l["segment"])


def _angio_a(p, row, ch, tr):
    """Angiography report of hospital A."""
    d = Doc()
    lang = 0 if tr else 1
    access = {"radial": ("sağ radiyal arter", "the right radial artery"), "femoral": ("sağ femoral arter", "the right femoral artery")}[p["access"]][lang]
    indication = {"ACS": ("akut koroner sendrom", "acute coronary syndrome"), "CCS": ("kararlı angina", "stable angina"),
                  "HFrEF": ("düşük ejeksiyon fraksiyonlu kalp yetersizliğinin etiyolojisi", "aetiology of heart failure with reduced ejection fraction"),
                  "HFpEF": ("efor dispnesi", "breathlessness on exertion")}.get(row["main_diagnosis"], ("atipik göğüs ağrısı", "atypical chest pain"))
    if tr:
        d.add(f"Koroner anjiyografi raporu. Endikasyon: {indication[0]}. ")
    else:
        d.add(f"Coronary angiography report. Indication: {indication[1]}. ")
    old_stents = [l for l in p["lesions"] if l["kind"] == "in-stent"]
    if old_stents:
        l = old_stents[0]
        year = 2012 + ch.index("stentyear", 12)
        v = SHORT_B[l["vessel"]] if l["vessel"] != "LCX" else ("Cx" if tr else "LCx")
        before = ch.index("stentbefore", 3)
        sb = [80, 90, 95][before]
        segword = {"ostial": ("ostiyal", "ostial"), "proximal": ("proksimal", "proximal"), "mid": ("orta segment", "mid"), "distal": ("distal", "distal"),
                   "body": ("gövde", "body")}[l["segment"]][0 if tr else 1]
        if tr:
            d.add(f"Öykü: {year} yılında {v} {segword} bölgesindeki %{sb} darlığa stent takılmış. ")
        else:
            d.add(f"History: a stent was implanted for {'an' if sb == 80 else 'a'} {sb}% stenosis of the {segword} {v} in {year}. ")
    if tr:
        d.add(f"İşlem {access} yoluyla 6F kateterlerle yapıldı. ")
        d.add({"right": "Sağ dominant sistem. ", "left": "Sol dominant sistem. ", "codominant": "Kodominant sistem. "}[p["dominance"]])
    else:
        d.add(f"The procedure was performed via {access} with 6F catheters. ")
        d.add({"right": "Right dominant system. ", "left": "Left dominant system. ", "codominant": "Codominant system. "}[p["dominance"]])
    by_vessel = {}
    for l in p["lesions"]:
        by_vessel.setdefault(l["vessel"], []).append(l)
    for v in ("LM", "LAD", "D1", "D2", "LCX", "OM1", "OM2", "RCA", "PDA"):
        _vessel_sentence(d, ch, "v" + v, v, by_vessel.get(v, []), tr, p["dominance"])
    if ch.random("lvgram") < 0.4:
        ef = int(row["lvef"])
        d.add(f"Sol ventrikülografi: Ejeksiyon fraksiyonu %{ef}. " if tr else f"Left ventriculography: ejection fraction {ef}%. ")
    if p["treatment"] == "PCI":
        v, seg = p["target_vessel"], p["target_segment"]
        size = ch.index("stentsize", 3)
        dims = (["2,75 × 18 mm", "3,0 × 24 mm", "3,5 × 28 mm"] if tr else ["2.75 × 18 mm", "3.0 × 24 mm", "3.5 × 28 mm"])[size]
        segword = {"ostial": ("ostiyal", "ostial"), "proximal": ("proksimal", "proximal"), "mid": ("orta segment", "mid"), "distal": ("distal", "distal"),
                   "body": ("gövde", "body")}[seg][lang]
        if tr:
            d.add(f"Girişim: {SHORT_B[v] if v != 'LCX' else 'Cx'} {segword} lezyonuna {dims} ilaç salınımlı stent (DES) implante edildi; TIMI 3 akım sağlandı. ")
        else:
            d.add(f"Intervention: a {dims} drug-eluting stent (DES) was implanted in the {segword} {SHORT_B[v] if v != 'LCX' else 'LCx'} lesion, with TIMI 3 flow. ")
    elif p["treatment"] == "CABG":
        d.add("Öneri: Kalp ve damar cerrahisi konsültasyonu (KABG)." if tr else "Recommendation: cardiac surgery consultation (CABG).")
    else:
        d.add("Öneri: Medikal tedavi." if tr else "Recommendation: medical treatment.")
    return d


def _angio_b(p, row, ch):
    """Angiography report of hospital B: telegraphic and in upper case."""
    d = Doc(transform=tr_upper)
    d.add("Koroner anjiyografi. Giriş: " + {"radial": "sağ radial", "femoral": "sağ femoral"}[p["access"]] + ". ")
    by_vessel = {}
    for l in p["lesions"]:
        by_vessel.setdefault(l["vessel"], []).append(l)
    for v in ("LM", "LAD", "D1", "D2", "LCX", "OM1", "OM2", "RCA", "PDA"):
        les = by_vessel.get(v, [])
        if not les and v in ("D1", "D2", "OM1", "OM2", "PDA"):
            continue
        d.add(SHORT_B[v], "VESSEL", None, v).add(": ")
        if v == "RCA" and p["dominance"] == "right" and ch.random("bdom") < 0.5:
            d.add("dominant, ")
        if not les:
            d.add(["doğal", "normal"][ch.index("bn" + v, 2)] + ". ")
            continue
        for j, l in enumerate(les):
            if j:
                d.add(", ")
            s = l["stenosis"]
            d.add(SEGMENT_B[l["segment"]], "SEGMENT", None, l["segment"]).add(" ")
            if l["kind"] == "in-stent":
                d.add("stent açık" if s == 0 else f"stent içi %{s}", "STENOSIS", None, s)
            elif s == 100:
                d.add("TO", "STENOSIS", None, s)
            elif s == 99 and ch.random(f"bsub{v}{j}") < 0.5:
                d.add("subtotal", "STENOSIS", None, s)
            elif s >= 90 and ch.random(f"bkr{v}{j}") < 0.3:
                d.add("kritik", "STENOSIS", None, s)
            elif s < 50 and ch.random(f"bpl{v}{j}") < 0.4:
                d.add("plaklı", "STENOSIS", None, s)
            elif s in RANGES and ch.random(f"brg{v}{j}") < 0.2:
                d.add("%" + RANGES[s], "STENOSIS", None, s)
            else:
                d.add(f"%{s}", "STENOSIS", None, s)
        if any(l["stenosis"] == 100 for l in les):
            d.add(", distali kollateralle doluyor")
        d.add(". ")
    if ch.random("blv") < 0.4:
        d.add(f"SV: EF %{int(row['lvef'])}. ")
    if p["treatment"] == "PCI":
        d.add(f"İşlem: {SHORT_B[p['target_vessel']]} {SEGMENT_B[p['target_segment']]} DES.")
    elif p["treatment"] == "CABG":
        d.add("Öneri: KVC konsültasyonu.")
    else:
        d.add("Öneri: medikal tedavi.")
    return d


def angiography_archive(seed=2026):
    """The angiography reports of the archive, one per patient with an angiography.

    Returns a table with patient_id, split, text_tr, text_en (empty for
    hospital B), entities_tr and entities_en (spans of VESSEL, SEGMENT and
    STENOSIS mentions; the code of a STENOSIS mention is its value in
    percent), and the truth: the largest stenosis of every territory
    (max_LM, max_LAD, max_LCX, max_RCA), its category from 0 to 4 (cat_LM
    ...), whether it is significant (sig_LM ...), left_main and n_vessels.
    """
    cohort, info, _ = _registry(seed)
    rows, start = [], 0
    for split, k in SPLITS:
        for i in range(start, start + k):
            row = cohort.iloc[i]
            p = info.get(row["patient_id"])
            if p is None:
                continue
            ch = Choices(seed, f"angio{i}")
            if split == "external":
                b = _angio_b(p, row, ch)
                text_tr, ent_tr, text_en, ent_en = b.text(), b.entities, "", []
            else:
                a_tr, a_en = _angio_a(p, row, ch, True), _angio_a(p, row, ch, False)
                text_tr, ent_tr, text_en, ent_en = a_tr.text(), a_tr.entities, a_en.text(), a_en.entities
            truth = {f"max_{t}": p[f"max_{t}"] for t in TERRITORIES}
            truth.update({f"cat_{t}": category(p[f"max_{t}"]) for t in TERRITORIES})
            truth.update({f"sig_{t}": p[f"sig_{t}"] for t in TERRITORIES})
            rows.append(dict(patient_id=row["patient_id"], split=split, text_tr=text_tr, text_en=text_en,
                             entities_tr=ent_tr, entities_en=ent_en, **truth,
                             left_main=p["left_main"], n_vessels=p["n_vessels"], treatment=p["treatment"]))
        start += k
    return pd.DataFrame(rows)
