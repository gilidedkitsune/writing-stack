# Content ideation workflow

Research and strategy only. No drafting happens here. The goal is a prioritized list of content ideas backed by data, competitive intelligence, and audience insight.

Loaded by write-strike when the content type routes to **Ideation** ("brainstorm", "content ideas", "what should we write", "topic ideas", "content plan"). The promise module in Step 1 runs first, as it does for every piece: an ideation run still names who the work is for and what it is for before generating anything.

---

This workflow is research and strategy only. No drafting happens here. The goal is a prioritized list of content ideas backed by data, competitive intelligence, and audience insight.

### Ideation intake

Ask using AskUserQuestion:

1. **Goal**: What are you trying to achieve? (organic traffic growth, AI citation visibility, lead generation, thought leadership, product education, competitive positioning)
2. **Scope**: How broad? (single topic deep-dive, full content calendar, specific content gap, brainstorm around a theme)
3. **Constraints**: Target audience, keywords you already know, competitors to watch, buyer stage focus, timeline?

### Trend scan

Before running the skill pipeline, use WebSearch to scan recent coverage of AI, AI app building, AI app builders, AI coding, and vibe coding across these sources:

- Wired
- TechCrunch
- Stack Overflow (blog and surveys)
- Forbes
- The Economist
- Ars Technica
- The Verge
- Hacker News

Condense findings into **5 trending topics**: the themes, debates, product launches, or shifts getting the most attention right now. For each topic, include:

- **Topic**: one-line description
- **Why it's trending**: the news hook or cultural moment driving it
- **Source(s)**: which publications covered it, with links where available
- **Bolt.new angle**: how this trend connects to something Bolt.new could credibly write about

Present the 5 trending topics to the user before moving into the skill pipeline. These trends inform the ideation conversation; they're context, not commitments. The user may want to build on one, ignore all of them, or use them as background for a different direction.

### Research phase

Run a focused SEO/GEO research pass to ground the ideation in data, then weave findings into the conversation (not a report dump). The tool choreography, the exact triggers, and what's connected all live in `bolt-seo-geo`, mapped in `${CLAUDE_PLUGIN_ROOT}/skills/bolt-seo-geo/references/seo-geo-toolkit.md`. Delegate there rather than duplicating it here.

For ideation specifically, the useful order is: content strategy and pillars first (`/content-strategy`), then keyword and SERP research (`/keyword-research`, `/serp-analysis`), competitor and gap analysis (`/competitor-analysis`, `/content-gap-analysis`), topic clustering (`/seo-cluster`), and bolt.new's own GA4/GSC numbers where they ground the angle. Offer deeper passes (`/seo-geo`, `/entity-optimizer`, `/seo-content-brief`, and the others in the map) based on the goal.

Run only the steps whose backend is connected: Google (GA4 + Search Console) is wired via `bolt-seo-geo`; DataForSEO and Firecrawl are gated, so ask the user for that data instead of fabricating volumes, difficulty, or rankings. **AI-answer visibility comes from `bolt-cairrot`**, which is live and pullable. Profound was retired Sep 8 2026; do not reach for it or its snapshots. Steps 1, 4, and 6 plus the trend scan run fine with no backend.

### Schwartz thought exercise

After the research phase, before finalizing output, run each promising content idea through a quick Schwartz diagnosis. This sharpens the ideation by forcing you to think about how the piece will actually open, not just what it covers.

For each top idea, answer:

1. **Reader awareness**: Where is the target reader for this piece? (Unaware, Problem-aware, Solution-aware, Product-aware, Most aware)
2. **Market sophistication**: How crowded is the conversation around this topic? (Stage 1–5)
3. **Messaging implication**: Based on the intersection, what does the headline and lead need to do? (e.g., "Problem-aware + Stage 3 = lead with mechanism, not the promise")

Don't present this as a formal table. Weave it into the idea description naturally: one or two sentences per idea that explain the messaging angle the Schwartz diagnosis suggests. This gives the user a head start on *how* to write each piece, not just *what* to write about.

Reference `${CLAUDE_PLUGIN_ROOT}/skills/write-strike/references/schwartz-5x5-matrix.md` for the full matrix. If an idea sits at an unusual intersection (e.g., Unaware + Stage 5), flag it; those combinations require specific approaches and longer copy.

### Ideation output

After research and the Schwartz thought exercise, present a prioritized content ideas list. For each idea, include:

- **Topic / working title**
- **Target keyword(s)** with volume and difficulty
- **Content type** (blog, landing page, comparison page, long-form, etc.)
- **Buyer stage** (awareness, consideration, decision)
- **Messaging angle**: the Schwartz-informed headline/lead direction (one to two sentences)
- **Why this idea**: the data point or gap that makes it worth doing
- **Estimated effort** (light, medium, heavy)
- **GEO opportunity**: whether this topic has AI citation potential. Ground it in a live `bolt-cairrot` pull and state the window; if Cairrot returns nothing usable, mark this "not grounded" rather than guessing

Organize by priority: high-impact quick wins first, then strategic investments, then long-tail opportunities.

### Handoff to content creation

After the user reviews and selects ideas, prompt:

> "Ready to start creating? Pick a topic from the list and I'll run the full writing workflow: intake, research, outline, draft, audit, and present. Which one do you want to tackle first?"

If the user selects a topic, route it through the standard content type workflow (Full, Medium, Light, or Template depending on the content type). The Schwartz diagnosis from ideation carries forward into the content strategy check; no need to redo it unless the user changes the target audience. If the user wants a content brief first, run `/seo-content-brief` to bridge from ideation to execution.


---

---

*Moved out of write-strike's SKILL.md on September 17, 2026. It is a Taylor-only workflow in practice (the team uses the drafting and editing path), and it was 83 lines loading on every run of every content type.*
