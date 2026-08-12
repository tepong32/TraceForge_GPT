# Excel 365 Workbook Engineering

**Answers the question:**

> **How should TraceForge safely create or modify an `.xlsx` workbook intended for Excel 365?**

## Scope

This guide governs generated or programmatically modified `.xlsx` workbooks whose required runtime is desktop Microsoft Excel 365. It applies whether work uses Python, another spreadsheet engine, direct OOXML manipulation, or a combination of tools.

It does not define the workbook's business rules. Those remain project evidence and must be confirmed separately.

Use [Spreadsheet Assessment and Business-Rule Discovery](Spreadsheet%20Assessment%20and%20Business-Rule%20Discovery.md) before redesigning an existing workbook whose intent is not already documented.

## Evidence Posture

This guide began with **project-observed** evidence from one phased Excel 365 workbook reconstruction. Excel repair behavior, known-good checkpoint recovery, and incremental formula isolation were directly observed. The broader formula and structure policies are conservative defaults supported by that experience but still require replication across other workbook types, Excel builds, locales, and automation tools.

Excel 365's successful open behavior remains the target-application validation authority. Project-specific business behavior must be confirmed independently.

## Compatibility Authority

Excel 365 is the final compatibility authority for an Excel 365 deliverable.

A workbook can be a valid ZIP package, valid OOXML, and readable by a library or another spreadsheet application while still causing Excel to repair or reject it. Programmatic validation is necessary but cannot establish the final compatibility claim.

TraceForge MUST NOT call a workbook “Excel 365 compatible” or “Excel 365 safe” unless the target Excel version opens it without a repair prompt or removed-content warning.

## Controlled Workbook Lifecycle

### 1. Discover

Before changing the workbook, identify:

- worksheets and their responsibilities;
- file format and target Excel channel, build, platform, locale, and regional settings when material;
- visible, hidden, and very-hidden worksheets;
- tables, named ranges, formulas, external links, data validation, protection, Notes, threaded Comments, and relationships;
- macros, add-ins, external connections, Power Query, data models, PivotTables, charts, and slicers when present;
- calculation mode, iterative calculation, workbook date system, and cached formula values;
- calculation and cross-sheet dependency chains;
- sources of truth and dependency direction;
- planned, actual, calculated, and manually controlled values;
- legitimate exceptions and user intervention points;
- known-good outputs used for business comparison.

Suspicious-looking values are questions, not automatic defects. Establish the business rule before normalizing data or replacing manual behavior.

### 2. Preserve a Known-Good Baseline

Keep each Excel-confirmed checkpoint as an immutable file. Do not overwrite the last confirmed-good workbook.

Use names that make the phase and compatibility status visible, for example:

```text
Phase03_Excel365Safe.xlsx
Phase04_Excel365Safe.xlsx
Phase05_Retry02_Excel365Safe.xlsx
```

### 3. Make One Logical Change

Introduce one coherent formula family, structure change, validation rule, or data-flow change per compatibility checkpoint. A small delta makes a failure attributable and reversible.

For formula-heavy work, a safe progression is:

1. static data and structure;
2. direct cross-sheet references;
3. one lookup class;
4. dependent lookup or calculation classes;
5. statutory or business arithmetic;
6. totals and net results;
7. reconciliation and audit formulas.

The exact sequence follows the workbook, but unrelated formula families should not enter an unproven checkpoint together.

### 4. Run Programmatic Preflight

Inspect, as applicable:

- ZIP/package integrity;
- workbook and worksheet relationships;
- sheet names and expected sheet count;
- table definitions and table parts;
- formulas introduced by the current change;
- defined names, data validation, and external links;
- macro, query, connection, pivot-cache, calculation, protection, and date-system parts when present;
- load and save behavior in the generating library;
- expected cell types, references, and dependency direction;
- Note and threaded-Comment counts, anchors, text, authorship, threads, and relationships when present.

Preflight diagnoses structural problems. It does not replace Excel validation.

