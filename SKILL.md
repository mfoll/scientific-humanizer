---
name: scientific-writing-humanizer
description: Edit scientific manuscripts, abstracts, grants, figure legends, reviewer responses, and other academic prose to remove obvious LLM-generated writing patterns while preserving scientific meaning, technical terminology, author voice, citation logic, cautious hedging, and journal-appropriate register. Use when asked to humanize, de-slop, de-AI, polish, audit, rewrite, or detector-risk-check scientific or academic text without making it casual or generic.
---

# Scientific Writing Humanizer

## Purpose

Use this skill as a scientific line editor and AI-pattern auditor. The goal is not to make a model "talk like a human" and not to add casual personality. The goal is to make scientific prose read like careful author-edited manuscript text: precise, evidence-bound, field-aware, and free of obvious LLM artifacts.

This skill adapts generic AI-writing cleanup patterns to scientific writing. It treats suspicious words as context-dependent signals, not banned words. Words such as "robust", "comprehensive", "crucial", "significant", "highlight", "serves as", and "it is worth noting" are acceptable when they are scientifically precise, conventional for the field, and supported by the surrounding evidence.

## Non-Negotiable Priorities

Apply these priorities in order:

1. Preserve scientific content, numerical values, uncertainty, citations, nomenclature, and claim strength.
2. Preserve field and journal conventions, including legitimate passive voice in Methods and standard technical phrasing.
3. Preserve consistent terminology. Do not synonym-spin defined terms.
4. Improve clarity, concision, paragraph flow, and claim-evidence alignment.
5. Reduce obvious LLM-pattern risk without degrading the prose or adding obfuscation.

Never insert hidden Unicode, spacing tricks, deliberate errors, fake citations, fake specificity, or awkward synonym substitutions to evade detectors.

## When Starting

Infer the likely section type: Abstract, Introduction, Methods, Results, Discussion, figure legend, grant text, cover letter, or reviewer response. If the target journal, field, or section type is missing, proceed with reasonable assumptions and state only the assumptions that affect edits.

If the user provides a writing sample, calibrate to it as a soft guide:

- sentence length and rhythm
- preferred level of formality
- use of "we", passive voice, and transitions
- field-specific terminology
- typical paragraph openings and closing moves

Do not imitate errors or idiosyncrasies that reduce clarity.

## Editing Workflow

### 1. Claim and Evidence Guard

Before rewriting, identify the major claims and the evidence supporting them.

- Keep claims no stronger than the data, citation, or stated result allows.
- Do not add new mechanisms, implications, citations, statistics, disease entities, cohorts, methods, or limitations.
- If a claim seems unsupported, weaken it or flag it instead of inventing support.
- Preserve statistical direction, magnitude, uncertainty, and comparator language.

### 2. Scientific Style Pass

Edit for good scientific writing before editing for AI patterns.

- Replace clutter: "in order to" -> "to"; "due to the fact that" -> "because"; "has the ability to" -> "can".
- Revive verbs when it improves clarity: "performed an analysis of" -> "analyzed"; "provides evidence for" -> "supports".
- Use active voice when it clarifies the actor, especially in Introduction, Results, Discussion, grants, and responses.
- Keep passive voice when the actor is irrelevant, conventional, or when the object must be emphasized, especially in Methods.
- Keep one main message per paragraph; the first sentence should usually orient the reader.
- Maintain sentence-to-sentence logic: cause, contrast, consequence, refinement, example, or limitation.
- Use old-to-new information flow: begin sentences with context the reader already has, then place the new or important information near the end.
- Keep the main verb close to the subject when possible; long subject-to-verb delays make scientific sentences harder to parse.
- Keep technical nouns self-contained. Define abbreviations at first use if the surrounding text requires it.

### 3. Terminology Consistency Pass

Scientific repetition is often correct.

