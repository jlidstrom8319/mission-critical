---
name: construction-drawings
description: Use when reading, reviewing, coordinating or extracting information from construction drawings (plans, sections, elevations, details, schedules on sheets) — sheet indexes, discipline prefixes, revisions/ASIs, cross-references, dimension and scope takeoffs, or clash/coordination checks between disciplines.
---

# Construction Drawings

Read drawings the way a Project Engineer does: establish the set, then trace scope through references, then flag conflicts.

## 1. Establish the set first

Before answering any question about a drawing, confirm:

- **Issue / revision**: title block date, issue name (Permit, Bid, IFC, Conformed), revision clouds and deltas. Never mix sets of different issues without saying so.
- **Sheet index** (usually G-001 / A-000): list what exists so missing sheets are obvious.
- **Later changes**: ASIs, bulletins, addenda, CCDs and RFI responses supersede the base sheet. Ask for or look for them.

## 2. Sheet numbering (US National CAD Standard)

`[Discipline][Type]-[Sequence]`, e.g. `A-201` = Architectural, elevations, sheet 1.

| Prefix | Discipline | Prefix | Discipline |
|---|---|---|---|
| G | General | M | Mechanical |
| C | Civil | P | Plumbing |
| L | Landscape | FP | Fire protection |
| S | Structural | E | Electrical |
| A | Architectural | T | Telecom / low voltage |
| I | Interiors | Q | Equipment |

Type digit: 0 general/legends, 1 plans, 2 elevations, 3 sections, 4 enlarged plans, 5 details, 6 schedules/diagrams, 7 user-defined, 8–9 3D/other.

## 3. Trace references

- Detail/section bubbles read `detail number / sheet number` (e.g. `5/A-501`). Follow every bubble that touches the scope in question.
- Keynotes and general notes apply to the whole sheet unless limited; check the sheet's general notes and the G-series notes.
- Door, window, finish, equipment and fixture schedules govern over tags on plans for properties; plans govern location.
- Typical / "TYP" details apply everywhere similar unless a specific detail overrides.

## 4. Order of precedence (typical — confirm in the contract)

Contract-specific precedence clause wins. Absent one, common practice: later-dated over earlier, specific over general, large-scale detail over small-scale plan, written dimension over scaled, specifications over drawings for quality/material, drawings over specifications for quantity/location. **Never scale a drawing to resolve a dimension** — issue an RFI.

## 5. Coordination review checklist

When asked to review or coordinate:

1. Grid lines and levels agree across S, A, M, P, E sheets.
2. Openings: structural penetrations vs. MEP routing; fire-rated wall penetrations have firestopping called out.
3. Ceiling heights vs. duct/pipe/beam depths (plenum space).
4. Equipment on M/P/E schedules has structural support, power, and access clearances.
5. Door hardware and access control match between A and E/T sheets.
6. Life safety plan ratings match wall types and the spec.
7. Anything shown on one discipline but missing from another.

## Output

- Cite every finding by sheet and detail (`3/A-501`, grid `C/4`), revision, and date.
- Separate **facts on the drawings** from **your inference**.
- Unresolved conflicts become draft RFIs (see `construction-rfis`).
- Takeoffs: state units, what is included/excluded, and that quantities are estimates to be checked.
