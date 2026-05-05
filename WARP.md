# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## What this repo is
This repository is a **scientific writing skill** implemented mostly as Markdown,
with one optional Python audit script.

The runtime artifact is `SKILL.md`: skill-aware agents read the YAML
frontmatter and the prompt/instructions that follow.

`README.md` is for humans: usage, scope, and a compact overview of the design.

## Key files (and how they relate)
- `SKILL.md`
  - The actual skill definition.
  - Starts with YAML frontmatter containing only `name` and `description`.
  - After the frontmatter is the editor prompt: the canonical scientific
    anti-LLM writing workflow.
- `README.md`
  - Human-facing summary of the fork and design principle.
- `scripts/audit_text_artifacts.py`
  - Optional deterministic artifact audit for hidden Unicode, spacing,
    repeated phrases, and watchlist clustering.

When changing behavior/content, treat `SKILL.md` as the source of truth, and update `README.md` to stay consistent.

## Common commands

### Run the optional text artifact audit

```bash
python scripts/audit_text_artifacts.py path/to/text.txt
```

or:

```bash
pbpaste | python scripts/audit_text_artifacts.py
```

## Making changes safely

- Preserve valid YAML frontmatter formatting.
- Keep `SKILL.md` concise enough to load as a skill.
- Keep word lists context-sensitive; do not turn them into global bans.
- Preserve the distinction between scientific editing and detector evasion.
- If you change behavior, update `README.md` to stay consistent.

### Documenting non-obvious fixes
If you change the prompt to handle a tricky failure mode, document the behavioral
change briefly in `README.md`.
