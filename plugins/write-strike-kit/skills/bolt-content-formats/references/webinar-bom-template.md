# Webinar Bill of Materials (BOM) Template

A production checklist and content template for Bolt.new webinars. Covers everything from planning through post-event content. Work through each section in order; skip what doesn't apply.

Based on the editorial-calendar template used for HustleFund, Storybook/Bolt, and other Bolt.new webinars. The calendar of record is now ContentedCal.

---

## Export the finished BOM (Notion page + ContentedCal entry)

Webinar BOMs do **not** export as `.docx`. The finished package (all drafted assets plus the run of show) ships as a **new Notion page**, so everything lives in one doc, and then gets logged in **ContentedCal**, the editorial calendar of record. Two steps, in order:

### 1. Create the Notion BOM page

Create a new page as a **child of the Webinar Hub** (parent page ID `395d971055d6809dad1bff2c70e24b50`, https://www.notion.so/stackblitz/Webinar-Hub-395d971055d6809dad1bff2c70e24b50) using the Notion MCP (`notion-create-pages`). One new doc per webinar, filed under the Hub.

- **Title:** the webinar title (append the date if the title alone is ambiguous)
- **Content:** the filled-in BOM below, rendered as Notion-flavored Markdown:
  - Toggle headings (`{toggle="true"}`) for collapsible sections (Content Review Checklist, Partner Details, SEO & GEO)
  - Checkboxes (`- [ ]`) for all checklist items
  - Tables for the content BOM tracker and the run-of-show timeline
  - Date fields rendered as `@YYYY-MM-DD` inline mentions where dates are filled in
- Fetch the Notion enhanced-markdown-spec resource (`notion://docs/enhanced-markdown-spec`) before building the page content to ensure correct syntax.
- Confirm with the user before creating; return the new page URL when done.

### 2. Log it in ContentedCal

ContentedCal (contentedcal.com) is the in-house Supabase app: write through the already-connected Supabase MCP (`mcp__supabase__execute_sql`). There is no separate ContentedCal API key or connector.

Before writing anything, ask the user which **workspace and project** the webinar belongs to (list their projects if needed), then confirm exactly what you're about to create. Insert into `content_items`:

- `title`: webinar title
- `content_type_id`: the workspace's "Webinar" content type
- `status`: the workspace's Backlog or Scheduled board column (user's call)
- `channel`: "Other" unless the user prefers a specific channel
- `due_date`: webinar date; `publish_date`: same, unless the user says otherwise
- `project_id`: the project the user picked
- `assignee_ids`: the owner(s) the user names
- `description`: one-line summary **plus the Notion BOM page URL from step 1**, so the calendar entry and the doc stay connected

Optionally offer one item per major BOM asset (landing page, email invite, social, recap) instead of a single item, mirroring how launch projects are structured. The schema evolves: check current columns with a `SELECT ... LIMIT 1` before inserting, and confirm with the user before any write.

---

## Event details

Fill these in first. Everything else flows from them.

- **Webinar title:**
- **Date and time:** (include timezone)
- **Duration:** (default: 45 min + 15 min Q&A)
- **Format:** (live demo, panel, fireside chat, workshop, AMA)
- **Platform:** (Luma, Zoom, StreamYard, etc.)
- **Recording plan:** (live only, recorded for replay, both)

### Speakers and roles

| Role | Name | Company | Bio needed? | Headshot needed? |
|------|------|---------|-------------|-----------------|
| Host / moderator | | | | |
| Speaker 1 | | | | |
| Speaker 2 | | | | |
| Guest / partner | | | | |

### Partner details

If co-hosted or co-marketed with a partner:

