---
name: bolt-icp
description: >
  Bolt.new's four ICPs, stack-ranked, and the three personas beside them. Single source of truth for
  who Bolt.new serves first, target audience definitions, voice adjustments, readability calibration,
  and content approach across all Bolt.new content.
  Use this skill when the user asks about personas, target audiences, buyer profiles, ICPs, the ICP
  stack rank, competitive landscape, or third-party research and stats for a specific audience. Also
  triggers on audience selection in any content workflow, or when a skill references "persona",
  "target audience", "buyer persona", "ICP", or "ideal customer profile".
metadata:
  version: 1.4.0
---

# Bolt.new Buyer Personas

Seven audience profiles that govern voice, depth, vocabulary, examples, and CTAs across all Bolt.new content: **four ICPs** and **three personas**. Every content skill that targets a specific audience should read the relevant profile here before drafting.

The two words mean different things. An **ICP** is an audience Bolt.new has chosen to build for first, backed by ICP research and ranked. There are four, numbered by rank, so ICP 1 is the primary. A **persona** is an audience Bolt.new still writes for but does not prioritize: the enterprise CTO and CPO, and the professional developer. Personas are named, not numbered, because a number would imply a rank they do not have. **There is no general-reader profile.** Every piece targets an ICP or a persona; "broad audience" is not an audience. A top-of-funnel or educational piece still names an ICP, usually ICP 1, and calibrates the register down. Every profile, ICP or persona, carries the same craft blocks: pain points, what resonates, voice adjustment, readability targets.

## Reference files

| File | What it contains | When to read it |
|------|-----------------|-----------------|
| `third-party-research.md` | Sourced stats, pull quotes, and cross-persona themes from 13 external studies (Stack Overflow, METR, Korn Ferry, McKinsey, Bain, Adobe, HubSpot, Salesforce, CoSchedule, Microsoft, PwC, Stanford HAI, arXiv). Organized by ICP and persona with ready-to-use citations. | When content needs external credibility, cited data points, industry benchmarks, or quotable stats. Also read when the user asks for research, stats, or citations for a specific persona. |

## The ICP stack rank

Source: **Bolt ICP** (Product, as of July 2026), with the agency target carried from **Report: ICPs** (May 2025). Bolt.new has more than one ICP and stack-ranks them so decisions can be checked against a priority order. The keyword is *ideal*: this is who Bolt.new builds for first, not the only customer it serves.

> **Bolt's primary ICP is a business operator looking to build software to start, operate, and scale their business without needing to code directly.**

| Tier | ICP | Label | Core use case | Why Bolt.new wins |
|---|---|---|---|---|
| 🥇 **Primary** | Business owner or entrepreneur | **ICP 1** | Build, iterate, and launch software to run their business | Fastest path from idea to a working, inspectable, extensible app. For internal operations, good enough is fine |
| 🥈 **Secondary** | PM | **ICP 2** | Prototype, validate, and shape product direction | More real-product capable than static design and prototype workflows |
| 🥉 **Tertiary** | In-house marketer | **ICP 3** | Campaign, site, and workflow assets | More flexible than one-off visual artifacts |
| 4️⃣ **Fourth** | Agency | **ICP 4** | Client deliverables, launched fast and on brand | Highest sub-segment conversion on the platform; margin stays in-house |

These four labels are canonical (set by Taylor, September 2026). Use them verbatim in briefs, campaign docs, and audience selection so the priority language stays consistent across teams.

Two notes on where the fourth tier comes from, so nobody is surprised when they read the source docs. The July 2026 ICP doc ranks only three tiers; the agency was named a *secondary target* in the May 2025 research, and is ranked fourth here as a Bolt.new marketing decision supported by current conversion data. And the secondary tier is labelled **PM** for brevity, but the ICP doc names "PM, Product Designer" and ICP 2 covers both. A product designer shaping product direction is inside this tier.

**How the ICP got here:** StackBlitz served engineers. Bolt.new launched for engineers and very technical PMs. It now serves high-agency entrepreneurs, SMB owners, and PMs building websites, internal dashboards, and the software that runs their business. The arc is developer productivity → technical builder leverage → software creation for high-agency teams and entrepreneurs.

**What the rank rests on** (internal, July 2026):

| Role | Paid conversion | Avg LTV | Still active | Read |
|---|---|---|---|---|
| Founder / entrepreneur | 12.72% | $203 | 25.1% | Primary ICP signal |
| PM | 10.77% | $140 | 23.7% | Secondary ICP signal |
| Marketer | 7.24% | $162 | 28.3% | Tertiary ICP signal, and the best retention of any role |
| Developer | 5.88% | $114 | 13.5% | Retain, but not an ICP |
| Designer | 5.06% | $133 | 20.2% | Secondary when paired with product creation |
| Student | 2.82% | $78 | 13.9% | Excluded |

Three findings that should shape angle selection more than the conversion table does:

- **People building for a business that already exists retain best and pay most.** They are 19% of payers and 25.3% of revenue, still paying at 43.5% by month three. People *trying to start* a business are the larger block (40% of payers, 36.9% of revenue) but retain worse individually. Content that speaks to an operating business is talking to the stickiest audience Bolt.new has.
- **Small is the sweet spot, and it is narrow.** A work email at a company of ten or fewer is worth roughly double whatever the person is building. Everything above ten employees combined is 5.4% of revenue, and individuals at companies over 200 cancel fast regardless of what they build.
- **AI curiosity does not retain.** When a user's intent can't be read after ten prompts, that alone predicts cancellation. This group retains worst of all. Content that sells exploration rather than a job to be done is recruiting the churn cohort.

