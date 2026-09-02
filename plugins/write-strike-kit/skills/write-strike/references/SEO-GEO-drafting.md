# SEO-GEO Drafting

The embedded drafting layer for write-strike: how to draft copy that ranks in Google **and** gets cited by AI answer engines (ChatGPT, Perplexity, Google AI Overviews, Gemini, Copilot). Apply to blog, long-form, and website copy. Layers on top of bolt-TOV-and-guidelines and noslops; it does not replace either.

This file is the **writing** layer only: how the words on the page earn rankings and citations. The **tooling** (keyword research, SERP analysis, audits, data pulls, post-draft optimizers) lives in the `bolt-seo-geo` skill. When the workflow needs a tool, delegate there.

---

## Internalize this first: SEO and GEO drafting have converged

You do not write two versions. The same pattern earns a Google ranking and an AI citation:

> Build every searchable piece as a clean question-tree of self-contained, answer-first sections. Lead each section with a short, neutral, source-attributed answer rich in first-hand specifics. Expand below with persuasion, nuance, and comprehensive coverage in plain language.

That single pattern satisfies the ranking factors and the AI-citation levers at once. Only three tensions need managing, and all three are resolved *inside* a section, not across the page (see "The three tensions").

---

## The shared spine (every searchable piece)

### 1. Self-contained, answer-first sections (the keystone)
Every H2/H3 is a complete, standalone answer to the question its heading poses. Open with the direct answer in the first one or two sentences (~40 to 60 words), then expand with evidence, nuance, and detail. Restate the subject noun at the top of each section; no "as mentioned above," no pronouns reaching back to an earlier section. Test each section: if it were the only thing on the page, or screenshotted alone, would it fully answer its heading? Passage-level ranking, featured snippets, and AI extraction all pull sections out of context, so a section that depends on its neighbors cannot be ranked or cited.

### 2. Question-shaped headers, clean hierarchy
Phrase headers as the question a person would actually type or ask, in their words, not a clever rephrase. Keep a clean H1 to H2 to H3 hierarchy with no skipped levels. Useful stems: What is / How does / Why / Which (best) / Should.

### 3. Concrete, sourced specifics (highest-leverage move)
Replace every vague claim with a number, a unit, context, and an inline source. This one habit feeds Google's Experience signal and the top AI-citation levers (statistics, quotations, cited sources) simultaneously.
- Weak: "Websites can get expensive." / "Studies show AI improves productivity."
- Strong: "A small business website from an agency typically costs $8,000 to $30,000 in 2026." / "In our 2026 onboarding of ~40 B2B accounts, imports failed most often at the data step."
Attribute inline, in the same sentence or passage as the claim ("according to [named source, year]"), hyperlinked to the original source. For web-published content (blogs and website pages), never use a footnote or a separate references block; inline attribution is itself the citation lever. (Exception: downloadable long-form assets such as ebooks, whitepapers, guides, and reports follow the Chicago superscript plus Works Cited appendix format in bolt-TOV-and-guidelines, since they are not competing for AI citations.) Inline-and-hyperlinked is the default for all web copy; a rare page-level exception, like a gated-asset download page, is a deliberate one-off. Prefer primary sources and first-party data.

### 4. Information gain
Every section must add something that does not already exist on the internet: an original observation, a real workflow, an actual cost breakdown, an honest tradeoff, a before/after with specifics. If a section could be written by someone who has never used the product, it adds nothing and earns nothing.

### 5. Entity-first, natural language
Write about the named real-world things (products, companies, concepts), not search phrases. Use full proper nouns on first mention in each section and tie each to its category ("Bolt.new, an AI app builder, ..."). Cover the related entities and subtopics a knowledgeable writer would naturally mention. Keyword density is dead in both SEO and GEO; stuffing is the single worst tactic. Write fluently, around a 7th to 9th grade reading level.

### 6. Definitive, non-hedged claims
Commit to a position where the evidence supports it. Cited and extracted text skews definitive; hedged "some say X, others Y" prose gives an engine nothing to lift and a reader nothing to trust. Hedge only on genuine uncertainty (and accuracy always wins). Pairs with noslops's specificity and anti-hedging rules.

### 7. Liftable structures
AI engines lift these near-verbatim and readers scan them:
- Comparison tables, each preceded by a plain sentence saying what the table shows.
- Bullet lists where each bullet is a complete standalone statement, not a fragment that needs the stem to parse.
- Numbered steps for any process or how-to.
- FAQ blocks of real questions with ~40 to 60 word, single-intent answers.

### 8. Freshness in the prose
Date claims in the sentence itself ("as of 2026"), use current-year stats, and give living pages a visible "last updated" line plus a one-line changelog. Refresh the actual numbers, never just the date, and never fake a date. AI engines rotate citations toward fresh content more aggressively than traditional search does.

---

## The three tensions (decide these inside each section)

Almost every SEO drafting rule now also serves GEO. Only three trade-offs remain, and each is resolved within the section, not by choosing one discipline over the other:

1. **Tone.** Lead each section with a neutral, factual answer (this wins the citation and the snippet), then layer brand voice and persuasion *below* the answer. Promotional tone up top measurably suppresses AI citation.
2. **Length.** Be comprehensive at the *page* level and concise at the *passage* level: many self-contained answer blocks under question headings, not one long undifferentiated essay.
3. **Stat and citation density.** Lean heavier on sourced statistics, quotations, and citations than legacy SEO instincts suggest (they are the strongest AI-citation levers), but every one must be attributed and naturally placed. Aim for "specific and sourced," not "stat-stuffed."

---

## Engine notes (FAST-MOVING: review monthly)

The engines barely overlap in what they cite, so write for retrieval and extraction, not for one blue-link rank.
- **ChatGPT:** favors an encyclopedic, definitional register and established entities; front-load the answer.
- **Perplexity:** searches live on every query and weights freshness heavily; be the cleanest extractable source and match conversational phrasing.
- **Google AI Overviews:** extracts tight standalone passages; strip promotional tone; question-shaped H2s plus stats win.
- **Gemini:** treat like AI Overviews until per-engine data exists.
- **Copilot:** draws from Bing's index but selection is not pure rank; lean on structure and readability.

---

## Cadence

- **DURABLE (quarterly review):** the shared spine (sections 1 to 8), the entity approach, E-E-A-T-in-prose, specificity, definitive language, liftable structures.
- **FAST-MOVING (monthly review):** the engine notes above, the exact numbers (the 40 to 60 word answer, the ~150 word passage, snippet sizes, freshness windows), and any llms.txt / markdown-first conventions. This file is wired into write-strike's monthly source-file check as the fast-moving layer; re-verify the FAST-MOVING items there.

---

## Source anchors

Princeton/Georgia Tech/Allen AI GEO study (KDD 2024, arXiv 2311.09735) for the citation-lever ranking (statistics, quotations, cited sources at the top; keyword stuffing at the bottom); Google Search Central helpful-content guidance for E-E-A-T and the experience pillar; published 2025 to 2026 analyses of per-engine citation behavior for the engine notes. Treat specific percentages as directional; the ranking of tactics is stable, the exact figures are not.
