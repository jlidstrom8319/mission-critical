---
name: construction-specs
description: Use when reading, summarizing or checking construction specifications (project manual) — CSI MasterFormat divisions and sections, SectionFormat Parts 1/2/3, submittal requirements, products and substitutions, quality assurance, testing, warranties, and Division 00/01 front-end and general requirements.
---

# Construction Specifications

## Structure

**MasterFormat (2018+)** numbers sections `DD SS SS` (e.g. `08 71 00 Door Hardware`).

| Div | Content | Div | Content |
|---|---|---|---|
| 00 | Procurement & contracting (bid forms, contract, conditions) | 14 | Conveying equipment |
| 01 | General requirements | 21 | Fire suppression |
| 02 | Existing conditions | 22 | Plumbing |
| 03 | Concrete | 23 | HVAC |
| 04 | Masonry | 25 | Integrated automation |
| 05 | Metals | 26 | Electrical |
| 06 | Wood, plastics, composites | 27 | Communications |
| 07 | Thermal & moisture protection | 28 | Electronic safety & security |
| 08 | Openings | 31 | Earthwork |
| 09 | Finishes | 32 | Exterior improvements |
| 10 | Specialties | 33 | Utilities |
| 11 | Equipment | 40+ | Process / industrial |
| 12 | Furnishings | | |
| 13 | Special construction | | |

**SectionFormat**: Part 1 General (scope, references, submittals, QA, delivery, warranty), Part 2 Products (manufacturers, materials, performance, fabrication), Part 3 Execution (examination, preparation, installation, field quality control, cleaning, protection).

## How to read a section

1. Read **Division 01** first — it governs every section: submittal procedures (01 33 00), substitutions (01 25 00), quality requirements (01 40 00), closeout (01 77 00 / 01 78 00). Technical sections often say "per Section 01 33 00" instead of repeating.
2. Read Division 00 for contract terms affecting the work (insurance, liquidated damages, payment, retainage).
3. In the technical section, note **related sections** — scope gaps often hide between them.
4. Identify the specifying method for products:
   - **Proprietary closed**: named product, no substitutes.
   - **Proprietary open / "or equal"**: named products, equals by substitution request.
   - **Performance**: meets stated criteria; contractor selects.
   - **Reference standard**: complies with ASTM/ANSI/UL etc.
5. Capture every **submittal**, **test**, **inspection**, **mock-up**, **warranty**, **attic stock / extra materials**, and **qualification** (installer, manufacturer, testing agency) requirement.

## Common outputs

- **Submittal register** rows: spec section, paragraph, submittal type (product data, shop drawings, samples, certificates, test reports, O&M, warranty), description, required-by. See `construction-submittals`.
- **Section summary**: scope, products/acceptable manufacturers, key performance criteria, execution must-dos, testing/inspections, warranty duration, closeout items.
- **Spec vs. drawings conflict list** → RFIs.

## Rules

- Quote the paragraph number (e.g. `09 91 23 – 2.2.B`) for every requirement you report.
- "Shall" is mandatory; "should"/"may" is not — preserve the distinction.
- Flag sections marked "Not Used", editorial notes left in by the specifier, references to outdated standards, and sections referenced but not included in the manual.
