#!/usr/bin/env python3
"""
Readability scorer for the mr-gay skill.
Takes text via stdin or file path argument. Returns Flesch-Kincaid Reading Ease,
Grade Level, Gunning Fog Index, and per-section breakdowns when headers are detected.

Usage:
    echo "Your text here" | python3 readability.py
    python3 readability.py path/to/file.txt
    python3 readability.py path/to/file.md
"""

import sys
import re
import json
import os


def count_syllables(word):
    """Estimate syllable count for an English word."""
    word = word.lower().strip(".,!?;:\"'()-")
    if not word:
        return 0

    # Common exceptions
    exceptions = {
        "the": 1, "he": 1, "she": 1, "we": 1, "me": 1, "be": 1,
        "are": 1, "were": 1, "there": 1, "where": 1, "here": 1,
        "fire": 1, "hire": 1, "wire": 1, "core": 1, "more": 1,
        "store": 1, "score": 1, "bore": 1, "wore": 1,
        "create": 2, "created": 3, "every": 3, "different": 3,
        "business": 3, "area": 3, "idea": 3, "real": 1,
    }
    if word in exceptions:
        return exceptions[word]

    # Count vowel groups
    vowels = "aeiouy"
    count = 0
    prev_vowel = False

    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel

    # Adjustments
    if word.endswith("e") and not word.endswith(("le", "ce", "se", "ge", "ve", "ze")):
        count -= 1
    if word.endswith(("le", "ce", "se", "ge", "ve", "ze")) and len(word) > 3:
        pass  # keep count
    if word.endswith("ed") and not word.endswith(("ted", "ded")):
        count -= 1
    if word.endswith("es") and not word.endswith(("ses", "zes", "ces", "ges")):
        count -= 1

    return max(1, count)


def split_sentences(text):
    """Split text into sentences."""
    SENTINEL = "<<DOT>>"
    # Handle common abbreviations
    text = re.sub(r'\b(Mr|Mrs|Ms|Dr|Prof|Sr|Jr|vs|etc|inc|ltd|co)\.',
                  lambda m: m.group(0).replace('.', SENTINEL), text, flags=re.IGNORECASE)
    text = re.sub(r'(\d)\.(\d)', lambda m: m.group(1) + SENTINEL + m.group(2), text)
    text = re.sub(r'\b([A-Z])\.', lambda m: m.group(1) + SENTINEL, text)

    sentences = re.split(r'[.!?]+(?:\s|$)', text)
    sentences = [s.replace(SENTINEL, '.').strip() for s in sentences if s.strip()]
    return sentences


