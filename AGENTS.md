# Guide for AI assistants

This repository contains the finished animated pet **Thin-Muscle Sun / 薄肌孙哥**, plus its generated source artwork, prompts and previews. Read this guide when a user gives you the repository link.

## Read first

- `README.md` or `README.zh-CN.md`: character, user-facing prompts and previews.
- `manifest.json`: authoritative sprite path, SHA-256, dimensions, frame counts and direction mapping.
- `docs/validation.json`: recorded checks for the published PNG.

## Choose the path for this environment

This guide can be read by Codex, Claude Code, WorkBuddy and other file-capable AI agents. Follow the available tools, rather than assuming the same integrations in every application.

- With authenticated Pets tools: obtain and validate the existing PNG, then use the import/create/select workflow below.
- With file access but no Pets integration: still obtain the PNG and manifest, verify the digest, and prepare the supplied previews. The optional preview script can render local outputs when Python and its dependencies are available. Report the prepared files and the specific missing activation integration.
- For remixing: use the image-generation tools and skills actually available in this environment. Report any generation capability that must be connected before making a requested visual change.

## Use the existing pet

When the user asks to install, use or activate this character:

1. Obtain `manifest.json` and `assets/spritesheet.png` from this repository, by cloning it or downloading the raw files. Save the PNG as a local binary file. For a link-only session, raw files are available under `https://raw.githubusercontent.com/Yixiang-Li/thin-muscle-sun-pet/main/`.
2. Check the PNG against the manifest's SHA-256 and byte length. Use the existing artwork; do not regenerate it or treat the complete atlas as a single character reference.
3. Inspect the published contact sheet and motion previews, and follow the available Pets skill or import workflow for an existing complete sprite sheet. Use the manifest's v2 layout for validation.
4. Run the Pets sprite-sheet preflight on the local PNG. If it passes, prepare its upload and create the requested custom pet using the returned upload session. Transfer the same validated bytes.
5. Select the new pet when the user requested activation. Use the stable ID returned by creation, then verify the name and active ID through the pet listing.
6. Report the actual result. If this environment lacks file access, Pets tools or an authenticated account, identify the missing capability and provide the relevant asset link. Do not claim activation without a successful tool result.

These steps require an AI environment with file access and connected Pets tools. A chat assistant that only reads text cannot perform the account-side creation.

## Remix the character

When the user asks for a visual or motion change:

- Ground all changed artwork in `source/base.png`, the approved strips in `source/strips/`, and the existing previews. The character's face, physique, outfit and drawing style are the default identity.
- Read `prompts/` for the selected generation instructions. Follow the installed image-generation and Pets creation skills for generation, extraction, assembly, validation and previews.
- Preserve the complete v2 contract from `manifest.json`: nine animation states and sixteen clockwise look directions. The `running` state means active work; directional movement uses `running-right` and `running-left`.
- Generate changed state strips or coherent look rows, then assemble the atlas deterministically. Show the resulting motion before creating or activating a revised pet.
- Create a separate new pet unless the user explicitly requests replacing an existing custom pet. Keep the published artwork unchanged when merely importing it.

## Documentation changes

Keep English and Chinese instructions consistent. Lead with the link-and-prompt workflow, followed by optional manual downloads and developer tools. Describe required AI capabilities accurately.

## 说明

用户要使用现成宠物时，读取清单、获取并校验最终 PNG，再通过可用的 Pets 工具创建、选中并核验。用户要改造时，以主造型和现有动作条为参考，沿用对应技能，保持完整布局并先展示动画。中英文使用说明保持一致，优先提供“仓库链接＋提示词”的入口。

