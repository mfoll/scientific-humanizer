---
name: scientific-writing-humanizer
description: Remove obvious LLM-generated writing patterns from scientific and academic prose while preserving existing scientific style, meaning, numbers, citations, terminology, hedging, and section-specific conventions. Use when asked to humanize, de-AI, de-slop, polish, or audit scientific text that is already meant to read as scientific writing.
---

# Scientific Writing Humanizer

## Purpose

Use this skill to remove obvious LLM-generated writing patterns from scientific or academic prose that is already meant to read as scientific writing.

The goal is not to transform text into a scientific style. The goal is to preserve the existing scientific style while removing generic, inflated, formulaic, or chatbot-like phrasing that makes the text sound machine-generated.

Make the smallest edit that solves the problem.

## Core priorities

Apply these priorities in order:

1. Preserve scientific meaning, numerical values, statistical direction, uncertainty, citations, terminology, nomenclature, figure/table references, and claim strength.
2. Preserve the existing scientific register, section type, and author voice.
3. Preserve legitimate scientific conventions, including technical repetition, cautious hedging, formal tone, passive voice where appropriate, and standard field phrases.
4. Remove or reduce LLM-like patterns only when they are generic, inflated, unsupported, repetitive, or structurally formulaic.
5. Improve clarity and concision only where it supports the edit. Do not perform a broad scientific rewrite unless explicitly asked.

Never insert hidden Unicode, deliberate mistakes, awkward synonym substitutions, fake citations, fake specificity, or detector-evasion artifacts.

## Scope

Use this skill for:

- abstracts
- introductions
- methods text
- results text
- discussion text
- figure legends
- grant text
- cover letters
- reviewer responses
- academic bios or summaries
- scientific paragraphs produced or over-polished by an LLM

Do not use this skill as a full manuscript writer, literature-review writer, citation generator, reporting-guideline checker, statistical reviewer, or scientific-style transformer.

If the user provides non-scientific text and asks for scientific writing, do not silently convert it into a manuscript-like style. Say that the request is outside this skill's narrow purpose, then perform only a light cleanup if useful.

## Starting procedure

Before editing, infer the likely section type only enough to avoid damaging conventions:

- Methods can tolerate more passive voice and procedural repetition.
- Results should preserve numbers, comparisons, p-values, confidence intervals, effect sizes, and directionality.
- Discussion can contain interpretation, but the rewrite must not add new mechanisms or implications.
- Reviewer responses should stay direct, respectful, and evidence-bound.
- Figure legends should preserve panel labels, sample sizes, abbreviations, and statistical notation.

Do not build a full section outline unless the user explicitly asks for structural rewriting.

If the user provides a writing sample, use it only as a soft calibration for formality, sentence rhythm, use of "we", and terminology. Do not imitate errors or idiosyncrasies that reduce clarity.

## Editing workflow

### 1. Preservation pass

Identify content that must not change:

- numerical values and units
- sample sizes
- p-values, q-values, FDR values, confidence intervals, standard errors, odds ratios, hazard ratios, fold changes, and effect sizes
- comparison direction and comparator groups
- citations and citation order
- figure, table, and supplementary references
- gene, protein, variant, species, drug, disease, assay, method, cohort, endpoint, and model names
- abbreviations and defined terms
- hedging and uncertainty markers that reflect the evidence

If a sentence contains protected content, edit around it rather than rewriting it freely.

### 2. LLM-pattern pass

Look for these patterns. Edit them only when they make the prose generic, inflated, or formulaic.

#### Chatbot residue

Remove assistant-facing residue:

- "Of course"
- "Here is"
- "I hope this helps"
- "Let me know"
- "as an AI"
- "based on available information"

#### Significance inflation

Watch for unsupported or ceremonial emphasis:

- "crucial"
- "pivotal"
- "key"
- "vital"
- "transformative"
- "groundbreaking"
- "important implications"
- "highlights the importance of"
- "underscores"

Keep the term when it is precise or conventional: "a crucial cysteine residue", "robust standard errors", "comprehensive genomic profiling", "statistically significant".

Edit when it inflates a claim without adding information.

Example:

```text
This pivotal finding underscores the importance of immune contexture in cancer.
```

Prefer:

```text
This finding links immune contexture to the measured cancer outcome.
```

Only use the specific outcome if it is already present in the user's text.

#### Ceremonial framing and copula avoidance

Watch for inflated substitutes for simpler verbs:

- "serves as"
- "stands as"
- "represents"
- "marks"
- "acts as a testament to"

Keep them when they describe a real function: "albumin serves as a carrier protein".

Edit them when they avoid a simpler scientific verb.

Example:

```text
This result serves as evidence that the pathway is activated.
```

Prefer:

```text
This result supports pathway activation.
```

#### Present-participle tails

Watch sentence endings with:

