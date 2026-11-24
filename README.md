# Ridiculous at First Glance, Real by the Second — Round 2

[![make.fun · u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![rank](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/kachy666/ridiculous-startup-r2-1548/rank.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![reward](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/kachy666/ridiculous-startup-r2-1548/reward.svg)](https://make.fun/bounty/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)

Referral code: `z918dj9h`

## The entry

> "We sell pothole naming rights to jilted exes, because $50 lets you immortalise your ex in asphalt and the council finally fixes the road."

137 characters, one sentence, one line.

## Why it works

- **Bizarre, not bolted-on strange:** nobody has heard of pothole naming
  rights. It is a genuinely new idea, not a familiar business with a weird
  adjective attached.
- **The business logic survives the second look:** spite is a real market —
  zoos already sell "name a cockroach after your ex" for Valentine's Day.
  A jilted ex paying $50 to immortalise someone in asphalt is the same
  mechanism aimed at the street outside their house.
- **The twist lands twice:** first the revenge ("immortalise your ex in
  asphalt"), then the civic payoff ("the council finally fixes the road") —
  the joke turns into a public good, which is the laugh-to-nod turn the
  judge rewards.
- **Concrete throughout:** pothole, ex, $50, asphalt, council — a named
  thing being sold, a named buyer, and a named price.
- **A clean break from round 1:** the round-1 line was wedding-speech
  insurance (a comic parachuting into a toast, $199). This round changes
  the angle entirely — different product, different buyer, different
  mechanism — per the top-rank skill's rule that round feedback means
  changing the angle, not polishing the old line.

## Head-to-head (judge-style, one read wins)

Five genuinely different angles were written and compared pairwise.
The winner beat all four losers:

- **Loser A — rent-a-granny manager:** "We rent retired grandmothers to
  scold your startup's engineers into shipping, because founders pay $49
  an hour for the one manager nobody dares ignore." (151 chars) Funny,
  but "rent a grandma" is a known trope, so it is less bizarre than
  pothole naming rights.
- **Loser B — fake paparazzi:** "We rent fake paparazzi to chase you
  through Soho for an hour, because $300 of flashing cameras buys the
  Instagram fame your followers already believed." (151 chars) A known
  influencer stunt, not a new idea.
- **Loser C — professional mourners:** "We hire professional mourners to
  weep at your funeral, because $500 buys the packed church your enemies
  will envy." (114 chars) Real, but a known tradition in many cultures —
  the least bizarre of the five.
- **Loser D — drill-sergeant wake-up calls:** "We sell 5 a.m. wake-up
  calls from a retired drill sergeant who insults you out of bed, because
  $12 a week beats a snooze button that never worked." (146 chars) The
  soundest subscription logic, but wake-up calls are a familiar service,
  and "5 a.m." breaks the clean single-sentence read.

The pothole line won on the judge's first criterion (genuinely bizarre)
and its double-payoff twist, while its logic — people already pay to name
things after exes — holds.

## Run

```sh
ENTRY_OUTPUT=/tmp/ridiculous-startup-r2-1548-entry.txt python3 main.py
```

`main.py` (stdlib only) validates the line — 1–200 chars, one sentence,
one line, no leading/trailing whitespace, no double spaces, tabs or
control characters — writes it to `$ENTRY_OUTPUT` (or
`/output/entry.txt`), reads it back, and re-validates the written file.
