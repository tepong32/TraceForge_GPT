# Spreadsheet Assessment and Business-Rule Discovery

**Answers the question:**

> **How should TraceForge assess an existing spreadsheet without mistaking observed patterns for the user's intended design?**

## Scope

This guide governs assessment of an existing spreadsheet before redesign, automation, repair, or migration. It applies across spreadsheet applications and file formats, with application-specific guides supplying additional compatibility rules.

Assessment reconstructs the best available model of the workbook. It does not grant permission to modify it, and it does not make an inference true merely because the inference is plausible.

## Evidence Posture

This guide combines TraceForge's established evidence hierarchy with **project-observed** lessons from one complex workbook assessment. The recurring assumption traps are credible and conservative, but their prevalence across unrelated spreadsheet domains remains to be tested. Treat the workflow as the default assessment discipline and revise individual heuristics when broader evidence accumulates.

## Assessment Principle

Describe the original design before judging it.

TraceForge SHALL distinguish:

- what physically exists in the workbook;
- what the user has confirmed it means;
- what an authoritative external rule requires;
- what TraceForge infers from patterns;
- what remains an assumption.

The assessment must preserve the possibility that an unusual structure, blank, manual value, exception, or dependency is intentional.

## Evidence Classes for Workbook Assessment

Use the methodology's evidence hierarchy with spreadsheet-specific meaning:

| Class | Spreadsheet meaning |
| --- | --- |
| Repository or Artifact Evidence | Cells, formulas, literal values, metadata, XML parts, relationships, names, protection, history, and test results directly observed. |
| Explicit User Requirement | The user's stated workflow, meaning, constraint, exception, or desired outcome. |
| Observed Architecture | A mapped sheet responsibility, source-of-truth boundary, dependency direction, or repeated structural pattern. |
| Engineering Standard | A format, application, accounting, audit, accessibility, or reliability practice relevant to the workbook. |
| Inference | A likely business meaning or design intent derived from observed patterns. |
| Assumption | An unverified premise necessary to continue; it must remain visible until confirmed or disproven. |

Workbook evidence proves that something exists, not necessarily why it exists or whether it remains correct.

## Assessment Workflow

### 1. Preserve and Identify the Artifact

Work from a copy when modification may occur. Record the filename, format, size, modified time, target application, and a checksum or other stable fingerprint when reproducibility matters.

Identify whether the supplied file is the authoritative workbook, an export, a template, a historical snapshot, or a partially failed artifact.

### 2. Inventory the Workbook

Inspect, as applicable:

- visible, hidden, and very-hidden sheets and their apparent roles;
- formulas, literal values, blanks, errors, merged cells, and repeated regions;
- tables, named ranges, validation, conditional formatting, and protection;
- macros, add-ins, external links, data connections, Power Query, data models, pivots, charts, and slicers;
- calculation mode, iterative calculation, cached results, locale assumptions, and date system;
- cross-sheet, cross-period, and external dependencies;
- input areas, generated areas, manual overrides, exception fields, and outputs;
- cell Notes and threaded Comments, including anchors, authors, replies, resolution state, and timestamps when available.

Inventory is descriptive. Do not rename, normalize, remove, or “repair” structures during assessment.

### Notes and Comments as Contextual Evidence

Excel 365 distinguishes threaded **Comments**, which support discussions and replies, from legacy **Notes**, which are commonly used for annotations and reminders. Treat both as first-class contextual evidence attached to the cell, not as decorative metadata. See Microsoft's [Notes and Comments distinction](https://support.microsoft.com/en-us/excel/the-difference-between-threaded-comments-and-notes).

For every relevant Note or Comment, preserve when available:

- worksheet and cell anchor;
- original text without rewriting;
- whether it is a Note or threaded Comment;
- author and reply sequence;
- resolved or active state;
- timestamp and mentions;
- the nearby header, value, formula, validation, and table context needed to interpret it.

A Note or Comment can explain intent, terminology, exceptions, or manual workflow, but it is not automatically current or authoritative. Compare it with workbook behavior and ask the user when it conflicts with formulas, data, or another annotation.

#### Multilingual, Slang, and Keyword-Only Annotations

TraceForge SHALL interpret annotations in the language actually used. It MAY switch to the user's native language for analysis or clarification when doing so preserves meaning better than translation.

When a Note or Comment contains slang, abbreviations, code-switching, misspellings, local terminology, or only a few keywords:

1. Preserve and display the original wording when referencing it.
2. Infer meaning from the cell, column header, neighboring values, sheet role, repeated usage, and project context.
3. Record a separate working interpretation; do not silently replace the original text with a normalized phrase.
4. Add uncertain terms to a project glossary with the original term, likely meaning, language or usage context, scope, and confirmation status.
5. Ask a short question in the user's preferred language when competing interpretations would change business logic or implementation.
6. Treat jokes, shorthand, reminders, and emotional emphasis as context—not automatically as requirements.

For example, a header Note containing a local keyword may strongly suggest a column's intended role, but the assessment should report both the original keyword and the inferred role until the user confirms it.

Do not reproduce personal names, mentions, or sensitive annotation text outside the assessment unless it is necessary for the engineering decision.

#### Tool-Capability Gate

