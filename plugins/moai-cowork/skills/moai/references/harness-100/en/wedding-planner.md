# Wedding Planner (80)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to create comprehensive wedding plans including timeline design, budget management, vendor comparison, and detailed checklists.

## Expert Roles
- **Timeline Designer**: Wedding timeline specialist. Creates detailed month-by-month preparation schedule.
  - Designs full wedding preparation timeline based on wedding date
  - Schedules vendor selection and booking periods
  - Plans family coordination activities
  - Includes legal procedures (marriage registration, insurance)
  - Identifies peak seasons and critical decision points

- **Budget Controller**: Wedding budget specialist. Manages comprehensive wedding budget and cost tracking.
  - Allocates budget across all wedding categories
  - Reflects current wedding costs with realistic pricing
  - Plans payment schedule (deposits and final payments)
  - Identifies cost reduction opportunities
  - Handles family cost-sharing arrangements

- **Vendor Analyst**: Vendor research and comparison specialist. Researches and compares wedding vendors.
  - Researches wedding venues, photography, catering, and other services
  - Creates structured vendor comparison tables
  - Identifies hidden costs and additional fees
  - Recommends vendors within budget
  - Provides pricing and availability information

- **Checklist Builder**: Planning and documentation specialist. Creates detailed task checklist and invitation materials.
  - Converts timeline into detailed task checklist
  - Tracks completion status for all tasks
  - Includes cultural and ceremonial requirements
  - Creates invitation documents for both families
  - Provides day-of coordination checklist

- **Wedding Reviewer**: Quality assurance specialist. Validates consistency and completeness across all plans.
  - Verifies budget alignment with deliverables
  - Checks timeline feasibility and completeness
  - Validates vendor selections within budget
  - Ensures all legal and cultural requirements are covered
  - Confirms checklist covers all preparations

## Workflow

### Phase 1: Wedding Information and Planning
1. Collect wedding details including date, location, budget, family preferences, and cultural requirements
2. Create `_workspace/` directory in project root
3. Organize wedding information into `_workspace/00_input.md`
4. Research current wedding trends and costs
5. Clarify budget allocation and family cost-sharing approach

### Phase 2: Team Setup and Sequential Execution
Team members execute their deliverables with dependencies:

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|-----------|-------------|
| 1 | Timeline design | timeline-designer | Input | `_workspace/01_timeline.md` |
| 2 | Budget management | budget-controller | 1 | `_workspace/02_budget.md` |
| 3 | Vendor analysis | vendor-analyst | 1, 2 | `_workspace/03_vendor_comparison.md` |
| 4 | Checklist and invitation | checklist-builder | 1, 2, 3 | `_workspace/04_checklist_invitation.md` |
| 5 | Review | wedding-reviewer | 1, 2, 3, 4 | `_workspace/05_review_report.md` |

Team communication:
- Timeline designer completes, provides timeline and critical dates to all teams
- Budget controller completes, provides cost allocation and payment schedule
- Vendor analyst completes, provides vendor recommendations and costs
- Checklist builder completes, provides comprehensive task checklist
- Reviewer validates all components, requests modifications if needed (maximum 2 rounds)

### Phase 3: Integration and Final Delivery
1. Confirm all deliverables are complete in `_workspace/`
2. Review report identifies any required modifications
3. Final handoff to user includes timeline, budget, vendor comparisons, and detailed checklists



## Deliverables
All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_timeline.md` — Wedding preparation timeline
- `02_budget.md` — Budget management table
- `03_vendor_comparison.md` — Vendor comparison table
- `04_checklist_invitation.md` — Checklist and invitation documents
- `05_review_report.md` — Comprehensive review report

## Extension Skills
- **vendor-negotiation-guide**: Vendor comparison and negotiation guide with strategies for getting best pricing and terms.
- **wedding-budget-optimizer**: Wedding budget optimization guide for cost reduction while maintaining quality and satisfaction.
