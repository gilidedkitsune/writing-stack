---
name: aeo-craft
description: >
  The AEO/GEO sculpting pass for Bolt.new content: audits and reshapes a finished draft so AI answer
  engines (ChatGPT, Perplexity, Google AI Overviews, Gemini, Copilot) can find, extract, and cite it,
  and plans the citability angle before drafting starts. Run it on EVERY blog or website piece bound
  for bolt.new after the stops-slop audit, and whenever the user says "AEO pass", "GEO pass", "aeo-craft",
  "optimize for AI citations", "will AI cite this?", "is this AEO/GEO optimized?", "citability", "make
  this liftable", or asks why a page isn't showing up in AI answers. Also run the Plan mode when a new
  piece targets a definitional or question-shaped query ("what is X", comparisons, how-tos) BEFORE the
  outline is locked. This is the house replacement for the generic /geo-content-optimizer: it knows the
  Bolt.new TOV, the consent tiers, the campaign's term strategy, and the Copydesk checks panel where present. Sculpting
  copy for machines never overrides writing for people: stops-slop and mr-gay still gate everything.
---

# AEO Craft

The sculpting pass. Other skills make the prose good; this one makes it **citable**: findable by retrieval, extractable in standalone passages, and safe to quote. It runs on drafts, not blank pages.

