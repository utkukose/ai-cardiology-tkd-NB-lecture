"""Small teaching helpers: answer checks and ECG paper plots.

The language of the printed messages and of the plot labels follows
set_language("en") or set_language("tr").
"""

import numpy as np

_STATE = {"lang": "en", "answers": {}}

TEXT = {
    "en": {
        "correct": "correct",
        "not_yet": "not yet",
        "expected_close": "the expected value is within {tol} of the answer",
        "missing": "write an answer in place of None first",
        "no_key": "no expected answer is registered for",
        "no_var": "the notebook has no variable named `{name}`. The code of the assistant must save its result under this name. Ask the assistant to do so, or run the ready code below.",
        "step_hint": "compare the code with the prompt, use the repair prompt of the prompt library or run the ready code below",
        "reference": "the reference code gives",
        "range": "plausible range {low} to {high}",
        "time": "Time (s)", "mv": "Amplitude (mV)",
        "bias": "Bias", "loa": "Limits of agreement",
        "mean_pair": "Mean of the two measurements (ms)",
        "diff_pair": "Difference (ms)",
    },
    "tr": {
        "correct": "doğru",
        "not_yet": "henüz değil",
        "expected_close": "beklenen değer cevaba {tol} kadar yakın olmalı",
        "missing": "önce None yerine bir cevap yazın",
        "no_key": "şu alıştırma için kayıtlı bir beklenen cevap yok:",
        "no_var": "defterde `{name}` adlı bir değişken yok. Asistanın kodu sonucunu bu adla kaydetmeli. Asistandan bunu isteyin ya da aşağıdaki hazır kodu çalıştırın.",
        "step_hint": "kodu promptla karşılaştırın, prompt kütüphanesindeki onarım promptunu kullanın ya da aşağıdaki hazır kodu çalıştırın",
        "reference": "hazır kodun sonucu:",
        "range": "makul aralık {low} ile {high} arası",
        "time": "Zaman (s)", "mv": "Genlik (mV)",
        "bias": "Sapma", "loa": "Uyum sınırları",
        "mean_pair": "İki ölçümün ortalaması (ms)",
        "diff_pair": "Fark (ms)",
    },
}


def set_language(lang):
    """Choose "en" or "tr" for messages and plot labels."""
    _STATE["lang"] = "tr" if str(lang).lower().startswith("tr") else "en"


def t(key):
    return TEXT[_STATE["lang"]][key]


def register_answers(answers):
    """Store the expected answers: {name: (value, tolerance)}."""
    _STATE["answers"].update(answers)


def _answer_key(name):
    """The registered name of an exercise, in either language of the course."""
    if name in _STATE["answers"]:
        return name
    for a, b in (("Exercise ", "Alıştırma "), ("Alıştırma ", "Exercise "), ("Step ", "Adım "), ("Adım ", "Step ")):
        if name.startswith(a) and b + name[len(a):] in _STATE["answers"]:
            return b + name[len(a):]
    return None


def check(name, answer):
    """Compare an answer with the registered expected value and print the result."""
    key = _answer_key(name)
    if key is None:
        print(f"{name}: {t('no_key')} {name}")
        return None
    expected, tol = _STATE["answers"][key]
    if answer is None:
        print(f"{name}: {t('missing')}")
        return None
    if isinstance(expected, str):
        ok = str(answer).strip().lower() == expected.lower()
    else:
        try:
            ok = abs(float(answer) - float(expected)) <= tol
        except (TypeError, ValueError):
            ok = False
    if ok:
        print(f"{name}: {t('correct')} ✓")
    else:
        hint = t("expected_close").format(tol=tol) if not isinstance(
            expected, str) else ""
        print(f"{name}: {t('not_yet')} ✗ {hint}".rstrip())
    return None


def check_step(name, variable, scope):
    """Check one step of the prompt path.

    name is the step ("Step 1.2" or "Adım 1.2"), variable the name under which
    the code of the assistant saves its result, and scope the namespace of the
    notebook (pass globals()). Missing variables give a short hint instead of
    an error message.
    """
    if variable not in scope:
        print(f"{name}: {t('not_yet')} ✗ " + t("no_var").format(name=variable))
        return None
    key = _answer_key(name)
    if key is None:
        print(f"{name}: {t('no_key')} {name}")
        return None
    expected, tol = _STATE["answers"][key]
    answer = scope[variable]
    if isinstance(expected, str):
        ok = str(answer).strip().lower() == expected.lower()
    else:
        try:
            ok = abs(float(answer) - float(expected)) <= tol
        except (TypeError, ValueError):
            ok = False
    if ok:
        print(f"{name}: {t('correct')} ✓ ({variable} = {answer})")
    else:
        print(f"{name}: {t('not_yet')} ✗ ({variable} = {answer}). " + t("step_hint") + ".")
    return None


def check_value(name, variable, expected, tol, scope):
    """Check a step against a value computed at run time.

    For data that only the participant holds, such as a personal copy of a data
    set, the expected value is computed in the same cell by the reference code.
    """
    if variable not in scope:
        print(f"{name}: {t('not_yet')} ✗ " + t("no_var").format(name=variable))
        return None
    answer = scope[variable]
    try:
        ok = abs(float(answer) - float(expected)) <= tol
    except (TypeError, ValueError):
        ok = False
    if ok:
        print(f"{name}: {t('correct')} ✓ ({variable} = {answer})")
    else:
        print(f"{name}: {t('not_yet')} ✗ ({variable} = {answer}; {t('reference')} {expected}). " + t("step_hint") + ".")
    return None