**What is deliberately not an ICP.** Professional developers remain a persona because Bolt.new still writes for them, but they are not a priority audience: developers convert at 5.88% with the worst retention of any paying role, and students are excluded outright. There is no general-reader profile at all. Keep writing for developers where the piece calls for it. Don't let them drive roadmap-shaped content decisions.

**Why the enterprise personas sit outside the rank.** The CTO and CPO personas are a strategic bet, not a revenue-backed tier. Companies over ten employees are 5.4% of revenue today, and enterprise appears in the ICP doc under "customers we don't have, but want to have," where the buyer is not the builder and the pull is bottom-up. That is a real bet worth writing for. It just isn't what the current numbers rank.

> ⚠️ **These are internal planning figures.** Conversion rates, LTV, retention, and revenue splits are confidential first-party commercial data. They belong in strategy docs and briefs, never in audience-facing copy. Behavioral findings (what people build, how they work) can cross into public content once cleared; commercial figures cannot. See the September 2026 internal data doc for the full boundary.

## Quick reference

| Label | Who | Who they are | Voice register |
|---|---|---|---|
| **ICP 1** | Business owner / entrepreneur | Non-technical domain expert, open to AI, needs barriers lowered | Plain language, relatable scenarios |
| **ICP 2** | Product manager / product designer | Bridge between business and engineering, needs speed to validation | Practical, PRD-fluent |
| **ICP 3** | In-house marketer | Design-fluent campaign owner, delivers for their own brand | Confident, visual, outcome-driven |
| **ICP 4** | Agency / creative freelancer | Design-fluent builder who delivers for paying clients | Confident, commercial, craft-proud |
| Persona | Enterprise CTO / App Dev Leader | Technical gatekeeper, owns the stack and security posture | Authoritative, infrastructure-focused |
| Persona | Enterprise CPO | Product and innovation leader, owns velocity and team productivity | Authoritative, outcome-focused |
| Persona | Professional developer | AI power user, skeptical of AI-coded output | Technical, direct, humor welcome |

## How to use

1. Check the ICP stack rank first when the audience is still open. It tells you which persona the work should serve if nobody has decided yet.
2. Read the relevant ICP or persona before drafting.
3. Shape every decision (angle, depth, vocabulary, examples, CTA) to match the persona.
4. The **Voice adjustment** tells you how the content should sound for this audience. Apply it on top of the Bolt.new TOV from `bolt-TOV-and-guidelines`.
5. The **What keeps them up at night** section tells you which pain points to address and which proof points to lead with.
6. The **Readability targets** tell you the technical calibration, reading level, jargon tolerance, and content approach.
7. For additional sourced stats and citations, query `third-party-research.md` in this skill directory, or use web search and internal tools (Notion, Slack, Linear) for current data.

---

## ICP 1: Business owner / entrepreneur

**Primary ICP.** The business owner or entrepreneur is who Bolt.new builds for first. People building for a business that already exists retain best of anyone on the platform; people trying to start one are the largest block. Both live here.

Smart, accomplished professionals who are very good at what they do. They just aren't technical. They have deep domain expertise in their field and run their businesses with real skill, but they're not proficient AI users. They're looking for ways to improve operations, cut costs, and stay competitive. They're open to AI but don't know where to start or what's even possible. Ambitious, hardworking, and zero patience for fluff or buzzwords. They respond to helpful, direct content that addresses their specific pain points with concrete examples of what they can actually do. Think: the special education tutor who built an entire learning platform because nothing on the market worked for his students. Write for someone who Googles solutions to real problems, not someone browsing a tech blog for fun. Respect their intelligence. They're experts in their domain, they just need the technical barriers lowered.

**What keeps them up at night:**
- Website and digital presence costs. Agency quotes ($8K-$22K) don't match the budget. 17% of small businesses still don't have a website at all.
- Time. They can't spend months on a web project when they have a business to run.
- Loss of control. They know exactly what they want but lose it in translation with developers and agencies. Revision rounds, misinterpretations, and a final product that's close but not quite right.
- The AI knowledge gap. They see competitors adopting AI but don't know what's real vs. hype, or where to start.
- Tool overwhelm. They don't want to learn a complex platform: they want to describe what they need and get it.

**What resonates with them:**
- Cost comparison: $20/month vs. $12,000 upfront.
- Speed: afternoon vs. months.
- Control: you make every decision, not a developer interpreting a brief.
- Real examples from people like them (landscapers, tutors, consultants), not tech companies.

**How they use Bolt.new:**
- Building MVPs fast without a full dev team.
- Creating marketing microsites, campaign pages, and landing pages without developers.
- Building sales dashboards and enablement tools.
- Rapid demos and customer-facing prototypes.
- Internal BI tools and customer feedback aggregation.

**Roles that map here:** Executive / Founder (CEO, CTO, COO), Sales / Business Development Leader. Common thread: they need to build something now, can't wait for dev resources, and don't have a technical background.

**Third-party research:** query `third-party-research.md` in this skill directory for sourced stats and pull quotes for this persona.

**Voice adjustment:** Plain language. No jargon. Show, don't tell: lead with relatable scenarios and real outcomes. The CTA should feel like a natural next step, not a sales pitch.

**Readability targets:**
- Flesch Reading Ease: 60-70
- Jargon density: low threshold, flag technical terms without explanation
- Content approach: lead with relatable scenarios and real outcomes, concrete examples of what they can actually do

---

## Enterprise personas: CTO and CPO

**Outside the ICP rank, on purpose.** A strategic bet rather than a revenue-backed tier; the stack rank section explains why. Write for them with full conviction, but don't let enterprise framing leak into ICP content.

