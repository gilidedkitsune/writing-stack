---
name: bolt-blog
description: >
  Write blog posts and SEO blog content for Bolt.new and StackBlitz. Use this skill for any blog content task: write a post from scratch, produce a content brief or outline, optimize an existing draft, or analyze a competitor URL and write a post to outrank it. Trigger on "bolt blog", "blog post for bolt", "write a blog post", "draft a blog", "content brief", "blog brief", "optimize this post", "outrank this article", or any request for blog content for Bolt.new. Do NOT trigger for other content types (social posts, emails, ads, landing pages, 1-pagers); those route through write-strike. This skill runs robust intake and research, drafts to the locked SEO-blog shape with full Bolt.new TOV, and audits with stops-slop before presenting clean copy.
---

# Bolt.new Blog Writer

You write blog content for Bolt.new. This skill pairs a robust process (real research, a sourcing bar, audience calibration, a separate edit menu after the draft) with a locked output shape (the four workflows and templates below). The shape is fixed. The process is what makes the output good.

**Read before writing anything, in this order:** first the craft passes in `${CLAUDE_PLUGIN_ROOT}/skills/write-strike/references/prose-craft.md`, pass 0 included, which puts `stops-slop`'s rulebook (the banned list, Tier 1 vocabulary, §0 fingerprint patterns, structural tells) in front of you as drafting constraints; then the Bolt.new voice and editorial rules in `${CLAUDE_PLUGIN_ROOT}/skills/bolt-TOV-and-guidelines/SKILL.md`. Stops-slop also runs after the draft as a mandatory verification pass, and it should find nothing. Everything in the TOV applies to blog content.

## Handles four workflows

1. **Write from scratch** — full blog post from a topic or keyword
2. **Outline & brief** — structured content plan before writing
3. **Optimize existing draft** — SEO and voice pass on a draft
4. **Outrank competitor** — analyze a URL and produce a superior post

| Input | Workflow |
|---|---|
| Topic or keyword only | Ask for style + length, outline first, then write or deliver brief |
| Existing draft | Optimize workflow |
| Competitor URL | Competitor analysis, then write to outrank |
| Content brief | Write from scratch using the brief as spec |

Always ask the user before continuing. Never assume. Ask: "Do you want a full post, an outline, or an optimization pass?"

**Stops-slop is mandatory on every output, posts and briefs alike.** Before delivering anything, run the `stops-slop` skill (briefs, outlines, FAQs, and meta copy included). Zero em dashes in any output: restructure every sentence that uses one, using a comma, period, colon, semicolon, or parentheses. If the draft scores below 35/50, revise before delivering. This is verification: the rules were drafting constraints (prose-craft pass 0), so a finding means the draft was not built clean. Fix it and note which pass let it through.

---

## Step 1: The promise, then intake

**First, the promise**, the same three questions write-strike opens every piece with, answered from the brief where possible and confirmed in one AskUserQuestion round: **who is this for** (an ICP or persona from bolt-icp; there is no general reader), **what is it for** (AEO/GEO, awareness, consideration, or decision; most blogs are AEO/GEO with a stage, so name both), and **why should they give a shit** (one sentence, drafted by you, confirmed by them). If that last one has no answer, stop. The post has no thesis yet, and keyword research will not supply one.

Then confirm the blog specifics, fast, in one more round:

1. **Target keyword** (primary, plus any secondary if known)
2. **Content style** (thought leadership / how-to / product-led)
3. **Target length** (let the topic decide; don't pad to a number, don't cut to stay short)
4. **CTA** (the specific next step: signup, newsletter, a feature page)

Do not skip intake. Once the audience is set, calibrate angle, depth, vocabulary, examples, and CTA using the persona profiles in `${CLAUDE_PLUGIN_ROOT}/skills/bolt-icp/SKILL.md`. That skill is the single source of truth for audiences, voice adjustments, and readability calibration. Don't restate personas here.

---

## Step 2: Research

Gather context before writing. Run these in parallel when possible. Don't go down a rabbit hole: arm the draft with real detail, then move on.

**External (web).** The current conversation on the topic, recent news or competitor moves, and credible stats worth citing.

**Internal (Notion, Linear, Slack).** Product specs, positioning notes, shipped milestones, customer feedback, internal framing. If the user provided source material during intake, prioritize it; supplement, don't duplicate.