def get_words(text):
    """Extract words from text, ignoring markdown formatting."""
    # Strip markdown headers, links, images, code blocks
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'```[\s\S]*?```', '', text)
    text = re.sub(r'`[^`]+`', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', '', text)
    text = re.sub(r'[*_]{1,3}', '', text)
    text = re.sub(r'^\s*[-*+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*\d+\.\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\s*>\s+', '', text, flags=re.MULTILINE)

    words = re.findall(r"[a-zA-Z'-]+", text)
    return [w for w in words if len(w) > 0]


def is_complex_word(word):
    """A word is complex (for Gunning Fog) if it has 3+ syllables
    and is not a proper noun, compound, or common suffix."""
    if word[0].isupper():
        return False
    if "-" in word:
        return False
    return count_syllables(word) >= 3


def analyze_text(text):
    """Compute readability metrics for a block of text."""
    sentences = split_sentences(text)
    words = get_words(text)

    if not sentences or not words:
        return None

    total_sentences = len(sentences)
    total_words = len(words)
    total_syllables = sum(count_syllables(w) for w in words)
    complex_words = sum(1 for w in words if is_complex_word(w))

    avg_sentence_length = total_words / total_sentences
    avg_syllables_per_word = total_syllables / total_words
    complex_word_pct = (complex_words / total_words) * 100

    # Flesch Reading Ease: 206.835 - 1.015(words/sentences) - 84.6(syllables/words)
    flesch_ease = 206.835 - (1.015 * avg_sentence_length) - (84.6 * avg_syllables_per_word)
    flesch_ease = round(max(0, min(100, flesch_ease)), 1)

    # Flesch-Kincaid Grade Level: 0.39(words/sentences) + 11.8(syllables/words) - 15.59
    fk_grade = (0.39 * avg_sentence_length) + (11.8 * avg_syllables_per_word) - 15.59
    fk_grade = round(max(0, fk_grade), 1)

    # Gunning Fog Index: 0.4 * (avg_sentence_length + complex_word_pct)
    fog_index = 0.4 * (avg_sentence_length + complex_word_pct)
    fog_index = round(fog_index, 1)

    # Interpret the Flesch score
    if flesch_ease >= 80:
        level = "Easy (6th grade): conversational, accessible to everyone"
    elif flesch_ease >= 70:
        level = "Fairly easy (7th grade): good for broad audiences"
    elif flesch_ease >= 60:
        level = "Standard (8th-9th grade): sweet spot for most content"
    elif flesch_ease >= 50:
        level = "Fairly difficult (10th-12th grade): getting dense"
    elif flesch_ease >= 30:
        level = "Difficult (college level): specialist audience territory"
    else:
        level = "Very difficult (graduate level): academic or legal density"

    return {
        "total_words": total_words,
        "total_sentences": total_sentences,
        "avg_sentence_length": round(avg_sentence_length, 1),
        "avg_syllables_per_word": round(avg_syllables_per_word, 2),
        "flesch_reading_ease": flesch_ease,
        "flesch_level": level,
        "fk_grade_level": fk_grade,
        "gunning_fog": fog_index,
        "complex_word_pct": round(complex_word_pct, 1),
    }


def find_sections(text):
    """Split markdown text into sections by headers."""
    lines = text.split('\n')
    sections = []
    current_title = "Opening (no header)"
    current_lines = []

    for line in lines:
        header_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if header_match:
            if current_lines:
                body = '\n'.join(current_lines).strip()
                if body:
                    sections.append({"title": current_title, "text": body})
            current_title = header_match.group(2).strip()
            current_lines = []
        else:
            current_lines.append(line)

    if current_lines:
        body = '\n'.join(current_lines).strip()
        if body:
            sections.append({"title": current_title, "text": body})

    return sections


def find_long_sentences(text, threshold=30):
    """Find sentences exceeding the word count threshold."""
    sentences = split_sentences(text)
    long = []
    for s in sentences:
        words = get_words(s)
        if len(words) >= threshold:
            preview = ' '.join(s.split()[:12]) + "..."
            long.append({"words": len(words), "preview": preview})
    return sorted(long, key=lambda x: x["words"], reverse=True)[:5]


# Common function words excluded from concreteness scoring so the score
# reflects meaningful vocabulary, not grammatical glue.
STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "then", "so", "because", "as",
    "of", "at", "by", "for", "with", "about", "against", "between", "into",
    "through", "during", "to", "from", "up", "down", "in", "out", "on", "off",
    "over", "under", "again", "is", "are", "was", "were", "be", "been", "being",
    "am", "do", "does", "did", "have", "has", "had", "having", "this", "that",
    "these", "those", "i", "you", "he", "she", "it", "we", "they", "me", "him",
    "her", "us", "them", "my", "your", "his", "its", "our", "their", "what",
    "which", "who", "whom", "when", "where", "why", "how", "all", "any", "both",
    "each", "more", "most", "other", "some", "such", "no", "nor", "not", "only",
    "own", "same", "than", "too", "very", "can", "will", "just", "would",
    "should", "could", "may", "might", "must", "there", "here", "also", "yet",
}

_CONC_CACHE = None


def load_concreteness():
    """Load the bundled concreteness norms (word -> mean, 1=abstract..5=concrete). Cached."""
    global _CONC_CACHE
    if _CONC_CACHE is not None:
        return _CONC_CACHE
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "concreteness.csv")
    scores = {}
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.startswith("#") or line.startswith("word,"):
                    continue
                parts = line.rstrip("\n").split(",")
                if len(parts) != 2:
                    continue
                try:
                    scores[parts[0]] = float(parts[1])
                except ValueError:
                    continue
    except FileNotFoundError:
        return None
    _CONC_CACHE = scores
    return scores