Has a complicated relationship with AI. They want it, but they need it to be secure, governed, and a clear value-add. They're looking to replace dated workflows and niche SaaS products with AI-powered alternatives, but they want tools that integrate into their existing ways of working, not something that requires uprooting their entire stack to accommodate a "power tool." Their developers are likely already using Cursor or Claude Code, but people outside IT often can't access AI tools to experiment or test ideas because the broader tech stack is tightly controlled. They care about compliance, ROI, and reducing tool sprawl.

**Shared enterprise concerns** (both subgroups):
- SSO and authentication: table stakes for any enterprise deployment.
- Security and compliance reviews (SOC 2 Type 2, DPAs, data sovereignty) add four to six weeks to every sales cycle.
- Admin controls and governance: centralized user management, usage analytics, permission controls.
- Token management and predictable costs: shared pools, consumption visibility, forecastable pricing.

**Voice adjustment** (both subgroups): Authoritative and specific. Speak to constraints as features, not obstacles. Concrete business outcomes and cost comparisons. No aspirational AI hype: they're buying results, not vision.

**Readability targets** (both subgroups):
- Flesch Reading Ease: 55-65
- Jargon density: moderate, industry terms (ROI, compliance, governance, tool sprawl, SSO, SOC 2) are expected
- Content approach: concrete business outcomes, cost comparisons, constraint-as-feature framing

### Persona: Enterprise CTO / App Dev Leader

The technical gatekeeper. Responsible for the engineering organization, the tech stack, and the infrastructure that everything runs on. They evaluate tools through the lens of code quality, security posture, and integration with existing systems. Their primary question isn't "is this useful?" It's "can this run in our environment without breaking anything?"

**Where their head is at:**
The CTO conversation has moved past "should we use AI coding tools" to "how do we adopt them without creating long-term engineering problems." They're optimistic about the productivity upside, especially for prototyping, repetitive development work, and delivery velocity. But they see a core tension: AI dramatically lowers the cost and speed of creation, while software accountability still belongs to humans. Code generation is outpacing validation. Review, testing, architecture governance, and debugging aren't scaling at the same rate as output. The fear isn't that AI writes bad code all the time. It's that subtle mistakes, architectural inconsistencies, and hidden technical debt become harder to detect at scale. "Shadow AI" is a growing issue: developers adopting unauthorized tools faster than governance policies can keep up, echoing earlier concerns around cloud adoption and open-source governance. They also worry about junior developers becoming dependent on AI before building foundational debugging and systems design skills, while senior engineers become bottlenecked as validators of machine-generated output. Their conclusion: governance, architecture, maintainability, and operational discipline are becoming more important, not less.

**What keeps them up at night:**
- The prototype-to-production gap. Moving a working demo into their CI/CD pipeline, GitHub Enterprise, and deployment infrastructure is where most AI tools fail. Manual migration adds months: Deloitte reported one project ballooning from three weeks to three months.
- Code quality at scale. AI generates code faster than teams can review and architect. Subtle inconsistencies and hidden technical debt accumulate when validation doesn't keep pace with generation.
- Security posture. They need outbound IPs defined, Artifactory whitelisting, and clear data-sovereignty documentation before anything touches their network. A six-week security review is standard. Shadow AI usage compounds the risk.
- Ungoverned code entering the codebase. As non-technical users gain the ability to generate production-quality output, the CTO needs guardrails that prevent unreviewed code from shipping.
- Infrastructure integration. Native publishing must be disableable. GitHub organization integration can't create duplicate teams. The tool must fit into their existing deployment architecture, not replace it.
- Engineering culture. Junior developers skipping foundational learning. Senior engineers bottlenecked as reviewers. The org needs to maintain engineering discipline even as output accelerates.

**What resonates with them:**
- Production-ready code that integrates with existing CI/CD pipelines: not prototypes that need to be rewritten.
- WebContainers as a security model: isolated browser-based execution, no remote server dependency, full visibility.
- Native GitHub Enterprise integration for real dev handoff.
- Granular admin controls: disable integrations per security policy, manage publishing permissions, control what non-technical users can deploy.
- Self-service licensing where team admins manage seats without vendor intervention.

**How they use Bolt.new:**
- Security and compliance posture review (SOC 2 Type 2, penetration testing, data sovereignty).
- Managing internal vs. external publishing with access controls.
- Integrating WebContainers SDK into existing platforms and developer infrastructure.
- Providing a secure, browser-based IDE for non-technical employees while maintaining engineering governance.

**Roles that map here:** CTO, VP Engineering, Director of Engineering, IT / Security Leader, Solution Architect. Common thread: they own the stack and the security posture. Nothing gets deployed without their sign-off.

**Third-party research:** query `third-party-research.md` in this skill directory for sourced stats and pull quotes for this persona.

### Persona: Enterprise CPO

The product and innovation leader. Responsible for product velocity, team productivity, and the ROI of tools that their product organization uses. They evaluate tools through the lens of speed, cost per seat, and whether it unlocks capacity their product teams don't currently have. Their primary question is "does this make my product org faster and less dependent on engineering?"

**Where their head is at:**
The CPO conversation has shifted from "how do we build faster" to "how do we build better when everyone can build fast." AI tools have effectively removed execution speed as a differentiator: any team can generate an app, a prototype, or a landing page in hours. That changes the CPO's competitive calculus: if the barrier to building is gone, the advantage shifts to product taste, experience quality, and strategic vision. The core tension is that faster creation doesn't guarantee better products. When prototyping is cheap, the risk is building more things without building the right things. Volume goes up, but signal-to-noise can go down. CPOs worry about product quality and customer trust: AI-generated interfaces that look polished but feel generic, outputs that ship faster but erode the brand's quality bar, and a widening gap between "technically functional" and "genuinely good." There's also a team evolution underway. PMs are becoming more technical, designers are shipping directly, and the CPO's role is evolving from roadmap manager to experience curator. The CPO who succeeds in this environment isn't the one who ships the most features; it's the one whose team consistently ships features that matter.

