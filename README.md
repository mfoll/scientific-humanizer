# Scientific Writing Humanizer

This fork adapts `blader/humanizer` for scientific and academic writing.

The skill is not a generic "make this sound human" prompt. It is a scientific line-editing and AI-pattern audit skill for manuscripts, abstracts, grants, figure legends, reviewer responses, and related academic prose.

## What changed from upstream

- Removed the generic "add soul/personality" behavior.
- Replaced word bans with context-sensitive scientific watch signals.
- Preserves legitimate scientific uses of terms such as "robust", "comprehensive", "crucial", "significant", and "serves as".
- Prioritizes claim fidelity, numerical accuracy, terminology consistency, cautious hedging, and section-specific scientific register.
- Adds a mechanical artifact audit script for hidden Unicode, odd spacing, repeated phrases, and watchlist clustering.
- Treats detector-risk checks as quality control, not as a promise of detector evasion.

## Skill file

The runtime skill is:

```text
SKILL.md
```

Install or copy this folder into the relevant skills directory for the agent environment you use.

## Optional artifact audit

For text already saved to a file:

```bash
python scripts/audit_text_artifacts.py path/to/text.txt
```

Or pipe text through stdin:

```bash
pbpaste | python scripts/audit_text_artifacts.py
```

The script is not an AI detector and does not produce a score. It flags mechanical issues that are easy to miss during editing:

- hidden or unusual Unicode characters
- missing spaces after punctuation
- repeated phrases
- clusters of context-sensitive AI-associated watch terms

## Design principle

Scientific repetition, passive voice, formal wording, and cautious hedging are not automatically AI-like. They become a problem when they are generic, unsupported, inflated, over-repeated, or used instead of naming the actual method, result, limitation, or implication.

The skill therefore asks the editor to decide:

- Is the phrase scientifically precise?
- Is it conventional in this field or target journal?
- Is it supported by data or citation logic?
- Is it consistent with the author's terminology?
- Is it doing real work in the sentence?

Only then should the editor rewrite it.

## Sources synthesized

- `blader/humanizer`: generic AI-writing pattern list.
- `labarba/sciwrite`: scientific clarity, clutter extraction, active/passive judgment, terminology consistency.
- `Master-cai/Research-Paper-Writing-Skills`: paragraph flow, reverse outlining, claim-evidence alignment.
- `K-Dense-AI/claude-scientific-writer` and `OpenLAIR/dr-claw`: IMRAD, reporting guidelines, section-specific scientific writing.
- Nature Methods and Gopen/Swan-style scientific writing guidance: audience, message, old-to-new flow, and sentence stress.
- `hanlulong/econ-writing-skill`: reader-first writing and concrete claims over vague contribution language.
- Pangram humanizer evidence: hidden Unicode, spacing artifacts, tortured phrases, repetitive substitutions, and limits of detector-oriented humanizers.

## License

Upstream project: MIT. This fork keeps the same license file.
