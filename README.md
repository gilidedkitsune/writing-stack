# Bolt Writing Plugins

Two Claude Code plugins for Bolt.new and StackBlitz content. One writes, one edits. Install both and they form a make-then-fix workflow.

- **write-strike-kit** writes the draft (9 skills behind one routing spine).
- **mr-gay** edits the draft (verdict-first review, then quick-fix or full report).

## Install (one time)

In Claude Code, add this marketplace, then install both plugins:

```
/plugin marketplace add gilidedkitsune/writing-stack
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

- "Draft a customer story about a team that shipped in a weekend" starts write-strike-kit.
- "Edit this" with a pasted draft starts mr-gay.

To call one explicitly, plugin skills are namespaced `plugin:skill`:

```
/write-strike-kit:write-strike     # start a piece
/mr-gay:mr-gay                     # edit a piece
```

### The make-then-fix flow

1. **Draft** in write-strike-kit. It picks the workflow for your content type, applies our voice and personas, pulls live SEO/GEO data when the piece needs it, and runs a slop check before handing the draft back.
2. **Sharpen** in mr-gay. It opens with a one-line verdict and the red-level issues, then you choose quick-fix or the full report.
3. **Loop** as needed. A structural rewrite goes back to write-strike-kit; line-level polish stays in mr-gay.

## What is in write-strike-kit

write-strike is the front door; it loads the others only when a job needs them.

| Skill | Job |
|---|---|
| write-strike | The writer and routing spine |
| bolt-TOV-and-guidelines | Brand voice, tone, and editorial rules |
| bolt-buyer-personas | Audience profiles and readability calibration |
| bolter-tones | Individual team-member voices |
| bolt-content-formats | Templates for fixed-shape content (customer story, webinar, sales enablement, creator brief) |
| bolt-blog | The blog content-type default: write, brief, optimize, outrank a competitor |
| ogilvy-copywriting | Persuasion principles, plus an optional voice |
| noslops | The AI-tells audit |
| bolt-seo-geo | Live SEO/GEO data and tooling (setup below) |

## bolt-seo-geo setup (per person)

bolt-seo-geo reads bolt.new's real Google Analytics and Search Console numbers using **your own** Google sign-in. Credentials live in `~/.config/claude-seo/` on your machine and are never stored in this repo. The first time you use it, follow the setup steps inside the skill. This plugin is internal only.

## Getting updates

When a new version is pushed, you receive it automatically on next launch, or pull it now:

```
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