**Where it sits in the craft topology:** prose-craft builds prose → SEO-GEO-drafting guides searchable drafting → stops-slop catches AI tells → mr-gay diagnoses the writing → **aeo-craft sculpts for machine citability**. Read `${CLAUDE_PLUGIN_ROOT}/skills/write-strike/references/SEO-GEO-drafting.md` before running a pass: it is the rulebook this skill enforces, including the shared spine, the three tensions, and the per-engine notes (its FAST-MOVING section is the single source for engine behavior — don't duplicate it here, read it there).

**What this skill does not do:** keyword/SERP/traffic data (that's `bolt-seo-geo`, which also says what's connected — never fabricate metrics), drafting voice (bolt-TOV + prose-craft), AI-tell cleanup (stops-slop). If the draft hasn't passed stops-slop, send it there first; sculpting slop makes citable slop.

## The measurement spine

This skill used to run blind. It doesn't now. **Cairrot is the backbone**: bolt.new's live AI-answer data across ChatGPT, Gemini, Claude, Perplexity, AI Overviews, DeepSeek, and Grok. Read it before you sculpt and again after you publish. Everyone on the team can have it; setup is at the bottom of this file.

**Primary path: the Cairrot MCP connector.** Load its tools with ToolSearch, keyword `cairrot` (the server prefix is a UUID that changes between sessions, so search by name, never by prefix). Eleven tools, and what this skill uses them for:

- `list_projects`, `get_project`: orient. The bolt.new project is the one you want.
- `get_index_schema`, then `build_lucene_query`: learn the field names, then scope a query to a topic, a model, and a window.
- `search_mentions`: **named**. Answers where "Bolt.new" appears in the text.
- `search_citations`: **cited**. Answers that link a bolt.new URL. The gap between these two is this skill's whole job.
- `search_fanouts`: the sub-questions an engine actually ran to build its answer, which is the question tree (pass 2) written by the engine itself.
- `search_crawler_hits`: which AI crawlers fetched which pages, for pass 8's freshness and cluster-link checks.
- `search_sentiment_phrases`, `search_runs`, `generate_report`: sentiment, run history, and one rolled-up artifact when a readout needs it.

Tool names as of Sep 2026, mapped from the tool surface rather than from schemas; if they've moved, `list_projects` and `get_index_schema` will orient you, and the first live run should confirm the mapping above.

**Fallback: the `bolt-cairrot` REST puller**, on machines that have that skill installed (Taylor's does). `cairrot_pull.py topics --days 30` returns the same named and cited numbers per topic and per model, and `competitors` the leaderboard. Same API, same project, same numbers; only the transport differs. Never mix the two in one table without saying so, and never fabricate a number if both are unavailable: sculpt blind, flagged blind.

The one number that drives everything is **named vs. cited**. Named is the engine writing "Bolt.new" in the answer text. Cited is the engine linking a bolt.new URL. They move independently, and the gap between them is this skill's entire job. Over the 30 days to Sep 3 2026, bolt.new was named in 6% of tracked answers and cited in 0.4%: engines know us and credit someone else.

**How to pull it.** Over the MCP, scope `search_mentions` and `search_citations` to the piece's topic and a 30-day window (build the filter with `build_lucene_query` after reading `get_index_schema`). With the puller, `cairrot_pull.py topics --days 30`. Either way, name the window on every number.

**The diagnosis table.** Pull the topic closest to the piece, then read the pair:

| Named | Cited | What it means | Passes to run hardest |
|---|---|---|---|
| High | Low | Engines already retrieve us and credit someone else. The best target on the board: the page is the only thing failing. | 3 answer-first, 4 definition, 5 receipts, 6 liftable |
| Low | Low | A retrieval problem, not a citability problem. Sculpting won't fix it. | 1 term, 2 tree, then reconsider the target |
| Low | High | Rare. Narrow authority. Protect it and build the cluster around it. | 8 freshness, cluster links |
| High | High | Working. Don't re-sculpt it; go find the next topic. | none |

**Per-model targeting.** Cairrot breaks every topic down by engine (a model filter on `search_mentions` and `search_citations` over the MCP, or the `topics` view in the puller), so sculpt for the engine you're losing rather than the one you already win. As of the 30 days to Sep 3 2026, "browser-based full-stack app creation" ran Perplexity 43%, AI Overviews 15%, Claude 7%, Gemini 3%, ChatGPT 3%, DeepSeek 0%: a Perplexity-shaped page ChatGPT ignores. The per-engine behavior notes stay in `SEO-GEO-drafting`'s FAST-MOVING section; Cairrot tells you which of those notes matter for this piece.

## Three modes

**Plan mode** (pre-outline). The user is choosing what a piece targets. Deliver a citability plan: term winnability call, the question set, the liftable-format plan, and the receipts inventory. Ten minutes here beats an hour of post-draft surgery.

**Sculpt mode** (post-draft, the default). Pull the Cairrot baseline for the target topic, then run the nine passes below in order against the finished draft. Apply fixes in place unless the user asked for audit-only; either way, report findings in the numbered dot format (🔴 Red 1 / 🟡 Yellow 2 / 🔵 Blue 3, stable numbers so the user can work items by handle). Severity: Red = the piece can't earn citations or makes an unsafe claim; Yellow = a lever is being left unpulled; Blue = polish.


**Measure mode** (post-publish). Baseline the target topic before the piece ships, re-pull after the engines have re-crawled, and report the movement on **named and cited separately** (they move independently, and only cited means the sculpt worked). This is the only feedback loop the skill has. Without it, every sculpt is a guess that never gets graded.

## The nine passes

### 1. Term winnability

Before optimizing for a term, ask two questions: can the term be won, and are we already in the answer without credit?

Start with Cairrot's per-topic named-versus-cited view (MCP: `search_mentions` against `search_citations`, scoped to the topic; puller: `topics`). A topic where we are **named often and cited rarely** is the highest-value target available, because retrieval already works and only the page is failing. A topic where we are neither named nor cited is a slower, more expensive bet, and often the wrong one for a sculpting pass. A **greenfield term** (nobody owns it in AI answers: "prompt queueing," "clustered prompting") gets the full definitional play: own the bare question "What is X?". An **owned term** (a forty-year-old CS concept, a competitor's brand, a saturated head query) cannot be taken head-on — every engine already has its answer. Scope it to the entity instead: not "What is a message queue?" (Kafka wins that forever) but "What is the message queue **in Bolt.new**?". The scoped question is winnable because only we can answer it. When the term choice is still open, say plainly which name is winnable and what the unwinnable name costs — that argument has changed launch naming before.

To check what's winnable: Cairrot's topic and competitor views (MCP: `search_mentions` and `search_citations` plus `search_fanouts` for who else the engines pull in; puller: `topics` and `competitors`) for where we already appear and who outranks us in the same answers, or a quick web check of who answers the bare question today.

### 2. The question tree

Every H2/H3 is a question a real person would type or ask an assistant, in their words ("Why did my credits go so fast?" beats "Understanding token consumption"). Clean H1→H2→H3, no skipped levels. Source real phrasings where they exist: the prompt set configured in Cairrot (visible in its web UI, and the basis for every number Cairrot returns), Cairrot's `search_fanouts` (the sub-questions an engine actually ran to build its answer, in the engine's own words), GSC queries via `bolt-seo-geo`, the FAQ language customers use on calls. One non-question H2 for a closing section is fine; a page of statement headers is a finding.