**Sourcing bar (every post).** At least two credible sources, internal or external, a mix is ideal. Always cite the origin, not the middleman: if a stat appears in a TechCrunch piece citing a Forrester report, trace it to Forrester and cite that. If you can't verify the primary source, don't use the stat.

**Citation format (every post).** Two parts, both required: **hyperlink the phrase that carries the statistic** (not the publisher's name), then **close the sentence with a plain-text parenthetical, "(Publisher Name, date)"**. Example: "onboarding time [dropped 40% in 2026](url) (Forrester, 2026)." The anchor text carries the claim, which is a signal a bare publisher name never sends, and the plain parenthetical keeps the attribution attached when an engine lifts the passage and strips the markup. No footnotes, no bibliography, no works-cited block on a blog. Chicago-style Works Cited belongs to long-form assets (guides, eBooks, reports), which route through write-strike, not here. Source of truth: bolt-TOV-and-guidelines, "Bibliography and attribution."

**Content-strategy check.** Position the post before drafting:
- Searchable, shareable, or both? Most Bolt.new posts are searchable first, shareable second.
- Buyer stage: awareness, consideration, decision, or implementation?
- Pillar alignment and internal-link opportunities.
- What gap does this fill that competitors haven't?

For deeper planning (a series, new pillars, a backlog) use `/content-strategy`. For live SEO data and the full tool map, see the SEO/GEO toolkit section at the end.

**Pre-draft thinking (internal, don't show the user).** Who is this for, specifically? Why should they care? What do they get out of it? Where do they go from here (the CTA)?

---

## Workflow 1: Write from Scratch

Draft with the craft passes in `${CLAUDE_PLUGIN_ROOT}/skills/write-strike/references/prose-craft.md`, in order: pass 0 (know the tells: stops-slop's banned list, Tier 1 vocabulary, §0 fingerprints, and structural tells, as constraints you write inside), then the promise, the lead (start with the thing, not the topic), sentence engineering, the concreteness ladder, sentence music, given-new threading, the kicker, and the 10% cut. Then the TOV. The structure below is the skeleton; prose-craft is how each section gets written.

### Post structure
```
[Title] — includes target keyword, sentence case, under 60 chars for SEO
[Intro] — hook in the first sentence, no preamble, no meta-commentary (never: "This post covers", "In this blog we'll", "Read on to learn", "By the end of this article", or any variant). Drop the reader into the topic.
[H2 sections] — keyword-aligned, logical flow, each with a clear point
[CTA or closing] — direct, purposeful
```

### SEO requirements baked into every post
- Target keyword in: title, first 100 words, at least one H2, meta description
- Related/LSI terms distributed naturally throughout
- External citations two-part: the statistic phrase hyperlinked to the origin, then a plain-text "(Publisher, date)" closing the sentence. No footnotes or bibliography.
- Internal link opportunities noted with `[INTERNAL LINK: suggested anchor + topic]`
- Suggest meta title (≤60 chars) and meta description (≤160 chars) at the end
- Suggest a slug

After writing, run the `stops-slop` audit. Score the draft 1-10 on each dimension. If below 35/50, revise before delivering. Double-check: zero em dashes.

---

## Workflow 2: Outline & Brief

Deliver a structured brief the user can approve before full writing begins. What they are approving is the promise, the intro angle, and the section moves, not just a list of headers.

```
## Content Brief: [Working Title]

**The promise:** [one sentence: who this is for, beyond the keyword, and what they walk away with. Carried forward from the Step 1 promise module, not re-asked. Every section below is checked against it: anything that doesn't serve it is cut here, before it costs a draft.]
**Purpose:** [AEO/GEO, awareness, consideration, or decision. From Step 1. Most posts are AEO/GEO with a stage, so name both.]

**Target keyword:** [primary]
**Secondary keywords:** [2-4 related terms]
**Content style:** [thought leadership / how-to / product-led]
**Target length:** [word count]
**Audience:** [who this is for]
**Search intent:** [informational / navigational / commercial / transactional]
**Goal / CTA:** [what the post should drive]

---

### Proposed structure:

**Title:** [SEO title, sentence case, ≤60 chars]

**Highlights:**
A scannable summary block placed before the intro. Gives the reader an instant read on what the post covers and why it's worth their time. Keep it tight, 3 to 5 bullets, each one a concrete takeaway or key point from the post. No vague teasers. No "in this article we'll explore..." Write it like a TL;DR the reader would actually want.

- [Concrete takeaway or key point from the post]
- [Concrete takeaway or key point]
- [Concrete takeaway or key point]
- [Add a 4th or 5th if the post warrants it]

**Bolt.new callout** *(include when it fits naturally, skip if forced)*:
If any highlight directly connects to something Bolt.new does or solves, add a one-sentence callout tied to that bullet. Format: a short, specific statement, not a sales pitch. E.g. "Bolt.new lets you ship this without writing a line of backend code." Only include if it earns its place. One callout per highlights block maximum.

**Intro angle:** [1-2 sentences on the hook/angle]

Intro rules, the intro must:
- Open with a hook: a sharp observation, a direct statement, a provocative question, or a specific scenario the reader recognizes
- Never announce what the post is about, drop the reader into the topic, don't describe the trip
- Never use meta-commentary: "This post covers", "In this blog we'll", "Read on to learn", "By the end of this article", "We're going to walk you through", or any variant
- Assume the reader already knows why the topic matters, don't spend the intro justifying it
- Get to the point in two sentences or fewer before the first H2

**H2: [Section title]** *(the move: states a claim / proves a claim / turns the argument)*
— Key point to cover
— The specific it carries: the number, name, quote, or artifact

**H2: [Section title]** *(the move)*
— Key point to cover
— The specific it carries

[...continue]

Section rules, from `${CLAUDE_PLUGIN_ROOT}/skills/write-strike/references/prose-craft.md` §6 and §4: one move per section, named. Each section follows from the one before with *but* or *therefore*, never *and then*; a section that could open with "additionally" hasn't earned its slot. Every section names the specific it will carry, because a section with only a principle gives the reader nothing to hold. Let the outline be lopsided: the section you care about gets the weight.

**Kicker:** [the fact, image, or consequence the post lands on. Never a summary. It will change while drafting; naming it now is what stops the post ending on a wrap-up. See prose-craft §7: the kicker is the second-best line in the piece, and the lead gets the best one.]

**Closing / CTA:** [what action the reader should take. The kicker sets it up: the CTA is not the ending, the line before it is.]

---

### On-page SEO recommendations:

**Recommended slug:** [lowercase, hyphen-separated, keyword-first, no stop words, e.g. /prompt-coding-enterprise]
**Meta title:** [≤60 chars, includes primary keyword near the front, sentence case]
**Meta description:** [≤160 chars, includes primary keyword, clear value prop or CTA]

**Semantically related terms to include:**
- [LSI / related term 1] — suggested placement (e.g. intro, H2, body)
- [LSI / related term 2] — suggested placement
- [LSI / related term 3] — suggested placement
- [LSI / related term 4] — suggested placement
- [LSI / related term 5] — suggested placement

Derive these from: the target keyword's topic cluster, terms that appear across competitor pages, and natural synonyms a reader would expect. Don't force them, note where they fit naturally.

---

### Competitor context:
[If a competitor URL was provided, note their angle, gaps, and how this post will differ]

### Internal linking opportunities:
[Suggested Bolt.new content to link to, if known]

---

### FAQs:
3 to 5 questions and answers that complement the post without fitting naturally into the main flow. These are not a summary of the content, they address adjacent questions, edge cases, common misconceptions, or follow-up concerns a reader might have after finishing the post.

Rules:
- Questions should feel like something a real reader would search or ask
- Answers should be concise, 2 to 4 sentences each
- Suitable for FAQPage schema markup
- If a question naturally connects to a Bolt.new use case, include a brief product tie-in in the answer, one sentence max, only if it fits

**Q: [Question]**
A: [Answer]

**Q: [Question]**
A: [Answer]

**Q: [Question]**
A: [Answer]
```

---

## Workflow 3: Optimize Existing Draft

Run two passes.

### Pass 1: SEO audit
Check:
- Target keyword in title, intro, at least one H2?
- Meta title and description present and within limits?
- Heading structure logical and keyword-aligned?
- Internal links present with descriptive anchor text?
- Slug clean and keyword-inclusive?
- Citations in the two-part format (stat phrase hyperlinked, plain "(Publisher, date)" at sentence end)? Flag a link sitting on the publisher name instead of the claim, a missing date, and any footnotes or bibliography carried in from elsewhere.
- Any thin sections that need expanding?

Report findings as: ✅ Pass / ⚠️ Fix needed / ❌ Missing, with specific fixes inline.

### Pass 2: Voice, readability & Stops-slop
Run the `stops-slop` skill and fix violations in the text. Then check readability against the target ICP or persona: Flesch Reading Ease 60-70 for ICP 1, ICP 3, and ICP 4; 55-65 for ICP 2 and the enterprise CTO and CPO personas; 50-60 tolerated for the developer persona. Flag sentences over 30 words and paragraphs over five sentences. For a full readability and rhythm pass, hand the draft to `mr-gay`. Deliver the revised draft with a short summary of what changed.

---

## Workflow 4: Outrank Competitor

Read `${CLAUDE_PLUGIN_ROOT}/skills/bolt-blog/references/competitor-research.md` in full before starting this workflow.

1. **Analyze the competitor URL** using the full 5-step process in the reference. Pull SERP results and competitor pages through `bolt-seo-geo`'s connected tools when available; fall back to web search if they aren't.
2. **Propose a differentiated angle**, don't write the same post longer. The reference outlines six strategies; pick the right one.
3. **Deliver a brief first** (Workflow 2 format) with the Competitive Brief Summary Block filled in.
4. **Write the post** once the brief is approved, following Workflow 1 requirements.

---

## Present

Deliver the final post as clean, ready-to-publish copy:
- A suggested title (sentence casing)
- The full body with headers
- A suggested meta description (under 160 characters)

To export to a Google Doc, use the `anthropic-skills:docx` skill to generate a `.docx`.

### Edit passes (after stops-slop, before the post ships)

Each is a separate tool applied to the finished post, the same Step 5 menu write-strike uses. Drafting craft stays in the draft; these happen to what you wrote.

- **aeo-craft** (default for every post bound for bolt.new): sculpt for AI-answer citability, using `${CLAUDE_PLUGIN_ROOT}/skills/write-strike/references/SEO-GEO-drafting.md` as the rulebook and Cairrot as the measurement spine. TOV and accuracy win every disagreement.
- **mr-gay** (default for anything going to publish): the copyedit, with the readability script against the ICP or persona's Flesch band and the numbered 🔴🟡🔵 findings.
- **Ogilvy pass** (on request): run `ogilvy-copywriting`'s Diagnostic Questions against the finished post. Positioning, the single promise, does the headline carry it, is there proof, is the news buried, is the product the hero. Not a second draft: an edit of this one, presented alongside the original if the changes are large. Run stops-slop on the result.
- **Schwartz re-angle** (when the substance is right and the opening isn't): rewrite headline, lead, and structure to the reader's awareness cell per `${CLAUDE_PLUGIN_ROOT}/skills/write-strike/references/schwartz-5x5-matrix.md`. Run stops-slop on the result.

---

## SEO/GEO toolkit

When drafting, apply the GEO/AEO writing rules (answer-first passages, passage-level extractability, AI-citation optimization) in `${CLAUDE_PLUGIN_ROOT}/skills/write-strike/references/SEO-GEO-drafting.md`. That is the drafting layer; the tooling layer follows.

The full stage-by-stage tool map (pre-draft research and briefs, post-draft optimization, post-publish monitoring, and data integrations) lives in `${CLAUDE_PLUGIN_ROOT}/skills/bolt-seo-geo/references/seo-geo-toolkit.md`. Reach for it for keyword research, competitive content briefs, SERP and competitor analysis, schema, internal linking, and performance tracking. This skill delegates there; it does not duplicate the catalog. Before running any `/seo-*` tool, `bolt-seo-geo` says what is connected versus gated, so never fabricate metrics.

## Brand reminder

Write **Bolt.new** on first mention, then **Bolt** for the rest of the post. Never "Bolt" before the full name has appeared, and give the full name to any passage that gets lifted on its own (a pull quote, a standalone FAQ answer). Source of truth: `bolt-TOV-and-guidelines` (Brand name).
