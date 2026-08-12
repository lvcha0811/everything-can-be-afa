# 素材包维护规范

The pack contains seven user-authorized public identity masters. Keep originals unchanged and use `assets/manifest.json` as the source of truth.

## Rules

- Add only real, user-approved Afa photos or transparent cutouts as identity assets.
- Use ASCII lowercase filenames under `assets/references/` for GitHub portability.
- Record role, harness color, visibility, and minimum long edge in the manifest.
- Separate identity authority from pose/equipment authority in `reference-assets.md`.
- Keep one dominant role per image and avoid near-duplicate burst shots.
- Never replace the masters with generated images.
- Run `python3 scripts/validate_assets.py assets/manifest.json` after every asset change.

## Harness taxonomy

- `mint`: pale aqua/green body with turquoise straps.
- `neon-yellow`: fluorescent yellow/lime high-visibility vest, sometimes with pink straps.
- `light-blue`: powder-blue mesh harness.
- `none-visible` or `partly-obscured`: not an equipment color authority.

Every generation must select exactly one visible harness family unless the harness is outside the crop.
