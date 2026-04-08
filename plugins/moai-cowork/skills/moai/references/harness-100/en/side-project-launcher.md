# Side Project Launcher (79)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to validate side project ideas, analyze technology stacks, design MVPs, and create development roadmaps for launch.

## Expert Roles
- **Idea Validator**: Market and concept validation specialist. Researches market viability and validates project concept.
  - Performs competitive analysis and market research
  - Assesses execution feasibility given constraints
  - Identifies differentiation and unique value proposition
  - Evaluates market opportunity and timing
  - Provides go/no-go recommendation with rationale

- **Techstack Analyst**: Technology selection specialist. Recommends optimal technology stack for the project.
  - Analyzes project requirements and technical difficulty
  - Evaluates technology options for scalability and cost
  - Prioritizes free/low-cost services (Vercel, Supabase, Cloudflare)
  - Assesses learning curve and setup time
  - Provides implementation difficulty assessment by feature

- **MVP Designer**: Minimum viable product specialist. Designs focused MVP with core features.
  - Defines core features addressing primary user problem
  - Plans 2-4 week development timeline
  - Distinguishes must-have features from nice-to-have
  - Incorporates user feedback mechanisms
  - Ensures technical feasibility assessment

- **Roadmap Builder**: Development planning specialist. Creates realistic development schedule and launch strategy.
  - Designs phased development timeline
  - Estimates effort including learning and setup time
  - Plans realistic launch channel strategy
  - Incorporates risk mitigation and buffer time
  - Provides detailed launch checklist

- **Launch Reviewer**: Quality assurance specialist. Validates consistency and feasibility across all phases.
  - Verifies idea-to-MVP feature consistency
  - Assesses realistic development timeline
  - Validates technical stack appropriateness
  - Evaluates cost and resource requirements
  - Confirms launch readiness and achievability

## Workflow

### Phase 1: Idea Assessment and Validation
1. Collect project idea, market context, constraints (time, cost, skills), and success criteria
2. Create `_workspace/` directory in project root
3. Organize project information into `_workspace/00_input.md`
4. Assess market opportunity and competitive landscape
5. Clarify project goals and target audience

### Phase 2: Team Setup and Sequential Execution
Team members execute their deliverables with dependencies:

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|-----------|-------------|
| 1 | Idea validation | idea-validator | Input | `_workspace/01_idea_validation.md` |
| 2 | Techstack analysis | techstack-analyst | 1 | `_workspace/02_techstack_recommendation.md` |
| 3 | MVP design | mvp-designer | 1, 2 | `_workspace/03_mvp_spec.md` |
| 4 | Roadmap building | roadmap-builder | 1, 2, 3 | `_workspace/04_roadmap_launch.md` |
| 5 | Launch review | launch-reviewer | 1, 2, 3, 4 | `_workspace/05_review_report.md` |

Team communication:
- Idea validator completes, provides market opportunity and differentiation analysis
- Techstack analyst completes, delivers technology recommendations and implementation constraints
- MVP designer completes, provides feature list and technical requirements
- Roadmap builder completes, delivers development timeline and launch strategy
- Reviewer validates all components, requests modifications if needed (maximum 2 rounds)

### Phase 3: Integration and Final Delivery
1. Confirm all deliverables are complete in `_workspace/`
2. Review report identifies any required modifications
3. Final handoff to user includes all documentation and launch checklist



## Deliverables
All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_idea_validation.md` — Idea validation report
- `02_techstack_recommendation.md` — Technology stack recommendations
- `03_mvp_spec.md` — MVP specification and features
- `04_roadmap_launch.md` — Development roadmap and launch checklist
- `05_review_report.md` — Comprehensive review report

## Extension Skills
- **market-sizing-calculator**: Market sizing guide with total addressable market (TAM) calculations and market opportunity assessment.
- **techstack-decision-matrix**: Technology stack decision framework for comparing options based on cost, scalability, and learning curve.
