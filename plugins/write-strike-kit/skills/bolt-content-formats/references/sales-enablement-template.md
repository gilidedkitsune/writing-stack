# Bolt.new Sales Enablement Templates

*Internal framework: structures for the three sales enablement assets: the battle card, the objection handler, and the competitive one-sheet. Use the matching template for the asset requested.*

Sales enablement content has one job: give the sales team repeatable, accurate language they can use in a live conversation. That means it has to be benefit-led (tie every feature to a business outcome), honest (acknowledge where we lose, because reps lose trust fast when a card oversells), and tight (a rep skims this between calls, not the night before).

For competitor facts, voice, and proof points, read the relevant persona in `bolt-buyer-personas` first. The competitive landscape sections (Persona 2a/2b for enterprise, Persona 4 for developers, Persona 5 for creatives) are the source of truth for how Bolt.new stacks up against Lovable, Replit, v0, Cursor, Webflow, and others.

---

## Shared Rules for All Three Assets

- **Benefit-led, always.** Never list a feature without the outcome it drives. "WebContainers" means nothing to a buyer. "Code runs in the browser, so there's no remote server for your security team to review" is the benefit.
- **Be honest about losses.** Every battle card has a "where they win" section. Reps trust a card that admits tradeoffs and stop trusting one that doesn't.
- **Repeatable language.** Write lines a rep can say out loud, verbatim, on a call. If it reads like marketing copy, rewrite it as speech.
- **Tie features to business outcomes.** Velocity, cost, governance, risk reduction, time to value. That's the language buyers decide in.
- **Always "Bolt.new," never "Bolt."**
- **No em dashes.** Use commas, colons, periods, or parentheses.
- **Date the facts.** Competitor pricing and positioning move fast. Note the "as of" date so reps know when a card needs a refresh.

---

# Asset 1: Battle Card (vs a named competitor)

*One card per competitor. Keep it to a single screen a rep can scan in under a minute. The worked example below uses Lovable; build the same structure for Replit, v0, Cursor, Webflow, and others using the competitive landscape in `bolt-buyer-personas`.*

## Pre-Draft Checklist

- **Which competitor, and for which persona?** A Lovable card for a creative (Persona 5) reads differently than a Cursor card for a CTO (Persona 2a). Name both.
- **What's the latest on their pricing and positioning?** Pull from `bolt-buyer-personas` and verify against current data. Note the date.
- **What are the real proof points?** Customer outcomes, metrics, named accounts we can reference. Get specifics.

## Structure

### 1. Competitor Snapshot
**Length:** 4-6 bullets
What they are, who they're for, pricing model, and their core strength. Be fair: reps need an accurate picture, not a strawman.

*Include:* what they do, their pricing model, their primary audience, their genuine strength, and any known weak spots (security incidents, pricing surprises, ecosystem lock-in).

### 2. Where Bolt.new Wins
**Length:** 3-5 points, each benefit-led
The differentiators that matter for this competitor and this persona. Feature, then outcome.

*Format each as:* [Capability] → [business outcome the buyer cares about].

### 3. Where They Win (be honest)
**Length:** 2-3 points
Where the competitor genuinely has the edge. Naming these earns rep trust and prepares them for pushback.

*Prompts:* What does this competitor do better? When is it the right call? What should a rep concede gracefully instead of arguing?

### 4. Landmines to Avoid
**Length:** 2-4 points
Traps in a competitive deal: claims not to make, comparisons that backfire, features to not overpromise.

### 5. Discovery Questions
**Length:** 4-6 questions
Questions that surface where Bolt.new fits and where the competitor falls short, without trashing them. Open-ended, outcome-focused.

### 6. Proof Points
**Length:** 3-5 items
Customer outcomes, metrics, named accounts, third-party stats. The evidence a rep drops into the conversation. Pull cited stats from `bolt-buyer-personas` (`third-party-research.md`) where relevant.

### 7. One-Line Positioning
**Length:** 1 sentence
The single line a rep says to frame Bolt.new against this competitor. Memorable, true, repeatable.

---

## Worked Example: Battle Card vs Lovable

*Persona context: most relevant for Persona 5 (creative / agency / freelancer) and Persona 1 (small business / founder). Facts as of June 2026, verify before use.*

**Competitor Snapshot**
- AI app builder that generates polished React apps from prompts. Strong, design-forward UI output.
- Credit-based pricing (around $25/mo for 100 credits). Costs climb with heavy iteration.
- Requires Supabase for the backend, which adds configuration and a third-party dependency.
- Primary draw: output looks good fast. Popular with creatives and founders building UI-first projects.
- Known weak spots: has had security incidents; credit model creates cost anxiety; weaker on enterprise governance.

