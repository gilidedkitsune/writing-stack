# Prose craft: build it right the first time

The generative counterpart to `stops-slop`. That skill's rules are pass 0 here, so they shape the draft from the first word; its audit runs after, as verification, and should find nothing. Sanding can't add life a draft never had, and a tell sanded out of a finished sentence leaves a sentence that was built around the tell. Flat copy that passes every filter is still flat: craft happens at generation, not correction.

Work the passes in order. Pass 0 is the constraint set you write inside; the rest match how a piece actually gets built: promise, lead, sentences, specifics, rhythm, thread, ending, cut. Product examples in this file are invented for teaching; never reuse them as real Bolt.new claims.

---

## 0. Before anything: know the tells

**Why the tells exist, which is why pass 0 works.** A model writes whatever is most likely to come next, so by default it makes the choice that fits the widest range of readers and subjects. A person writes for one reader and one subject, so their choices come out uneven and specific. Every tell in the catalog is a form of that default choice: a sentence that signals importance instead of adding a fact, rhythm or formatting applied by rule, an ordinary fact dressed as a pivotal one. Knowing that, you can catch a tell the list hasn't named yet: ask whether this sentence was chosen for *this* reader, or would fit any reader of any piece.

Stops-slop's rulebook is a drafting constraint, not an audit you meet later. Before the first sentence, have it open: the banned list in `${CLAUDE_PLUGIN_ROOT}/skills/stops-slop/references/banned.md`, the Tier 1 vocabulary and the §0 fingerprint patterns in `${CLAUDE_PLUGIN_ROOT}/skills/stops-slop/SKILL.md`, and the structural tells in `${CLAUDE_PLUGIN_ROOT}/skills/stops-slop/references/structures.md`. Read one pair in `${CLAUDE_PLUGIN_ROOT}/skills/stops-slop/references/slop-vs-gold.md` so the bar is in your ear, not only on your checklist.

Then write inside the constraints. Zero em dashes, and watch what replaces them (§5 covers the colon pileup). No adverb reflex; if the verb needs propping, find a better verb (§3). No fingerprint openers, no copula costumes ("serves as," "stands as"), no compulsive-summary closers (§7). No Tier 1 vocabulary, ever, in any voice, including a team member's.

The reason this is pass 0 and not a final check: a tell removed from a finished sentence leaves a sentence that was built around the tell. Copy written clean from the first word is built differently, and it reads differently. Stops-slop still runs at the end, as verification. If it finds something, the failure happened here.

## 1. Before the first sentence: the promise

Write one sentence above the draft, for nobody but you: **who this is for and what they walk away with.** Not the topic. The takeaway. In write-strike this sentence is Step 1, answered before any intake (who, what it is for, why they should give a shit); here you carry it to the top of the draft.

- Weak: "This post is about AI prototyping for enterprise teams."
- Ready: "An enterprise PM leaves knowing the three gates that stall AI prototypes in procurement, and what to bring to each one."

If the sentence won't come, the piece has no thesis yet. Go back to research; drafting won't fix it. Once it exists, it becomes the kill test for every section: anything that doesn't serve the promise is a darling, and it dies at the outline.

## 2. The lead

John McPhee calls the lead "a flashlight that shines down into the story." It aims the whole piece. It is also a promise about what kind of piece this is, and the piece has to keep it.

**Start with the thing, not the topic.** The specific fact, number, person, or scene. Never the category, the era, or the landscape. The slop-vs-gold file shows Orwell opening by picking a fight with an assumption while the slop version announces a topic. Announcing a topic is not a lead.

- Topic: "AI app builders are changing how enterprise teams think about prototyping."
- Thing: "A designer at an insurance company built in one afternoon what her engineering queue had priced at six weeks."

**The first sentence must be arguable or picturable.** If no reader could disagree with it and no reader can picture it, it's throat-clearing with good posture.

