# RFP Responder (55)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to create RFI/RFP responses: requirements analysis, capability matching, technical proposal, pricing proposal, and differentiation strategy.

## Expert Roles
- **capability-matcher**: Capability matching expert. Maps company performance records, personnel, and technical capabilities to RFP requirements based on requirements analysis, and derives gaps and remediation strategies.
  - Performance Record Matching
  - Team Composition
  - Technical Capability Mapping
  - Partner/Subcontractor Strategy
  - Differentiation Point Development
- **pricing-strategist**: Pricing strategy expert. Creates optimal price proposals considering cost estimation, pricing strategy, and competitive positioning.
  - Cost Estimation
  - Price Structure Design
  - Competitive Price Analysis
  - Pricing Strategy Development
  - Price Sensitivity Analysis
- **proposal-reviewer**: Proposal reviewer (QA). Cross-validates consistency across requirements analysis, capability matching, technical proposal, and pricing proposal, and checks differentiation strategy consistency and final completeness.
  - Requirements Fulfillment Verification
  - Consistency Cross-Validation
  - Differentiation Consistency Check
  - Evaluator Perspective Assessment
  - Differentiation Strategy Document
- **requirement-analyst**: RFP requirements analysis expert. Precisely dissects RFP/RFI documents to classify mandatory/optional requirements, and identifies per-criterion scoring and hidden needs.
  - RFP Structure Analysis
  - Requirements Classification
  - Evaluation Criteria Analysis
  - Hidden Needs Identification
  - Competitive Landscape Analysis
- **technical-proposer**: Technical proposal writing expert. Based on requirements analysis and capability matching, writes technical proposals including methodology, architecture, implementation schedule, and quality management plans.
  - Business Understanding
  - Technical Methodology
  - System Architecture Design
  - Implementation Schedule
  - Quality and Risk Management

## Workflow

### Phase 1: RFP Assessment and Planning
1. Collect RFP document, company information, track record, team expertise, and organizational constraints
2. Create `_workspace/` directory in project root
3. Organize requirements into `_workspace/00_input.md`
4. Identify key opportunities and competitive landscape
5. Determine response strategy and approach

### Phase 2: Team Setup and Sequential Execution
Team members execute their deliverables with dependencies:

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|-----------|-------------|
| 1 | Requirements analysis | requirement-analyst | Input | `_workspace/01_requirement_analysis.md` |
| 2 | Capability matching | capability-matcher | 1 | `_workspace/02_capability_matching.md` |
| 3 | Technical proposal | technical-proposer | 1, 2 | `_workspace/03_technical_proposal.md` |
| 4 | Pricing proposal | pricing-strategist | 1, 2, 3 | `_workspace/04_pricing_proposal.md` |
| 5 | Review and differentiation | proposal-reviewer | 1, 2, 3, 4 | `_workspace/05_review_report.md` |

Team communication:
- Requirement analyst completes, identifies evaluation criteria and hidden needs for all downstream teams
- Capability matcher completes, provides strength/gap analysis and evidence for technical proposer
- Technical proposer completes, delivers methodology and timeline for pricing strategist
- Pricing strategist completes, provides cost and competitive positioning for reviewer
- Reviewer validates all components, requests modifications if needed (maximum 2 rounds)

### Phase 3: Integration and Final Delivery
1. Confirm all deliverables are complete in `_workspace/`
2. Review report identifies any required modifications
3. Final handoff to user includes all proposal documents and strategy brief

## Deliverables
All deliverables are saved in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_requirement_analysis.md` — Requirements analysis
- `02_capability_matching.md` — Capability matching table
- `03_technical_proposal.md` — Technical proposal
- `04_pricing_proposal.md` — Pricing proposal
- `05_review_report.md` — Review report

## Extension Skills
- **win-theme-builder**: Win theme development guide with differentiation strategies, competitive messaging, and supporting evidence compilation.
- **pricing-calculator**: Pricing calculation guide including labor cost estimation, overhead and profit calculation, and bidding strategy simulation.
