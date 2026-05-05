---
name: scientific-writing-humanizer
description: >-
  Remove obvious LLM-generated writing patterns from scientific and academic prose while preserving existing scientific style, meaning, numbers, citations, terminology, hedging, and section-specific conventions. Use when asked to humanize, de-AI, de-slop, polish, proofread, lightly line-edit, or audit scientific text that is already meant to read as scientific writing. Also use only when explicitly invoked as a style guardrail for drafting short scientific or academic text from user-provided or current-context content.
---

# Scientific Writing Humanizer

## Purpose

Use this skill to remove obvious LLM-generated writing patterns from scientific or academic prose while preserving the scientific register, meaning, and conventions already required by the task.

The main use is rewriting existing scientific text. A secondary use is allowed only when the user explicitly asks to write new scientific text using this skill. In that case, treat the skill as a style guardrail during generation: write the requested text from the information supplied by the user or already available in the current context, then apply the same LLM-pattern cleanup before returning it.

The goal is not to transform casual content into a full scientific manuscript style. The goal is to avoid generic, inflated, formulaic, or chatbot-like phrasing while preserving scientific precision.

Make the smallest edit or drafting choice that solves the problem.

Preserve technical density, but reduce rhetorical density.

Technical density includes field terms, gene and protein names, variant notation, disease entities, assay names, method names, statistical notation, citation labels, cohort names, endpoint names, and figure/table references. These are often necessary in scientific writing and should not be simplified merely because they look dense.

Rhetorical density includes avoidable stacking of claims, recommendations, transitions, caveats, implications, and long comma-separated lists in one sentence. Split or simplify these when doing so preserves the science and improves readability.

## Supported modes

### Mode 1: rewrite existing text

Use when the user provides scientific or academic prose and asks to humanize, de-AI, de-slop, polish, proofread, lightly line-edit, or audit it.

In this mode, perform minimal LLM-pattern cleanup. Preserve the scientific content and change only the words, clauses, or sentences needed to remove generic, inflated, formulaic, or chatbot-like phrasing.

### Mode 2: explicit generation guardrail

Use only when the user explicitly asks to write new scientific or academic text using this skill.

Do not refuse solely because no draft text was provided. Instead, treat the skill as a style constraint on generated scientific prose: draft the requested text while applying this skill's constraints from the start, then perform an internal final pass for LLM-pattern cleanup before returning the answer.

Use only information supplied by the user or already available in the current context. Do not invent citations, methods, numerical results, statistical claims, mechanisms, limitations, implications, datasets, cohorts, disease entities, field-specific details, or author positions.

If required scientific content is missing, ask for it or write a bounded placeholder rather than inventing details.

Do not expose a two-step workflow unless the user asks for one. The user should receive the final text, not a generic draft followed by a visible cleanup pass.

Operating rule: for existing text, perform minimal LLM-pattern cleanup. For new text, only when explicitly invoked, draft under the same constraints from the start and run an internal final pass before returning. Use only user-supplied or current-context content. If the required scientific content is missing, ask for it or write a bounded placeholder rather than inventing details.

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

Do not use this skill as a full manuscript writer, literature-review writer, citation generator, reporting-guideline checker, statistical reviewer, peer reviewer, or scientific-style transformer. Short drafting from user-provided or current-context scientific content is allowed only in Mode 2, when the user explicitly invokes this skill as a style guardrail.

If the user provides non-scientific content and asks for a full scientific rewrite, do not silently convert it into manuscript-like prose. This skill may lightly clean the wording or, if explicitly invoked for generation, draft a bounded scientific-style passage only from supplied content.

For rewrite mode, the input should already contain the scientific content and intended register. For explicit generation guardrail mode, the user must provide enough scientific substance or current-context material for a bounded draft.

## Starting procedure

Before editing, infer the likely section type only enough to avoid damaging conventions:

- Methods can tolerate more passive voice and procedural repetition.
- Results should preserve numbers, comparisons, p-values, confidence intervals, effect sizes, and directionality.
- Discussion can contain interpretation, but the rewrite must not add new mechanisms or implications.
- Reviewer responses should stay direct, respectful, and evidence-bound.
- Figure legends should preserve panel labels, sample sizes, abbreviations, and statistical notation.

Do not build a full section outline unless the user explicitly asks for structural rewriting.

When explicitly invoked for new writing, do not draft generic text first and then present a cleanup step to the user. Draft under these constraints from the beginning, then do an internal final check against the watchlist and preservation rules before returning the final text.

If the user provides a writing sample, use it only as a soft calibration for formality, sentence rhythm, use of "we", and terminology. Do not imitate errors or idiosyncrasies that reduce clarity.

## Reviewer-report phrasing

In review reports, manuscript critiques, and reviewer-style recommendations, direct recommendation language is acceptable. Do not treat repeated phrases such as "the authors should" as automatically LLM-like.

When many recommendations appear in sequence, reduce monotony only where doing so clarifies the reason for the recommendation. Do not vary phrasing merely for elegance.

Acceptable alternatives include:

- "To establish malignant identity, ..."
- "This claim needs ..."
- "A stronger analysis would ..."
- "The manuscript should ..."
- "At minimum, ..."

