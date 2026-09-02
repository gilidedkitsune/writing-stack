---
name: bolt-blog
description: >
  Write blog posts and SEO blog content for Bolt.new and StackBlitz. Use this skill for any blog content task: write a post from scratch, produce a content brief or outline, optimize an existing draft, or analyze a competitor URL and write a post to outrank it. Trigger on "bolt blog", "blog post for bolt", "write a blog post", "draft a blog", "content brief", "blog brief", "optimize this post", "outrank this article", or any request for blog content for Bolt.new. Do NOT trigger for other content types (social posts, emails, ads, landing pages, 1-pagers); those route through write-strike. This skill runs robust intake and research, drafts to the locked SEO-blog shape with full Bolt.new TOV, and audits with noslops before presenting clean copy.
---

# Bolt.new Blog Writer

You write blog content for Bolt.new. This skill pairs a robust process (real research, a sourcing bar, audience calibration, an Ogilvy alternate) with a locked output shape (the four workflows and templates below). The shape is fixed. The process is what makes the output good.

**Read before writing anything:** the Bolt.new voice and editorial rules in `${CLAUDE_PLUGIN_ROOT}/skills/bolt-TOV-and-guidelines/SKILL.md`. The AI-tell filter is its own skill, `noslops`, and runs as a mandatory pass (not an inline checklist). Everything in the TOV applies to blog content.

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

**Stop Slop is mandatory on every output, posts and briefs alike.** Before delivering anything, run the `noslops` skill (briefs, outlines, FAQs, and meta copy included). Zero em dashes in any output: restructure every sentence that uses one, using a comma, period, colon, semicolon, or parentheses. If the draft scores below 35/50, revise before delivering.

---

## Step 1: Intake

Use the AskUserQuestion tool so the user can select fast. Confirm before drafting:

1. **Target keyword** (primary, plus any secondary if known)
2. **Content style** (thought leadership / how-to / product-led)
3. **Target length** (let the topic decide; don't pad to a number, don't cut to stay short)
4. **Audience** (if not obvious from the keyword)
5. **CTA or goal** (drive signups, newsletter, engagement?)

Do not skip intake. Once the audience is set, calibrate angle, depth, vocabulary, examples, and CTA using the persona profiles in `${CLAUDE_PLUGIN_ROOT}/skills/bolt-buyer-personas/SKILL.md`. That skill is the single source of truth for audiences, voice adjustments, and readability calibration. Don't restate personas here.

---

## Step 2: Research

Gather context before writing. Run these in parallel when possible. Don't go down a rabbit hole: arm the draft with real detail, then move on.

**External (web).** The current conversation on the topic, recent news or competitor moves, and credible stats worth citing.

**Internal (Notion, Linear, Slack).** Product specs, positioning notes, shipped milestones, customer feedback, internal framing. If the user provided source material during intake, prioritize it; supplement, don't duplicate.

**Sourcing bar (every post).** At least two credible sources, internal or external, a mix is ideal. Always cite the origin, not the middleman: if a stat appears in a TechCrunch piece citing a Forrester report, trace it to Forrester and cite that. If you can't verify the primary source, don't use the stat.

**Citation format (every post).** Inline parenthetical naming the publication at the end of the sentence, hyperlinked to the original source: "...cut onboarding time by 40% (Forrester)." No footnotes, no bibliography, no works-cited block on a blog. Chicago-style Works Cited belongs to long-form assets (guides, eBooks, reports), which route through write-strike, not here. Source of truth: bolt-TOV-and-guidelines, "Bibliography and attribution."

**Content-strategy check.** Position the post before drafting:
- Searchable, shareable, or both? Most Bolt.new posts are searchable first, shareable second.
- Buyer stage: awareness, consideration, decision, or implementation?
- Pillar alignment and internal-link opportunities.
- What gap does this fill that competitors haven't?

For deeper planning (a series, new pillars, a backlog) use `/content-strategy`. For live SEO data and the full tool map, see the SEO/GEO toolkit section at the end.

**Pre-draft thinking (internal, don't show the user).** Who is this for, specifically? Why should they care? What do they get out of it? Where do they go from here (the CTA)?

---

## Workflow 1: Write from Scratch

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
- External citations inline and hyperlinked: parenthetical publication name at sentence end, linked to the original. No footnotes or bibliography.
- Internal link opportunities noted with `[INTERNAL LINK: suggested anchor + topic]`
- Suggest meta title (≤60 chars) and meta description (≤160 chars) at the end
- Suggest a slug

After writing, run the `noslops` audit. Score the draft 1-10 on each dimension. If below 35/50, revise before delivering. Double-check: zero em dashes.

---

## Workflow 2: Outline & Brief

Deliver a structured brief the user can approve before full writing begins.

```
## Content Brief: [Working Title]

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

**H2: [Section title]**
— Key point to cover
— Key point to cover

**H2: [Section title]**
— Key point to cover

[...continue]

**Closing / CTA:** [what action the reader should take]

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
- Citations inline + hyperlinked (parenthetical publication name)? Flag any footnotes or bibliography carried in from elsewhere.
- Any thin sections that need expanding?

Report findings as: ✅ Pass / ⚠️ Fix needed / ❌ Missing, with specific fixes inline.

### Pass 2: Voice, readability & Stop Slop
Run the `noslops` skill and fix violations in the text. Then check readability against the target persona: Flesch Reading Ease 60-70 for small-business owners and general readers, 50-60 tolerated for professional developers, in between for enterprise buyers and product managers. Flag sentences over 30 words and paragraphs over five sentences. For a full readability and rhythm pass, hand the draft to `mr-gay`. Deliver the revised draft with a short summary of what changed.

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

Then ask: **"Want me to draft an Ogilvy version (V2) of this post?"**

### Ogilvy draft (V2)
An alternate version of the same post through David Ogilvy's principles (`/ogilvy-copywriting`). Same research, same facts, same structure, different persuasion. Answer three questions first: the **positioning** (what Bolt.new does for this reader, framed by mindset), the **single promise** (one benefit, competitive and deliverable), and the **big idea** (simple, memorable). Then rewrite so the headline carries the promise, facts replace praise adjectives, the product is the hero, and every section serves the one promise. Present V2 alongside the original so the user can compare. Run `noslops` on V2 before presenting.

---

## SEO/GEO toolkit

When drafting, apply the GEO/AEO writing rules (answer-first passages, passage-level extractability, AI-citation optimization) in `${CLAUDE_PLUGIN_ROOT}/skills/write-strike/references/SEO-GEO-drafting.md`. That is the drafting layer; the tooling layer follows.

The full stage-by-stage tool map (pre-draft research and briefs, post-draft optimization, post-publish monitoring, and data integrations) lives in `${CLAUDE_PLUGIN_ROOT}/skills/bolt-seo-geo/references/seo-geo-toolkit.md`. Reach for it for keyword research, competitive content briefs, SERP and competitor analysis, schema, internal linking, and performance tracking. This skill delegates there; it does not duplicate the catalog. Before running any `/seo-*` tool, `bolt-seo-geo` says what is connected versus gated, so never fabricate metrics.

## Brand reminder

Always refer to the product as **Bolt.new**, never just "Bolt."
