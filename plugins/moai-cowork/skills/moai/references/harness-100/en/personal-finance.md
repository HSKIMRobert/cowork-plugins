# Personal Finance (78)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
A harness where an agent team collaborates to create comprehensive personal financial management plans through income-expense analysis, budget design, investment strategy, and tax optimization.

## Expert Roles
- **Financial Analyst**: Financial analysis specialist. Analyzes personal financial situation and diagnoses financial position.
  - Analyzes income and expense patterns
  - Identifies expense structure and optimization opportunities
  - Assesses savings capacity and current assets
  - Evaluates existing liabilities and debt
  - Provides financial position diagnosis

- **Budget Planner**: Budget design specialist. Creates realistic and achievable budget with savings goals.
  - Designs category-based budgets aligned with income
  - Sets realistic savings targets and goals
  - Provides phased milestones (monthly to yearly progression)
  - Identifies cost reduction opportunities
  - Plans for both short-term and long-term goals

- **Investment Advisor**: Investment strategy specialist. Recommends optimal asset allocation and portfolio design.
  - Analyzes investment capacity from budget plan
  - Recommends asset allocation matching risk profile
  - Suggests specific investment vehicles (ETF, pension savings, ISA)
  - Balances growth objectives with tax efficiency
  - Designs diversified portfolio approach

- **Tax Strategist**: Tax optimization specialist. Develops tax savings strategy and retirement planning.
  - Optimizes tax deductions and credits
  - Plans tax-efficient investment strategies
  - Designs retirement savings approach
  - Identifies additional tax savings opportunities
  - Provides retirement income projections

- **Finance Reviewer**: Quality assurance specialist. Validates consistency across all financial plans.
  - Verifies income-expense-savings relationships
  - Cross-validates budget, investment, and tax plans
  - Assesses plan feasibility and realism
  - Ensures goal alignment across all phases
  - Identifies gaps and inconsistencies

## Workflow

### Phase 1: Financial Assessment and Goal Setting
1. Collect financial information including income, expenses, assets, liabilities, and financial goals
2. Create `_workspace/` directory in project root
3. Organize financial data into `_workspace/00_input.md`
4. Assess current financial position
5. Clarify financial objectives and constraints

### Phase 2: Team Setup and Sequential Execution
Team members execute their deliverables with dependencies:

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|-----------|-------------|
| 1 | Financial analysis | financial-analyst | Input | `_workspace/01_financial_analysis.md` |
| 2 | Budget planning | budget-planner | 1 | `_workspace/02_budget_plan.md` |
| 3 | Investment strategy | investment-advisor | 1, 2 | `_workspace/03_investment_strategy.md` |
| 4 | Tax strategy | tax-strategist | 1, 2, 3 | `_workspace/04_tax_strategy.md` |
| 5 | Review | finance-reviewer | 1, 2, 3, 4 | `_workspace/05_review_report.md` |

Team communication:
- Financial analyst completes, provides expense structure and savings capacity assessment
- Budget planner completes, provides investment capacity and savings targets
- Investment advisor completes, provides tax considerations for tax strategist
- Tax strategist completes, provides tax-optimized investment approach
- Reviewer validates all components, requests modifications if needed (maximum 2 rounds)

### Phase 3: Integration and Final Delivery
1. Confirm all deliverables are complete in `_workspace/`
2. Review report identifies any required modifications
3. Final handoff to user includes all financial plans and implementation roadmap



## Deliverables
All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_financial_analysis.md` — Income-expense analysis and financial position diagnosis
- `02_budget_plan.md` — Budget design and savings plan
- `03_investment_strategy.md` — Investment strategy and portfolio recommendations
- `04_tax_strategy.md` — Tax optimization approach and retirement planning
- `05_review_report.md` — Comprehensive review report

## Extension Skills
- **compound-interest-simulator**: Compound interest calculation guide with investment growth projections and savings goal timeline analysis.
- **financial-ratio-analyzer**: Financial ratio analysis framework for personal finances including liquidity, solvency, and efficiency metrics.
