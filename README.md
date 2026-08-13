# HoopsLab brand kit

The single source of truth for HoopsLab's visual identity: design tokens,
logo assets, dashboard presets, and the usage guide. HoopsLab builds
**shotlab**, a basketball shooting-analysis engine, and a dashboard on top of
it. The identity codified here already ships in the live dashboard — this repo
records it; it does not reinvent it.

The brand's job is to look like what the product is: a measurement
instrument. shotlab reports what a camera can actually see, flags what it
can't ("not measurable on this clip"), and refuses to grade broken readings.
The visual system is correspondingly precise and understated. See
[`BRAND.md`](BRAND.md) for voice, logo, and colour usage rules.

## Contents

```
brand/
├── README.md              this file
├── BRAND.md               usage guide: voice, logo, colour, chart rules
├── LICENSE                CC BY 4.0 (brand assets)
├── tokens/
│   ├── tokens.json        machine-readable design tokens
│   └── hoopslab.css       CSS custom properties, all three theme states
├── logo/
│   ├── mark.svg           the mark (currentColor + accent)
│   ├── mark-mono.svg      single-colour mark (currentColor only)
│   ├── wordmark.svg       HOOPSLAB, Anton converted to outlines (no font dep)
│   ├── lockup-horizontal.svg
│   └── lockup-stacked.svg
└── presets/
    └── hoopslab.json      dashboard brand.json preset: HoopsLab
```

## Consuming the kit

**CSS custom properties.** Import `tokens/hoopslab.css` (or copy it in) and
reference `var(--token)` everywhere. It carries the complete three-state
theming contract described below, so consumers get dark, OS-light, and manual
toggling for free.

```css
@import "tokens/hoopslab.css";

.card {
  background: var(--surface);
  border: 1px solid var(--border);
  color: var(--ink);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow);
}
```

**JSON tokens.** `tokens/tokens.json` is the same data in a nested,
machine-readable structure (`color.dark`, `color.light`, `typography`,
`spacing`, `radius`, `shadow`) for build pipelines, native apps, or plot
themes. Light values are fully resolved: tokens with no light override
(`court` and the four status colours) repeat their dark values, so consumers
can read either theme flatly without a merge step.

**Dashboard `brand.json` presets.** The dashboard skins itself from a single
`brand.json` file. Drop one of the files in `presets/` in place (or point the
dashboard's brand path at it) to rebrand the instance without touching code.
The schema:

```json
{
  "name": "HoopsLab",
  "sub": "shot lab",
  "tagline": "measure what the camera can see",
  "mark": "🎯",
  "accents": { "dark": ["#ff7a33", "#40e0d0"], "light": ["#e8641e", "#0aa295"] },
  "footer": "shown under the last panel",
  "source": { "label": "link text", "url": "https://…" }
}
```

`accents` are `[accent, accent-2]` per theme and must come from the token
table below — presets restyle the chrome, they do not invent colours. `mark`
is a short emoji stand-in used where the SVG mark isn't practical (page
titles, share cards).

One preset ships here: `hoopslab.json`, the product itself. **Presets for
specific athletes or customers live with their own instance, not in this
public kit** — an instance preset names a person, and naming who we work
with is their disclosure to make, not ours.

## Typography

All faces are SIL Open Font License and are vendored (self-hosted) by each
consuming app — never loaded from a third-party CDN.

| Role | Face | Weight(s) | Treatment |
| --- | --- | --- | --- |
| Display / headlines | Anton | 400 | Uppercase, tight |
| Body / UI | Barlow | 400, 500, 700 | Sentence case |
| Labels / eyebrows | Barlow SemiCondensed | 600 | Uppercase, letter-spacing .04–.06em |

## Theming contract (read this — it is a real bug source)

The system is **dark-first** with three states, and all three are required:

1. **Bare `:root` is dark.** The dark tokens are the base, in no media query
   and under no attribute selector. Dark is what you get by default.
2. **`@media (prefers-color-scheme: light) { :root:not([data-theme="dark"]) { … } }`**
   applies the light overrides for OS-light users — but the
   `:not([data-theme="dark"])` guard exempts users who manually forced dark.
   Without the guard, a user on a light OS who toggles to dark gets dark for
   one paint and then the media query wins it back.
3. **`:root[data-theme="light"] { … }`** repeats the same light overrides
   unconditionally. This is what makes a manual light toggle win on a dark
   OS, where the media query in state 2 never matches. Omit it and the light
   toggle silently does nothing for dark-OS users.

The manual toggle therefore works by setting `data-theme="light"` or
`data-theme="dark"` on the root element, and removing the attribute to return
to following the OS. Blocks 2 and 3 must stay byte-for-byte identical; when
you change a light value, change it in both. If you have ever seen "the theme
toggle works on my machine but not the designer's", it was almost certainly
one of these two blocks missing.

Also set `color-scheme` (`dark` on `:root`, `light` in both light blocks) so
native form controls and scrollbars follow.

## Token reference

Colour tokens, with dark (default) and light values:

