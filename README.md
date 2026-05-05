# Scientific Writing Humanizer

A lightweight skill for removing obvious LLM-generated writing patterns from scientific and academic prose while preserving the scientific style already present.

This is not a general scientific rewriter. It is a narrow editing skill for text that is already intended to be scientific, academic, or manuscript-like.

## Purpose

The skill edits scientific prose to reduce generic LLM patterns such as inflated significance language, ceremonial framing, vague attribution, empty transitions, formulaic future-work language, chatbot residue, and unnecessary synonym cycling.

It is designed to avoid a common failure mode of generic "humanizers": removing or altering phrasing that is legitimate in scientific writing. Scientific repetition, cautious hedging, formal tone, passive voice in Methods, and terms such as "robust", "significant", "comprehensive", and "serves as" are not automatically LLM signatures.

## What this does

- Removes generic LLM-like phrasing when it is unsupported, inflated, repetitive, or formulaic.
- Preserves scientific meaning, numbers, citations, uncertainty, terminology, and claim strength.
- Preserves legitimate scientific conventions, including technical repetition and appropriate passive voice.
- Treats suspicious words as context-sensitive watch signals, not banned words.
- Uses minimal edits rather than broad rephrasing.

## What this does not do

- It does not transform casual prose into scientific prose.
- It does not write manuscripts, literature reviews, methods sections, or reporting-guideline-compliant papers.
- It does not add citations, mechanisms, results, limitations, or implications.
- It does not score text as AI-generated or human-generated.
- It does not promise AI-detector evasion.
- It does not include a detector, CLI audit tool, or mechanical artifact scanner.

Dedicated tools already exist for mechanical AI-pattern scanning and detector-style audits, such as `ai-text-audit`, `QRY91/slopsquid`, and `brandonwise/humanizer`. This repository deliberately stays focused on the prompt-level scientific editing skill.

## Runtime skill

The runtime skill is:

```text
SKILL.md
```

Install or copy this folder into the relevant skills directory for the agent environment you use.

## Design principle

The central rule is:

> Remove the LLM pattern, not the scientific writing.

A phrase should be changed only after checking whether it is scientifically precise, conventional in context, supported by the surrounding evidence, consistent with the author's terminology, and doing real work in the sentence.

Examples:

- Keep "statistically significant" when it reports a statistical result.
- Keep "robust standard errors" when it names a method.
- Keep "comprehensive genomic profiling" when it names an assay or standard practice.
- Keep "albumin serves as a carrier protein" when "serves as" expresses biological function.
- Edit "This pivotal finding underscores..." when it inflates the result without adding information.
- Edit "This result serves as evidence that..." when "supports" is clearer and no meaning is lost.

## Recommended use

Use this skill for:

- abstracts
- introductions
- methods paragraphs
- results paragraphs
- discussion paragraphs
- figure legends
- grants
- reviewer responses
- scientific summaries
- academic text that has become too LLM-like after drafting or polishing

The input should already contain the scientific content and intended register. The skill should not invent missing scientific detail.

## Responsible use

This skill is an editing aid. Authors remain responsible for the content, accuracy, originality, citations, and disclosure obligations of any manuscript or submission.

Check the target journal or publisher policy for AI-use disclosure requirements. For biomedical manuscripts, ICMJE recommends disclosure when AI-assisted technologies are used in submitted work, and states that AI tools should not be listed as authors. Elsevier similarly requires author oversight and disclosure for generative-AI use in manuscript preparation, while distinguishing this from basic grammar, spelling, and punctuation checks.

## Source lineage

This fork adapts the general AI-writing-pattern cleanup idea from `blader/humanizer` to scientific and academic prose.

Other scientific-writing prompts and guides informed the preservation rules, but this repository is not intended to be a full scientific rephraser or manuscript-writing system.

## License

MIT. The upstream project is MIT licensed.