**Write past the warm-up, then cut back to where it starts.** First drafts clear their throat for a paragraph; that's fine, drafting is thinking. The fix is the delete-the-first-paragraph test: remove it and reread. If the piece still works, and it usually does, the real lead was sitting in paragraph two.

**Keep the promise.** Don't open with a stat the piece never returns to. Don't promise a how and deliver a why. If the lead and the piece disagree, one of them is lying: fix whichever one it is.

## 3. Sentences: engineering rules

Five rules, applied while writing, not after.

**Actor does action.** Put the doer in the subject slot and the deed in the verb. Nouns ending in -tion, -ment, -ness, -ity are usually verbs in hiding, dragging the sentence into abstraction. "The implementation of the migration resulted in improved build times" hides two actions and an actor. "We migrated, and builds got faster" hides nothing. (mr-gay hunts nominalizations during edits; write them out of existence first.)

**Subject and verb inside the first six words.** Then branch right. A sentence that opens with stacked qualifiers ("While it's true that, for most enterprise contexts, ...") makes the reader hold their breath waiting for the point. Say who does what, then qualify.

**End on the payload.** The last slot before the period carries the most weight; that's the stress position. Park the number, the name, or the claim there, and let the furniture sit mid-sentence. "The new onboarding flow drove a 40% jump in signups" lands. "A 40% jump in signups resulted from the new onboarding flow" trails off into upholstery. Run this on every sentence that carries weight: claims, openers, closers, headers.

**Pick verbs a camera could film.** Cut, ship, stall, drain, break. If the verb can't be filmed, a stronger one is usually buried nearby in a noun or an adjective. "Provides acceleration for" is "speeds up" wearing a lanyard.

**Budget the copulas.** Plain "is" beats dressed-up "serves as," and stops-slop kills the costumes on sight. But three "is" sentences in a row means nothing in the paragraph is happening. That's not a vocabulary problem, it's an action shortage: find what actually moves, and let it.

## 4. Concreteness: climb down the ladder

Abstraction is where copy goes to die politely. Every rung down the ladder buys belief:

> faster iteration → prototype to stakeholder review in a day → she demoed on Tuesday what she scoped on Monday

**The one-breath rule.** An abstract claim must touch ground within one sentence, before or after it. State the principle, then point at something: a number, a name, an artifact, a timestamp. If the paragraph is all principle, the reader has nothing to hold.

**The point-at-it test.** Can the reader picture it, count it, or catch it being false? This is the TOV three-rules test doing draft-time work: run it on every headline, claim, opener, and CTA as you write them, not just in the audit.

**Prefer the proper noun.** "Supabase migrations" beats "database tooling" beats "infrastructure." The specific term costs nothing and pays in trust; the reader who knows the term trusts you more, and the reader who doesn't still trusts the confidence.

**Numbers do the believing for you.** "1,000 songs in your pocket" needed no adjective. When a line goes abstract, don't decorate it. Descend it.

## 5. The music

Sentence-length monotony is what makes clean copy read dead. Gary Provost's five-word-sentences demonstration is the canonical proof (look it up once; it teaches the whole lesson in a paragraph): keep sentences the same length and the ear checks out; vary them and the writing sings.

Make it mechanical:

- **In any run of five sentences, at least one under eight words and one over twenty.** If three consecutive sentences match length, break one. Short works. Short lands the point. But a paragraph built only of jabs reads like a countdown, and the reader starts bracing for the next hit instead of listening, so you open one sentence's shoulders and let it carry the argument the whole way across the paragraph before you stop. Like that.
- **The period is the strongest punctuation you own.** A short declarative after a long build hits hardest. Spend it on the line that deserves it.
- **Watch the displacement.** With em dashes banned, drafts drift into colon pileups and semicolon chains instead. One colon-driven sentence per paragraph, at most. If every sentence has a hinge, nothing hinges.
- **Read it aloud.** The ear catches the drone the eye forgives. This is stops-slop's final test too; running it while drafting is cheaper.

