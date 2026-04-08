---
name: moai-product-innovation
description: "제품 & 혁신 — 프로덕트 매니저, 프로젝트 트래커, AI 전략, 지속가능성 감사, 다양성 & 포용, 정부 지원금 기획, 파트너십 개발, UX 리서치, 사용자 피드백 분석 하네스. PM, 로드맵, 기능명세, AI전략, 디지털전환, UX, 사용자 리서치, 정부 지원금, R&D, 파트너십, 제휴."
---

# 제품 & 혁신 (⑩ product-innovation)

> MoAI-Cowork v0.2.0 | 9 하네스

## 하네스 (전략 가이드)

| ID | 한국명 | 설명 |
|----|--------|------|
| product-manager | 프로덕트 매니저 | PRD, 기능 명세, 우선순위 결정, 로드맵 |
| project-tracker | 프로젝트 트래커 | 프로젝트 일정, 마일스톤, 리소스 관리 |
| ai-strategy | AI 전략 | AI/ML 도입 전략, 디지털 전환 로드맵 |
| sustainability-audit | 지속가능성 감사 | 환경 영향 평가, 지속가능성 지표 |
| diversity-inclusion | 다양성 & 포용 | DEI 전략, 포용적 조직 문화 설계 |
| gov-funding-plan | 정부 지원금 기획 | R&D 과제, SBIR/STTR, 정부 사업 신청 |
| partnership-development | 파트너십 개발 | 전략적 제휴, MOU, 공동사업 기획 |
| ux-research | UX 리서치 | 사용자 인터뷰, 유저빌리티 테스트, 페르소나 |
| user-feedback-analysis | 사용자 피드백 분석 | VOC 분석, NPS, 제품 개선 인사이트 |

→ 하네스 파일: `references/harness/{id}.md`

## 실행 규칙

1. 사용자 요청 수신 → 해당 하네스 판별
2. `references/harness/{id}.md` 로드 → 전략 가이드에 따라 실행
3. `--deepthink` 또는 복잡 전략 판단 → `mcp__sequential-thinking__sequentialthinking` 호출
4. 결과물 생성 후 사용자 검토 요청

※ 이 스킬은 전략 가이드 전용이며, 실행 스크립트는 포함하지 않는다.
