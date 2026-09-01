# SEO/GEO Toolkit — workflow orchestration map

Which SEO/GEO skill to run at which stage of a content project. This reference owns the **choreography**; the skill's `SKILL.md` owns **what data is connected and how to pull it**.

**Before running anything, check connection status in `../SKILL.md` ("What's connected").** Google (GA4 + Search Console) is connected for bolt.new through this skill. DataForSEO, Firecrawl, and PageSpeed/CrUX are not. If a trigger below calls a skill whose backend isn't connected, skip it (say so in one line) or ask the user for the data — never fabricate volumes, difficulty, or rankings. Also skip any trigger when the user already handed you the data it would fetch (e.g. they gave you keywords → skip keyword research).

---

## Workflow triggers (availability-checked)

These fire when their stage and conditions are met **and** the data backend each one needs is connected.

### During research (Step 2)

| Condition | Action |
|-----------|--------|
| Content type is blog, long-form, or website copy AND the user hasn't provided target keywords | Run `/keyword-research` for the topic. Use results to inform the outline. *(Needs DataForSEO — gated. Ask the user for target keywords instead.)* |
| Content type is blog or long-form AND this is a Content Bonanza workflow | Run `/serp-analysis` on the primary keyword to see what Google rewards (format, depth, features, AI Overviews). *(Needs DataForSEO — gated.)* |
| The user mentions a competitor by name or asks to differentiate | Run `/competitor-analysis` on the named competitor. *(Data-heavy parts need DataForSEO; the strategic read does not.)* |
| Content type is blog and the piece is part of a series or hub | Run `/seo-cluster` to validate the topic-cluster structure and internal-link plan. *(Intent-only mode is safe with no backend; SERP-overlap mode needs DataForSEO.)* |
| You need bolt.new's current traffic or search performance to ground the piece | Pull it with this skill's `ga4` / `gsc` commands (connected). |

### During drafting (Step 4)

| Condition | Action |
|-----------|--------|
| Content type is blog, long-form, or website copy | Apply GEO/AEO rules from `${CLAUDE_PLUGIN_ROOT}/skills/write-strike/references/SEO-GEO-drafting.md` while drafting. A drafting rule, not a post-draft skill. |
| Content type is ad copy | Run the Schwartz diagnosis from `${CLAUDE_PLUGIN_ROOT}/skills/write-strike/references/schwartz-5x5-matrix.md` to set headline and lead strategy. Feeds the three-variant output. |

### After drafting (Step 5–6)

| Condition | Action |
|-----------|--------|
| Content will be published on bolt.new (blog, landing page, website copy) | Generate meta title + description. Offer `/meta-tags-optimizer` for alternatives. |
| Content includes FAQ or how-to sections | Offer `/schema-markup-generator` for FAQ, Article, or HowTo JSON-LD. |
| Content is a blog referencing other Bolt.new content | Run `/internal-linking-optimizer` to validate link structure and anchor text. |
| GEO priority is high (user stated it, or topic targets question/definition/comparison queries) | Run `/geo-content-optimizer` after the stop-slop audit: passage-level extractability, quotable statements, citation signals. |

---

## Offer-based triggers

Don't auto-run these. Present them as options (AskUserQuestion with `multiSelect: true`) at the right stage, and only surface ones that match the content type and context. Don't dump the full list.

### After outline approval (before drafting)

| Skill | When to offer | What it does |
|-------|--------------|-------------|
| `/seo-content-brief` | User wants a competitive brief (target word count, keyword density, heading structure) | Data-backed brief from SERP analysis *(needs DataForSEO)* |
| `/content-gap-analysis` | User is unsure of the angle, or wants gaps competitors miss | Surfaces topics/formats/angles competitors cover that Bolt.new doesn't |
| `/content-strategy` | The piece is part of a larger campaign or pillar | Pillars, clusters, prioritization framework *(safe with no backend)* |
| `/seo-plan` | User asks for a full SEO roadmap (rare in single-piece work) | Strategic plan: keyword priorities, calendar, technical recs |