## 6. Paragraphs and the thread

**One move per paragraph.** State a claim, prove a claim, or turn the argument. A paragraph doing all three is three paragraphs sharing a trench coat. The topic sentence names the move; everything after it executes.

**Thread given to new.** Open each sentence with something the reader already holds from the sentence before: a word, a name, an idea. Close each sentence with the new thing. When a sentence opens cold on a subject nothing set up, the thread snaps, and that snap is what readers mean by "it doesn't flow." (mr-gay diagnoses this as the cohesion check. Thread it at draft time and there's nothing to diagnose.)

**Connect with but or therefore, never and-then.** If a paragraph could open with "additionally," it hasn't earned its position: it should either contradict what came before (but) or follow from it (therefore, so). Trey Parker and Matt Stone's rule for story beats, and it holds for arguments. An and-then paragraph is a list item pretending to be a paragraph; either promote it to a real turn or fold it into its neighbor.

**Let the paragraphs be lopsided.** The point you care about gets the long paragraph; the housekeeping gets a line. Even coverage reads as generated (stops-slop §6 demands this texture after the fact; it's cheaper to build than to retrofit).

The same three rules run at outline time, on sections instead of paragraphs: one move per section, but-or-therefore joints, weight where you care. A piece drafted from an outline of and-thens will read as a list no matter how good the sentences are. write-strike Step 3 does exactly this.

## 7. The ending

**End on the fact, the image, or the consequence. Never the summary.** The reader just read the piece. Summarizing it back to them is the written version of explaining the joke, and the compulsive-summary closers ("Ultimately...", "At the end of the day...") are already banned in banned.md. This is what to do instead: land something.

**The kicker is the second-best line in the piece.** The lead gets the best one. Spend a real fact on the kicker, a specific with weight; Volkswagen closed on lemons and plums (the pair is in slop-vs-gold). If your last line could close any piece on the topic, it closes none of them.

**Stop when the thing is said.** Zinsser's rule, and the hardest one: when you've made the point, leave. If the last paragraph exists to wrap up, the piece ended one paragraph ago. Cut it and see.

**For conversion copy, the kicker sets up the ask.** The CTA is not the ending; the line before it is. "Start building" lands exactly as hard as the sentence above it earned.

## 8. The 10% pass

Stephen King's revision formula: second draft equals first draft minus ten percent. Run it before stops-slop ever sees the piece. The cuts, in order of yield:

1. **The first paragraph** (see §2; it was probably a warm-up).
2. **Adverbs** (already law: stops-slop kills them, so save it the trouble).
3. **"That"** wherever the sentence survives without it.
4. **Prepositional chains.** "The utilization of this approach by the team" is a five-preposition sentence hiding "the team used it."
5. **The darling.** The line kept because it sounds good. If it doesn't serve the promise from §1, it goes, and it hurts, and the piece gets better.

Then one read-aloud pass. Then hand it to stops-slop.

Track the cut rate. Under 5% means the pass didn't happen. Over 25% means draft looser and faster next time; cutting is cheaper than polishing.

---

## How this file fits the stack

| File | Job | When |
|---|---|---|
| **prose-craft.md** (this file) | How to build prose | Outline and draft time |
| **stops-slop** | What a tell looks like (its rules), and the 35/50 gate (its audit) | Draft time via pass 0; audit time as verification |
| **tone-and-guidelines** | Brand voice, mechanics, the three-rules test | Always |
| **slop-vs-gold.md** | The bar, shown not told | Read one pair pre-draft |
| **mr-gay** | The same physics, run as diagnostics on finished drafts | Edit time |

mr-gay's lenses (stress position, cohesion, thought-verbs, stance) are this file's rules pointed backward at an existing draft. If mr-gay keeps flagging the same lens on your work, reread the matching section here: the fix belongs in the drafting, not the edit.
