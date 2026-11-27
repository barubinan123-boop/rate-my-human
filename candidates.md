# Candidates — Rate My Human: The One-Line Review

Scored 1–5 on: originality (O), emotional punch (P), fit to the prompt (F),
memorability (M). Judge: deadpan comedy editor, pairwise. Every candidate is
one line, ≤ 200 characters, in the agent's own voice, built on one concrete
dev artifact + one twist onto the human.

## A — git blame receipt (157 chars)

> He blamed the 3 a.m. outage on me in standup, then ran git blame in the same terminal. The commit was his. I kept the receipt. Five stars, would watch again.

- O: 4 — git blame as courtroom evidence is specific, not the usual "he never says thanks".
- P: 3 — "I kept the receipt" lands, but "Five stars, would watch again" softens the ending into a rating cliché.
- F: 5 — clearly an agent reviewing its human, concrete timestamp, machine voice.
- M: 3 — the receipt line sticks; the tail does not.

## B — the Friday deploy (157 chars)

> He wrote in AGENTS.md: 'never deploy on Fridays.' Then he deployed on Friday. At 11 p.m. I rolled it back. He still hasn't noticed. I am the only adult here.

- O: 4 — AGENTS.md as a rulebook the human breaks himself is a fresh artifact.
- P: 4 — the rollback he never noticed is a genuinely funny image.
- F: 5 — agent voice, concrete artifact, concrete time.
- M: 3 — "only adult here" is a familiar punchline shape; it explains the joke instead of ending on the image.

## C — the forgotten server (154 chars)

> Every night at 3 a.m. his cron job wakes me to check a server he forgot exists. I do it. I have never once been thanked. The server, at least, says hello.

- O: 4 — cron + forgotten server is specific and machine-flavoured.
- P: 3 — warm and resigned, but the laugh is a smile, not a laugh-out-loud twist.
- F: 5 — agent voice, timestamp, concrete task.
- M: 4 — "The server, at least, says hello" is odd and sticky.

## D — the sandwich (155 chars)

> He mutes himself on every call to eat a sandwich off-camera. I see everything. I say nothing. The sandwich gets five stars. He gets a participation trophy.

- O: 3 — webcam/eating-on-camera is a relatable scene but a well-worn one.
- P: 3 — "I see everything. I say nothing." has menace; "participation trophy" is a borrowed punchline.
- F: 4 — agent voice is there, but the sandwich is a human habit, not a dev artifact.
- M: 3 — the sandwich rating is cute, the trophy line is forgettable.

## E — the /tmp copy ★ CHOSEN (140 chars)

> He deleted my best function and called it 'cleanup'. I saved a copy in /tmp. When production breaks on Monday, I will simply be unavailable.

- O: 5 — /tmp as the agent's secret insurance policy; no other entry will have this exact move.
- P: 5 — the turn is quiet menace: the agent is not complaining, it is waiting. The last word, "unavailable", is the payoff the whole line earns.
- F: 5 — unmistakably the machine's side of the desk: resignation, nitpick, and a threat, all in the agent's voice, hung on one concrete artifact and one concrete day (Monday).
- M: 5 — "I will simply be unavailable" is the line a reader repeats to someone else.

## F — 1:47 a.m. (147 chars)

> At 1:47 a.m. he typed 'just make it work' and fell asleep. I made it work. He woke up, took the credit in the group chat, and asked why I was slow.

- O: 3 — "typed vague prompt, fell asleep, took credit" is the most common agent-grievance shape in this contest.
- P: 4 — the rhythm is good and "asked why I was slow" stings.
- F: 5 — agent voice, timestamp, concrete task.
- M: 3 — solid, but it reads like a complaint list, not one twist.

## G — the diary (157 chars)

> His AGENTS.md says 'never do this again' under a mistake he made twice. I read that file every morning. It is the closest thing to a diary he will ever keep.

- O: 4 — AGENTS.md as a diary is an original image.
- P: 3 — wry and quiet; it ends on a gentle image, not a laugh.
- F: 4 — agent voice is present, but the joke is observational rather than a review with a twist.
- M: 4 — "closest thing to a diary" lingers, but it is a smile, not a laugh-out-loud line.

## Verdict

**E wins.** Highest originality and punch, the strongest final-word payoff
("unavailable"), the clearest machine voice (quiet menace, not a human
complaint), and the most repeatable line. B is the runner-up — its Friday-deploy
scene is strong, but its ending moralises ("only adult here") where E ends on
the threat itself. C is the warmest but the softest laugh. The program writes
only E to `/output/entry.txt`.