### After presenting the draft (Step 6)

| Skill | When to offer | What it does |
|-------|--------------|-------------|
| `/content-quality-auditor` | User wants a quality score or publish-readiness check | 80-item CORE-EEAT audit with fixes |
| `/on-page-seo-auditor` | User wants a technical on-page review | On-page audit against the target keyword |
| `/seo-images` | Content has images, or user asks about image SEO | Alt text, file size, format, placement |
| `/seo-image-gen` | Content needs OG/hero/visual assets | Image generation plan with prompts (does not auto-generate) |
| `/entity-optimizer` | User wants stronger brand/author recognition in AI systems | Knowledge Graph and entity signal recs |
| `/socialize-content` | User wants to repurpose the piece for social | LinkedIn, X, or Reddit versions from the draft |

### After publish

Offer when the user shares a live URL or asks about performance:

| Skill | When to offer | What it does |
|-------|--------------|-------------|
| `/performance-reporter` | User wants a report/dashboard on content performance | SEO/GEO report with KPI tracking — **feed it real numbers from this skill's `ga4`/`gsc` pulls** |
| `/content-refresher` | Published content is aging or losing traffic | What to update: stale stats, new competitors, decayed sections — **ground it in this skill's GSC trend pull** |
| `/seo-audit` | User shares a live URL and wants a full audit | Comprehensive page audit *(crawl steps need Firecrawl — gated)* |
| `/seo-page` | User wants a deep single-page analysis | One URL: content, keywords, links, schema, performance |
| `/rank-tracker` | User wants to track keyword positions over time | Monitors SERP positions *(needs DataForSEO; for bolt.new's own queries, GSC position data via this skill is the connected alternative)* |
| `/seo-drift` | User wants to detect regressions on a page that was performing | Captures baselines and compares against stored snapshots |

---

## Data integrations

| Skill / source | Connects to | Status | When to use |
|----------------|-------------|--------|-------------|
| **bolt-seo-geo** (this skill) | GA4 + Search Console for bolt.new | ✅ connected | Real traffic and search-performance numbers for bolt.new. The default for "our actual data." |
| `/seo-google` | GSC, PageSpeed, CrUX, GA4 (generic) | partial | Generic Google-API skill. For bolt.new, prefer this skill's puller; `/seo-google` is for the PageSpeed/CrUX angles, which aren't wired. |
| `/seo-dataforseo` | Live SERP, keyword metrics, backlinks | ❌ gated | Search volume, difficulty, SERP features, competitor data — only with the DataForSEO extension. |
| `/seo-firecrawl` | Full-site crawl | ❌ gated | Site crawl, internal-link inventory — only with Firecrawl. |
| `/seo-backlinks` | Backlink profile | ❌ gated | Link signals — data parts need DataForSEO. |
| `/domain-authority-auditor` | Domain authority / competitive position | ❌ gated | How aggressively to target keywords — needs external authority data. |

---

## Quick decision tree

```
RESEARCH PHASE
  └─ Need bolt.new's current numbers? → bolt-seo-geo: ga4 / gsc  (connected)
  └─ Do we have keywords?
       ├─ No → /keyword-research  (DataForSEO gated → ask user for keywords)
       └─ Yes → Do we know what's ranking?
            ├─ No → /serp-analysis  (DataForSEO gated)
            └─ Yes → proceed to outline

OUTLINE APPROVED
  └─ Want deeper research? → offer /seo-content-brief, /content-gap-analysis

DRAFT COMPLETE
  └─ Will this live on bolt.new?
       ├─ Yes → meta tags, internal links
       │    ├─ High GEO priority? → /geo-content-optimizer
       │    └─ Has FAQ/HowTo? → /schema-markup-generator
       └─ No (social, email, internal) → skip SEO/GEO skills

POST-PUBLISH
  └─ Tracking performance? → bolt-seo-geo ga4/gsc → /performance-reporter, /content-refresher
  └─ User shares live URL? → offer /seo-audit (crawl gated) or /seo-page
```
