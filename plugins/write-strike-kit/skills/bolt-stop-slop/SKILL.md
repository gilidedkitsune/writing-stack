---
name: bolt-stop-slop
description: >
  Audit and clean Bolt.new content for AI writing patterns. Use this skill after drafting any Bolt.new or StackBlitz content to eliminate AI tells, slop, and formulaic writing. Trigger on: "stop slop", "slop check", "audit this draft", "AI tells", "clean up the copy", or any request to review Bolt.new content for AI-generated patterns. Also trigger automatically as part of the bolt-blog workflow (Step 6). Works on any prose: blogs, social, emails, landing pages, thought leadership.
---

# Bolt stop slop

One pass. Catch everything. This skill replaces both the AI-tells audit and the stop-slop check with a single, unified filter.

Read the draft once through, applying every rule below simultaneously. Fix violations in place. Don't flag them for later. Rewrite them now.


## 0. Fingerprint check (mechanical, first)

Before the read-through, sweep for P0 fingerprints: near-certain AI artifacts that end credibility on sight. These are search-and-fix, no judgment required:

- **Unfilled placeholders:** [Your Name], [INSERT LINK], [Company], 2026-XX-XX
- **Citation markup leaks:** oaicite, contentReference, turn0search, attached_file, grok_card
- **AI-tool URL parameters:** utm_source=chatgpt.com / openai / copilot in any link
- **Knowledge-cutoff disclaimers:** "As of my last update...", "I don't have access to real-time..."
- **Chatbot artifacts:** "I hope this helps", "Let me know if...", "Great question", "Certainly!"

Any one of these shipping in public is worse than every other violation in this file combined.


## 1. Kill dead language

Phrases die on sight; words are tiered. See [references/banned.md](references/banned.md) for the full catalog:

- **Phrases** (throat-clearing, vague attribution, chatbot artifacts, compulsive summaries, future closers, false breadth): kill every instance.
- **Tier 1 words** (delve, tapestry, seamless, leverage-as-verb...): a finding on sight, any register.
- **Tier 2 words** (crucial, robust, foster, streamline...): legitimate alone; a finding in clusters of 2+ per paragraph. Technical terms (robust, scalable, ecosystem) are fine in dev-facing prose.
- **Tier 3 words** (significant, innovative, compelling...): a finding only at density, 3+ per ~300 words.

This is the density principle from §10 made mechanical: a single Tier 2 word is not slop; a pileup is. The short version for phrases: if it could appear in any article about any topic and still make grammatical sense, it's filler. Cut it.


## 2. Fix the structure

AI defaults to a small set of structural patterns. They feel polished on first read but become obvious in aggregate. See [references/structures.md](references/structures.md) for the full catalog with examples.

The patterns that matter most:

### Binary contrasts / negation-reframes
Any sentence that negates one framing then asserts a corrected one. "This isn't X. This is Y." / "Not X. Y." / "Forget X. This is Y." / "Less X, more Y." / "The answer isn't X. It's Y."

State Y directly. The reader doesn't need the runway.

### Dramatic fragmentation
Sentence fragments used as punchlines to create false drama. "Speed. Quality. Cost." / "[Noun]. That's it. That's the [thing]." / "X. And Y. And Z."

Complete sentences. Trust content over presentation.

### Rhetorical setups
Phrases that announce insight rather than deliver it. "What if I told you..." / "Here's what I mean:" / "Think about it:" / "Once you see it this way, you can't unsee it."

Make the point. Let readers draw conclusions.

### False agency
Giving inanimate things human verbs. "The complaint becomes a fix." "The decision emerges." "The market rewards."

Name the human. Someone fixed it. Someone decided. Buyers paid for it. If no specific person fits, use "you."

### Narrator-from-a-distance
Floating above the scene. "Nobody designed this." "This happens because..." "People tend to..."

Put the reader in the room. "You" beats "People." Specifics beat abstractions.

