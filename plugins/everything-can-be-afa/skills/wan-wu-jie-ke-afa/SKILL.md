---
name: wan-wu-jie-ke-afa
description: Replace a person, animal, mascot, object, or main subject in a raster image with the fixed Shiba Inu character 阿发 (Afa), or create a new Afa image from bundled identity references. Use for “万物皆可阿发”, “把主角换成阿发”, “换成我这只柴犬”, “按原姿势画阿发”, posters, comics, memes, photos, pixel art, and requests that specify mint/green, fluorescent-yellow, or light-blue harness colors, the yellow 阿发 name tag, pose transfer, dog anatomy, grounding, lighting, or minimal-change edits.
---

# 万物皆可阿发

Use the built-in image generation/editing tool. Treat replacements as identity-preserving edits, not scene redesigns. The bundled photos are authorized public reference assets and are the default identity source.

## Load resources

- Read [references/character-bible.md](references/character-bible.md) before every Afa generation or edit.
- Read [references/reference-assets.md](references/reference-assets.md) and select the smallest useful asset set before calling the image tool.
- Read [references/prompt-patterns.md](references/prompt-patterns.md) when composing or revising the prompt.
- Read [references/asset-pack.md](references/asset-pack.md) only when auditing or updating the pack.
- Run `python3 scripts/validate_assets.py assets/manifest.json` before relying on bundled assets.

## Choose harness color

1. Obey an explicit user color. Map “绿色/绿胸背/薄荷绿/蓝绿色” to `mint`; “黄色/荧光黄/黄绿色” to `neon-yellow`; “浅蓝/蓝色胸背” to `light-blue`.
2. If the edit target already depicts Afa and the user says “其他不变”, preserve its current harness color.
3. If color is unspecified, use `mint` as the general default. Use `neon-yellow` only when the user asks for the classic fluorescent look or the selected pose reference shows it. Use `light-blue` only when explicitly requested or when reproducing the bundled sleeping reference.
4. Never blend multiple harness palettes. The yellow name tag reading `阿发` is independent of harness color and remains the signature label whenever visible.

## Execute

1. Inspect every supplied image. Label exactly one direct edit target; label other images as identity, harness/tag, body/proportion, pose, or style references.
2. Resolve the subject to replace. Ask one focused question only when multiple subjects are equally plausible.
3. Extract invariants: aspect ratio, crop, camera, subject position, pose, props, background, text, lighting, palette, and medium.
4. Select bundled assets by role and requested harness color. Always include a face anchor; add at most one equipment anchor and one pose/body anchor unless more are genuinely necessary.
5. Apply the identity hierarchy from the character bible. Preserve Afa's face first, then the exact `阿发` tag, selected single-color harness, natural Shiba body/paws, and curled tail.
6. Transfer the original pose as far as canine anatomy allows. Use light anthropomorphism only when the scene requires it; do not default to a human body with a dog head.
7. Build the prompt from the pattern reference. State the single requested change first, then repeat invariants and avoid items. Quote required text verbatim.
8. Generate or edit without reconfirming when target, subject, and references are clear.
9. Inspect the result. If one correctable defect dominates, make one targeted revision while repeating all invariants.

## Quality gate

- Identity: recognizable as the same young red Shiba Inu, not a generic Shiba.
- Face: ears, eyes, cream eyebrow transition, muzzle, face width, and expression match the identity references.
- Harness: exactly one requested color family; no unintended palette mixing.
- Name tag: yellow tag visible when composition allows, with legible black `阿发`; never claim exact text when visibly wrong.
- Anatomy: paws remain paws; limbs, joints, body length, and curled tail are coherent.
- Pose: action, orientation, gaze, and placement follow the replaced subject unless canine anatomy requires a minimal adjustment.
- Preservation: background, other characters, props, text, layout, crop, aspect ratio, and style stay unchanged unless requested.
- Composite: contact, perspective, scale, shadows, color temperature, and light direction fit the scene.
- Text: all user-specified Chinese copy is correct and appropriately positioned.

If exact Chinese text remains unreliable after one targeted revision, explain the limitation and offer deterministic typography/compositing rather than declaring success.

## Interpret common requests

- “万物皆可阿发”: replace the named or obvious focal subject with Afa while preserving the source visual logic.
- “其他不变”: change only the named subject or detail; repeat the preservation list in every prompt.
- “动作不变”: copy pose, orientation, camera angle, and placement; adjust only anatomically impossible details.
- “长相 100% 还原”: maximize identity fidelity without promising mathematical exactness.
- “看清楚名牌”: improve tag visibility and local clarity without changing the whole crop.
- “拟人化”: anthropomorphize action and staging, not automatically hands, feet, or body proportions.
- “参考图 1/2/3”: preserve the user's numbering exactly; never silently reorder.

Save outputs non-destructively. Do not overwrite the edit target unless explicitly requested.
