# Writing Stack

Three Claude Code plugins for written content. One researches, one writes, one edits. Install all three and they form a find-then-make-then-fix workflow.

- **the-stacks** researches: stats, quotes, and sources traced to their primary origin, with a do-not-cite trap list and ready-to-use citations.
- **write-strike-kit** writes the draft (9 skills behind one routing spine).
- **mr-gay** edits the draft (verdict-first review, then quick-fix or full report).

## Install (one time)

In Claude Code, add this marketplace, then install all three plugins:

```
/plugin marketplace add gilidedkitsune/writing-stack
/plugin install the-stacks@writing-stack
/plugin install write-strike-kit@writing-stack
/plugin install mr-gay@writing-stack
```

You will be asked to trust the marketplace the first time. After that you are set.

> **This repo is private**, so two things have to be true before Step 1:
> 1. You have a **collaborator invite** to this repo (ask Taylor) and you've accepted it.
> 2. Your git is **signed in to GitHub** on this machine — run `gh auth login`, or have an SSH key on your GitHub account.
>
> If `/plugin marketplace add` fails, it's almost always one of those. Quick test: you should be able to run `git clone git@github.com:gilidedkitsune/writing-stack.git`. Fix the access, then retry Step 1.

## How to use them

The skills **trigger automatically** when you describe a task, so most of the time you just talk:

- "Find stats for this piece" or "what's the competitive landscape" starts the-stacks.
- "Draft a customer story about a team that shipped in a weekend" starts write-strike-kit.
- "Edit this" with a pasted draft starts mr-gay.

To call one explicitly, plugin skills are namespaced `plugin:skill`:

```
/the-stacks:the-stacks             # research a claim, a stat, a landscape
/write-strike-kit:write-strike     # start a piece
/mr-gay:mr-gay                     # edit a piece
```

### The find-make-fix flow

1. **Research** in the-stacks, when a piece needs real stats, quotes, or a competitive landscape, not vibes. Every finding is traced to its primary source, dated, checked against the trap list, and handed back as a stat card ready to paste.
2. **Draft** in write-strike-kit. It picks the workflow for your content type, asks who it's for and applies the default voice (or a specific person's, from bolter-tones), pulls live SEO/GEO data when the piece needs it, and treats stops-slop's rules as drafting constraints from the first sentence, not a cleanup pass.
3. **Sharpen** with the edit menu. stops-slop runs first and always, then whichever the piece needs: mr-gay for the copyedit, the Ogilvy pass for persuasion, aeo-craft for citability on anything bound for publication.
4. **Loop** as needed. A structural rewrite goes back to write-strike-kit; line-level polish stays in mr-gay; a thin or stale source goes back to the-stacks.

## What is in write-strike-kit

write-strike is the front door; it loads the others only when a job needs them.

| Skill | Job |
|---|---|
| write-strike | The writer and routing spine |
| tone-and-guidelines | The default voice, plus editorial rules and writing tips |
| bolter-tones | Voice profiles for writing as a specific person instead of the default. Empty for now; add a profile whenever that's the job |
| content-formats | Templates for fixed-shape content (customer story, webinar, sales enablement, creator brief) |
| blog | The blog content-type default: write, brief, optimize, outrank a competitor |
| ogilvy-copywriting | Persuasion principles, plus an optional voice |
| stops-slop | The AI-tells filter and the 35/50 gate, applied as drafting constraints |
| aeo-craft | The citability sculpt for published work: gets a draft found, extracted, and cited by AI answer engines |
| seo-geo | Live SEO/GEO data and tooling (setup below) |

There's no persona library anymore: write-strike asks who a piece is for directly (role, seniority, what they already know) instead of picking from a ranked list.

## seo-geo setup (per person)

seo-geo reads your site's real Google Analytics and Search Console numbers using **your own** Google sign-in. Credentials live in `~/.config/claude-seo/` on your machine and are never stored in this repo; the GA4 property and Search Console domain it targets come from a `config.json` you set up, not a baked-in default. The first time you use it, follow the setup steps inside the skill.

## the-stacks setup (per person)

the-stacks points at your own research libraries so verified finds and known-bad stats compound over time instead of getting re-researched every run. It ships with five placeholders left blank in `the-stacks/SKILL.md`; fill each in with wherever that material lives for you (a Notion page, a Google Doc, a folder, a URL, it doesn't matter):

| Placeholder | What to put there |
|---|---|
| `[VERIFIED SOURCE LIBRARY]` | Where you keep stats you've already traced to origin |
| `[TRAP LIST LOCATION]` | Your Do Not Cite list of known-bad stats (can live inside the library) |
| `[RESEARCH HUB]` | Where finished research reports get filed |
| `[YOUR COMPETITIVE SET]` | The companies to track by default for market intel |
| `[YOUR DOCS LOCATION]` | Where exported documents should be saved |

Starting from nothing is fine: create two empty pages, a source library and a research hub, and let them fill up. The skill offers to deposit verified finds and newly discovered traps every time it runs.

## Getting updates

When a new version is pushed, you receive it automatically on next launch, or pull it now:

```
/plugin update the-stacks@writing-stack
/plugin update write-strike-kit@writing-stack
/plugin update mr-gay@writing-stack
```

## For the maintainer

The plugin copies are **generated** from the live skills in `~/.claude/skills/` by `build.py`, which rewrites every cross-skill path to the `${CLAUDE_PLUGIN_ROOT}` form that installed plugins require. The live skills stay the single source of truth. To ship an update:

1. Edit the skills in `~/.claude/skills/` as usual.
2. Regenerate with a bumped version: `python3 build.py 1.1.0`
3. Commit and push (or publish from GitHub Desktop).

Bumping the version is what triggers teammates' updates. Pushing new commits without a version bump will not deliver changes.

This marketplace is the **only** distribution channel. The claude.ai Shared Skills library was retired (Jul 2026): uploads there went stale between deploys and duplicate copies hijacked skill routing in desktop sessions. Don't re-upload skills to it; point people here.
