---
name: moai-education-research
description: "교육 & 연구 — 강의 빌더, 시험 대비, 논문 어드바이저, 학술 논문, 리서치 어시스턴트, 어학 튜터, 역량 모델러 하네스. 강의, 커리큘럼, 온라인 교육, 시험, 자격증, 수능, 논문, 학술, 리서치, 어학, 외국어, 역량 모델."
---

# 교육 & 연구 (④ education-research)

> MoAI-Cowork v0.2.0 | 7 하네스

## 하네스 (전략 가이드)

| ID | 한국명 | 설명 |
|----|--------|------|
| course-builder | 강의 빌더 | 커리큘럼 설계, 학습 목표, 온라인 강의 제작 |
| exam-prep | 시험 대비 | 시험 전략, 학습 계획, 기출 분석 |
| thesis-advisor | 논문 어드바이저 | 연구 설계, 문헌 검토, 논문 구조화 |
| academic-paper | 학술 논문 | 학술 논문 작성, 인용, 피어 리뷰 대비 |
| research-assistant | 리서치 어시스턴트 | 데이터 수집, 분석, 보고서 작성 |
| language-tutor | 어학 튜터 | 외국어 학습 전략, 회화 연습, 문법 |
| competency-modeler | 역량 모델러 | 직무 역량 분석, 스킬 갭 파악, 성장 경로 |

→ 하네스 파일: `references/harness/{id}.md`

## 실행 규칙

1. 사용자 요청 수신 → 해당 하네스 판별
2. `references/harness/{id}.md` 로드 → 전략 가이드에 따라 실행
3. `--deepthink` 또는 복잡 학술 분석 → `mcp__sequential-thinking__sequentialthinking` 호출
4. 결과물 생성 후 사용자 검토 요청

※ 이 스킬은 전략 가이드 전용이며, 실행 스크립트는 포함하지 않는다.
