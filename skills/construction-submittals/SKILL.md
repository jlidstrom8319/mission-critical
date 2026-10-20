---
name: construction-submittals
description: Use when building a submittal register/log, preparing or reviewing submittals (product data, shop drawings, samples, certificates, test reports, O&M manuals, warranties), checking a submittal against the spec and drawings, tracking review status, or handling substitution requests.
---

# Construction Submittals

## Build the register from the spec

For every technical section, pull each item under "Submittals" (usually Part 1, 1.3–1.6) plus those added by Division 01 (closeout, warranties, O&M, LEED/sustainability).

| Column | Notes |
|---|---|
| Submittal # | `[Section]-[seq]` e.g. `08 71 00-001`; revisions as `.1`, `.2` |
| Spec section & paragraph | `08 71 00 – 1.4.B` |
| Description | Hardware schedule, product data, etc. |
| Type | Product data / shop drawing / sample / mock-up / certificate / test report / qualification / O&M / warranty / closeout |
| Action vs. informational | Action = requires approval before fabrication |
| Responsible sub | |
| Required on-site date | Back-schedule from install |
| Submit-by date | = on-site − (review time × cycles) − fabrication − delivery |
| Reviewer(s) | Architect, engineer of record, consultant |
| Status & dates | Sent, returned, action code |

Use the review duration stated in Division 01 (often 10–14 working days, longer for delegated design); allow at least one resubmittal cycle on long-lead items.

## Pre-submission (contractor) review

Before forwarding a sub's submittal, check:

1. Correct spec section, project name, submittal number, and revision.
2. Every required item in the spec paragraph is included.
3. Products match specified manufacturers/models, or a substitution request is attached.
4. Options, sizes, colors, ratings, finishes are marked/highlighted; irrelevant options crossed out.
5. Dimensions and quantities match the drawings; field dimensions verified where required.
6. Interfaces with other trades coordinated (embeds, power, supports, openings).
7. Required certifications, stamps (delegated design PE stamp), test reports, and warranties present.
8. Deviations from the contract documents are listed explicitly — a submittal approval does not authorize an unlisted deviation.

Apply the contractor's review stamp only after this check.

## Reviewer action codes (typical)

- **Approved / No exceptions taken**
- **Approved as noted / Make corrections noted** — proceed, incorporate notes
- **Revise and resubmit** — do not fabricate
- **Rejected / Not approved**
- **Received for information / record only**

Use the exact codes defined in the project's Division 01.

## Substitutions

Follow 01 25 00: deadlines (often before bid or within N days of award), the required comparison (specified vs. proposed, with data), effect on schedule, cost, and other trades, and the requester's representations. A substitution submitted as a normal submittal is a red flag.

## Output

- Registers as tables (or CSV/XLSX when asked), sorted by spec section.
- Review comments numbered, each citing the spec paragraph or drawing reference it is based on.
