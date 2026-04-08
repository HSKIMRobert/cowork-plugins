---
name: moai-operations-hr
description: "운영 & HR — 채용 파이프라인, 온보딩 시스템, 운영 매뉴얼, 고객 지원, 피드백 분석, 조달 문서, 원격 근무 운영, 리스크 레지스터 하네스. 채용, 면접, 온보딩, 신입 교육, 운영, 프로세스, CS, 고객 지원, 피드백, 설문, 조달, 구매, 원격 근무, 재택, 리스크."
---

# 운영 & HR (⑧ operations-hr)

> MoAI-Cowork v0.2.0 | 8 하네스

## 하네스 (전략 가이드)

| ID | 한국명 | 설명 |
|----|--------|------|
| hiring-pipeline | 채용 파이프라인 | JD 작성, 면접 설계, 평가 기준, 채용 프로세스 |
| onboarding-system | 온보딩 시스템 | 신입 온보딩, 체크리스트, 멘토링 프로그램 |
| operations-manual | 운영 매뉴얼 | 업무 프로세스, 운영 규정, 워크플로우 설계 |
| customer-support | 고객 지원 | CS 응대 가이드, FAQ, 에스컬레이션 프로세스 |
| feedback-analyzer | 피드백 분석 | 설문 설계, 응답 분석, 인사이트 도출 |
| procurement-docs | 조달 문서 | 구매 요청서, 발주서, 벤더 평가 |
| remote-work-ops | 원격 근무 운영 | 재택근무 정책, 협업 도구, 생산성 관리 |
| risk-register | 리스크 레지스터 | 위험 식별, 영향 평가, 대응 계획 |

→ 하네스 파일: `references/harness/{id}.md`

## 실행 규칙

1. 사용자 요청 수신 → 해당 하네스 판별
2. `references/harness/{id}.md` 로드 → 전략 가이드에 따라 실행
3. `--deepthink` 또는 복잡 조직 설계 → `mcp__sequential-thinking__sequentialthinking` 호출
4. 결과물 생성 후 사용자 검토 요청

※ 이 스킬은 전략 가이드 전용이며, 실행 스크립트는 포함하지 않는다.