- **Partner company:**
- **Co-marketing goals:** (what both sides want out of this)
- **Partner goals:** (what the partner specifically needs: leads, brand exposure, product demo)
- **Partner deliverables:** (what they're providing: speaker, audience, promotion, content)
- **Approval process:** (who signs off on what, and by when)

---

## Audience and positioning

- **Target persona:** (small business owner / founder / entrepreneur; enterprise CTO / App Dev Leader; enterprise CPO; product manager; professional developer; marketer / creative agency / creative freelancer; general reader). See bolt-buyer-personas for the full profiles.
- **Funnel stage:** (TOFU / MOFU / BOFU)
- **Campaign type:** (thought leadership, product education, customer showcase, partner co-marketing)
- **What the audience gets out of it:** (be specific: not "learn about AI" but "see how to build a working site in 30 minutes")
- **Why they should care enough to register:** (the hook: what makes this worth an hour of their day)

---

## Content BOM

Every webinar generates multiple content assets. Check off what's needed and track status. Date fields are blank by default; fill in as dates are confirmed.

### Pre-event content

| Asset | Owner | Due date | Status | Notes |
|-------|-------|----------|--------|-------|
| Landing page / Luma description | | | | |
| Registration confirmation email | | | | |
| Reminder email (24 hours before) | | | | |
| Reminder email (1 hour before) | | | | |
| Email invite to existing list | | | | |
| Social: Eric Simons LinkedIn announcement | | | | |
| Social: Eric Simons X announcement | | | | |
| Social: Brand LinkedIn announcement | | | | |
| Social: Brand X announcement | | | | |
| Social: LinkedIn reminder (day of) | | | | |
| Social: X reminder (day of) | | | | |
| Partner cross-promotion posts | | | | |
| Slide deck / visual assets | | | | |
| Speaker prep doc / talking points | | | | |
| Demo script (if live demo) | | | | |

### Day-of content

| Asset | Owner | Due date | Status | Notes |
|-------|-------|----------|--------|-------|
| Opening script / host intro | | | | |
| Q&A moderation plan | | | | |
| Live social posts during event | | | | |
| CTA slide / closing offer | | | | |

### Post-event content

| Asset | Owner | Due date | Status | Notes |
|-------|-------|----------|--------|-------|
| Recording upload and hosting | | | | |
| Follow-up email (attendees) | | | | |
| Follow-up email (no-shows + recording link) | | | | |
| Social: Eric Simons recap (LinkedIn) | | | | |
| Social: Eric Simons recap (X) | | | | |
| Social: Brand recap (LinkedIn) | | | | |
| Social: Brand recap (X) | | | | |
| Blog recap or writeup | | | | |
| Short video clips from recording | | | | |
| Quote cards from speakers | | | | |
| Slide deck share (if applicable) | | | | |

---

## Copy templates

### Landing page / Luma description

Structure:
1. **Hook**: one sentence on why this matters right now
2. **What you'll learn**: three to four bullet points, outcome-oriented
3. **Who this is for**: one sentence targeting the persona
4. **Speaker bios**: two to three sentences each, credibility-focused
5. **CTA**: register button with specific language ("Save your spot" not "Submit")

### Email invite

- **Subject line:** specific and benefit-led. No "Join us for a webinar." Say what they'll get.
- **Body:** hook → what they'll learn (bullets) → speaker credibility → date/time → CTA
- **CTA:** single, clear ("Register now" or "Save your spot")

### Reminder emails

- **24-hour reminder:** restate the hook + logistics (date, time, link). Keep it short.
- **1-hour reminder:** just the link and a one-liner. "Starting in an hour. Here's your link."

### Follow-up emails

- **Attendees:** thank you → key takeaway → recording link → CTA (try Bolt.new, book a demo, etc.)
- **No-shows:** no guilt trip. "Here's what you missed" → recording link → same CTA

---

## Social promotion

### Voice

All webinar content, including brand social posts, uses the standard Bolt.new TOV from bolt-TOV-and-guidelines.

**Exception:** Social posts attributed to Eric Simons use his tone profile. Read `${CLAUDE_PLUGIN_ROOT}/skills/bolter-tones/references/eric-simons-tone.md` before drafting his posts. Apply his voice on top of the Bolt.new editorial guidelines. This applies only to Eric's social posts, not to landing pages, emails, or other webinar content.

### LinkedIn posts

Draft three posts minimum per account (Eric Simons + brand):
1. **Announcement** (one to two weeks before): what the webinar covers and why it matters
2. **Reminder** (day of or day before): shorter, urgency-focused, link to register
3. **Recap** (day after): key takeaway, link to recording

Target 800-1,300 characters. Professional with a sense of humor.

### X posts

Draft three posts minimum per account (Eric Simons + brand):
1. **Announcement**: hook + link. Target ~250 characters.
2. **Day-of reminder**: "Starting in [time]" + link
3. **Recap / highlight**: one standout moment or quote + link to recording

Brevity first. More room for personality than LinkedIn.

---

## SEO and GEO

If the webinar generates a blog recap or landing page that will live on bolt.new:

### SEO
- **Primary keyword:**
- **Secondary keywords:**
- **Search intent:** (informational / navigational / commercial / transactional)
- **Target SERP feature:** (featured snippet / people also ask / image pack / etc.)
- **Slug / URL:**
- **Meta title:**
- **Meta description:**
- **Internal links to include:**
- **External references:**

### GEO (Generative Engine Optimization)
- **Target AI platforms:** (ChatGPT / Perplexity / Google AI Overview / etc.)
- **Entity coverage:** (what brand, product, or concept should this content reinforce?)
- **Citation-worthy claims:** (stats, quotes, or definitions that should be clearly attributable)
- **Structured answer blocks:** (FAQ-style sections or direct answers to include)

---

## Content review checklist

### Writer self-review
- [ ] All copy is complete and on-brief
- [ ] Facts and claims verified
- [ ] Internal links added where applicable
- [ ] SEO / GEO elements incorporated (if web-published)
- [ ] Bolt.new TOV applied to all content (landing page, emails, brand social, slides, recap)
- [ ] Eric Simons tone applied to his social posts only

### Editor review
- [ ] Tone and voice on-brand
- [ ] Legal / compliance check (if needed)
- [ ] Final copy approved

### SME review
- [ ] Product specs and demo claims accurate
- [ ] Speaker bios and titles correct
- [ ] Approved

**Reviewer notes:**

---

## Timeline

| Milestone | Target date | Owner | Complete |
|-----------|------------|-------|----------|
| Event details locked | | | - [ ] |
| Speaker prep doc complete | | | - [ ] |
| Landing page live | | | - [ ] |
| First email invite sent | | | - [ ] |
| Social announcements posted | | | - [ ] |
| Slide deck finalized | | | - [ ] |
| Reminder emails scheduled | | | - [ ] |
| Webinar day | | | - [ ] |
| Recording uploaded | | | - [ ] |
| Follow-up emails sent | | | - [ ] |
| Social recaps posted | | | - [ ] |
| Blog recap published | | | - [ ] |
