# Intake by content type

The per-type intake questions for write-strike Step 1. Read only the block for the detected content type. Pick the two that matter most for Round 1 (they batch with the audience and mode questions in one AskUserQuestion call) and carry the rest into Round 2. Skip anything the brief already answered.

Where a block says to load a template from `bolt-content-formats`, that template's own pre-draft checklist is part of the intake for that type.

---

**Blog:** delegated to `bolt-blog` at routing; it runs its own intake. Don't run blog intake here.

**Customer story:**
- Load `${CLAUDE_PLUGIN_ROOT}/skills/bolt-content-formats/references/customer-story-template.md` and work through its Pre-Draft Checklist
- Customer name, company, what they built, the problem before, the measurable outcome
- Available assets: interview transcript, quotes, screenshots, data?

**Social:**
- Platform (LinkedIn, X, Reddit)
- Key message or hook
- Links or assets to include
- Part of a series or standalone?

**Email:**
- Email type (announcement, nurture, transactional, sequence)
- Subject line direction (if the user has one in mind)
- Single CTA: what should the reader do?

**Website copy:**
- Page type: general web copy (homepage, feature page, pricing page, solution page, persona page, industry page) or single-use landing page (campaign, ad, event)?
- Primary CTA

Then ask page-type-specific follow-ups:

- **General web copy:** What kind of page? (homepage, feature, pricing, solution, persona, industry, etc.) What's the page's primary job? Key differentiators or messaging to hit?
- **Single-use landing page:** Traffic source (paid ad, email, social, event)? What does the referring content promise? Single conversion goal?

**Long-form (whitepaper, ebook, guide, survey/research report):**
- Topic and thesis
- Target length (~2,000–5,000+ words)
- Chapter/section structure (if the user has one)
- Source material and citation constraints (the format itself is fixed: Chicago superscript + Works Cited, per tone-and-guidelines)
- Survey/research report variant, also ask: data source (spreadsheet, survey tool, raw data), key findings the user wants highlighted, visualization needs (tables, charts to describe)

**Ad copy:**
- Platform and format (Google Ads, Meta, LinkedIn, display)
- Character limits
- Target audience (which persona, this drives the variant output)
- Key message or offer
- Landing page URL (for message match)

**Executive brief / 1-pager:**
- Format: executive summary (1-2 pages, summarizes a source document) or 1-pager (single page, stands alone)?
- Source document or subject, and the goal
- Key decisions, recommendations, or must-include points to surface
- Distribution context (sales leave-behind, conference handout, email attachment)

**Byline / thought leadership:**
- Named author and their voice/perspective
- Publication target (if any)
- Core argument or thesis

**Webinar:**
- Load `${CLAUDE_PLUGIN_ROOT}/skills/bolt-content-formats/references/webinar-bom-template.md` and work through the Event Details section first
- Webinar title, date/time, format, platform, speakers
- Partner details (if co-hosted)
- Target persona and funnel stage
- Which content assets are needed (the BOM checklist: landing page, emails, social, slides, recap)
- Voice: all webinar content uses the default voice. Personal tone profiles apply only to social posts attributed to a named person (see Webinar-specific in Step 4)

**Sales enablement:**
- Load `${CLAUDE_PLUGIN_ROOT}/skills/bolt-content-formats/references/sales-enablement-template.md` and work through the relevant asset's checklist
- Asset type (battle card, objection handler, competitive one-sheet)
- Target buyer persona
- Key objections or competitive positioning

**Creator brief:**
- Load `${CLAUDE_PLUGIN_ROOT}/skills/bolt-content-formats/references/creator-brief-template.md` and work through its Pre-Brief Checklist
- Creator type (influencer, content partner, agency)
- Deliverables expected
- Key messages and guardrails