**Where Bolt.new Wins**
- Unlimited iteration on higher tiers → creatives and PMs can refine without watching a credit meter, which is how real client and product work actually happens.
- Full-app capability, not just UI → buyers ship working apps with data and flows, not a pretty front end that stalls at the backend.
- Design System Agent → brand-consistent output at scale, the antidote to generic AI sameness. No equivalent in Lovable.
- No forced backend dependency → fewer moving parts for the buyer to configure and fewer third parties for security to review.
- Native GitHub integration → real handoff to engineering, not a code export a developer has to untangle.

**Where They Win (be honest)**
- For a quick, single-screen UI mockup, Lovable's output is fast and looks great. If the buyer only needs a polished landing page and nothing more, it's a fair fit.
- Their pricing entry point is simple to understand for a first-time buyer who only wants to dabble.

**Landmines to Avoid**
- Don't claim Lovable's output quality is poor. It isn't. Compete on iteration economics, full-app capability, and governance, not on "their UI is worse."
- Don't get into a credit-by-credit pricing math debate on the call. Reframe to total cost of real, iterative work.
- Don't promise a feature is live if it's in beta. Stay inside what's shipped.

**Discovery Questions**
- When you build something, how much do you iterate before it's right? (Surfaces credit-model pain.)
- Does this need a real backend, data, and user accounts, or is it mostly a front-end experience?
- How important is keeping output on-brand across everything your team or clients produce?
- Who owns the handoff to engineering today, and how clean is that handoff?
- Has your security team weighed in on the tools your team uses?

**Proof Points**
- Design System Agent enforces brand consistency from non-technical builders (no competitor equivalent).
- Cite a customer who moved from UI-only tooling to shipping a full working app on Bolt.new (pull a current named story).
- > "Only 4% of marketers use AI to write entire pieces independently: the overwhelming norm is human-directed, AI-assisted creation." (HubSpot AI Trends for Marketers 2025) Use to frame Bolt.new as the force multiplier, not the autopilot.

**One-Line Positioning**
Lovable gets you a good-looking screen; Bolt.new gets you a working app you can iterate on, keep on-brand, and hand to engineering.

---

# Asset 2: Objection Handler

*A repeatable format for the objections reps hear most, plus worked examples for Bolt.new buyers. The format is the product: once a rep internalizes it, they can handle objections this card doesn't cover.*

## The Format

For every objection, fill in five parts:

1. **The objection:** what the buyer actually says, in their words.
2. **Why they raise it:** the real concern underneath. (Often not what they said.)
3. **The reframe:** how to shift from the worry to the relevant truth. Acknowledge first, then reframe. Never dismiss.
4. **Proof:** the evidence that backs the reframe: a feature tied to an outcome, a metric, a customer, a cited stat.
5. **What to say:** a verbatim line the rep can use on the call.

**Notes:** Acknowledge before you reframe. "That's a fair concern" lands better than jumping straight to the rebuttal. Keep the "what to say" line short enough to say in one breath.

---

## Worked Example 1: "Is AI-generated code production-ready?"

- **The objection:** "AI tools spit out demos, not real code. We'd just have to rebuild it."
- **Why they raise it:** They've been burned. They've reviewed AI-generated PRs that looked right and broke in edge cases, or inherited prototypes that couldn't be refactored into a real codebase. Most relevant for Persona 2a (CTO) and Persona 4 (developer).
- **The reframe:** The gap isn't "AI code is bad," it's "most tools stop at the prototype." Bolt.new is built for the handoff: real code, native GitHub integration, output engineering can pick up and refine rather than throw away.
- **Proof:** Native GitHub integration for real dev handoff. WebContainers for transparent, inspectable execution. Point to a developer-facing customer story where the output went to production. (Cite a current one.)
- **What to say:** "Fair concern, most tools stop at the demo. The difference here is the output is real code in your GitHub, so your engineers refine it instead of rebuilding it. Want to see what the handoff actually looks like?"

---

## Worked Example 2: "What about security and compliance?"