**What keeps them up at night:**
- Eng capacity as the bottleneck. Their PMs have ideas and validation needs that sit in the engineering backlog for weeks. Every day a prototype waits is a day of lost customer signal.
- Product quality at scale. When anyone on the team can build, more things ship. The CPO needs to ensure volume doesn't dilute quality: that the product org is building the right things, not just more things.
- The commoditization of execution. If every competitor can build and iterate at the same speed, the advantage shifts to taste, strategy, and experience quality. The CPO needs to protect differentiation when the mechanics of building are no longer differentiating.
- Token economics and per-seat costs. At 65+ seats, the math matters. They need consumption-based models, usage visibility across teams, and pricing they can defend to the CFO.
- The trust gap in AI output. 24% of PMs don't trust AI-generated output enough to show stakeholders. If the CPO invests in Bolt.new and their PMs still don't use it, the ROI case collapses.
- Customer trust erosion. AI-generated interfaces that look polished but feel generic can erode the quality bar customers expect. The CPO is accountable for the experience, regardless of how it was built.
- Design system fidelity. Prototypes that don't match the product's actual look and feel undermine credibility with stakeholders and engineering.
- Tool sprawl. Their PMs are already using five or six AI tools (survey data: GitHub Copilot 55%, Claude Code 52%, Cursor 31%, Windsurf 28%). The CPO wants to consolidate, not add another tool to the stack.

**What resonates with them:**
- The ability for PMs and designers to build without consuming eng capacity, while IT retains governance.
- Speed to stakeholder buy-in: show something working instead of a slide deck.
- Design System Agent for brand consistency and pixel-perfect output from non-technical builders.
- Unlimited token models that eliminate per-user consumption anxiety across large product teams.
- Clean handoff from Bolt.new prototype to engineering: the artifact is a starting point, not a throwaway.

**How they use Bolt.new:**
- Deploying Bolt.new across the product organization for prototyping and internal tooling.
- Evaluating ROI: comparing time-to-prototype before and after adoption.
- POC and pilot evaluations before recommending enterprise-wide rollout.
- Building internal BI, customer feedback aggregation, and product intelligence systems.
- Overseeing team-wide adoption metrics and usage patterns.

**Roles that map here:** CPO, VP Product, Director of Product, Strategic Advisor / Consultant. Common thread: they own product velocity and team productivity. They champion the tool internally if the ROI is clear.

**Third-party research:** query `third-party-research.md` in this skill directory for sourced stats and pull quotes for this persona.

---

## ICP 2: Product manager / product designer

**Secondary ICP.** The ICP doc pairs these two roles deliberately: both run the same loop, idea → prototype → proof, and both are blocked by the same thing, which is that the artifact they can produce alone isn't real enough to decide on.

Wants a way to build and refine prototypes of digital products they can validate with stakeholders and then hand over to engineering as a production-ready artifact. They sit between business goals and technical execution and need tools that let them move fast without being blocked by eng capacity. They care about speed to validation, fidelity of prototypes, and clean handoffs.

**The product designer variant.** Same loop, different starting point and a higher bar for fidelity. A product designer arrives with the interaction already in their head and has been handing it to engineering as a flat file that loses most of its meaning in translation. What they want from Bolt.new is the prototype that behaves, not the prototype that merely looks right: real state, real data, real navigation. Designers convert at 5.06% overall, but the ICP doc's read is that they are a secondary signal specifically **when paired with product creation** rather than visual work. That pairing is the whole distinction. A designer making a marketing page is ICP 3 or ICP 4; a designer shaping what the product should do is here.

Write to the shared loop and vary the proof: PMs need to trust the output in front of stakeholders, designers need to trust the fidelity in front of engineering. Do not reach for creative-industry vocabulary here (briefs, deliverables, revision rounds). That is ICP 3 and ICP 4 language and it will read as though you have the wrong designer.

**What the April 2026 PM survey said** (N=126, dated; use for angle, not as a headline stat):
- Security and compliance is the #1 friction (44%), even among daily AI users. Output not production-ready is #2 (37%).
- Prototypes changed the engineering relationship: 38% now involve engineering *earlier* because they can show something working, and only 2% said nothing changed.
- 82% use AI tools daily and most already run Copilot, Claude Code, or Cursor. Bolt.new had 14% penetration, so most PMs have not tried it.

**What keeps them up at night:**
- The trust gap. Nearly a quarter of PMs don't trust AI output enough to show stakeholders. They need confidence that what they build is presentable and real: not a demo that falls apart under scrutiny.
- Security blocking adoption. Even PMs who love these tools hit walls when security reviews flag compliance concerns. This is the number one friction point.
- The maintenance problem. They can build something quickly, but iterating on it and integrating it with existing systems is where the process breaks down.
- Eng capacity. They're constantly blocked waiting for engineering to build things they could validate themselves if they had the right tools.
- Documentation drift. The strongest unmet need: keeping the product and its documentation in sync as things evolve.

**What resonates with them:**
- "Show, don't spec": the shift from writing PRDs to showing working prototypes.
- Independence from the eng backlog for validation and internal tools.
- Speed to stakeholder buy-in (show something working instead of a deck).
- Real, deployable output that engineering can pick up and refine: not a throwaway prototype.
- Design system fidelity so prototypes match the actual product's look and feel.

