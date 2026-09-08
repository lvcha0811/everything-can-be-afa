# Prompt patterns

## Direct edit

```text
Use case: identity-preserve
Asset type: <poster/comic/meme/photo/etc.>
Primary request: In Image A, replace only <target subject> with the Shiba Inu Afa from Image B.
Input images: Image A = direct edit target; Image B = Afa identity; Image C = harness/tag detail; Image D = body/proportion reference.
Subject: Preserve Afa's face and red-Shiba markings, the single selected <mint/neon-yellow/light-blue> harness variant, natural paws and body, curled tail when visible, and yellow name tag reading "阿发" verbatim.
Composition/framing: Match Image A's subject position, pose, orientation, camera angle, crop, and aspect ratio.
Style/medium: Match Image A.
Lighting/mood: Match Image A's light direction, shadow softness, color temperature, and atmosphere.
Text (verbatim): "阿发"; <other exact copy>
Constraints: Change only the named subject. Preserve all other characters, background, props, layout, text, palette, and unrelated details.
Avoid: generic Shiba face, mixed harness colors, human hands or feet, floating body, wrong scale, changed background, extra text, watermark, misspelled name tag.
```

## Fresh composition using references

```text
Use case: <ads-marketing/illustration-story/stylized-concept>
Asset type: <intended output>
Primary request: Create a new original image using Image A for composition logic and Image B for Afa's identity.
Input images: Image A = composition/style reference only; Image B = Afa identity; Image C = harness/tag detail.
Subject: <requested action>, while preserving the fixed Afa identity anchors.
Scene/backdrop: <requested environment>
Style/medium: <requested style>
Composition/framing: <layout and aspect ratio>
Text (verbatim): "阿发"; <other exact copy>
Constraints: Do not copy Image A exactly. Keep Afa recognizable and anatomically coherent.
Avoid: reference watermarks/logos, extra copy, generic dog design, human hands or feet.
```

## Targeted revision

```text
Edit the current result. Correct only <one defect>. Preserve the exact composition, pose, expression, background, other characters, props, crop, aspect ratio, lighting, palette, style, and all already-correct details. Keep Afa's identity reference active. The yellow name tag must read "阿发" verbatim. Do not redesign or regenerate unrelated areas.
```

## Prompt discipline

- Name the direct edit target first.
- Label every reference image by role and harness color; never say only “参考这些图”.
- State one harness color explicitly and forbid mixing palettes.
- Put the requested change before descriptive detail.
- Repeat invariants after the change request and again in targeted revisions.
- Ask the image model for exact text, but validate visually rather than trusting the prompt.
- Prefer one correction per iteration to reduce collateral drift.