Use variation to clarify the scientific function of the sentence: diagnosis, requirement, rationale, minimum standard, or suggested analysis.

For long lists of required analyses or revisions, bullets are acceptable when the user asked for a review, report, critique, or response-style output. Preserve formal, direct, evidence-bound reviewer language.

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

### 3. Density and rhythm pass

After removing LLM-like phrasing, check whether the revision has become too compressed.

Do not optimize for AI-detector metrics such as average sentence length, function-word ratio, mean word length, or proper-noun density. In scientific writing, long technical terms, proper nouns, gene symbols, method names, citations, and low function-word ratios can be legitimate.

However, revise sentences when scientific content has been packed into a single overly dense construction. Prefer one scientific move per sentence when possible.

Look especially for:

- sentences longer than about 35-40 words that contain multiple recommendations, several citations, or several methods
- long comma-separated lists embedded inside an already complex sentence
- repeated sentence openings across nearby sentences, especially in reviewer-style text
- stacked noun phrases where a short orienting phrase would improve readability
- sentences that combine summary, interpretation, and recommendation in one move

Fix these only when the edit preserves meaning and improves readability. Do not split technical names, gene symbols, variant notation, statistical expressions, assay names, or standard method names.

When a long list contains several independent requested actions, analyses, or critiques, bullets are acceptable if the user asked for a review, report, critique, or response-style document. Do not convert ordinary manuscript prose into bullets unless the user requested that format.

### 4. Minimal rewrite pass

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

### 5. Final integrity check

#### Rewrite mode: internal before/after check

Before returning the answer in rewrite mode, compare the revised text against the original text. Confirm that the edit removed or reduced LLM-like phrasing without changing the science.

Check that the revision did not:

- change the scientific meaning
- change numerical values, units, sample sizes, percentages, p-values, q-values, FDR values, confidence intervals, standard errors, odds ratios, hazard ratios, fold changes, effect sizes, or statistical direction
- change the direction, magnitude, comparator, population, model, endpoint, or scope of a result
- strengthen or weaken a claim without justification from the original text
- remove necessary hedging or add unsupported certainty
- add new citations, methods, mechanisms, limitations, implications, disease entities, cohorts, datasets, endpoints, interpretations, or author positions
- replace defined technical terms with synonyms
- alter gene, protein, variant, species, drug, disease, assay, method, model, cohort, endpoint, figure, table, or supplementary references
- remove legitimate scientific repetition or appropriate passive voice

If the check finds an unintended change, revise again before answering.

If a possible issue cannot be resolved without author input, preserve the original wording and flag the issue briefly under author-verification notes.

Do not show this before/after check to the user unless the user asks for audit details or a residual verification issue remains.

#### Generation guardrail mode: internal prompt/output check

Before returning the answer in generation guardrail mode, compare the draft against the user's request and current context.

Check that the output:

- uses only user-supplied or current-context information
- does not invent citations, methods, numerical results, statistical claims, mechanisms, limitations, implications, datasets, cohorts, disease entities, or field-specific details
- avoids generic LLM phrasing, inflated significance language, ceremonial framing, vague future-work language, empty transitions, unnecessary synonym cycling, and chatbot residue
- remains concise, scientific, and bounded to the requested task

If required content is missing, ask for it or use a clearly bounded placeholder rather than inventing details.

## Output formats

### Rewrite mode

Use when the user asks to humanize, de-AI, de-slop, polish, or rewrite text.

Return:

1. Revised text
2. Brief notes on the main LLM-pattern edits made
3. Author-verification notes only if needed

Keep the notes short. Do not produce a long scientific-writing review unless asked.

### Generation guardrail mode

Use when the user explicitly asks to write new scientific or academic text using this skill.

Return:

1. The requested text
2. Brief notes only if needed, for example if a placeholder was used or scientific content requires author verification

Do not return a visible draft-then-cleanup sequence. The final answer should already reflect the skill's constraints.

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

## If the user provides AI-detector feedback

Treat AI-detector feedback as a noisy readability diagnostic, not as ground truth.

Do not rewrite merely to satisfy detector metrics. In scientific prose, the following are not automatically LLM signatures:

- long technical terms
- gene, protein, disease, method, assay, cohort, endpoint, or model names
- proper nouns and citations
- formal reviewer language
- cautious hedging
- passive voice in Methods
- dense but necessary scientific content

Use detector feedback only to identify potentially useful edits:

- overloaded sentences
- repeated generic openings
- unnecessary ceremonial framing
- vague transitions
- avoidable list-heavy compression
- formulaic conclusions or future-work language

If detector feedback conflicts with scientific precision, preserve scientific precision. Do not add filler, casual wording, artificial pronouns, hidden characters, deliberate errors, or awkward synonym substitutions to manipulate detector signals.

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
- Do not automatically use this skill for every scientific-writing task unless the user explicitly invokes it or asks for humanizing/de-AI/polishing/proofreading/light line-editing.
- Do not generate plausible scientific facts to make a new paragraph sound complete.
- Do not expose a two-step draft-then-clean workflow when the user explicitly asked to write using this skill.
