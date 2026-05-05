# WARP.md

This file provides guidance to WARP (warp.dev) when working with this repository.

## What this repo is

This repository is a narrow prompt-level skill for lightly editing scientific or academic prose that is already meant to read as scientific writing.

The runtime artifact is `SKILL.md`: skill-aware agents read the YAML frontmatter and the instructions that follow.

`README.md` is for humans: scope, usage, responsible-use framing, and source lineage.

## Key files

- `SKILL.md`
  - The actual skill definition.
  - Starts with minimal YAML frontmatter containing `name` and `description`.
  - Defines the canonical behavior: remove obvious LLM-generated writing patterns while preserving existing scientific style, meaning, numbers, citations, terminology, hedging, and section-specific conventions.
- `README.md`
  - Human-facing summary of the product scope and design principle.
- `LICENSE`
  - MIT license attribution for upstream and this adaptation.

There is intentionally no detector, score generator, CLI audit tool, mechanical scanner, benchmark suite, or bundled script in this repository. Dedicated external tools already exist for that layer.

## Making changes safely

- Keep this repository focused on prompt-level scientific LLM-pattern cleanup.
- Preserve valid YAML frontmatter formatting.
- Keep `SKILL.md` concise enough to load as a skill.
- Keep watchlists context-sensitive; do not turn them into global word bans.
- Preserve the distinction between removing LLM-like phrasing and optimizing for AI-detector evasion.
- Do not add scripts, tests, examples, benchmarks, workflow files, or source catalogs unless the product scope explicitly changes.
- If behavior changes, update `README.md` to stay consistent.
