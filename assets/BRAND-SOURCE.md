# Brand asset provenance

All BitConcepts brand assets in this repo are consumed copies from the
single source of truth: **BitConcepts/brand-assets**, tag **v1.0.0**
(https://github.com/BitConcepts/brand-assets). Per that repo's
BRAND.md, assets are never forked or redrawn locally — a change is
made there and re-pulled here. Verify any copy against the sha256 in
that repo's `assets-manifest.json`.

| File here | Source in brand-assets v1.0.0 | sha256 (manifest) |
|---|---|---|
| assets/bitconcepts-logo-horizontal.svg | logo/bitconcepts-logo-horizontal.svg | bf32b3181b5c6dadcac9d81029d7efdde507838813f24f2b839123d639d3832b |
| assets/bitconcepts-mark-512.png | logo/png/bitconcepts-mark-512.png | ea83b28fee69eeac1dde7aeed125e737e8d1cae5e68ebf48ee3fd1ca0d3e857d |
| assets/og-card.png | social/og-card.png | fc95e30f0d297421767a1ca98ece8ce67d170825e341c7289f46b57d23a56e5e |
| assets/favicon.svg | favicon/favicon.svg | ee41dfdb1b9d8662c08d8b70f97d9690cde95fbf88a15a1170f0928276160515 |
| assets/favicon-32.png | favicon/favicon-32.png | 5e648c0d4189951b0ae0b4808f23127b4a8a010df7a72be6bf90e613b529a1da |
| assets/apple-touch-icon.png | favicon/apple-touch-icon.png | ad89aad26d53de7f0c8759caeebacd2c943f3229f687b26082c824258ca1c023 |
| favicon.ico | favicon/favicon.ico | 2c6f44491d6a89a1a32be3dbebb6d796c302bc7789a40fec1928ff8840abbd8a |

All copies were hash-verified against the manifest at consumption
time (2026-10-11). The site palette (styles) already matches the
canonical palette in brand-assets `color/palette.json`:
Charcoal Field #1A1D21, Charcoal Card #22262B, Circuit Blue #03A1D0,
Circuit Bright #38C2EC.

The research tracker at /research/ carries its own inline instance
of the mark from its judged build; that is a separate artifact and
is not governed by this file.
