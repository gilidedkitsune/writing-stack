# Competitor Research & Analysis Reference

Use this reference whenever a competitor URL is provided or the goal is to outrank existing content.

**Data source:** pull SERP results and competitor pages through `bolt-seo-geo`'s connected tools when available (`/serp-analysis`, `/competitor-analysis`, `/content-gap-analysis`). Check `bolt-seo-geo` first for what's connected versus gated. Only fall back to live web search if those tools aren't available. Don't fabricate SERP positions or metrics.

---

## Step 1: Search, Collect, and Inventory Competitor Pages

### 1a. Run searches

Search for the target keyword on both Google and Bing. Use the keyword exactly as provided, do not modify it. Prefer `bolt-seo-geo`'s SERP tools; if they're gated, use web search.

- Pull the top 3 organic results per engine (skip ads, featured snippets, and People Also Ask boxes).
- Collect up to 6 URLs total. Deduplicate: if the same URL appears in both, count it once and note it ranked on both.

Record the SERP inventory before fetching:

| # | Engine | URL | Title (as shown in SERP) | Position |
|---|---|---|---|---|
| 1 | Google | ... | ... | 1 |
| 2 | Google | ... | ... | 2 |
| 3 | Google | ... | ... | 3 |
| 4 | Bing | ... | ... | 1 |
| ... | | | | |

Note any patterns visible from the SERP alone: are results mostly how-tos? Listicles? Product pages? Opinion pieces? This signals the dominant search intent before you read a single page.

---

### 1b. Fetch and inventory each page

For each URL in the SERP inventory, fetch the full page and extract:

| Signal | What to capture |
|---|---|
| Title tag | Exact text, character count |
| Meta description | Exact text, character count |
| H1 | Exact text |
| H2s / H3s | Full heading list in order |
| Word count | Approximate total |
| Target keyword | Primary keyword the page is optimized for |
| Secondary keywords | Recurring terms and phrases throughout the body |
| Slug | The URL path |
| Internal links | Anchor text + destination (note if they link to product/pricing pages) |
| External links | Any cited sources or outbound links |
| CTA | What action the page drives, and where |
| Publish / update date | How fresh is the content? |
| Author / byline | Named author or anonymous? |
| Structured data | Any schema markup present? |

Produce one inventory table per page. Label each clearly with its source URL and SERP position.

---

### 1c. If a specific competitor URL was also provided by the user

Fetch and inventory it using the same table above, in addition to the SERP results. Label it as "User-provided URL" to distinguish it from SERP discoveries.

---

## Step 2: Evaluate Content Quality

Score each area honestly, the goal is to find where they're beatable.

### Depth & coverage
- Does the post fully answer the search query, or does it skim the surface?
- Are there subtopics a reader would expect that are missing or underdeveloped?
- Does it go beyond the obvious, or is it a rehash of common knowledge?

### Accuracy & freshness
- Is the information current? Look for outdated stats, deprecated tools, or stale advice.
- Are claims supported with sources, or asserted without evidence?

### Structure & readability
- Is the heading structure logical, or does it meander?
- Are sections balanced, or are some thin and padded?
- Does the intro get to the point, or does it waste the first 200 words?
- Does it use walls of text, or is it scannable?

### Search intent match
- Does the content match what someone searching this keyword actually wants?
  - Informational: does it teach?
  - How-to: does it give clear steps?
  - Commercial: does it help compare or decide?
- Is there a mismatch between the keyword and what the post delivers?

### CTA & conversion
- Is the CTA relevant and timely, or bolted on at the end?
- Does the post earn the CTA, or does it feel like a bait-and-switch?

---

## Step 3: Identify the Gaps

After the quality eval, list specific gaps, these become your competitive advantages:

**Content gaps** — topics, subtopics, or angles the post doesn't cover that a reader would want.

**Depth gaps** — sections that exist but are too shallow. Where could you go deeper and add real value?

**Freshness gaps** — outdated information you can replace with current data, examples, or context.

**Perspective gaps** — the post covers what, but not why it matters, or how it applies to a specific audience (e.g., devs, founders, enterprise teams).

**Structural gaps** — the information exists but is buried, poorly organized, or hard to scan.

**Intent gaps** — the post is optimized for the keyword but doesn't actually satisfy the reader's real question.

---

## Step 4: Define the Differentiated Angle

Don't write the same post longer. Pick one of these strategies:

| Strategy | When to use it |
|---|---|
| **Go deeper** | Competitor is shallow. You can cover the topic more thoroughly and usefully. |
| **Sharper angle** | Competitor is generic. You can speak directly to a specific audience or use case. |
| **Fresher take** | Competitor is outdated. You have current data, examples, or context they don't. |
| **Better structure** | Competitor is hard to scan or poorly organized. Your structure alone is the win. |
| **Product-led** | Competitor can't tie the topic back to a product. You can, naturally, not forcefully. |
| **Stronger POV** | Competitor is neutral to a fault. A clear opinion or stance makes the post more memorable and linkable. |

State the chosen strategy in the content brief under "Competitor context."

---

## Step 5: Competitive Brief Summary Block

Include this block in every content brief when a competitor URL is involved:

```
### Competitor analysis: [competitor URL]

**Their angle:** [1 sentence summary of what they're going for]
**Word count:** ~[X] words
**What they do well:** [be honest, note genuine strengths]
**Key gaps:**
- [Gap 1]
- [Gap 2]
- [Gap 3]
**Our differentiated angle:** [1-2 sentences on what makes this post better]
**Strategy:** [Go deeper / Sharper angle / Fresher take / Better structure / Product-led / Stronger POV]
```

---

## Multiple Competitor URLs

If more than one URL is provided, run Steps 1-3 on each, then synthesize:
- What does every competitor cover? (table stakes, must include)
- What does only one cover? (worth considering)
- What does nobody cover? (biggest opportunity)

Produce a single differentiated angle that beats the field, not just one post.
