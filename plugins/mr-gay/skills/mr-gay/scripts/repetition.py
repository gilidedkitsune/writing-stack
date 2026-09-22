#!/usr/bin/env python3
"""
Repetition scanner for the mr-gay skill.
Counts content-word repetition (nouns, verbs, adjectives; function words stripped),
groups inflections, and reports the repeaters a reader feels: how often, how dense,
and how tightly clustered. Proper nouns and acronyms are listed separately, untiered.

Usage:
    echo "Your text here" | python3 repetition.py
    python3 repetition.py path/to/file.txt
    python3 repetition.py path/to/file.md
    python3 repetition.py path/to/file.md --terms "forge,model,plan"
Subject terms (from the title automatically, plus --terms) and proper nouns are reported but never tiered.
Stdlib only. Refuses .docx (extract the text first).
"""
import sys, re, json, os
from collections import Counter, defaultdict

STOP = set("""
a an the this that these those there here it its itself i me my mine myself we us our ours ourselves you your yours yourself yourselves
he him his himself she her hers herself they them their theirs themselves who whom whose which what where when why how
and or but nor so yet for if then than as because while although though unless until whether either neither both
of in on at to from by with without about above below over under between among through during before after into onto upon
across along around behind beside beyond inside outside toward towards within against via per off out up down
is am are was were be been being have has had having do does did doing done
can could will would shall should may might must ought
not no nor never none nothing nobody nowhere neither
very just also too only even still already often always sometimes usually rarely
more most less least much many some any all each every few several such own same other another
one two three four five six seven eight nine ten first second third next last
yes well okay ok maybe perhaps rather quite really actually simply basically
get got gets getting go goes going went gone come comes came coming
thing things way ways lot lots kind sort
s t re ve ll d m
""".split())

IRREG = {"went":"go","gone":"go","made":"make","built":"build","said":"say","took":"take","taken":"take","gave":"give","given":"give",
 "ran":"run","wrote":"write","written":"write","saw":"see","seen":"see","knew":"know","known":"know","thought":"think","found":"find",
 "left":"leave","told":"tell","kept":"keep","began":"begin","begun":"begin","brought":"bring","bought":"buy","chose":"choose","chosen":"choose",
 "grew":"grow","grown":"grow","held":"hold","led":"lead","lost":"lose","met":"meet","paid":"pay","sent":"send","showed":"show","shown":"show",
 "spent":"spend","stood":"stand","understood":"understand","won":"win","broke":"break","broken":"break","spoke":"speak","spoken":"speak",
 "fell":"fall","felt":"feel","meant":"mean","sold":"sell","taught":"teach","caught":"catch","dealt":"deal","drew":"draw","drawn":"draw",
 "threw":"throw","thrown":"throw","wore":"wear","worn":"wear","woke":"wake","hid":"hide","hidden":"hide","rose":"rise","risen":"rise",
 "people":"person","children":"child","men":"man","women":"woman","teams":"team","data":"data","better":"good","best":"good","worse":"bad","worst":"bad"}

def clean_markdown(text):
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)            # front matter
    text = re.sub(r"```.*?```", " ", text, flags=re.S)                   # code blocks
    text = re.sub(r"`[^`]*`", " ", text)                                 # inline code
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)                    # images
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)                 # links -> text
    text = re.sub(r"<[^>]+>", " ", text)                                 # html
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"^\s{0,3}#{1,6}\s*", "", text, flags=re.M)            # header marks
    text = re.sub(r"^\s*[-*+>]\s+", "", text, flags=re.M)                # list/quote marks
    text = re.sub(r"[*_]{1,3}", "", text)                                # emphasis
    return text

def lemma(w, surface):
    if w in IRREG: return IRREG[w]
    cands = []
    if len(w) > 4 and w.endswith("ies"): cands.append(w[:-3] + "y")
    if len(w) > 4 and w.endswith("ied"): cands.append(w[:-3] + "y")
    if len(w) > 3 and w.endswith("es") and w[-3] in "sxz": cands.append(w[:-2])
    if len(w) > 4 and w.endswith("sses"): cands.append(w[:-2])
    if len(w) > 5 and w.endswith("ing"):
        b = w[:-3]; cands += [b + "e", b, b[:-1] if len(b) > 2 and b[-1] == b[-2] else b]
    if len(w) > 4 and w.endswith("ed"):
        b = w[:-2]; cands += [b + "e", b, b[:-1] if len(b) > 2 and b[-1] == b[-2] else b]
    if len(w) > 3 and w.endswith("s") and not w.endswith("ss"): cands.append(w[:-1])
    if len(w) > 4 and w.endswith("ly"): cands.append(w[:-2])
    for c in cands:                       # prefer a base that actually occurs in the text
        if c in surface: return c
    for c in cands:
        if c + "e" in surface: return c + "e"
    return cands[0] if cands else w

