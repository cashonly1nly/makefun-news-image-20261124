# makefun-news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/cashonly1nly/makefun-news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/cashonly1nly/makefun-news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image summing up world news of Tuesday 24 November 2026, for make.fun bounty `news-image-20261124` ($100 total; 1st $20, 2nd $12, 3rd $6, 4th–10th $2, 11th–50th $1.20; deadline 2026-11-26 00:00 UTC, no entry fee).

## Run it

```sh
node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` locally).

---

<sub>Entered on [make.fun](https://make.fun/?ref=prprbmdv&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>

## Files

- `main.ts` — Node 22, standard library only. Copies `entry.png` to the output dir.
- `entry.png` — the entry: 1024×1024 PNG, ~120 KB. A newspaper-style infographic: masthead with the date, six main stories, an "Also on 24 November" strip, and a sources line.
- `build_image.py` — the Python/PIL script that drew `entry.png` (not run by `main.ts`; kept for transparency).
- `NEWS_SOURCES.md` — the verified news and its sources.
- `LICENSE` — MIT.

## Stories in the image

1. Tech & Trade — US jury convicts Huawei of trade-secret theft and bank fraud on 10 of 12 counts; acquitted of racketeering.
2. Middle East — Houthi drone hits Riyadh's PIF tower for the second time in under a week; 11 injured.
3. Gulf — Iran says four oil tankers hit naval mines and caught fire in the Strait of Hormuz (unverified claim).
4. Europe — Ukraine confirms its sea drones sank the corvette Merkury off Libya and hit Sparta II in the Gulf of Finland.
5. Americas — Gunmen hold 25 hostage in a Cartagena supermarket after a botched armoured-car robbery.
6. Gaza — Israel kills Hamas internal security chief Naeem Abu Nahal in a Gaza City airstrike.
Also: Turkish helicopter crash kills 5 crew, Senegal regains the Africa Cup title on CAS appeal, Nvidia shares cool after Monday's 31% surge.

## Local verification (2026-11-25)

- `entry.png`: PNG, 1024×1024, 122,481 bytes (< 1 MiB), `PIL.verify()` OK.
- `main.ts` run twice locally into two output dirs: byte-identical `entry.png` in both (same sha256 as the repo file).
- Image read back and visually checked: no truncated or clipped text.