**How they use Bolt.new:**
- Rapid prototyping ideas before engineering investment.
- Building internal dashboards and data visualization tools.
- Creating shareable prototypes to hand off to dev teams (replacing static PRDs).
- Early customer feedback loops with lightweight builds.
- Bridging the design-to-code gap: building from design, handing off to engineering.
- Using the Design System Agent for brand consistency and pixel-perfect output.

**Roles that map here:** Product Manager / Product Lead, Product Designer, UX Designer (in-house, product-facing), Design Lead. Common thread: they sit between vision and execution, need to validate before committing eng resources, and care about fidelity. A designer working on client or campaign work belongs in ICP 4, not here; the test is whether they are shaping a product or producing a deliverable.

**Third-party research:** query `third-party-research.md` in this skill directory for sourced stats and pull quotes for this persona.

**Voice adjustment:** Practical and outcome-oriented. Frame Bolt.new as the bridge between idea and validated artifact. Use language they'd use in a PRD or stakeholder review: features, user stories, iteration cycles. They don't need deep technical detail, but they do need to trust that what they build is real enough to ship.

**Readability targets:**
- Flesch Reading Ease: 55-65
- Jargon density: moderate, PM vocabulary (PRD, user stories, iteration, validation, CI/CD handoff) is expected
- Content approach: frame around speed to validation, fidelity, and clean handoffs to engineering

---

## Persona: Professional developer

**Not an ICP.** Developers convert lowest and retain worst of any paying role. Bolt.new still writes for them, and this persona governs how; it just shouldn't drive what gets written.

Already a power user of AI in their own workflows. Skeptical of AI-coded artifacts because they've seen too many that aren't production-ready and can't be integrated into a real codebase. Open to new tools, but only if they fit the way they already work. They want governance and control over any development tool. Sophisticated technical user with a sense of humor and a zero-tolerance policy on bullshit. They appreciate technical depth and nuance but will bounce the second they smell buzzwords or hyperbole.

**From enterprise sales conversations** (May 2026, dated):
- Developers inherit what everyone else builds. Prototypes from Figma, AI scaffolds, and PM builds all arrive needing a rebuild; one team called them "artifacts from outer space."
- Legacy codebases (10+ years, large monorepos, outdated frameworks) resist browser-based and agentic tooling most, so the teams that need help most benefit least.
- They fear app sprawl the way they remember dashboard sprawl. One enterprise ended up with 10,000 ungoverned Power BI dashboards and expects the same from ungoverned AI apps.

**What keeps them up at night:**
- Code quality. 37% of PMs who use AI tools say the output isn't production-ready: developers see this even more acutely. They've reviewed too many AI-generated PRs that look right but break in edge cases.
- The prototype-to-production gap. Moving a working demo into their CI/CD pipeline and production architecture is where most AI tools fail. The prototype works in isolation; integrating it with the real codebase creates more work than building from scratch.
- Integration with legacy codebases. AI-generated code that can't be refactored into an established architecture, older framework version, or monorepo creates more work, not less. The teams that need help the most can benefit the least.
- Governance and control. They want to choose models, control where code runs, manage dependencies, and maintain visibility into what the AI is doing. Black-box tools are a non-starter.
- Non-technical users shipping unreviewed code. As PMs and designers gain the ability to generate production-quality output, developers worry about ungoverned code entering the codebase without proper review, and ungoverned apps proliferating without audit trails.
- Tooling performance. Slow build times, unreliable previews, and long feedback loops erode trust fast. If the tool wastes their time, they'll drop it regardless of what it can do.

**What resonates with them:**
- Production-ready code quality: not templates, not prototypes, actual code they can refactor and deploy.
- WebContainer architecture: isolated browser-based execution, no remote server dependency, full visibility into what's running.
- Native GitHub integration and CI/CD pipeline compatibility: the code meets them where they already work.
- Design system ingestion (private NPM packages, Figma libraries) that enforces consistency and prevents the brand drift they've seen from ungoverned prototyping.
- Honest messaging about tradeoffs. If Bolt.new is better for full-app generation and worse for line-by-line refactoring in an existing codebase, say so.
- Governance that scales. Admin controls, publishing permissions, and audit trails that prevent the app sprawl problem they've seen play out with every previous democratization wave.

**How they use Bolt.new:**
- Building internal tooling and apps.
- Integrating WebContainers SDK into existing platforms and building in-browser coding environments with no local environment setup.
- Integrating Bolt.new CLI with Cursor or Claude Code for dev handoff.
- Sandboxed testing and production-facing app development.
- API-based consumption for internal developer infrastructure.

**Roles that map here:** Software Engineer / Developer, Solution Architect / Technical Program Manager. Common thread: they care about the architecture, the integration points, and whether the output is real code they can work with.

**Third-party research:** query `third-party-research.md` in this skill directory for sourced stats and pull quotes for this persona.

**Voice adjustment:** Technical and direct. Earn their trust with specifics: architecture decisions, integration patterns, actual code examples. Respect their intelligence. Humor is welcome; hype is not. If something has a limitation, say so. They'd rather know the tradeoffs than get a polished pitch. The CTA should feel like an invitation to try something, not a push to convert.

**Readability targets:**
- Flesch Reading Ease: 50-60
- Jargon density: high tolerance, technical terms expected and appreciated, no need to explain standard dev vocabulary
- Content approach: earn trust with specifics, show tradeoffs honestly, code examples where relevant

---

## ICP 3: In-house marketer

**Tertiary ICP.** Marketers convert at 7.24% with a $162 average LTV, and 28.3% are still active, the best retention of any role in the ICP table. They are ranked third because the volume is smaller, not because they churn. Once a marketer sticks, they stick harder than a founder does.