def main():
    args = sys.argv[1:]; extra_terms = set()
    if "--terms" in args:
        i = args.index("--terms"); extra_terms = {t.strip().lower() for t in args[i+1].split(",") if t.strip()} if i+1 < len(args) else set()
        del args[i:i+2]
    if args:
        p = args[0]
        if p.lower().endswith((".docx", ".doc", ".pdf")):
            print(json.dumps({"error": "Binary document. Extract the text first, then pipe it in."})); return
        if not os.path.exists(p):
            print(json.dumps({"error": f"File not found: {p}"})); return
        raw = open(p, encoding="utf-8", errors="replace").read()
    else:
        raw = sys.stdin.read()
    if not raw.strip():
        print(json.dumps({"error": "No text provided"})); return

    text = clean_markdown(raw)
    paras = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    m = re.search(r"^\s{0,3}#\s+(.+)$", raw, flags=re.M)
    # headerless title: only when there is more than one paragraph, the first line is short,
    # and it does not end like a sentence (a one-line stdin input or a social post is body, not title)
    first = paras[0].split("\n")[0].strip() if paras else ""
    title = m.group(1) if m else (first if len(paras) > 1 and len(first.split()) <= 15 and not first.endswith((".", "!", "?")) else "")
    tok_re = re.compile(r"[A-Za-z][A-Za-z.\-']*[A-Za-z]|[A-Za-z]")

    # pass 1: surface forms + proper-noun evidence
    surface = Counter(); cap_mid = Counter(); low_cnt = Counter(); total = 0
    for para in paras:
        sents = re.split(r"(?<=[.!?])\s+", para.strip())
        for s in sents:
            toks = tok_re.findall(s)
            titlecase = len(toks) <= 12 and sum(t[0].isupper() for t in toks) >= 0.6 * max(len(toks), 1)
            for i, t in enumerate(toks):
                total += 1
                base = re.sub(r"'(s|re|ve|ll|d|m|t)$", "", t.lower().strip(".-'"))
                if not base: continue
                surface[base] += 1
                if t[0].isupper() and i > 0 and not titlecase: cap_mid[base] += 1
                if t[0].islower(): low_cnt[base] += 1
    acronym = lambda t: t.isupper() and 2 <= len(t) <= 5
    proper = {b for b, c in cap_mid.items() if c >= 2 and c >= 2 * low_cnt[b] and b not in STOP}
    for b in list(surface):
        if any(acronym(f) for f in [b.upper()]) and b.upper() in raw: proper.add(b)

    # pass 2: lemmatize content words, track per-paragraph clustering
    lem_count = Counter(); lem_forms = defaultdict(Counter); lem_paras = defaultdict(Counter); prop_count = Counter()
    content_total = 0
    subject = set()
    for t in tok_re.findall(title):
        b = t.lower().strip(".-'")
        if b and b not in STOP and len(b) >= 3: subject.add(lemma(b, surface))
    subject |= {lemma(t, surface) for t in extra_terms}
    for pi, para in enumerate(paras):
        for t in tok_re.findall(para):
            base = re.sub(r"'(s|re|ve|ll|d|m|t)$", "", t.lower().strip(".-'"))
            if not base or base in STOP or len(base) < 3 or base.isdigit(): continue
            if base in proper or "." in base:
                prop_count[base if "." in base else t.strip(".,")] += 1; continue
            L = lemma(base, surface)
            content_total += 1; lem_count[L] += 1; lem_forms[L][base] += 1; lem_paras[L][pi] += 1

    per_1k = lambda c: round(c * 1000 / max(total, 1), 1)
    reps = []; subj = []
    for L, c in lem_count.most_common(60):
        if c < 2: break
        mx = max(lem_paras[L].values()); touched = len(lem_paras[L])
        row = {"lemma": L, "count": c, "per_1k_words": per_1k(c), "forms": dict(lem_forms[L].most_common()),
               "paragraphs_touched": touched, "max_in_one_paragraph": mx}
        if L in subject:
            subj.append(row); continue
        # tiers: clustering first (what a reader feels), then piece-wide density
        marked = len(L) >= 7 or "-" in L
        row["tier"] = ("red" if (mx >= 3 and c >= 4) or (c >= 8 and per_1k(c) >= 10) or (marked and c >= 8)
                       else "yellow" if (c >= 5 and per_1k(c) >= 5 and mx >= 2) or (marked and c >= 5) else "note")
        row["why"] = ("clusters" if mx >= 3 else "marked word, recurs" if marked and c >= 5 else "dense" if per_1k(c) >= 5 else "")
        reps.append(row)
    reps.sort(key=lambda r: ({"red": 0, "yellow": 1, "note": 2}[r["tier"]], -r["max_in_one_paragraph"], -r["count"]))
    result = {
        "words_total": total, "paragraphs": len(paras), "content_words": content_total,
        "unique_content_lemmas": len(lem_count), "content_variety": round(len(lem_count) / max(content_total, 1), 3),
        "reds": sum(r["tier"] == "red" for r in reps), "yellows": sum(r["tier"] == "yellow" for r in reps),
        "title_detected": title, "subject_terms_untiered": subj[:10],
        "repeaters": [r for r in reps if r["tier"] != "note"] + [r for r in reps if r["tier"] == "note"][:10],
        "proper_nouns_and_acronyms": [{"term": k, "count": v} for k, v in prop_count.most_common(12)],
        "how_to_read": "max_in_one_paragraph is the column a reader feels. Subject terms and proper nouns are counted but never tiered; pass more with --terms. A tic is fixed by restructuring, never by a synonym."
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