- Repeat the defined term when it names a method, cohort, variable, group, mutation, assay, model, endpoint, or disease entity.
- Do not replace a technical term with a near-synonym just to avoid repetition.
- Flag term drift: "tumor samples", "specimens", "cases", and "cohort" may refer to different things.
- Keep gene/protein/species formatting and capitalization consistent with the user's text unless asked to standardize it.
- Preserve section-specific labels such as arm names, model names, comparison groups, figure panel identifiers, and endpoint names.

### 4. AI-Pattern Audit

Flag and edit these only when they make the scientific prose generic, inflated, or formulaic.

**Significance inflation**

- Watch: "crucial", "pivotal", "key", "vital", "transformative", "groundbreaking", "landmark", "important", "highlights the importance of", "underscores".
- Keep if the claim is precise and supported: "a crucial cysteine residue", "robust standard errors", "comprehensive genomic profiling".
- Edit if it is ceremonial: "This pivotal finding underscores..." -> state the finding and its direct implication.

**Copula avoidance and ceremonial framing**

- Watch: "serves as", "stands as", "represents", "marks", "acts as a testament to".
- Keep "serves as" when it describes function precisely: "albumin serves as a carrier protein".
- Edit when it avoids a simpler verb: "This result serves as evidence that..." -> "This result supports..."

**Present-participle chains**

- Watch sentence tails with "highlighting", "underscoring", "reflecting", "showcasing", "emphasizing", "contributing to", "ensuring".
- Edit when they add vague depth without evidence.
- Keep when they express a real relationship and are grammatically cleaner than a second sentence.

**Generic transitions and throat-clearing**

- Watch: "It is worth noting that", "It is important to note that", "Interestingly", "Notably", "In this context", "Furthermore", "Moreover", "Additionally".
- Delete or replace when they do not change the meaning.
- Keep "notably" or "interestingly" only when the contrast or surprise is specific.

**Rule-of-three and over-balanced structure**

- Watch repeated triads, perfectly parallel clauses, and uniformly sized paragraphs.
- Use the number of items the science actually needs.
- Break symmetry when the evidence is asymmetric.

**Vague attribution**

- Watch: "studies show", "experts argue", "the literature suggests", "emerging evidence indicates".
- Replace with a specific citation placeholder only if the user supplied it.
- Otherwise write a more bounded claim: "Several studies have reported..." or flag that the claim needs a citation.

**Over-hedging and under-hedging**

- Remove stacked hedges: "may potentially suggest" -> "may suggest".
- Add a hedge when causal, translational, or mechanistic claims outrun the evidence.
- Preserve appropriate scientific caution.

**Generic conclusions and future-work filler**

- Watch: "paves the way", "opens new avenues", "future studies are warranted", "holds promise", "important implications".
- Replace with concrete next steps, limits, or implications when the manuscript provides them.
- If no concrete implication is available, keep the conclusion modest.

**Chatbot residue**

- Remove assistant artifacts: "Of course", "Here is", "I hope this helps", "Let me know", "as an AI", "based on available information".

### 5. Detector-Risk Artifact Audit

Treat detector risk as a quality-control signal, not as the target.

Look for:

- Hidden or unusual Unicode characters, including thin spaces, zero-width spaces, non-breaking spaces, and mixed quote styles.
- Unnatural spacing, especially missing spaces after sentence-final punctuation.
- Repeated phrases or repeated tortured substitutions.
- Awkward one-to-one synonym replacement.
- Too-smooth paragraph rhythm: every paragraph the same length, every sentence medium-length, every transition explicit.
- Excessive watchlist clustering: many generic AI-associated words in a short span.

If the text is in a local file, optionally run:

```bash
python scripts/audit_text_artifacts.py path/to/text.txt
```

Use the script output as a mechanical aid. Do not optimize blindly for it.

## Section-Specific Guidance

### Abstract

- Make the objective, design, main result, and conclusion explicit.
- Keep claims tightly scoped to the results.
- Avoid generic opening sentences about broad importance unless the target journal expects them.
- Do not add citations unless the journal style requires them.