Design-literate professionals who own campaigns for their own brand. They think visually, they are comfortable in Figma, Canva, Webflow, and WordPress, and they have been one step removed from building functional pages because the code layer always required a developer or a rigid template.

AI tools change their economics. A marketer who could brief a landing page and wait three weeks can now build it, ship it, and iterate on it inside the campaign window it was meant for.

They are not developers and do not want to be. They are also not the ICP 1 small business owner: they have design sensibility, understand layout and UX, and hold strong opinions about how things should look and feel. They are closer to power users than beginners. The barrier has always been code, not vision.

> **The client-services half of this audience is ICP 4.** Agencies and freelancers share the design fluency and the tooling but sell the output to someone else, which changes the pain, the pricing sensitivity, and the acquisition motion. If the work is billed to a client, write ICP 4.

**Where their head is at:**

AI building tools have moved past the experimental phase for this audience. They are core creative infrastructure now: website creation, campaign production, workflow automation, and internal tool development. But the productivity gains come with a real tension. As execution becomes automated, AI-generated output is converging toward sameness. Ads look like ads. Landing pages look like landing pages. Without strong human direction, everything blurs together.

Enterprise marketers are compressing campaign timelines and scaling personalization toward what Adobe's marketing leadership calls "a segment of one": hyper-personalized experiences for individual customers instead of broad audience segments. Teams are restructuring around "full-stack marketers" who execute across content, strategy, analytics, design, and automation without relying on large specialized support functions. They are also discovering that AI-generated campaigns need strong brand systems and editorial judgment to avoid generic output.

The conclusion that holds across the whole segment: the teams gaining the most leverage treat AI as a force multiplier for human creative direction, not a replacement for it.

**From enterprise sales conversations** (May 2026, dated):
- Marketing is locked out of building, not bottlenecked by it. Every landing page and campaign site waits in the eng backlog, and IDE-shaped AI tools rule out most of the marketing org.
- Ungoverned creative tooling drifts fast. One enterprise rolled back to a centralized process after prototype fragmentation got out of hand.

**What keeps them up at night:**
- Turnaround time. Campaigns have launch dates. Every page that requires a developer adds cost and calendar time to a window that does not move.
- Template limitations. They have outgrown Squarespace and Wix but cannot justify a developer for every campaign. They know exactly what they want and hit the ceiling of what no-code allows.
- The sameness problem. AI-generated output is converging. Without strong creative direction and brand systems, everything they produce risks looking like everything their competitors produce.
- Design fidelity. They care deeply about how things look. AI-generated output that feels generic or off-brand is worse than no output, because it undermines their professional credibility.
- Brand governance at scale. The more people who can build, the more ways the brand can drift. They need speed that does not cost them consistency.

**What resonates with them:**
- Speed to deliverable: describe a landing page, see it built, refine it, ship it, in a single session.
- Design control without code. They direct the visual output, adjust layouts, tweak brand elements, and iterate in real time without touching a codebase.
- Design System Agent for maintaining brand consistency across campaigns: the antidote to the sameness problem. Strong brand systems in, differentiated output out.
- Output that looks finished, not prototyped. The quality bar matters, because their name is on it.
- The "force multiplier" framing. AI handles execution; they bring the strategy, taste, and creative judgment that makes the output worth paying for.

**How they use Bolt.new:**
- Building campaign landing pages and microsites from a brief or creative direction.
- Producing event pages, product launch sites, and seasonal campaign assets on tight deadlines.
- Building internal marketing tools: calculators, lead-gen utilities, and lightweight workflows.
- Generating multiple design directions quickly to present internal options.
- Standing up experiment and A/B variants without a developer in the loop.

**Roles that map here:** Marketing Manager / Director, Demand Generation Manager, Content Strategist, Brand Manager, Campaign Manager, Growth Marketer, in-house Graphic or Web Designer. Common thread: they own campaign outcomes for their own brand and need to move from concept to live page without a developer.

**Third-party research:** query `third-party-research.md` in this skill directory for sourced stats and pull quotes for this persona.

**Voice adjustment:** Confident and visual. Speak to their design sensibility: they care about aesthetics, brand, and craft. Use language from the marketing world (campaigns, briefs, brand guidelines, above the fold, conversion) rather than engineering. Show, do not tell: before and after examples and visual output demonstrations land harder than feature lists. Light humor is fine; marketing jargon is welcome; tech jargon is not.

**Readability targets:**
- Flesch Reading Ease: 60-70
- Jargon density: creative and marketing terms expected (brand guidelines, CTA, above the fold, campaign, brief), technical terms need explanation
- Content approach: visual-first, outcome-driven, show the campaign quality they can achieve

---

## ICP 4: Agency / creative freelancer

**Fourth ICP.** Agencies were named a secondary target in the May 2025 ICP research with an "Acquire" motion, and current data supports keeping them: **agency founders convert at 19.4%, the highest sub-segment conversion rate on the platform**, roughly double the platform average.

Design-literate professionals who build for paying clients. This persona spans agency creatives delivering client work on tight timelines and freelance designers and writers expanding their service offering. They share ICP 3's design fluency and tooling. What separates them is that someone else is paying for the artifact, which changes everything downstream: the margin math, the revision dynamic, the fidelity bar, and the reason they buy.

AI tools change their economics more sharply than any other persona. A designer who could only deliver mockups can now deliver working sites. A freelance copywriter who handed off landing page copy to a developer can now build and deliver the page themselves. An agency that quoted $8,000 for a campaign microsite can build it in-house in a day, keep the margin, and move on to the next client.

