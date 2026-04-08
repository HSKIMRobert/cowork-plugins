---
name: moai-lifestyle
description: "라이프스타일 — 여행 플래너, 식단 플래너, 운동 프로그램, 개인 재무, 웨딩 플래너, 이벤트 기획, 부동산 분석, 육아 가이드, 시니어 케어, 사이드 프로젝트 런처 하네스. 여행, 맛집, 식단, 다이어트, 운동, 피트니스, 결혼, 웨딩, 이벤트, 행사, 부동산, 육아, 사이드 프로젝트, 부업."
---

# 라이프스타일 (⑥ lifestyle)

> MoAI-Cowork v0.2.0 | 10 하네스

## 하네스 (전략 가이드)

| ID | 한국명 | 설명 |
|----|--------|------|
| travel-planner | 여행 플래너 | 여행 일정, 맛집, 숙소, 예산 관리 |
| meal-planner | 식단 플래너 | 영양 균형, 식단 구성, 장보기 리스트 |
| fitness-program | 운동 프로그램 | 운동 계획, 루틴 설계, 진도 관리 |
| personal-finance | 개인 재무 | 가계부, 저축 전략, 투자 기초 |
| wedding-planner | 웨딩 플래너 | 결혼 준비, 스드메, 예산, 일정 관리 |
| event-organizer | 이벤트 기획 | 행사 기획, 세미나, 워크샵, 컨퍼런스 |
| real-estate-analyst | 부동산 분석 | 매매/전세 분석, 입지 평가, 수익률 |
| parenting-guide | 육아 가이드 | 아이 발달, 교육 전략, 학교 준비 |
| elderly-care-planning | 시니어 케어 | 노인 돌봄 계획, 복지 서비스, 건강 관리 |
| side-project-launcher | 사이드 프로젝트 런처 | 부업 아이디어, 수익화 전략, 시간 관리 |

→ 하네스 파일: `references/harness/{id}.md`

## 실행 규칙

1. 사용자 요청 수신 → 해당 하네스 판별
2. `references/harness/{id}.md` 로드 → 전략 가이드에 따라 실행
3. `--deepthink` 또는 복잡 의사결정 → `mcp__sequential-thinking__sequentialthinking` 호출
4. 결과물 생성 후 사용자 검토 요청

※ 이 스킬은 전략 가이드 전용이며, 실행 스크립트는 포함하지 않는다.
