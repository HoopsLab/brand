# PNG exports

Rendered from the SVGs in the parent directory — **do not edit these by
hand.** Change the SVG and re-export (see `../../tools/export-png.py`).

Every file is RGBA with a transparent background.

## Naming

```
<asset>-<width>[-on-dark].png
```

The SVGs draw in `currentColor`, which a PNG cannot carry, so each asset
is exported twice:

| Suffix | Ink colour | Use on |
|---|---|---|
| *(none)* | `#12141c` | light backgrounds |
| `-on-dark` | `#f4f5f9` | dark backgrounds |

`mark.svg` keeps its accent reading point (`#ff7a33`) in both variants;
`mark-mono` is single-colour throughout.

## Which file to use

| Need | File |
|---|---|
| Favicon | `mark-32.png`, `mark-16.png` |
| App icon / avatar | `mark-512.png` or `mark-1024.png` |
| Slide or doc header | `lockup-horizontal-1024.png` |
| Print / large format | `lockup-horizontal-2048.png` |
| Square-ish placement | `lockup-stacked-800.png` |
| Type only | `wordmark-800.png` |

**Prefer the SVG wherever it is supported.** It scales, it inherits
colour, and it is a fraction of the size. These exports exist for the
places that cannot take one: social avatars, some slide tools, print
workflows, and image-only embeds.

Minimum sizes from [`../../BRAND.md`](../../BRAND.md) still apply — below
16px the mark should not be rendered at all.