- **The objection:** "We can't put an AI tool in front of our team without a security review, and that takes forever."
- **Why they raise it:** Security review adds four to six weeks to every enterprise cycle, and "shadow AI" (teams adopting tools faster than governance can keep up) is a live fear. Most relevant for Persona 2a (CTO) and the enterprise buyer generally. Note: security is the top friction point even for PM power users (44%).
- **The reframe:** Bolt.new's architecture is built for this conversation. WebContainers run code in the browser, so there's no remote server executing your code, a fundamentally different (and easier to review) security model. Pair that with granular admin controls and SSO.
- **Proof:** WebContainers (browser-based execution, no remote server dependency). Granular admin controls and publishing governance. SSO and standard enterprise controls. Disableable native publishing per security policy.
- **What to say:** "That's exactly the right question to ask. The architecture is built for it: code runs in the browser, not on our servers, so your security team is reviewing a much simpler model. I can get you the security documentation to start that review now."

---

## Worked Example 3: "We already use Cursor."

- **The objection:** "Our developers already have Cursor. Why would we add another tool?"
- **Why they raise it:** They're wary of tool sprawl and don't want to pay for overlapping capabilities. Most relevant for Persona 2a (CTO) and Persona 4 (developer).
- **The reframe:** Cursor and Bolt.new solve different problems, and they're complementary. Cursor is for developers doing line-by-line work in an existing codebase. Bolt.new is for generating full apps and letting non-developers (PMs, designers, marketers) build without consuming engineering capacity. This isn't "replace Cursor," it's "stop routing every internal build through your engineers."
- **Proof:** Bolt.new CLI integrates with Cursor for handoff. Position the split honestly: Cursor for working in existing code, Bolt.new for new-app generation and empowering non-dev teammates. (This honest framing is itself the proof for a skeptical developer.)
- **What to say:** "Keep Cursor, your developers should. Bolt.new isn't competing with it. It's for everything that currently lands on your engineers' backlog from product and marketing. They build it, your engineers review instead of build. The two even integrate for handoff."

---

# Asset 3: Competitive One-Sheet

*A single page that positions Bolt.new at a glance, for a specific buyer. Less about head-to-head combat (that's the battle card) and more about the clear, standalone case for Bolt.new. One sheet per persona where useful.*

## Pre-Draft Checklist

- **Who's the buyer?** Name the persona (read it in `bolt-buyer-personas`). The differentiators and proof points change by audience.
- **What's the one thing they should remember?** The single positioning idea the sheet drives home.
- **What proof do we have for this buyer?** Customer outcomes, metrics, cited stats relevant to them.

## Structure

### 1. Positioning
**Length:** 2-3 sentences
The standalone case for Bolt.new for this buyer. What it is, who it's for, and the core promise, in language the persona uses. Lead with the outcome, not the technology.

### 2. Key Differentiators
**Length:** 3-5 points, benefit-led
What sets Bolt.new apart, each tied to a business outcome. These are the points that hold up whether or not a competitor is in the room.

*Format each as:* [Capability] → [outcome the persona cares about].

*Examples of the shape (adapt to the persona):*
- WebContainers (browser-based execution) → a simpler security model and no remote server to review.
- Design System Agent → brand-consistent output at scale, even from non-technical builders.
- Native GitHub integration → clean handoff to engineering, real code, not a throwaway.
- Full-app generation → working apps with data and flows, not just UI components.
- Multi-stakeholder collaboration → developers, PMs, designers, and marketers in one tool instead of a different tool per role.

### 3. Proof Points
**Length:** 3-5 items
The evidence behind the positioning: customer outcomes, named accounts, metrics, third-party stats. Pull cited data from `bolt-buyer-personas` (`third-party-research.md`). Lead with the strongest number.

### 4. Target Buyer
**Length:** 2-4 sentences, or a short profile
Who this sheet is built for: the persona, their role, what keeps them up at night, and the trigger that makes them look for a tool like Bolt.new. This orients the rep on who to hand the sheet to and when.

*Prompts:*
- Which persona, and which roles map to it?
- What pain point opens the conversation?
- What's the moment Bolt.new becomes relevant for them?

---

## Tone Reminders

- **Benefit, not feature.** Every line answers "so what?" for the buyer.
- **Honest beats hype.** Concede real losses on the battle card. Acknowledge real concerns in the objection handler. Reps trust honest collateral and use it.
- **Say it out loud.** If a line can't be spoken naturally on a call, rewrite it.
- **One idea per asset.** The one-sheet has one positioning idea. The battle card has one competitor. The objection handler has one format.
- **Keep it current.** Date competitor facts and pricing. Flag for refresh.
- **Always Bolt.new.** Never just "Bolt."
- **No em dashes.** Use commas, colons, periods, or parentheses.