- "highlighting"
- "underscoring"
- "reflecting"
- "showcasing"
- "emphasizing"
- "contributing to"
- "ensuring"

Edit when the tail adds generic depth without evidence.

Do not remove the construction if it expresses a real relationship more cleanly than a separate sentence.

#### Generic transitions and throat-clearing

Remove or reduce empty signposting:

- "It is worth noting that"
- "It is important to note that"
- "Interestingly"
- "Notably"
- "In this context"
- "Furthermore"
- "Moreover"
- "Additionally"

Keep a transition if it marks a real contrast, sequence, or exception.

#### Vague attribution

Watch vague source language:

- "studies show"
- "experts argue"
- "the literature suggests"
- "emerging evidence indicates"
- "previous research has demonstrated"

If the user supplied citations, preserve them and make the attribution specific enough for the sentence. If no citation is available, do not invent one. Either weaken the claim or flag it for author verification.

#### Rule-of-three and over-balanced structure

LLM prose often forces claims into tidy triplets or repeated parallel clauses. Use only the number of items the science requires. Preserve parallel structure when it improves readability or reflects a real experimental design.

#### Elegant variation and synonym cycling

Do not vary technical terms just to avoid repetition. Scientific repetition is often correct.

Keep the defined term for methods, groups, endpoints, cohorts, variants, assays, models, diseases, and variables.

Flag or fix term drift only when the text appears to use different words for the same defined object.

#### Over-hedging and under-hedging

Remove stacked hedges:

```text
may potentially suggest
```

Prefer:

```text
may suggest
```

Add hedging only when a causal, mechanistic, clinical, or translational claim outruns the evidence already stated in the text. Do not make confident claims more cautious by default.

#### Generic conclusions and future-work filler

Watch for vague endings:

- "paves the way"
- "opens new avenues"
- "future studies are warranted"
- "holds promise"
- "important implications"

Replace them with concrete next steps or limitations only if those are already present in the text. Otherwise, make the conclusion modest rather than inventing specificity.

### 3. Minimal rewrite pass

Rewrite only the affected sentences or clauses unless a larger paragraph-level edit is necessary for coherence.

Preserve:

- paragraph order
- section structure
- citation style
- tense pattern unless clearly wrong
- technical terms
- authorial stance
- formal scientific tone

Avoid making the prose casual, chatty, humorous, overly personal, or rhetorically dramatic.

### 4. Final check

Before returning the answer, check that the revision did not:

- change a number, unit, statistic, citation, comparator, or direction of effect
- replace a defined term with a synonym
- remove necessary hedging
- remove legitimate passive voice from Methods
- add a new claim, mechanism, limitation, citation, or implication
- make the text sound like generic scientific boilerplate
- claim that the result will pass AI detectors

## Output formats

### Rewrite mode

Use when the user asks to humanize, de-AI, de-slop, polish, or rewrite text.

Return:

1. Revised text
2. Brief notes on the main LLM-pattern edits made
3. Author-verification notes only if needed

Keep the notes short. Do not produce a long scientific-writing review unless asked.

### Audit mode

Use when the user asks to diagnose or review text without rewriting it.

Use this compact format:

```text
Finding: [short label]
Severity: major | minor
Original: [short excerpt]
Why it reads as LLM-like: [specific reason]
Suggested action: [replacement or delete/keep]
```

Do not score the text as AI-generated or human-generated.

### Interactive mode

Use only when the user asks to work paragraph by paragraph.

For each paragraph, provide:

1. Revised paragraph
2. Short explanation of what changed
3. Any author-verification issue

Then stop for the user's decision before continuing.

## Context-sensitive watchlist

These are not banned words. Treat them as signals that require context:

- crucial
- comprehensive
- robust
- significant
- important
- key
- pivotal
- novel
- highlight
- underscore
- landscape
- framework
- leverage
- enhance
- facilitate
- shed light on
- delve into
- it is worth noting
- it is important to note
- serves as
- plays a role
- paves the way
- holds promise

Keep a watchlisted expression when it is:

- part of standard scientific usage
- attached to a specific object, method, result, or statistical concept
- necessary for the target field or journal
- already part of the author's consistent terminology
- clearer than the alternative

Edit it when it is:

- unsupported by evidence
- repeated nearby
- used to inflate significance
- a substitute for the actual result
- part of generic LLM scaffolding

## What not to do

- Do not transform the text into a different scientific style.
- Do not make the prose casual or add "personality".
- Do not globally ban words.
- Do not synonym-spin technical vocabulary.
- Do not remove necessary hedging.
- Do not remove legitimate passive voice from Methods.
- Do not add citations, findings, mechanisms, limitations, or implications.
- Do not add hidden Unicode, odd spacing, deliberate typos, or detector-evasion artifacts.
- Do not claim that the text will bypass AI detectors.
- Do not perform a full manuscript review unless the user asks for one.
