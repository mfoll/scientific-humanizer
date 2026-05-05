# Scientific Writing Humanizer

A lightweight skill for removing obvious LLM-generated writing patterns from scientific and academic prose while preserving the scientific style required by the task.

The main use is rewriting existing scientific text. The skill can also act as a manual style guardrail when explicitly invoked during generation, for example: "write this paragraph using the scientific-writing-humanizer skill." It is not a general scientific rewriter or manuscript-writing system.

## Purpose

The skill edits scientific prose to reduce generic LLM patterns such as inflated significance language, ceremonial framing, vague attribution, empty transitions, formulaic future-work language, chatbot residue, and unnecessary synonym cycling.

It is designed to avoid a common failure mode of generic "humanizers": removing or altering phrasing that is legitimate in scientific writing. Scientific repetition, cautious hedging, formal tone, passive voice in Methods, and terms such as "robust", "significant", "comprehensive", and "serves as" are not automatically LLM signatures.

## What this does

- Removes generic LLM-like phrasing when it is unsupported, inflated, repetitive, or formulaic.
- Preserves scientific meaning, numbers, citations, uncertainty, terminology, and claim strength.
- Preserves legitimate scientific conventions, including technical repetition and appropriate passive voice.
- Treats suspicious words as context-sensitive watch signals, not banned words.
- Uses minimal edits rather than broad rephrasing.
- Can act as a style guardrail during generation when explicitly invoked, so the agent writes under the anti-LLM-pattern constraints from the start.

## What this does not do

- It does not transform casual prose into scientific prose.
- It does not act as a full manuscript writer, literature-review writer, reporting-guideline checker, or scientific-content generator.
- It does not add citations, mechanisms, results, limitations, or implications.
- It does not invent citations, methods, numerical results, mechanisms, datasets, limitations, or implications when used for generation.
- It does not score text as AI-generated or human-generated.
- It does not promise AI-detector evasion.
- It does not include a detector, CLI audit tool, or mechanical artifact scanner.

Dedicated tools already exist for mechanical AI-pattern scanning and detector-style audits, such as `ai-text-audit`, `QRY91/slopsquid`, and `brandonwise/humanizer`. This repository deliberately stays focused on the prompt-level scientific editing skill.

## Usage modes

This skill supports two uses.

### 1. Rewrite existing scientific text

Use this when you provide a paragraph, abstract, figure legend, response to reviewers, or other scientific prose and ask the agent to humanize, de-AI, de-slop, polish, proofread, or lightly line-edit it.

The skill should make minimal edits that remove LLM-like patterns while preserving scientific meaning, numbers, citations, terminology, hedging, and section conventions.

### 2. Explicit generation guardrail

Use this when you explicitly ask the agent to write new scientific or academic text using the `scientific-writing-humanizer` skill.

```text
Write a short paragraph about this project using the scientific-writing-humanizer skill.
```

In this mode, the skill acts as a style guardrail during drafting. The agent should write under the skill's constraints from the start and perform an internal final pass before returning the text. It should use only information you supplied or information already present in the current context.

This mode is not intended as an automatic default for every scientific-writing task. It is also not a full manuscript-writing, citation-generation, literature-review, or reporting-guideline tool.

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

For rewrite mode, the input should already contain the scientific content and intended register. For explicit generation guardrail mode, the prompt should provide enough scientific substance to draft from without inventing details.

## Responsible use

This skill is an editing aid. Authors remain responsible for the content, accuracy, originality, citations, and disclosure obligations of any manuscript or submission.

Check the target journal or publisher policy for AI-use disclosure requirements. For biomedical manuscripts, ICMJE recommends disclosure when AI-assisted technologies are used in submitted work, and states that AI tools should not be listed as authors. Elsevier similarly requires author oversight and disclosure for generative-AI use in manuscript preparation, while distinguishing this from basic grammar, spelling, and punctuation checks.

## Source lineage

This fork adapts the general AI-writing-pattern cleanup idea from `blader/humanizer` to scientific and academic prose.

Other scientific-writing prompts and guides informed the preservation rules, but this repository is not intended to be a full scientific rephraser or manuscript-writing system.

## License

MIT. The upstream project is MIT licensed.