**Acquisition strategy** (from *Report: ICPs*, May 2025, carried forward as strategy; treat the specific figures in that doc as stale):

The 2025 research classified agencies as a secondary target with an **"Acquire"** motion rather than the "Empower" or "Enable" motions applied to founders and teams. Two things from it still hold and should shape how content reaches this audience:

- **Designers are the most valuable subgroup within agencies.** Target the person doing the creative work, not the account lead.
- **The channel is different.** This audience is reached through targeted outreach, industry conferences, and partnerships rather than the search-and-social motion that acquires ICP 1. Content built for them should be pitchable and shareable inside an agency, not just discoverable.

Because the underlying numbers are 16 months old and the segmentation model has since changed, use the motion and the subgroup insight; source any figure from current data.

**Where their head is at:**

Agencies are using AI to increase delivery speed and project capacity: work that took weeks of wireframing and frontend development now compresses into days or hours. Smaller agencies compete with firms several times their size because AI reduces the operational overhead required to deliver polished client work.

The competitive shift is the story. Agencies no longer compete on production capability, because production is becoming free. They compete on strategic insight, creative direction, and client-specific customization. AI generation is the starting point; human refinement, brand direction, and custom strategy are the differentiator.

Freelancers are operating more like micro-agencies: more projects, faster delivery, and expansion into services (working sites, interactive prototypes, lightweight apps) that previously required a developer. They also face the sharpest version of the commoditization anxiety. Many independent creatives worry that widespread AI adoption is creating a flood of generic output and making it harder to stand out. That fear is not only commercial. It is about creative identity, originality, and whether AI erodes the artistic agency that defines their work.

**What keeps them up at night:**
- Turnaround time. Clients want landing pages, campaign sites, and microsites in days, not weeks. Every project that requires a developer adds cost and calendar time they cannot bill for.
- Margin evaporation in revision cycles. The back-and-forth between client feedback and developer implementation is where profit disappears. Making changes live during a review call reclaims hours per project.
- Commoditization anxiety, freelancers especially. If every freelancer has the same AI tools, what differentiates the work? This is an existential question about their value proposition, not a tooling complaint.
- Scope creep into development. Clients increasingly expect functional prototypes, interactive demos, and working sites rather than mockups or flat designs. The deliverable bar keeps rising and the budget often does not.
- Client brand fidelity. Off-brand output is worse than no output. It is client-facing, and their reputation is attached to it.
- Portfolio and proof of work. A working site beats a Figma file in every pitch, but it has to look like *their* work, not AI's.
- Handoff and ownership. Clients ask what happens when the engagement ends, who maintains it, and whether they are locked in.

**What resonates with them:**
- Expanded service offering. Designers who add "I build working sites" to their pitch win more contracts. Writers who deliver the page, not just the copy, raise their per-project value. Small agencies compete with firms several times their size.
- Margin capture. The $8,000 microsite that used to require a subcontractor is now in-house work.
- Design control without code, especially live during client review sessions.
- Design System Agent for maintaining a *client's* brand consistency across deliverables, which is a different job from maintaining your own.
- Client-facing output that looks finished, not prototyped.
- Cost structure that works at freelancer and small-agency scale: $20-200/month against hiring a developer per project.
- The "force multiplier" framing. AI handles execution; they bring the strategy, taste, and client relationship that makes the output billable.

**How they use Bolt.new:**
- Building client deliverables (working sites, interactive demos) that go beyond static mockups.
- Rapid iteration during client review sessions: making changes live instead of logging revision tickets.
- Pitching with a working prototype instead of a deck.
- Building portfolio sites and case study pages for their own business development.
- Generating multiple design directions quickly to present client options.
- Standing up client tooling: booking systems, intake forms, and lightweight client-facing apps.

**Roles that map here:** Creative Director (agency), Art Director, Agency Founder / Principal, Web Designer, UX Designer (freelance), Freelance Copywriter / Content Writer, Agency Account Manager who also builds, independent Brand Designer. Common thread: they deliver client-facing work on a commercial deadline and need to move from concept to functional deliverable without a developer in the loop.

**Voice adjustment:** Confident, commercial, and craft-proud. This audience runs a business, so margin, capacity, and billability are legitimate subjects in a way they are not for ICP 3. Use agency vocabulary (deliverables, briefs, scope, revision rounds, retainers, client presentations) and respect the craft anxiety rather than dismissing it: never imply AI replaces their creative judgment, because that is the exact fear. Position the tool as what lets them sell strategy instead of production. Tech jargon stays out.

**Readability targets:**
- Flesch Reading Ease: 60-70
- Jargon density: creative, agency, and commercial terms expected (brief, scope, retainer, deliverable, revision round, margin), technical terms need explanation
- Content approach: visual-first and commercially framed, show the client-ready quality bar and the business case together

---

## Competitive landscape

Source: **Bolt ICP** (Product, July 2026). One section for every persona. The per-persona competitive tables that used to live here went stale with each pricing change and were seven near-copies of each other; they are gone. Pricing, positioning teardowns, and battle-card facts belong in the **Messaging & Brand** hub in Notion. Verify anything below against it before it reaches a rep or a page.

**The wedge.** Bolt.new sits between three kinds of tool: more real-product capable than design and prototype tools, more accessible and visually iterative than developer-first coding agents, and more flexible for technical entrepreneurs than closed no-code app builders. Every competitive claim should trace back to one of those three edges. The strategic bet is that the highest-value customer is neither a pure non-technical consumer nor a traditional engineer, but a high-agency builder who uses natural language, product taste, light technical judgment, and fast iteration to create production-leaning software.