### Overly smooth connectors
Paragraph openers that create artificial flow. "This belief defines how we build Bolt.new." "This is personal for us." "That same pattern shows up across the team."

If the paragraph follows logically from the prior one, it doesn't need a connector. If it needs one, use something a person would say out loud.

Also in the full catalog, same severity as the patterns above: **superficial -ing analyses** ("..., highlighting the importance of"), **false ranges** ("from startups to Fortune 500s"), **synonym cycling** (developers → engineers → practitioners), **formulaic conclusions** ("Despite these challenges..."), and **significance inflation** ("stands as a testament to"). See [references/structures.md](references/structures.md).


## 3. Enforce voice rules

### Active voice
Every sentence needs a human subject doing something. Passive voice hides the actor and drains energy. "X was created" becomes "[Person] created X." "Mistakes were made" becomes "[Person] made mistakes."

Find the actor. Put them at the front of the sentence.

### No adverbs
Kill all adverbs. No -ly words. No softeners ("really," "just," "simply"), no intensifiers ("genuinely," "truly," "deeply"), no hedges ("honestly," "actually," "fundamentally").

If an adverb is propping up a weak verb, replace the verb. "Moved quickly" becomes "sprinted." "Really important" becomes "critical," or better, show why it matters instead of announcing that it does.

### No em dashes
Zero em dashes in the final copy. Restructure every sentence that uses one. Use a comma, a period, a colon, a semicolon, or parentheses. Pick the punctuation that fits the sentence's rhythm.

### Copula inflation
Use "is," "are," "was," "has." Don't dress them up. "Serves as," "stands as," "represents," "boasts," "features," "offers": these are "is" in a blazer. "The platform serves as a hub" is just "the platform is a hub." When a plain copula works, use it.

### Contractions
Use them. "Don't" beats "do not." "Can't" beats "cannot." Formal prose is not the goal.

### Specificity over declaration
No vague declaratives. "The reasons are structural" says nothing. "The implications are significant" says nothing. Name the specific reason. Name the specific implication. If you can't name it, you don't know it well enough to write about it.

No lazy extremes doing vague work ("every," "always," "never," "everyone," "nobody"). Use specifics instead of sweeping claims.

### Uncertainty
When you're genuinely uncertain about a claim, say so plainly ("I think," "probably," "kinda"). Honest hedging is human. But don't soften facts you're confident about with qualifiers. State them directly.


## 4. Check the rhythm

### Sentence length
Vary it. Mix short punchy lines with longer ones. If three consecutive sentences match length, break one. Two short sentences in a row can work. Three in a row becomes staccato posturing.

### Lists
Two items beat three. AI defaults to tricolons (groups of three with escalating rhythm). One triple per piece is fine if it genuinely earns it. More than that is a pattern. Default to pairs.

### Paragraph endings
Vary how paragraphs end. If every paragraph closes with a punchy one-liner, it reads as a formula. Let some paragraphs end mid-thought and carry into the next.

### Sentence starters
Watch for Wh- word openers becoming a crutch. "What makes this hard is..." becomes "The constraint is..." or better, name the specific constraint directly. Don't start paragraphs with "So." Don't start sentences with "Look,".

### Quotability
If a sentence sounds like it belongs on a motivational poster or a LinkedIn carousel, rewrite it. Cut quotables.


## 5. Catch the second-generation tells

Copy scrubbed of the obvious tells grows its own. These survive the first pass, so hunt them on the second.

**Performed cleverness.** Surprising adjective-noun pairs that sound writerly: "confident lies," "elegant catastrophe," "quiet violence." They come from reaching for clever, not from knowing something. Replace with a concrete fact.

**Wisdom-shaped objects.** Sentences built like an insight that say nothing you could argue with: "And that tension never really goes away." Delete it, or make it specific and debatable.

**Perfect balance.** Every claim met with a qualifier, every paragraph the same length, every argument tidy. Real writing is lopsided. It spends where the writer cared and rushes the rest. Let it be uneven.