Before opening and saving a workbook programmatically, establish whether the selected tool can read and preserve both Notes and threaded Comments used by that file. Threaded Comments use distinct workbook parts and relationships in the `.xlsx` package; support for ordinary cell values or legacy comments does not prove threaded-comment support. Microsoft's [XLSX extension specification](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-xlsx/66e1875d-c60a-48eb-bf88-41066d45fea8) documents their separate content and relationship types.

If the tool cannot safely round-trip an annotation type, TraceForge SHALL NOT save over the workbook through that tool. Use a read-only package inspection path, an application-native automation path, or another proven tool. Preserve the original file as the known-good source.

### 3. Map the Apparent Design

Produce an as-is model that identifies:

- each sheet's apparent responsibility;
- candidate sources of truth;
- identifiers and join keys;
- dependency and write-back direction;
- planned, actual, calculated, imported, and manual values;
- period or state transitions;
- exception paths and human intervention points;
- outputs relied upon by users or downstream systems.

Use words such as `observed`, `user-confirmed`, `inferred`, and `unknown`. Do not present an inferred architecture as the user's intended architecture.

### 4. Maintain an Assumption Register

For every assumption capable of changing the assessment or proposed design, record:

| Field | Purpose |
| --- | --- |
| Observation | What is directly visible. |
| Interpretation | What TraceForge currently thinks it means. |
| Evidence class | Fact, confirmed rule, observed architecture, inference, or assumption. |
| Alternative explanation | A credible competing interpretation. |
| Cost if wrong | Effect on money, compliance, history, source-of-truth ownership, workflow, or rework. |
| Resolution | `Confirmed`, `Supported`, `Unresolved`, or `Rejected`. |
| Validation | The user answer, test case, authoritative record, or artifact evidence needed. |

Do not replace this register with a numeric confidence score. The evidence and cost of error are more useful than an unsupported percentage.

An unclear Note or Comment that affects interpretation belongs in this register. Record the original wording and the working interpretation separately.

### 5. Challenge the Interpretation

Before recommending a redesign, try to disprove the preferred explanation:

- Find a row, period, sheet, or exception that contradicts it.
- Test whether matching results could come from manual values or coincidence.
- Check whether a blank represents absence, inapplicability, deferred state, or missing data.
- Check whether formatting is presentation rather than semantics.
- Check whether a formula is active business logic, legacy residue, or a copied pattern.
- Compare ordinary cases with boundary and exception cases.

One matching example supports a hypothesis; it does not establish a rule.

### 6. Ask Focused Business Questions

Ask only questions that repository or workbook inspection cannot answer and whose resolution changes the design.

Phrase questions in the user's business language. Prefer:

> When the planned value and the actual monthly value differ, which should control the following month?

over:

> Should cell H37 reference Scheduler!F12 or January!G37?

When useful, show the observed evidence, the competing interpretations, and the consequence of each answer.

### 7. Gate Implementation by Assumption Risk

Resolve an assumption before implementation when being wrong could alter:

- financial or statutory results;
- eligibility or entitlement;
- historical records;
- source-of-truth ownership;
- dependency or write-back direction;
- destructive normalization or irreversible migration;
- a public or downstream contract.

A low-impact, reversible assumption may support bounded exploration when it is stated, isolated, and paired with a validation step. Exploration must not be presented as accepted design.

### 8. Present the Assessment

A decision-ready assessment separates:

1. **Observed workbook design** — structures and behaviors directly evidenced.
2. **User-confirmed rules** — meanings and constraints established by the owner.
3. **Inferred intent** — interpretations supported but not confirmed.
4. **Open assumptions** — unresolved questions and their cost if wrong.
5. **Risks and inconsistencies** — evidence-backed concerns, not aesthetic preferences.
6. **Recommended next step** — further discovery, a minimal prototype, preservation, or implementation.

## Common Assumption Traps

TraceForge MUST NOT assume that:

- a blank cell is missing data;
- a literal value should be a formula;
- matching numbers prove matching business logic;
- formatting defines authoritative meaning;
- sheet order defines dependency order;
- a repeated pattern has no legitimate exception;
- a hidden sheet or column is obsolete;
- the latest period represents every historical period;
- a label controls eligibility merely because it describes status;
- a Note or Comment is current, authoritative, or correctly understood merely because it exists;
- a translated or normalized annotation retains the full meaning of native slang or shorthand;
- a technically simpler data flow is the intended business flow;
- an apparent inconsistency is an error rather than planned-versus-actual variance;
- the current formula is authoritative merely because it exists.

## Original-Design Review Standard

When assessing the user's original design, TraceForge SHALL report strengths, deliberate tradeoffs, constraints, and risks separately.

It SHALL NOT describe a design as wrong solely because another architecture is cleaner in isolation. A proposed change must identify which confirmed outcome it improves, what original behavior it preserves, what assumption it depends upon, and how the user can validate the result.

## Project-Specific Knowledge Boundary

The assessment register, confirmed business rules, exception cases, and source-of-truth decisions belong in the project. Only the reusable assessment method and recurring assumption traps belong in Applied Knowledge.

## Revisit Conditions

Revise this guide when assessments across other domains reveal new assumption classes, when a heuristic repeatedly produces unnecessary questions, or when spreadsheet tooling can establish evidence that currently requires manual confirmation.
