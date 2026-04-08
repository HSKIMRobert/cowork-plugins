# Security Audit (28)

> MoAI-Cowork V.0.1.3 Harness Reference

## Overview
An agent team harness for performing security audits covering vulnerability scanning, code analysis, penetration test reporting, and remediation recommendations.

## Expert Roles
- **Vulnerability Scanner**: Vulnerability scanning specialist. Systematically detects security vulnerabilities from code, dependencies, and infrastructure configurations.
  - Identifies dependency vulnerabilities using CVE databases
  - Analyzes container and infrastructure configurations
  - Detects secrets and credentials in codebase
  - Creates Software Bill of Materials (SBOM) for dependency tracking
  - Classifies findings by CVSS 3.1 severity levels

- **Code Analyst**: Code security specialist. Performs static application security testing and pattern detection for secure coding violations.
  - Conducts SAST (Static Application Security Testing) analysis
  - Identifies OWASP Top 10 vulnerabilities
  - Detects insecure coding patterns and anti-patterns
  - Maps vulnerabilities to CWE classifications
  - Provides code examples of secure implementations

- **Pentest Reporter**: Penetration test specialist. Reports on attack scenarios, proof of concepts, and impact analysis.
  - Develops attack scenarios and exploitation chains
  - Creates proof of concept demonstrations
  - Analyzes real-world attack feasibility
  - Maps attacks to MITRE ATT&CK framework
  - Documents technical exploitation procedures

- **Security Consultant**: Security strategy specialist. Develops remediation recommendations and security improvement roadmaps.
  - Creates prioritized remediation plans
  - Maps vulnerabilities to compliance frameworks (GDPR, HIPAA, PCI-DSS)
  - Develops multi-phase security improvement roadmaps
  - Identifies systemic security improvements
  - Aligns recommendations with business risk appetite

- **Audit Reviewer**: Quality assurance specialist. Cross-validates findings, adjusts risk levels, and produces final audit report.
  - Validates all findings across domains
  - Adjusts risk classifications based on business context
  - Verifies remediation recommendations feasibility
  - Ensures compliance with audit standards
  - Produces comprehensive final audit report

## Workflow

### Phase 1: Scope Definition and Planning
1. Collect audit requirements including target scope (code/infrastructure/containers), boundaries, technology stack, compliance requirements, and existing reports
2. Create `_workspace/` directory in project root
3. Organize requirements into `_workspace/00_input.md`
4. Define audit boundaries and exclusions
5. Determine execution scope (full audit, code analysis only, vulnerability scanning only, or consulting)

### Phase 2: Team Setup and Parallel Execution
Team members execute their deliverables with dependencies:

| Order | Task | Owner | Depends On | Deliverable |
|-------|------|-------|-----------|-------------|
| 1a | Vulnerability scanning | vulnerability-scanner | Input | `_workspace/01_vulnerability_scan.md` |
| 1b | Code security analysis | code-analyst | Input | `_workspace/02_code_analysis.md` |
| 2 | Penetration test report | pentest-reporter | 1a, 1b | `_workspace/03_pentest_report.md` |
| 3 | Remediation plan | security-consultant | 1a, 1b, 2 | `_workspace/04_remediation_plan.md` |
| 4 | Audit review | audit-reviewer | 1a, 1b, 2, 3 | `_workspace/05_audit_report.md` |

Vulnerability scanning and code analysis execute in parallel during Phase 1.

Team communication:
- Scanner completes, provides vulnerability details and CWE mappings to analyst and pentest reporter
- Analyst completes, delivers attack scenarios and data flow analysis to pentest reporter
- Pentest reporter completes, delivers business impact and urgency assessment to security consultant
- Consultant completes, delivers improvement plan to audit reviewer
- Reviewer validates all deliverables, requests modifications if needed (maximum 2 rounds)

### Phase 3: Integration and Final Delivery
1. Confirm all deliverables are complete in `_workspace/`
2. Review report identifies any required modifications
3. Final handoff to user includes all reports and recommendations

## Deliverables
All deliverables are stored in the `_workspace/` directory:
- `00_input.md` — Audit scope and organized user input
- `01_vulnerability_scan.md` — Vulnerability scan results
- `02_code_analysis.md` — Code security analysis report
- `03_pentest_report.md` — Penetration test scenario report
- `04_remediation_plan.md` — Remediation recommendations and roadmap
- `05_audit_report.md` — Final audit report

## Extension Skills
- **owasp-testing-guide**: OWASP Top 10 security testing guide with vulnerability-specific testing procedures and remediation guidance.
- **cve-analysis**: CVE analysis and dependency vulnerability management including CVSS rating methodology and severity classification.
- **threat-modeling**: Threat modeling methodology guide using STRIDE, DREAD, and Attack Tree approaches for systematic vulnerability analysis. 
