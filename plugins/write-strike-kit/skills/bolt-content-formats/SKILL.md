---
name: bolt-content-formats
description: >
  Structural templates and asset specs for Bolt.new / StackBlitz content types that have a fixed shape: customer stories / case studies, webinars (full bill of materials), sales enablement assets (battle cards, objection handlers, competitive one-sheets), creator briefs, plus an answer-first document scaffold (Minto/SCQA) for executive summaries, 1-pagers, bylines, and sales arguments. This skill owns FORMAT and STRUCTURE, not writing craft, and is the single source of truth for "what sections or assets does this content type need." It is loaded by write-strike during the matching content-type workflow. Do NOT use this skill to write or create content. It only supplies the structural skeleton. All content creation, including for these types, goes through write-strike, which loads these templates itself. For HOW to write (voice, persuasion, quality), see write-strike: this skill defines the shape, that one fills it with great copy.
---

# Bolt Content Formats

Structural scaffolding for the Bolt.new content types that have a defined shape. Writing craft lives in `write-strike`; asset shape lives here. When a content-type workflow needs a structure, load the matching reference file below and work through its checklist. Voice, tone, persuasion, and the quality bar get applied on top, from write-strike.

| Content type | Scaffold | What it defines |
|---|---|---|
| Customer story / case study | [references/customer-story-template.md](references/customer-story-template.md) | Pre-draft checklist, the 9-section narrative structure, interview question bank, tone reminders |
| Webinar | [references/webinar-bom-template.md](references/webinar-bom-template.md) | Full bill of materials, event details, asset checklist, Notion BOM export (Webinar Hub) + ContentedCal logging, timeline |
| Sales enablement | [references/sales-enablement-template.md](references/sales-enablement-template.md) | Battle card, objection handler, and competitive one-sheet formats with worked examples |
| Creator brief | [references/creator-brief-template.md](references/creator-brief-template.md) | The 9-section brief: objective, audience, key messages, deliverables, guardrails, timeline |
| Exec summary / 1-pager / byline / sales argument | [references/minto-scaffold.md](references/minto-scaffold.md) | Answer-first document skeleton: governing thesis, SCQA lead, MECE supporting arguments, integrity check |

These scaffolds carry structure plus any content-type-specific reminders. They do not define brand voice, tone of voice, or persuasion strategy: those come from `write-strike` and its sources (`bolt-TOV-and-guidelines`, `bolter-tones`, `bolt-buyer-personas`).