def check_range(name, variable, low, high, scope):
    """Check that a result whose exact value differs between computers lies in a plausible range."""
    if variable not in scope:
        print(f"{name}: {t('not_yet')} ✗ " + t("no_var").format(name=variable))
        return None
    answer = scope[variable]
    try:
        ok = low <= float(answer) <= high
    except (TypeError, ValueError):
        ok = False
    rng = t("range").format(low=low, high=high)
    if ok:
        print(f"{name}: {t('correct')} ✓ ({variable} = {answer}; {rng})")
    else:
        print(f"{name}: {t('not_yet')} ✗ ({variable} = {answer}; {rng}). " + t("step_hint") + ".")
    return None


def ecg_paper(ax, t0, t1, v0, v1):
    """Draw ECG paper: 0.04 s x 0.1 mV small boxes, 0.2 s x 0.5 mV large."""
    minor, major = "#F7D2D2", "#E9A0A0"
    for x in np.arange(np.floor(t0 / 0.04) * 0.04, t1 + 1e-9, 0.04):
        ax.axvline(x, color=minor, lw=0.4, zorder=0)
    for y in np.arange(np.floor(v0 / 0.1) * 0.1, v1 + 1e-9, 0.1):
        ax.axhline(y, color=minor, lw=0.4, zorder=0)
    for x in np.arange(np.floor(t0 / 0.2) * 0.2, t1 + 1e-9, 0.2):
        ax.axvline(x, color=major, lw=0.8, zorder=0)
    for y in np.arange(np.floor(v0 / 0.5) * 0.5, v1 + 1e-9, 0.5):
        ax.axhline(y, color=major, lw=0.8, zorder=0)
    ax.set_xlim(t0, t1)
    ax.set_ylim(v0, v1)


def plot_strip(ax, time, signal, label=None, v_range=(-1.0, 1.5), color="k"):
    """One lead on ECG paper."""
    time = np.asarray(time)
    ecg_paper(ax, time[0], time[-1], *v_range)
    ax.plot(time, signal, color=color, lw=0.9)
    if label:
        ax.text(time[0] + 0.03, v_range[1] - 0.25, label, fontsize=11,
                fontweight="bold")
    ax.set_xlabel(t("time"))
    ax.set_ylabel(t("mv"))


LAYOUT = [["I", "aVR", "V1", "V4"], ["II", "aVL", "V2", "V5"],
          ["III", "aVF", "V3", "V6"]]


def plot_12lead(time, leads, title=None, v_range=(-1.3, 2.0), names=None):
    """Standard 3 x 4 layout of 2.5 s per column and a lead II strip.

    time: array of times (s); leads: mapping from lead name to signal
    (a pandas DataFrame works); names: optional mapping from the standard
    names to the column names of leads (for example "I" -> "i").
    """
    import matplotlib.pyplot as plt
    names = names or {}
    time = np.asarray(time)
    fig = plt.figure(figsize=(13, 9))
    grid = fig.add_gridspec(4, 4, hspace=0.08, wspace=0.02)
    for r in range(3):
        for c in range(4):
            ax = fig.add_subplot(grid[r, c])
            lead = LAYOUT[r][c]
            sel = (time >= time[0] + 2.5 * c) & (time < time[0] + 2.5 * c + 2.5)
            x = np.asarray(leads[names.get(lead, lead)])[sel]
            ecg_paper(ax, time[sel][0], time[sel][-1], *v_range)
            ax.plot(time[sel], x, "k", lw=0.8)
            ax.text(time[sel][0] + 0.05, v_range[1] - 0.35, lead,
                    fontsize=11, fontweight="bold")
            ax.set_xticks([])
            ax.set_yticks([])
    ax = fig.add_subplot(grid[3, :])
    sel = time <= time[0] + 10.0
    ecg_paper(ax, time[sel][0], time[sel][-1], *v_range)
    ax.plot(time[sel], np.asarray(leads[names.get("II", "II")])[sel], "k",
            lw=0.8)
    ax.text(time[0] + 0.05, v_range[1] - 0.35, "II", fontsize=11,
            fontweight="bold")
    ax.set_yticks([])
    ax.set_xlabel(t("time"))
    if title:
        fig.suptitle(title, y=0.92)
    return fig


def plot_bland_altman(ax, a, b, color="#9B1B1B"):
    """Bland-Altman plot of two sets of measurements (ms)."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    mean = (a + b) / 2
    diff = a - b
    bias = diff.mean()
    sd = diff.std(ddof=1) if len(diff) > 1 else 0.0
    ax.scatter(mean, diff, color=color, zorder=3)
    ax.axhline(bias, color="k", lw=1.2, label=f"{t('bias')} = {bias:.1f} ms")
    for k in (-1.96, 1.96):
        ax.axhline(bias + k * sd, color="k", lw=0.9, ls="--")
    ax.plot([], [], "k--", lw=0.9,
            label=f"{t('loa')}: {bias - 1.96 * sd:.1f} / {bias + 1.96 * sd:.1f} ms")
    ax.set_xlabel(t("mean_pair"))
    ax.set_ylabel(t("diff_pair"))
    ax.legend(loc="best", fontsize=9)
    return bias, bias - 1.96 * sd, bias + 1.96 * sd
