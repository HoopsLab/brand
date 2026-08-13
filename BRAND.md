# HoopsLab brand usage guide

HoopsLab is a measurement instrument, not a hype supplement ad. Everything in
this guide flows from one commitment: we report what the camera can actually
see, we flag what it can't, and we refuse to grade broken readings. If a
design or a sentence would make a reading sound more certain than it is, it is
off-brand.

## Voice and tone

Precise, understated, sports-technical. Write like a lab notebook that a coach
would trust, not like an ad. Numbers come with units and context. Uncertainty
is stated, never hidden. Superlatives are earned by data or not used at all.

Three calibration pairs:

| Do | Don't |
| --- | --- |
| "Median release 0.68 s against a 0.54 s typical." | "AI-powered elite shot fixing." |
| "Elbow angle not measurable on this clip — camera below rim line." | "Our AI sees everything about your shot." |
| "7 of 10 makes today; arc consistency improved for the third straight session." | "He's basically automatic now. Unstoppable." |

Rules of thumb:

- Every quantitative claim carries a unit and, where relevant, a comparison
  point ("against a 0.54 s typical"), never a bare adjective.
- When a metric can't be read from the footage, say so in those terms: "not
  measurable on this clip", with the reason if known. Absence of data is a
  finding, not an embarrassment.
- No grade is better than a wrong grade. Copy never papers over a refused
  reading.
- Avoid "AI-powered", "revolutionary", "elite", "unlock", "game-changing".
  Prefer "measured", "estimated", "flagged", "within/outside typical range".
- Sentence case for prose. Uppercase is reserved for the display face (Anton)
  and eyebrow labels (Barlow SemiCondensed SemiBold, tracking .04–.06em).

## Logo

Files live in `logo/`. All are hand-authored SVG on a 64-unit grid, drawn with
`currentColor` plus the accent so they invert cleanly across themes.

- `mark.svg` — the ball-as-instrument mark: a basketball whose seams double as
  a reticle, with an accent-coloured reading point at centre.
- `mark-mono.svg` — single-colour variant, `currentColor` only. Use where the
  accent can't be reproduced (engraving, single-ink print, favicons on
  unknown backgrounds).
- `wordmark.svg` — "HOOPSLAB" set in Anton and converted to outlines, so it
  renders identically with no font installed. The viewBox is exactly the
  type's advance width, which is what makes the clear-space rule below
  measurable.
- `lockup-horizontal.svg`, `lockup-stacked.svg` — mark + wordmark with clear
  space built in.

### Clear space

The clear-space unit is one quarter of the mark's height (16 units on the
64-unit grid). Keep at least one unit of empty space on all sides of the mark,
the wordmark, and both lockups. The lockup files already include this padding
in their viewBox — rendering them edge-to-edge in a container gives correct
clear space automatically. Do not crop tighter than the shipped files.

### Minimum sizes

- Mark: 16 px square (it is the favicon). Below 16 px, do not render it.
- Wordmark: 12 px cap height on screen; 4 mm in print.
- Horizontal lockup: 120 px wide. Below that, drop to the mark alone.
- Stacked lockup: 72 px wide. Below that, drop to the mark alone.

### Logo don'ts

- Do not recolour the mark's reading point with anything but the theme's
  accent (`#ff7a33` dark / `#e8641e` light), or use `mark-mono.svg`.
- Do not add glows, gradients, bevels, or drop shadows to any logo asset.
- Do not re-set the wordmark as live text. It is Anton converted to outlines;
  live text re-flows, re-hints and re-spaces across platforms, and the shipped
  outlines are the trademark. Use the SVG.
- Do not rotate, skew, outline, or place the mark on the hero gradient.

## Colour

Dark is the default theme; light is a first-class override. Full token
reference and the three-state theming contract are in `README.md` and
`tokens/hoopslab.css`.

Do:

- Use `--accent` (orange) as the single dominant brand colour; `--accent-2`
  (teal) is a supporting counterpoint, used sparingly.
- Keep text on `--ink`/`--ink-2`/`--muted`; keep hairlines on `--grid`,
  `--baseline`, `--border`.
- Reserve `--border-hot` for genuinely "hot" emphasis (active selection,
  live state), not decoration.
- Reserve the hero gradient (`--hero-grad`) for hero moments — one per view
  at most.

Don't:

- Don't introduce new hues. The palette is closed; extensions go through this
  repo.
- Don't use status colours (`--good`, `--warning`, `--serious`, `--critical`)
  decoratively. They mean something.
- Don't put long-form text in `--accent` or on the hero gradient.
- Don't hand-mix "close enough" oranges. There are exactly two accent oranges,
  one per theme.

## Chart colours

These rules are load-bearing; breaking them breaks accessibility.

1. `--series-1` (blue), `--series-2` (orange), `--series-3` (green) are a
   colour-vision-deficiency-validated set. They are the only colours for
   multi-series data. **Never swap brand accents in for them**, even though
   `--series-2` happens to share a value with `--accent` in each theme — the
   set was validated together and travels together.
2. Series order is fixed: first series gets `--series-1`, second `--series-2`,
   third `--series-3`. Do not reassign per chart to "look better".
3. Grades always pair a letter with a colour (e.g. "B" on `--good`-tinted
   chip). Meaning must never ride on hue alone — every colour-coded value
   needs a text or shape counterpart.
4. `--band` marks target/typical ranges; `--baseline` marks reference lines;
   `--grid` stays at hairline weight. Charts on the court diagram sit on
   `--court`.
5. When a reading is flagged "not measurable", show it as flagged (muted, with
   the flag label) — never plot it as if it were a valid data point, and never
   grade it.

## What the brand must never do

- Never imply medical, physiotherapeutic, or biomechanical certification. The
  engine reports camera-visible kinematics; it does not diagnose, prescribe,
  or clear anyone to train.
- Never fabricate or imply athlete endorsement. Featuring measurement of an
  athlete's footage is not the athlete endorsing HoopsLab, and copy must not
  blur that line.
- Never use an athlete's likeness, footage, handle, or name in marketing
  without written consent covering that specific use. **This is not
  hypothetical** — there is analysis in the organisation built on footage
  whose creator has not been asked yet, and until he has agreed in writing,
  nothing derived from it ships publicly: no promo cut, no landing page, no
  paid campaign, and no repository that names him. Treat every new context as
  needing its own sign-off, and treat "it's already public" as irrelevant to
  the question.
- **Naming who we work with is their disclosure to make, not ours.** That
  applies to this kit too: partner and athlete presets belong with their own
  private instance, never in a public brand repository.
- Never present an estimate as a measurement, or a refused reading as a score.
- Never dress the product in hype-supplement aesthetics: no lens flares, no
  chrome, no "beast mode" copy, no fake urgency.