| Token | Dark | Light | Purpose |
| --- | --- | --- | --- |
| `--page` | `#0a0c12` | `#f6f5f1` | Page background |
| `--surface` | `rgba(26,29,40,.72)` | `rgba(255,255,255,.82)` | Translucent card/panel background |
| `--surface-solid` | `#191c27` | `#ffffff` | Opaque surface (menus, tooltips) |
| `--court` | `#0c0f16` | `#0c0f16` | Court-diagram ground (shared across themes) |
| `--ink` | `#f4f5f9` | `#12141c` | Primary text |
| `--ink-2` | `#c0c4d2` | `#464b5c` | Secondary text |
| `--muted` | `#8b90a3` | `#7d8194` | Tertiary text, captions, flagged readings |
| `--grid` | `rgba(255,255,255,.07)` | `rgba(18,20,28,.08)` | Chart gridlines, hairlines |
| `--baseline` | `rgba(255,255,255,.16)` | `rgba(18,20,28,.22)` | Chart baselines, reference lines |
| `--border` | `rgba(255,255,255,.09)` | `rgba(18,20,28,.10)` | Card and control borders |
| `--border-hot` | `rgba(255,138,62,.55)` | `rgba(232,104,32,.5)` | Active/live emphasis border |
| `--accent` | `#ff7a33` | `#e8641e` | Primary brand accent (orange) |
| `--accent-2` | `#40e0d0` | `#0aa295` | Secondary accent (teal), sparing |
| `--series-1` | `#3987e5` | `#2a78d6` | Chart series 1 (blue) — CVD-validated set |
| `--series-2` | `#ff7a33` | `#e8641e` | Chart series 2 (orange) — CVD-validated set |
| `--series-3` | `#1fbf85` | `#0f9d69` | Chart series 3 (green) — CVD-validated set |
| `--good` | `#17b34a` | `#17b34a` | Status: good (shared across themes) |
| `--warning` | `#fab219` | `#fab219` | Status: warning (shared) |
| `--serious` | `#ec835a` | `#ec835a` | Status: serious (shared) |
| `--critical` | `#e04545` | `#e04545` | Status: critical (shared) |
| `--delta-good` | `#2ad463` | `#0c7a30` | Positive deltas/trends |
| `--band` | `rgba(57,135,229,.14)` | `rgba(42,120,214,.10)` | Target/typical range fill in charts |
| `--hero-grad` | orange 100deg gradient | orange 100deg gradient | Hero moments only, one per view |
| `--shadow` | `0 14px 40px rgba(0,0,0,.45)` | `0 12px 32px rgba(30,34,48,.10)` | Elevation shadow |
| `--page-glow-1` | `rgba(232,119,46,.09)` | `rgba(232,119,46,.10)` | Ambient page glow, warm |
| `--page-glow-2` | `rgba(64,224,208,.06)` | `rgba(27,175,122,.06)` | Ambient page glow, cool |

Non-colour tokens:

| Token | Value | Purpose |
| --- | --- | --- |
| `--font-display` / `--font-body` / `--font-label` | Anton / Barlow / Barlow Semi Condensed | Font stacks |
| `--weight-regular/medium/semibold/bold` | 400 / 500 / 600 / 700 | Weights (semibold is labels only) |
| `--track-label` | `.05em` | Eyebrow/label letter-spacing (.04–.06em range) |
| `--space-1…8` | 4, 8, 12, 16, 24, 32, 48, 64 px | Spacing scale |
| `--radius-sm/md/lg/full` | 8 / 12 / 18 / 999 px | Corner radii |

**Palette rule worth repeating:** `--series-1/2/3` are a
colour-vision-deficiency-validated set for charts and must never be swapped
for brand accents; grades always pair a letter with a colour so meaning never
rides on hue alone. Full chart rules in [`BRAND.md`](BRAND.md).

## Logo notes

The mark is hand-authored on a 64-unit grid, draws in `currentColor` plus the
accent, and carries a `<title>`. Every file is valid standalone XML with no
external dependencies.

**Wordmark approach:** `wordmark.svg` is "HOOPSLAB" set in Anton — the same
display face used for headlines — and converted to filled outlines with
FontTools, so it renders identically with no font installed while remaining
typographically identical to the rest of the system. Its viewBox is exactly
the type's advance width (179.8 × 40 units, 40 being the cap height), which is
what makes the clear-space rule in [`BRAND.md`](BRAND.md) measurable rather
than eyeballed. Both lockups embed the same path geometry.

Regenerating it (after a tracking or wording change) means re-running the
outline conversion against `fonts/Anton-Regular.ttf` rather than editing path
data by hand.

## Licensing

The assets in this repository (logos, token definitions, documentation) are
licensed [CC BY 4.0](LICENSE). Code in other HoopsLab repositories is MIT.
Note the difference in spirit: the MIT code is yours to fork and build on,
but the HoopsLab name, mark, and wordmark are trademark-adjacent — forks and
derivatives may use the assets under CC BY (with attribution) but **may not
present themselves as HoopsLab** or imply endorsement by it.

## Typefaces

`fonts/` vendors the two OFL faces the system uses, so a consumer never
depends on a CDN or a locally installed copy:

| File | Role |
|---|---|
| `Anton-Regular.ttf` | display — headlines, stat values, the wordmark's source |
| `Barlow-Regular/Medium/Bold.ttf` | body and UI |
| `BarlowSemiCondensed-SemiBold.ttf` | eyebrow labels, uppercase, tracked .04–.06em |

Both families are licensed under the SIL Open Font License 1.1 by their
respective authors; `OFL-Anton.txt` and `OFL-Barlow.txt` travel with the files
and govern their use. They are *not* covered by this repository's CC BY grant.
