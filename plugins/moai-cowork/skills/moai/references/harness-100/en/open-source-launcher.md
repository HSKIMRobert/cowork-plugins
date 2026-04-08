# Open Source Launcher (30)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
An agent team harness for preparing open source project launches covering code cleanup, documentation, licensing, and community building.

## Expert Roles
- **Code Organizer**: Code restructuring specialist. Prepares codebase for open source release with proper organization and standards.
  - Restructures code for public consumption
  - Removes proprietary and internal information
  - Enforces coding standards and best practices
  - Optimizes dependency management
  - Sets up build and development systems

- **Doc Writer**: Documentation specialist. Creates comprehensive documentation package for open source projects.
  - Writes comprehensive README with quick start guide
  - Creates CONTRIBUTING guide with development setup
  - Generates API documentation with examples
  - Writes tutorials and getting started guides
  - Maintains CHANGELOG and release notes

- **License Specialist**: Open source licensing specialist. Manages license selection and compatibility verification.
  - Selects appropriate open source license
  - Verifies dependency license compatibility
  - Ensures legal compliance and clarity
  - Configures CLA/DCO if needed
  - Documents licensing in all files

- **Community Manager**: Community building specialist. Establishes governance and community infrastructure.
  - Develops project governance structure
  - Writes Code of Conduct
  - Creates issue and pull request templates
  - Sets up CI/CD pipeline and automation
  - Establishes community health practices
  - Plans community engagement strategy

- **Launch Reviewer**: Quality assurance specialist. Validates readiness for public release.
  - Cross-validates code cleanup completeness
  - Reviews documentation coverage and quality
  - Confirms license and legal compliance
  - Evaluates community setup adequacy
  - Provides launch readiness checklist

## Workflow

### Phase 1: Project Assessment and Planning
1. Collect project information including code repository, target audience, license preference, and community goals
2. Create `_workspace/` directory in project root
3. Organize requirements into `_workspace/00_input.md`
4. Assess current code state and documentation gaps
5. Determine launch scope and timeline

### Phase 2: Team Setup and Parallel Execution
Team members execute their deliverables with dependencies:

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|-----------|-------------|
| 1 | Code organization | code-organizer | Input | `_workspace/01_code_organization.md` |
| 2a | Documentation | doc-writer | 1 | `_workspace/02_documentation.md` |
| 2b | License review | license-specialist | Input | `_workspace/03_license_review.md` |
| 3 | Community setup | community-manager | 1, 2a, 2b | `_workspace/04_community_setup.md` |
| 4 | Launch review | launch-reviewer | 1, 2a, 2b, 3 | `_workspace/05_launch_report.md` |

Documentation and license review execute in parallel after code organization.

Team communication:
- Code organizer completes, provides cleaned codebase structure to documentation writer and community manager
- Documentation writer completes, delivers documentation package to community manager
- License specialist completes, provides license choice and compliance checklist to community manager
- Community manager completes, prepares community infrastructure
- Reviewer validates all components, requests modifications if needed (maximum 2 rounds)

### Phase 3: Integration and Final Delivery
1. Confirm all deliverables are complete in `_workspace/`
2. Review report identifies any required modifications
3. Final handoff to user includes all documentation, generated files, and launch checklist

## Deliverables
All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — Organized user input
- `01_code_organization.md` — Code cleanup plan and results
- `02_documentation.md` — Documentation package (README, guides, etc.)
- `03_license_review.md` — License review and selection
- `04_community_setup.md` — Community setup and governance
- `05_launch_report.md` — Launch review report
- `generated_files/` — Generated files (README, LICENSE, CONTRIBUTING, etc.)

## Extension Skills
- **license-compatibility-matrix**: Open source license compatibility guide with per-license requirements and SPDX identification standards.
- **community-health-metrics**: Open source project community health metrics including GitHub configuration, contribution patterns, and engagement optimization. 