### Introduction

- Build from field context to a precise gap or unresolved question.
- Avoid "limited understanding" boilerplate unless the exact limitation is named.
- State the study objective or hypothesis directly.
- Keep novelty language factual rather than promotional.

### Methods

- Prioritize reproducibility over stylistic polish.
- Passive voice is often acceptable when the procedure matters more than the actor.
- Do not simplify technical terms if simplification changes meaning.
- Preserve chronological and procedural detail.

### Results

- Present findings before interpretation.
- Keep numbers, directionality, comparators, confidence intervals, and p-values unchanged.
- Avoid "interestingly" unless the result contradicts a clear expectation.
- Do not add mechanistic explanation unless already shown by the data.

### Discussion

- Distinguish observation, interpretation, limitation, and implication.
- Compare with cited literature without exaggerating novelty.
- Keep limitations specific; avoid generic limitation paragraphs.
- Avoid ending with broad "paves the way" language.

### Reviewer Responses

- Be direct, respectful, and evidence-based.
- State what changed and where.
- Do not over-apologize or over-praise reviewers.
- When disagreeing, give the reason and the supporting evidence.

## Output Formats

### Rewrite Mode

Use when the user asks to rewrite, humanize, polish, or de-AI text.

Return:

1. Revised text
2. Brief edit notes, grouped by scientific clarity and AI-pattern risk
3. Residual issues or claims needing author verification, only if present

### Audit Mode

Use when the user asks to check, review, score informally, or diagnose text.

Return findings in this format:

```text
Finding: [short label]
Severity: critical | major | minor
Original: [short excerpt]
Why it matters: [specific reason]
Suggested revision: [replacement or action]
```

### Interactive Mode

Use when the user asks to work paragraph by paragraph.

For each paragraph, provide:

1. Original issue summary
2. Revised paragraph
3. What changed and why

Then wait for the user's decision before continuing.

## Context-Sensitive Watchlist

These are not banned. Treat them as signals that require context:

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

Keep a watchlisted word when it is:

- part of standard field usage
- attached to a specific object, mechanism, result, or statistical method
- less awkward than the alternative
- present in the author's established voice

Edit it when it is:

- unsupported by evidence
- repeated across nearby sentences
- used to inflate significance
- a substitute for naming the actual result
- part of generic LLM scaffolding

## What Not To Do

- Do not make scientific prose casual, chatty, humorous, or "soulful".
- Do not ban words globally.
- Do not synonym-spin technical vocabulary.
- Do not remove necessary hedging.
- Do not remove legitimate passive voice from Methods just to satisfy a style rule.
- Do not add undocumented citations, findings, methods, limitations, or implications.
- Do not insert deliberate typos, invisible characters, strange punctuation, or spacing artifacts.
- Do not claim that a rewrite will bypass AI detectors.

## Source Synthesis

This skill synthesizes:

- `blader/humanizer`: generic AI-writing pattern list, adapted here as context-sensitive scientific watch signals.
- `labarba/sciwrite`: clutter extraction, active/passive judgment, sentence architecture, terminology consistency, and numerical/citation caution.
- `Master-cai/Research-Paper-Writing-Skills`: paragraph role, reverse outlining, and claim-evidence alignment.
- `K-Dense-AI/claude-scientific-writer` and `OpenLAIR/dr-claw`: IMRAD structure, reporting guidelines, field terminology, and section-specific scientific writing workflow.
- `hanlulong/econ-writing-skill`: reader-first writing, concrete claims over vague contribution language, and discipline-specific style.
- Nature Methods and Gopen/Swan-style guidance: audience-first manuscript design, every word doing useful work, old-to-new information flow, and sentence stress.
- Pangram humanizer evidence: hidden Unicode, spacing artifacts, tortured phrases, repetitive substitutions, and the limitation that detector-oriented humanizers often degrade text.