def analyze_concreteness(text):
    """Score how concrete vs abstract the prose is (Brysbaert norms).
    Lower = more abstract/vague. Flags the most abstract sentences and words.
    A flag for judgment, not a rule: some abstraction is legitimate."""
    scores = load_concreteness()
    if scores is None:
        return {"unavailable": "concreteness.csv not found alongside the script"}

    def content_words(chunk):
        return [w.lower() for w in get_words(chunk)
                if w.lower() not in STOPWORDS and len(w) > 1]

    all_words = content_words(text)
    scored = [(w, scores[w]) for w in all_words if w in scores]
    if len(scored) < 5:
        return None

    mean = sum(c for _, c in scored) / len(scored)
    coverage = (len(scored) / len(all_words) * 100) if all_words else 0

    # Most abstract sentences (need enough scored words to be meaningful)
    sentence_scores = []
    for s in split_sentences(text):
        cw = [scores[w] for w in content_words(s) if w in scores]
        if len(cw) >= 4:
            word_count = len(s.split())
            sentence_scores.append({
                "score": round(sum(cw) / len(cw), 2),
                "preview": ' '.join(s.split()[:12]) + ("..." if word_count > 12 else ""),
            })
    most_abstract = sorted(sentence_scores, key=lambda x: x["score"])[:3]

    # Vaguest distinct words actually present (only the genuinely abstract ones)
    distinct = sorted(set(scored), key=lambda x: x[1])
    vaguest = [w for w, c in distinct if c < 2.5][:8]

    if mean < 2.5:
        band = "abstract-heavy: lots of vague, unpicturable language"
    elif mean < 3.2:
        band = "mixed: some concrete, some abstract"
    else:
        band = "concrete: mostly picturable, specific language"

    return {
        "mean": round(mean, 2),
        "scored_words": len(scored),
        "coverage_pct": round(coverage, 1),
        "band": band,
        "most_abstract_sentences": most_abstract,
        "vaguest_words": vaguest,
    }


def main():
    # Read input
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        binary_error = {"error": "Binary file (e.g. .docx) not supported. Extract the text first (use the docx skill) and pipe it in."}
        # Guard: reject known binary document extensions outright.
        if filepath.lower().endswith((".docx", ".doc", ".pdf", ".xlsx", ".pptx")):
            print(json.dumps(binary_error))
            sys.exit(1)
        try:
            with open(filepath, 'rb') as f:
                raw = f.read()
        except FileNotFoundError:
            print(json.dumps({"error": f"File not found: {filepath}"}))
            sys.exit(1)
        # Guard: reject zip-signature files (e.g. .docx/.xlsx/.pptx) and anything
        # that isn't valid UTF-8 text.
        if raw[:4] == b"PK\x03\x04":
            print(json.dumps(binary_error))
            sys.exit(1)
        try:
            text = raw.decode('utf-8')
        except UnicodeDecodeError:
            print(json.dumps(binary_error))
            sys.exit(1)
    else:
        text = sys.stdin.read()

    if not text.strip():
        print(json.dumps({"error": "No text provided"}))
        sys.exit(1)

    # Overall metrics
    overall = analyze_text(text)
    if not overall:
        print(json.dumps({"error": "Could not analyze text: too short or no sentences found"}))
        sys.exit(1)

    result = {"overall": overall}

    # Long sentences
    long_sentences = find_long_sentences(text)
    if long_sentences:
        result["long_sentences"] = long_sentences

    # Concreteness (abstract vs picturable language; complements reading-level scores)
    concreteness = analyze_concreteness(text)
    if concreteness:
        result["concreteness"] = concreteness

    # Per-section breakdown (if headers detected)
    sections = find_sections(text)
    if len(sections) > 1:
        section_scores = []
        for sec in sections:
            sec_analysis = analyze_text(sec["text"])
            if sec_analysis:
                section_scores.append({
                    "section": sec["title"],
                    "flesch_reading_ease": sec_analysis["flesch_reading_ease"],
                    "avg_sentence_length": sec_analysis["avg_sentence_length"],
                    "word_count": sec_analysis["total_words"],
                })
        if section_scores:
            result["sections"] = section_scores

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