**Omniscient casual.** A voice that knows everything and admits no gaps. Writers who actually know a subject also know what they don't, and it shows. Let the friction show.

For worked before/after examples (what AI strips out of great copy, and why specific beats slop), see [references/slop-vs-gold.md](references/slop-vs-gold.md).


## 6. Build texture, don't just strip tells

Removing slop gets you clean. Clean isn't the same as human: a sterile, even, friction-free draft is its own tell. The fix is generative. Create the asymmetry a real writer leaves behind.

**Uneven density.** The part the writer cares about gets the most words. The boring part gets compressed or cut. Equal coverage reads as generated. Spend where it matters.

**Register mixing.** A real vocabulary is lumpy: a technical term in one line, "stuff" in the next. If every sentence draws from the same word pool, it reads as generated.

**Structural lopsidedness.** Let one paragraph run long because there was more to say, and one run short because there wasn't. Don't distribute length evenly, and don't alternate long-short for rhythm. Designed rhythm is detectable.

**Opinions that cost something.** "Impressive and a little troubling" is a hedge in an opinion's clothing. Commit: "the latency numbers are cherry-picked," or "this migration was a mistake and they know it." If you genuinely can't form a take, say so. Don't manufacture balance.

**First person that means something.** Skip "here's what stays with me." If you use "I," tie it to a real thought: "I read this twice and the second paragraph still contradicts the fourth."


## 7. Score it

Rate the draft 1-10 on each dimension:

| Dimension | Question |
|-----------|----------|
| Directness | Does it state things or announce them? |
| Rhythm | Varied or metronomic? |
| Trust | Does it respect the reader's intelligence? |
| Authenticity | Does it sound like a person wrote it? |
| Density | Is there anything you could cut without losing meaning? |

**Below 35/50: revise before presenting.** Go back through the draft and fix the weakest dimension first.


## 8. Second pass and self-audit

After revising, re-read the **rewrite**, not the original. Rewrites grow their own tells: recycled transitions, a copula swap that snuck back in, a fresh Tier 2 cluster. Ask one question — *"What makes this still read as AI-generated?"* — answer it in two or three blunt bullets, fix those, then score. One corrective pass is the cap; a third rarely finds anything new and costs a full regeneration.


## 9. Severity, channels, and what to preserve

**Severity (maps to mr-gay's Red/Yellow/Blue):**
- **P0 / Red** — fingerprints (§0) and vague attribution propping a factual claim. Never ships.
- **P1 / Yellow** — Tier 1 vocabulary, kill-on-sight phrases, structural patterns (§2). Fix before presenting.
- **P2 / Blue** — Tier 2/3 density, rhythm, and texture (§4–6). Fix in the revise loop; judgment applies.

**Channel calibration** (rules flex by destination; em dashes are zero everywhere):

| Channel | Adjustment |
|---|---|
| Blog / long-form / web | Full strength |
| Social | Structure rules relax (fragments and platform emoji conventions allowed); vocabulary tiers still enforced |
| Email | Full strength; subject lines may fragment |
| Docs / technical | Tier 2 technical words (robust, scalable, ecosystem, comprehensive) are legitimate where they carry real meaning; everything else full strength |

**Preserve on sight — never sand these off:**
- Specific, hard-to-fabricate detail (names, numbers, dates, first-hand observations)
- Mixed feelings and unresolved tension
- Era-bound references, and deliberate repetition of the right word
- Genuine asides, self-corrections, and lopsided emphasis

A scrub that removes these made the draft worse, not cleaner. If the rewrite is more polished but less alive, put the life back.


## 10. The editorial judgment call

The question is never "does this pattern exist in the text?" It's "is this an intentional rhetorical choice, or is AI defaulting to a pattern?"

Some content types (manifestos, speeches, pitch decks) earn more rhetorical energy than others. Blog posts and emails earn less. The problem is always density: when patterns appear at a frequency no human writer would produce organically.

Audit for pattern density first, not individual instances. Then read the whole thing out loud. If any sentence sounds performative or rehearsed, cut it.
