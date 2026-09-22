---
name: bolter-tones
description: >
  Reference library of individual voice and tone profiles, for writing in a specific
  person's voice instead of the default. Empty for now: add a profile whenever a
  specific person's voice needs to be reproduced. Until then, everything uses the
  default voice from tone-and-guidelines.
user-invokable: false
metadata:
  version: 2.0.0
---

# Skill: Bolter-Tones

**Goal:** Provide structured voice and tone reference profiles for writing convincingly as a specific person, when that's the job. This is the exception path; the default voice for everything is `tone-and-guidelines`.

## Available Voices

| Person | Role | Handle | Menu blurb | File |
|---|---|---|---|---|
| *(none loaded yet)* | | | | |

This table is the **single source of truth for the voice roster**. write-strike builds its voice-selection menu from it at draft time (the default voice from `tone-and-guidelines` + these rows via their Menu blurbs + Ogilvy). **Adding a voice:** drop a profile file in `${CLAUDE_PLUGIN_ROOT}/skills/bolter-tones/references/`, add a row here with a short Menu blurb; write-strike's menu follows automatically, no edit there. Follow the shape of a full profile: core traits, sentence patterns, what they avoid, tone spectrum, voice in 5 words.

## How to Use
1. Read the relevant person's tone file before drafting content in their voice.
2. Match their sentence patterns and topic framing.
3. Avoid anything listed in their "What They Avoid" section.
4. If no profile exists for the person the draft needs, say so and fall back to the default voice (`tone-and-guidelines`) rather than inventing one.