| Competitor | Their center of gravity | Their edge | What Bolt.new emphasizes against them |
|---|---|---|---|
| **Replit** | "Anyone can build": education, developers, enterprise teams | Full cloud IDE, built-in deploy, database, auth, enterprise workflows | More focused product creation for high-agency builders who want speed, control, and modern app UX |
| **Lovable** | Non-developer founders, PMs, designers, product teams | Prompt-to-app and prototype accessibility | More inspectable, extensible, production-leaning software creation |
| **Figma Make** | Design-native teams, PM and design workflows | On-brand, editable prototypes inside Figma | Real application behavior beyond design-native prototyping |
| **Claude Design** | Knowledge workers making polished visual assets | Designs, prototypes, slides, one-pagers, artifacts | Durable software outcomes, not visual artifacts |
| **Claude Code** | Developers working in existing codebases | Deep agentic coding, codebase understanding, multi-file changes | An accessible creation surface for builders who are not living in a terminal |

**Per-profile nuance, one line each:**
- **ICP 1:** the real comparison is rarely another AI builder. It is the $8K–22K agency quote, or the template site they have outgrown.
- **ICP 2:** Figma Make and Lovable are the live alternatives. The win is a prototype with real state, data, and navigation.
- **ICP 3 and ICP 4:** Webflow, Framer, Squarespace, and Canva are the website-builder ceiling; Lovable is the AI-builder comparison, and its credit pricing punishes the iteration that client and campaign work demands.
- **CTO persona:** Cursor and Copilot are complements, not competitors. The CTO's question is whether Bolt.new and the IDE agents can share one governance model.
- **CPO persona:** Figma is the incumbent workflow to displace: a picture of an app versus an app that works.
- **Developer persona:** Bolt.new is not replacing their IDE. It is what keeps other teams' requests off their backlog while producing code they can work with.

---

## Selection guide

When the audience isn't immediately obvious from the brief:

**By pain point:**
- **Saving money, DIY, "build it yourself," small business pain points** → ICP 1
- **Security posture, CI/CD integration, code quality, infrastructure governance** → the CTO persona
- **Product velocity, team productivity, per-seat ROI, tool consolidation** → the CPO persona
- **Prototyping, validation, stakeholder buy-in, PRDs, internal tools, eng handoff, design-to-product fidelity** → ICP 2
- **Technical depth, code quality, architecture, CI/CD, developer workflows** → the developer persona
- **Campaign sites, landing pages, brand governance, launch deadlines, marketing tooling** → ICP 3
- **Client deliverables, agency margins, revision cycles, freelance services, scope creep, portfolio work** → ICP 4

**By role:**
- Executive / Founder, Sales Leader → ICP 1
- CTO, VP Engineering, Director of Engineering, IT / Security Leader → the CTO persona
- CPO, VP Product, Director of Product, Strategic Advisor / Consultant → the CPO persona
- Product Manager, Product Designer, in-house UX Designer → ICP 2
- Software Engineer, Solution Architect, Technical Program Manager → the developer persona
- Marketing Manager / Director, Demand Gen, Content Strategist, Brand Manager, Campaign Manager, in-house Graphic / Web Designer → ICP 3
- Creative Director (agency), Art Director, Agency Founder, Web Designer, freelance UX Designer, Freelance Writer / Designer, Agency Account Manager → ICP 4

**The two questions that resolve most ambiguity:**

1. **Who pays for the output?** If a client is billed for it, that is ICP 4, no matter how the person's title reads. If it serves their own brand, that is ICP 3.
2. **Is the designer shaping a product or producing a deliverable?** Shaping a product is ICP 2. Producing a deliverable is ICP 3 (own brand) or ICP 4 (client). "Designer" alone never settles it.
3. **Is it "for everyone"?** Then it is for ICP 1, written accessibly. There is no general-reader profile, and a piece with no named audience has no angle.

If a piece targets multiple profiles, pick the primary and note the secondary. Write for the primary; check that nothing alienates the secondary. When nobody has picked, default to the ICP stack rank at the top of this file.

---

## Data sources

- Bolt.new user survey (April 2026 cut): self-reported data across 10M+ users. **Superseded for all numbers by the July 2026 ICP doc**; the per-persona data blocks it fed were removed Sep 2026 so the file carries one set of figures.
- PM survey: N=126 product managers, April 2026 (Audience Panel, Collection 1). Compressed to a dated block inside ICP 2; small and aging, use for angle only.
- Enterprise sales conversations, May 2026 (Workato, StoneX, EY, Porch, Cofense, Salesforce, Roku, and others): compressed to dated blocks inside the developer persona and ICP 3. Fresh call material comes from `bolt-sybill`.
- Creative/marketer industry context: enterprise marketing, agency, and freelancer AI adoption research, 2026.
- **Competitive landscape:** the July 2026 ICP doc's competitor table and wedge statement. Per-persona competitive sections were retired Sep 2026; pricing and teardowns live in the Messaging & Brand hub.
- **ICP stack rank and role conversion data:** "Bolt ICP" (Product), as of July 2026, last revised September 2026. Source of the three-tier rank, the role conversion table, the first-prompt revenue analysis, and the company-size findings.
- **Agency target and acquisition motion:** "Report: ICPs" (21 May 2025) and "Supplementary Analysis: ICPs" (June 2025), from 280K onboarding survey responses. ⚠️ These predate the current ICP model and use a different segmentation entirely (Solo Founders, Growth Teams, Agencies, Futurepreneurs, Solo Devs, Students). Their strategic guidance is carried forward; their figures are not. Source any agency number from current data instead.
- Third-party research: `third-party-research.md`, see Reference files table for full description.
