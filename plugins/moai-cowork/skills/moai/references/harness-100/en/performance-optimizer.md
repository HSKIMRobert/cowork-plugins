# Performance Optimizer (29)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
An agent team harness for performance optimization covering profiling, bottleneck analysis, optimization, and benchmarking.

## Expert Roles
- **Profiler**: Performance profiling specialist. Measures CPU, memory, I/O, and network performance with hotspot identification.
  - Captures CPU usage patterns and hotspots
  - Measures memory allocation and garbage collection
  - Analyzes I/O operations and disk patterns
  - Tracks network latency and bandwidth usage
  - Generates detailed profiling reports with visualization

- **Bottleneck Analyst**: Performance analysis specialist. Identifies performance bottlenecks and calculates optimization impact.
  - Analyzes profiling data for hotspots
  - Identifies root causes of performance degradation
  - Quantifies impact scope and business implications
  - Prioritizes optimization opportunities
  - Estimates expected performance improvements

- **Optimization Engineer**: Performance optimization specialist. Implements code, query, and architectural optimizations.
  - Optimizes application code and algorithms
  - Improves database queries and indexing
  - Refactors architecture for performance
  - Implements caching strategies
  - Provides before/after code comparisons

- **Benchmark Manager**: Benchmarking specialist. Designs tests, executes benchmarks, and analyzes performance improvements.
  - Designs comprehensive performance test scenarios
  - Executes benchmarks in controlled environments
  - Measures pre-optimization and post-optimization performance
  - Detects performance regressions
  - Integrates benchmark tests into CI/CD pipeline

- **Perf Reviewer**: Quality assurance specialist. Validates optimizations and ensures no regressions.
  - Cross-validates profiling and optimization results
  - Evaluates performance regression risks
  - Verifies optimization completeness
  - Assesses architectural impact
  - Produces final performance report

## Workflow

### Phase 1: Problem Definition and Analysis
1. Collect performance concerns including system/component focus, performance goals, SLA requirements, and usage patterns
2. Create `_workspace/` directory in project root
3. Organize requirements into `_workspace/00_input.md`
4. Identify baseline performance metrics
5. Determine optimization scope (application-level, database, infrastructure, or full stack)

### Phase 2: Team Setup and Sequential Execution
Team members execute their deliverables with dependencies:

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|-----------|-------------|
| 1 | Profiling | profiler | Input | `_workspace/01_profiling_report.md` |
| 2 | Bottleneck analysis | bottleneck-analyst | 1 | `_workspace/02_bottleneck_analysis.md` |
| 3 | Optimization plan | optimization-engineer | 2 | `_workspace/03_optimization_plan.md` |
| 4 | Benchmarking | benchmark-manager | 3 | `_workspace/04_benchmark_results.md` |
| 5 | Performance review | perf-reviewer | 1, 2, 3, 4 | `_workspace/05_review_report.md` |

Team communication:
- Profiler completes, provides detailed profiling data and hotspot identification
- Bottleneck analyst completes, delivers impact assessment and optimization priorities
- Optimization engineer completes, delivers optimized code and implementation details
- Benchmark manager completes, provides performance improvement metrics
- Reviewer validates all optimizations, requests modifications if needed (maximum 2 rounds)

### Phase 3: Integration and Final Delivery
1. Confirm all deliverables are complete in `_workspace/`
2. Review report identifies any required modifications
3. Final handoff to user includes all reports and optimized code

## Deliverables
All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_profiling_report.md` — Profiling results
- `02_bottleneck_analysis.md` — Bottleneck analysis report
- `03_optimization_plan.md` — Optimization plan and implementation
- `04_benchmark_results.md` — Benchmark results and comparison
- `05_review_report.md` — Review report

## Extension Skills
- **query-optimization-patterns**: SQL/NoSQL query optimization patterns including execution plan analysis, indexing strategies, and N+1 query resolution.
- **caching-strategy-selector**: Caching strategy selection guide covering Cache Aside, Write Through, Write Behind patterns with Redis/Memcached configuration and TTL management. 
