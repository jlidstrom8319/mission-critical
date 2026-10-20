---
name: construction-schedules
description: Use when building, reviewing or analyzing a construction schedule — CPM logic, critical path, float, look-aheads, baseline vs. update comparison, delay and time-impact analysis, schedule specification compliance (e.g. Section 01 32 16), or exports from Primavera P6, Microsoft Project or similar.
---

# Construction Schedules

## Core concepts

- **CPM**: activities linked by logic (FS, SS, FF, SF) with lags. Early/late dates come from the forward and backward pass.
- **Total float** = late finish − early finish. **Critical path** = longest path / lowest float to the completion milestone.
- **Free float**: delay possible without moving any successor.
- **Constraints** override logic — treat every hard constraint as suspect unless contractually required.
- **Data date**: everything before it is actual; after it is forecast.

## Schedule quality checks (DCMA-14 style)

| Check | Typical threshold |
|---|---|
| Missing predecessors/successors (open ends) | ≤ 5% (only start/finish milestones open) |
| Leads (negative lags) | 0 |
| Lags | ≤ 5% of relationships |
| FS relationships | ≥ 90% |
| Hard constraints | ≤ 5% |
| High float (> 44 working days) | ≤ 5% |
| Negative float | 0 (or explained) |
| Durations > 44 working days | ≤ 5% (except procurement/LOE) |
| Invalid dates (actuals after data date / forecasts before it) | 0 |
| Resource/cost loading | per spec |

Also check: realistic calendars (weather, holidays), procurement chains (submittal → review → fabrication → delivery) for long-lead items, inspections and commissioning activities present, and milestones matching contract dates.

## Updates and comparisons

When comparing an update to the previous update or baseline, report:

1. Change in forecast completion and in critical-path float.
2. Change in the critical path itself (which activities entered/left).
3. Logic, duration, constraint, and calendar changes made by the scheduler (not progress).
4. Activities that started/finished out of sequence.
5. Percent complete vs. planned.

## Look-aheads

A 3-week look-ahead lists activities by trade/area for the next 3 weeks (plus 1 week back), with constraints that must clear first: submittals approved, materials on site, RFIs answered, inspections, predecessors complete, access/permits.

## Delay analysis

- Identify the delay event, the date, the activities it affected, and whether they were on the critical path at that time.
- Methods: time impact analysis (prospective fragnet), windows analysis, as-planned vs. as-built. State which one you used and its limits.
- Distinguish **excusable/compensable**, **excusable/non-compensable**, and **non-excusable**; and flag **concurrent delay**. Entitlement depends on the contract — present analysis, not legal conclusions.
- Note notice requirements and deadlines in the contract.

## Output

Tables with activity ID, name, dates, float, and the change. Always state the data date and file/version analyzed.