### 3. Answer-first, self-contained sections

Each section opens with the direct, neutral answer in ~40–60 words, then expands with voice, nuance, and persuasion below. The screenshot test: if this section were screenshotted alone, does it fully answer its heading? No pronouns reaching into a previous section, subject noun restated at the top. Promotional tone in the first sentences of a section measurably suppresses citation: brand energy lives below the answer, never instead of it.

### 4. The definitional block

For any piece that defines something, one sentence-cluster must carry four signals together: the **term**, the **entity tied to its category** ("Bolt.new, an AI app builder"), the **claim**, and the **date** ("as of August 2026"). Engines lift definitions whole; a definition missing its entity or date gets lifted without credit or rots silently. Write it quotable: it should survive out of context as a complete, attributed fact.

### 5. Receipts

Walk the draft claim by claim. Every stat, cost, or behavior claim carries the two-part inline citation: the **phrase carrying the statistic is hyperlinked to the origin**, then the sentence closes with a **plain-text parenthetical, "(Zylo, 2026)"**. Never a middleman, never a footnote (web copy; downloadable long-form keeps its Chicago format). The split matters most to this skill: engines strip markup when they lift a passage, so the plain parenthetical is what keeps the attribution attached to the claim, while the anchor text tells them what the linked source says. A link sitting on the publisher name instead of the claim wastes the anchor. First-party specifics are the strongest lever: a named customer's real number, an actual workflow, an honest tradeoff. Honest-frictions sections ("what's hard about this") are citation magnets AND trust builders — protect them from over-polish. Three gates on every receipt: origin verified (not laundered from an aggregator — check the do-not-cite trap lists in the RE source library and campaign handoffs), consent tier checked for any named customer (first name + last initial unless Full-consent naming is confirmed; anonymized means *unidentifiable*, not just unnamed), and internally consistent with the campaign's other live pages (two public pages contradicting each other on the same number is a Red).

### 6. Liftable formats

Tables are the highest-citability format; every comparison or multi-attribute explanation should consider one, always preceded by a plain sentence saying what the table shows. A well-designed table can also settle a nuance prose keeps fumbling (a "who can do what" column ends a permissions ambiguity in a way no paragraph can — build columns that answer the follow-up question). Also: numbered steps for any process, bullets where each line stands alone without its stem, and literal artifacts (real prompts, real quotes, real commands) in liftable form — engines quote verbatim material verbatim.

### 7. The FAQ

Five to eight questions at the end, phrased exactly as users ask assistants, each answered in ~40–60 self-contained words with one intent per answer. No overlap with the body's H2s (adjacent questions, edge cases, objections) and no verbatim duplication with sibling pieces' FAQs — engines deduplicate, and the campaign should cover more ground, not the same ground twice. Structure it FAQPage-schema-ready and note whether the CMS emits the schema.

### 8. Freshness and trust-completeness

