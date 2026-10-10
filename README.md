# Thin-Muscle Sun · 薄肌孙哥

[English](README.md) · [简体中文](README.zh-CN.md) · [MIT license](LICENSE)

A Justin Sun cartoon gym companion, working very hard on very small biceps.

A 2D animated companion with bold black outlines and flat colors, in an American adult sitcom cartoon style. Part of the same cartoon universe as [Spectator Feng · 看戏峰哥](https://github.com/Yixiang-Li/spectator-feng-pet).

![All nine animations](previews/all-states.gif)

## Give the link to your AI

Use **Codex, Claude Code, WorkBuddy, or another AI assistant with file and tool access**. Give it the repository link and a task in plain language.

| Assistant | Where to start | Expected workflow |
| --- | --- | --- |
| Codex with Pets enabled | Paste the prompt in a Codex chat | Fetch, validate, create and select the pet through Pets |
| [Claude Code](https://code.claude.com/docs/en/mcp) | Paste the prompt in your project session and ask it to read `AGENTS.md` | Prepare the files and previews; activate through Pets if those tools are connected |
| [WorkBuddy](https://cloud.tencent.com/product/workbuddy) or a similar agent | Paste the prompt in a task with file access | Prepare the files and previews; activate through Pets if those tools are connected |

Copy this prompt:

```text
Read https://github.com/Yixiang-Li/thin-muscle-sun-pet and its AGENTS.md.
I want to use "Thin-Muscle Sun" as my animated pet. Fetch and validate the ready-made artwork for me.
If you have Pets creation and selection tools, create and activate it, then verify the result.
Otherwise, prepare the files and animation previews first, then tell me which integration is needed for activation.
Execute the steps you can perform in this environment.
```

You give the link and the request; the AI does the file work. Account-side activation uses connected Pets tools.

### Remix with AI

```text
Read https://github.com/Yixiang-Li/thin-muscle-sun-pet and its AGENTS.md.
Use this character as the reference. Change its active-work animation to [describe the action you want].
Preserve the face, physique, outfit and cartoon style. Keep the complete Pets animation layout.
Show me the resulting animation, then create and select it as a new pet.
```

[AGENTS.md](AGENTS.md) gives the AI the asset locations and the import, verification and remix workflow.

## Manual download (optional)

- [Download the transparent sprite sheet](https://github.com/Yixiang-Li/thin-muscle-sun-pet/raw/refs/heads/main/assets/spritesheet.png)
- [Complete animation video](previews/all-states.mp4)
- [Look-direction loop](previews/look-loop.gif)
- [All poses](docs/contact-sheet.png) · [Direction sheet](docs/directions.png)

You can also attach the downloaded PNG in a chat with Pets enabled and ask the AI to create and select "Thin-Muscle Sun".

## Dumbbell curls

![Featured action](previews/states/running.gif)

![Four action frames](previews/motion-stills.png)

## Animation layout

The transparent PNG is **1536 × 2288** pixels: 8 columns × 11 rows, with **192 × 208** cells. It contains 73 populated cells and 15 empty transparent cells. Frame indexes start at zero. Metadata is in [manifest.json](manifest.json).

| Row | State | Frames | Action |
| --- | --- | ---: | --- |
| 0 | `idle` | 6 | Breathing and blinking |
| 1 | `running-right` | 8 | Run right |
| 2 | `running-left` | 8 | Run left |
| 3 | `waving` | 4 | Wave while holding weights |
| 4 | `jumping` | 5 | Jump and land |
| 5 | `failed` | 8 | Droop after a failed effort |
| 6 | `waiting` | 6 | Expectant asking shrug |
| 7 | `running` | 6 | Dumbbell curls with comic effort |
| 8 | `review` | 6 | Inspect his tiny biceps |
| 9 | Look directions | 8 | 000°–157.5°, clockwise |
| 10 | Look directions | 8 | 180°–337.5°, clockwise |

`000` means up, `090` screen-right, `180` down and `270` screen-left. The `running` state is the active-work animation, separate from directional movement. Individual GIFs are in [previews/states](previews/states).

## Source and remixing

- [source/base.png](source/base.png): canonical character design.
- [source/strips](source/strips): selected generated animation and gaze strips.
- [prompts](prompts): the selected generation prompts, plus derivation notes where applicable.
- [scripts/render_previews.py](scripts/render_previews.py): portable preview rendering from the final PNG.

Artwork was generated with OpenAI image generation, then extracted, registered, assembled and checked using the Pets creation workflow. The preview script is included; the hosted Pets service and plugin internals are separate dependencies. AI generation is not guaranteed to reproduce the same artwork from a prompt alone. Reference photographs are not redistributed.

To render previews and extract the 57 standard-state frames locally, use Python 3.10 or newer:

```bash
python -m pip install -r requirements.txt
python scripts/render_previews.py assets/spritesheet.png --output-dir generated-previews
```

## Validation

The published PNG is byte-identical to the validated pet artwork. Structural checks, quality checks and Pets preflight passed. Jump lift is **29 px**, with **0 px** landing-baseline difference. See [docs/validation.json](docs/validation.json) for the digest and original validation results.

The 67.5° and 247.5° intermediate gazes have subtle pitch; they were accepted after reviewing the full loop. All four cardinal directions passed independent blind review.

## License and credits

The original generated artwork, prompts, documentation and preview script are released under the [MIT license](LICENSE). These are unofficial humorous caricatures. [Credits and references](docs/CREDITS.md).