Before any programmatic round trip, verify that the selected tool preserves every annotation type present. If it cannot preserve Notes or threaded Comments, do not use that tool to save the deliverable. After generation, compare the annotation inventory with the known-good baseline and inspect representative multilingual or keyword-only annotations in Excel.

### 5. Open in Excel 365

Have the target user or an authorized test environment open the produced workbook in Excel 365. Any repair prompt, removed-content warning, corrupted-content warning, or unexpected compatibility conversion fails this gate.

Missing, converted, detached, or truncated Notes or threaded Comments also fail the gate when those annotations are part of the workbook's documentation or workflow.

User compatibility QA should be lightweight: first ask whether the file opens cleanly. Request deeper manual inspection only for behavior that cannot be established programmatically.

### 6. Validate Business Behavior

Application compatibility and business correctness are independent gates:

- **Gate A — Technical:** Excel 365 opens the workbook without repair and its package structure remains sound.
- **Gate B — Business:** Calculations, manual controls, dependencies, exceptions, and outputs match the intended rules.

Passing either gate does not imply passing the other. Compare representative results with known-good outputs and test legitimate exception paths.

### 7. Promote or Revert

If both required gates pass, preserve the artifact as the next known-good baseline. If a gate fails, return to the previous confirmed-good baseline and investigate the single delta.

Never build the next phase from a failed workbook or stack speculative repairs onto a corrupt artifact.

## Formula Policy

Prefer formulas that are transparent, auditable, and supported by the target environment:

- direct references;
- `IF` and `IFERROR`;
- `XLOOKUP` when the target version supports it;
- `INDEX` and `MATCH`;
- simple arithmetic;
- `SUMIFS` and similarly established aggregations.

More sophisticated dynamic-array or volatile constructions—including `FILTER`, `LET`, `MAP`, `HSTACK`, `INDIRECT`, and `OFFSET`—are not universally prohibited. Prove each required function independently in the target workbook and Excel version before making it foundational.

Formula elegance does not justify a larger compatibility surface.

## Native Excel Structures

Preserve existing Excel Tables, named ranges, validations, and other useful native behavior unless evidence identifies them as the failure source.

Do not remove all tables or flatten workbook structures as a generic repair strategy. Inspect the relevant XML and relationships when a structure-specific failure is demonstrated. Avoid introducing unnecessary new structures during compatibility isolation.

## Data-Flow and Manual-Control Rules

Before automating a field, identify:

- its authoritative source;
- whether it is planned, actual, calculated, or manual;
- whether changes flow one way or in both directions;
- whether previous-period state intentionally affects the current period;
- which exceptions require human control.

Do not infer a business rule merely because a generated number matches an existing workbook. The existing value may be manual, exceptional, or coincidental.

Preserve deliberate one-way flows and manual override points. Do not introduce reverse write-back, silent correction, or automatic normalization without an explicit rule and test.

## Failure Protocol

When Excel repairs or rejects a workbook:

1. Quarantine the failed artifact; do not use it as a new base.
2. Record the last confirmed-good checkpoint and the single change introduced.
3. Capture Excel's repair message or recovery log when available.
4. Compare package parts and relationships against the known-good file.
5. Remove or isolate only the suspect delta.
6. Regenerate from the known-good baseline.
7. Repeat programmatic and Excel validation.

## Project-Specific Knowledge Boundary

Workbook-specific rules—such as payroll eligibility, salary progression, period precedence, budget-versus-actual policy, or special-event processing—must remain in that project's canonical documentation or ADRs.

This guide may preserve the engineering pattern those rules reveal, such as “confirm dependency direction” or “distinguish planned and actual values,” but not the project-specific rule itself.

## Revisit Conditions

Revise this guide when repeated use demonstrates a safer workflow, a supported generation tool provides authoritative Excel-level validation, a formula or OOXML behavior changes materially, or evidence shows that a current conservative rule causes more risk than it prevents.

## Operational Summary

```text
Known-good workbook
→ one logical change
→ programmatic preflight
→ Excel 365 open test
→ business validation
→ PASS: preserve new baseline
→ FAIL: revert to known-good baseline
```