Dates live in sentences, not just bylines ("as of 2026," "launched in August 2026" — never "this week"/"today," which go stale or false the day after the publish slot moves). Numbers current, never a refreshed date on stale numbers. Trust-complete means: named author, at least one real example, internal links to the docs and to cluster siblings (hub-and-spoke linking is itself a citation signal — new pieces link the cluster, and older cluster pieces should gain a link back when they're next touched).

### 9. The glaze (claim-safety valve)

When a factual claim can't be verified before publish (a feature behavior awaiting engineering confirmation, a number pending review), don't guess and don't cut the section. Rewrite to claim-neutral phrasing that is true in every possible world (state only the certain facts; make control and recoverability the message), and **bank the stronger upgrade sentences** somewhere durable (a Copydesk comment anchored to the passage where Copydesk is present; otherwise a clearly marked note at the end of the draft) so the post-confirmation edit is a paste, not a rewrite. A glazed passage ships honest; an optimistic one ships a retraction.

## Output contract

After a Sculpt pass:

1. Numbered findings (🔴/🟡/🔵, lens-tagged: Term, Tree, Answer-first, Definition, Receipts, Liftable, FAQ, Freshness, Glaze) — applied or listed, per the user's ask.
2. The citability checklist: each of the nine passes as pass / warn / fail with one line of detail.
3. Copydesk, where present (Taylor's local editor; the tell is a `.copydesk/` directory beside the draft in `~/Documents/Drafts`): mirror the checklist into its checks panel (`.copydesk/checks/<urlencoded-filename>.json`, shape: `{summary, updated (ms epoch), items: [{label, status, detail}]}`) and anchor pending-confirmation items as Copydesk comments so they live next to the text. Without Copydesk, put the checklist at the end of the delivered draft.
4. **Name the Cairrot baseline the pass targeted**: topic, named %, cited %, and the window ("browser-based full-stack app creation, named 20.6% / cited 0%, 30 days to Sep 3 2026"). If you sculpted without a pull, say so plainly.
5. Name what was protected: honest-frictions passages, deliberate campaign refrains, and verbatim quotes are load-bearing — a pass that sands them off made the piece worse.

For worked before/after examples of every pass (real ones from the Bolt.new campaign, not invented), read `${CLAUDE_PLUGIN_ROOT}/skills/aeo-craft/references/worked-examples.md` — especially before your first run.

## Reality checks

- Readability still gates: sculpting must keep the piece inside its persona's Flesch band (bolt-icp). A perfectly liftable page nobody enjoys reading loses the human half of the audience, and engines increasingly follow human engagement.
- **Cairrot is the only AI-visibility source. Profound was retired Sep 8 2026.** Pull Cairrot for everything. Two archived snapshots survive on disk as frozen history and must never supply a current number. **Never put Cairrot and Profound figures in one table or one sentence:** different prompt sets, not comparable, and the gap between them reads as a collapse when it is only a change of instrument. Name the source and the window on every number.
- **Small samples are volatile.** The tracked prompt set is small, so single-window swings are noise. Prefer trend over any one pull, and never build a campaign claim on a single number.
- **Cairrot measures the prompt set we configured,** not the whole internet. Competitor numbers are directly comparable to ours on that basis, but they cannot support a public "Nth most visible AI app builder" claim.
- **Never fabricate a metric.** If a pull comes back empty, say so and sculpt blind, flagged as blind.
- When aeo-craft and the TOV disagree, TOV wins; when aeo-craft and accuracy disagree, accuracy wins. The skill exists to earn citations for true, well-written things.

## One-time setup: Cairrot (per user, about five minutes)

Cairrot is the AI-visibility source for bolt.new, and everyone on the team can have it. The skill runs without it (Plan and Sculpt work blind, flagged blind), but Measure needs it, and a sculpt you can't measure is a guess.

1. **Get a Cairrot login** on the bolt.new project (ask Taylor). In Cairrot, Account Settings → Create API Key. Prefer a project-scoped key over a global one, and treat it like a password: never paste it into chat, a doc, or a skill file.
2. **Add the connector** in Claude Desktop → Settings → Connectors → add custom connector. Server: `https://api.cairrot.com/api/v1/mcp`. Auth: OAuth, Client ID `Cairrot-MCP`, your API key as the client secret. If "Add custom connector" is missing, the workspace setting `allow_quick_web_setup` is off for your account; ask Taylor to route it to the admin.
3. **Confirm.** Start a new session (one that was already open won't see the new tools), ToolSearch `cairrot`, run `list_projects`. If bolt.new is listed, you're wired.

Treat the connector as read-only for this skill: query reports, never edit. Cairrot's keyword and competitor lists are edited with `PUT` calls that replace the whole list, so one careless write wipes the tracking set the whole team's numbers rest on.

On Taylor's machine the `bolt-cairrot` skill's REST puller is already present and returns the same numbers; the connector is not required there.
