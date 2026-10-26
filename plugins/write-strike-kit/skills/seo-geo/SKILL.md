---
name: seo-geo
description: >
  First-party, CONNECTED source for your site's live SEO and traffic data: Google Analytics 4 (sessions, users, engagement, traffic by channel) and Google Search Console (impressions, clicks, CTR, position, top queries and pages), authenticated as the user. AI-visibility (GEO/AEO) numbers are NOT here: they come from a Cairrot connector, where one is configured. Use whenever the task needs your site's REAL numbers — "how's our traffic", "traffic by channel", "top search queries", "what are we ranking for", "Search Console", "GSC", "GA4", "organic clicks", "impressions", "CTR", "AI visibility", "share of voice", "are we cited by AI", "AEO" — or to feed live data into a performance report or content refresh. Also use to set up or troubleshoot the GA4 / Search Console connection, and to check what SEO data is connected vs. gated before running any /seo-* skill (never fabricate metrics; if a backend isn't connected, this skill says so). Prefer it over generic SEO skills when the task needs your site's actual data. Carries real Google credentials and whatever property IDs you configure — handle it with the same care as any other analytics access.
---

# seo-geo — live GA4 + Search Console for your site (plus the AI-visibility snapshot)

> **Handle with care.** This skill reads through your own real Google credentials, and the GA4 property ID / Search Console domain it uses come from your own config (see setup below), not a baked-in default. It contains **no passwords** — every user authenticates with their own Google account that already has access to the site's Analytics and Search Console. Do not redistribute a configured copy publicly. Credential handling is covered under **Sharing & credentials** at the bottom; read it before you hand this to anyone.

This skill pulls **real** traffic and search-performance numbers for your site and provides the honest map of which SEO data sources are connected. Two jobs:

1. **Pull live data** — GA4 (how people reach and use your site) and Search Console (how your site performs in Google search). AI-answer visibility is *not* pullable; read it from wherever your AI-visibility snapshot lives, if you have one.
2. **Govern the rest** — tell you, before any `/seo-*` skill runs, whether the data it needs is actually connected, so nobody ships invented numbers.

---

## What's connected (and what is NOT)

Read this before running any data skill. The rule that matters: **if a backend isn't connected, do not invent its output. Skip it (say so in one line) or ask the user for the data.** Never fabricate search volumes, keyword difficulty, rankings, or traffic.

**✅ CONNECTED — Google, for your site** (this skill, read-only, signed in as the user):
- **GA4** — sessions, users, engagement rate, page views, broken out by default channel group (Organic Search, Direct, Referral, etc.). Answers "how much traffic, from where, how engaged."
- **Search Console** — impressions, clicks, CTR, average position, by query or by page. Answers "what are we ranking for and how does it perform in Google."

**✅ CONNECTED where configured — AI-answer visibility, via Cairrot.** Live AEO numbers — visibility, named-vs-cited, per-model breakdown, competitor leaderboard, sentiment, AI-crawler hits — come from a **Cairrot** connector when one is set up (per-user setup in `aeo-craft`). **Use Cairrot for every AI-visibility question**; this skill doesn't carry that data itself. If you ever replace your AI-visibility tool, don't mix numbers across tools in one table or report the gap as a decline: different methodologies over different prompt sets aren't comparable, it's a change of instrument. Always name the source and the date window on every number.

**❌ NOT connected — keep gated, never fabricate:**
- **DataForSEO** (live SERP, search volume, keyword difficulty): the data parts of `/keyword-research`, `/serp-analysis`, `/seo-cluster`, `/seo-content-brief`, `/seo-dataforseo`, `/competitor-analysis`, `/seo-backlinks`.
- **Firecrawl** (full-site crawl): `/seo-firecrawl`, and the crawl steps in `/seo-audit`.
- **PageSpeed / CrUX** (Core Web Vitals field data): not wired.

**Always safe with no backend** (logic/judgment, no live data): `/content-strategy`, `/meta-tags-optimizer`, `/schema-markup-generator`, `/internal-linking-optimizer`, `/socialize-content`, and any WebSearch-driven trend scan. For AI-citation optimization, `aeo-craft` replaced the generic `/geo-content-optimizer` (retired Sep 2026); its Plan and Sculpt modes run without a backend, flagged blind, and only Measure needs Cairrot.

Connecting DataForSEO or Firecrawl is a one-time install for whoever owns the skills, not a content task. Hand it off rather than wiring it mid-draft.

---

## Pulling data

The bundled puller is `${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py` (on a standard install: `${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py`). Once `config.json` is set (see setup below), the data commands need no arguments; otherwise pass `--property`/`--site` on each call. Run it with the system `python3`.

```bash
# GA4 — traffic by channel, last 28 days (default)
python3 ${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py ga4
python3 ${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py ga4 --days 90

# Search Console — top queries, last 28 days (default)
python3 ${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py gsc
python3 ${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py gsc --dimension page --limit 50 --days 90

# List the GA4 properties this account can see (to find or confirm an ID)
python3 ${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py properties

# One-time (or when a pull fails with an auth error): sign in / refresh
python3 ${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py auth
```

Output is JSON straight from Google's APIs — read the numbers off it; don't round or embellish. A GA4 response carries rows of `[channel] → sessions, users, engagementRate, screenPageViews`; a GSC response carries rows of `[query or page] → clicks, impressions, ctr, position`.

**Two things to know about the numbers:**
- **Search Console lags 2–3 days.** The `gsc` command already ends its window 3 days back, so "last 28 days" means the 28 days ending 3 days ago. Don't expect yesterday's search data.
- **A Domain-level GA4 rollup can span multiple properties.** If the signed-in account can see more than one (a help center, a status page, staging), pass `--property <id>` to target the right one; run `properties` to get the IDs.

If `ga4` or `gsc` returns an auth error, the sign-in expired (see the note in setup) — run `auth` again and retry. If it says the OAuth client is missing, the user hasn't done the one-time setup below.

### Feeding other skills

When `/performance-reporter`, `/content-refresher`, or a content brief needs real traffic or search numbers, pull them here first, then hand the JSON to that skill. For AI-answer KPIs, pull them live from your Cairrot connector and pass the figures with their window. That's the whole point of having a connected source: those skills stop guessing.

For **which** `/seo-*` skill to run at **which** stage of a content project (research, outline, post-draft, post-publish), see `${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/references/seo-geo-toolkit.md` — the full orchestration map with a decision tree. This skill owns *what's connected and how to pull it*; that reference owns *the workflow choreography*.

---

## One-time setup (the wiring)

Each user does this once, on their own machine, with their own Google account. It takes ~10 minutes and it's a setup task, not a content task — if the person is non-technical, Claude can run the terminal steps for them; the human only needs to click through Google's screens.

**Prerequisite — Google access.** The account you'll sign in with must already be able to see the target site in both tools: at least **Viewer** on the GA4 property and at least a **Full/Restricted** user in Search Console. (Read access is enough — this skill never writes.) If they can't see the data in the GA4 and Search Console web UIs, fix that first.

1. **Make a Google Cloud project.** In [console.cloud.google.com](https://console.cloud.google.com), create a project (e.g. `claude-seo`).
2. **Enable three APIs** in that project (APIs & Services → Library): **Google Analytics Data API**, **Google Analytics Admin API** (powers the `properties` listing), and **Google Search Console API**.
3. **Configure the OAuth consent screen** — User type *External*, add the signing-in Google account as a *Test user*. (External + testing is fine; see the expiry note below.)
4. **Create an OAuth client** (APIs & Services → Credentials → Create credentials → OAuth client ID) of type **Desktop app**. Download its JSON.
5. **Place credentials.** Save that download as `~/.config/claude-seo/oauth_client.json`. (Create the folder if needed.)
6. **Install the Python deps:** `pip install google-auth google-auth-oauthlib google-api-python-client`
7. **Sign in:** `python3 ${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py auth` — a browser opens; approve the read-only scopes. This writes `~/.config/claude-seo/token.json`. Done.
8. **Set your property.** Create `~/.config/claude-seo/config.json` with `{"ga4_property": "properties/<id>", "gsc_site": "sc-domain:<your-domain>"}` (run `properties` first to find the GA4 ID). Without it, `ga4`/`gsc` need `--property`/`--site` on every call.

**Why OAuth-as-the-user, not a service account.** A service account would need to be *added* to the GA4 property (Administrator) and Search Console (Owner). Most of us only have Editor (GA4) / Full (GSC), which can read fine through the API but can't add a service-account user. Signing in as the user sidesteps that entirely — you read through the access you already have. No admin grants required.

**Token expiry.** While the consent screen is in *External / testing* mode, Google expires the saved sign-in roughly weekly. When a pull fails with an auth error, just re-run `auth`. (Moving the project to *Internal*, if the Google Workspace admin allows it, removes the weekly expiry.)

---

## Sharing & credentials

This skill is built to be handed to teammates and trusted agencies. Keep it safe:

- **The bundle has no secrets.** Only `SKILL.md`, `${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/scripts/seo_pull.py`, and `${CLAUDE_PLUGIN_ROOT}/skills/seo-geo/references/`. The puller reads credentials from `~/.config/claude-seo/`, which is **outside** the skill — so packaging or copying the skill never carries a password.
- **Each recipient brings their own credentials.** They run the one-time setup above with *their own* Google account (which must have access to the target site's data). Nobody shares `token.json` or `oauth_client.json`.
- **Treat `oauth_client.json`, `token.json`, and `config.json` like passwords.** Never paste their contents into chat, commit them to a repo, drop them in the skill folder, or send them over email/Slack. If one leaks, delete the OAuth client in Google Cloud Console and re-create it.
- **The IDs inside config.json are not secrets** (a GA4 property number and a domain name) but treat them as internal: they reveal which site this points at.
