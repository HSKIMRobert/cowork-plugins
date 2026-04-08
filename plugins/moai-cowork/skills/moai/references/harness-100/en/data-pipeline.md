# Data Pipeline (27)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
An agent team harness that collaborates to design and implement data pipelines covering ingestion, transformation, loading, quality verification, and monitoring.

## Expert Roles
- **ETL Architect**: ETL architecture design specialist. Analyzes data sources, designs schemas across pipeline layers (Raw → Staging → Curated → Analytics), determines CDC and transformation strategies, selects appropriate technologies, and creates transformation code.
  - Performs source data analysis (database, API, flat files, streaming sources)
  - Designs multi-layer schema architecture for data transformation
  - Determines change data capture and incremental load strategies
  - Specifies transformation logic (dbt models, SQL, Spark)
  - Selects storage formats and optimization strategies (Parquet, Delta, Iceberg)

- **Data Quality Manager**: Data quality specialist. Manages data profiling, establishes verification rules, detects anomalies, tracks data lineage, and monitors quality metrics throughout the pipeline.
  - Performs data profiling and distribution analysis
  - Establishes quality verification rules (Great Expectations, dbt tests)
  - Implements statistical anomaly detection
  - Tracks data lineage and transformation impacts
  - Sets up quality dashboards and SLA monitoring

- **Scheduler Engineer**: Pipeline orchestration specialist. Designs DAGs, manages dependencies, configures retry strategies, optimizes resource allocation, and automates pipeline execution schedules.
  - Designs directed acyclic graphs (DAGs) for pipeline execution
  - Configures task dependencies and execution order
  - Implements retry and failure recovery strategies
  - Allocates computational resources and manages costs
  - Schedules periodic and event-triggered executions

- **Monitoring Specialist**: Monitoring and reliability specialist. Tracks pipeline execution metrics, builds dashboards, configures alerts, and ensures SLA compliance through comprehensive monitoring.
  - Monitors pipeline execution metrics and performance
  - Creates dashboards for data availability and quality
  - Configures alert thresholds and escalation policies
  - Tracks service level agreements (SLAs)
  - Provides runbooks for operational troubleshooting

- **Pipeline Reviewer**: Quality assurance and validation specialist. Cross-validates architecture, ensures operational readiness, evaluates consistency across all phases, and provides feedback for improvements.
  - Validates ETL architecture design completeness
  - Verifies scheduling configuration and DAG correctness
  - Confirms data quality rule implementation
  - Reviews operational readiness and risk mitigation
  - Provides comprehensive feedback for refinements

## Workflow

### Phase 1: Input Collection and Analysis
1. Collect user requirements including data sources, target systems, business requirements, constraints, and existing configurations
2. Create `_workspace/` directory in project root
3. Organize input into `_workspace/00_input.md`
4. Identify existing components and relevant project context
5. Determine execution scope (full pipeline, verification only, DAG only, or monitoring only)

### Phase 2: Team Setup and Parallel Execution
Team members execute their deliverables with dependencies:

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|-----------|-------------|
| 1 | ETL architecture design | etl-architect | Input | `_workspace/01_etl_architecture.md` |
| 2a | Data quality plan | data-quality-manager | Phase 1 | `_workspace/02_data_quality_plan.md` |
| 2b | Scheduling configuration | scheduler-engineer | Phase 1 | `_workspace/03_scheduler_config.md` |
| 3 | Monitoring setup | monitoring-specialist | 1, 2a, 2b | `_workspace/04_monitoring_setup.md` |
| 4 | Pipeline review | pipeline-reviewer | 1, 2a, 2b, 3 | `_workspace/05_review_report.md` |

Data quality plan and scheduling configuration execute in parallel after architecture is complete.

Team communication:
- ETL architect completes first, provides schema and business rules to quality manager and scheduler
- Quality manager completes, delivers verification locations and SLA criteria to monitoring specialist
- Scheduler completes, provides DAG execution metrics to monitoring specialist
- Reviewer validates all deliverables, requests modifications if needed (maximum 2 rounds)

### Phase 3: Integration and Final Delivery
1. Confirm all deliverables are complete in `_workspace/`
2. Review report identifies any required modifications
3. Final handoff to user includes all documents and code

## Deliverables
All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_etl_architecture.md` — ETL architecture design document
- `02_data_quality_plan.md` — Data quality management plan
- `03_scheduler_config.md` — Scheduling configuration and DAG definitions
- `04_monitoring_setup.md` — Monitoring dashboard and alert configuration
- `05_review_report.md` — Review report
- `pipeline_code/` — Pipeline implementation code

## Extension Skills
- **data-quality-framework**: Comprehensive data quality guide covering accuracy, completeness, timeliness, consistency with implementations in Great Expectations, dbt tests, and custom validation frameworks.
- **dag-orchestration-patterns**: Pipeline orchestration pattern guide including Airflow DAG patterns, retry strategies, dependency management, and execution optimization.
