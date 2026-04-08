---
name: moai-business-strategy
description: "비즈니스 & 전략 — 스타트업 런처, 시장 조사, 재무 모델, 가격 전략, 투자자 보고서, 경쟁 분석, 비즈니스 모델 캔버스, 시장 진출, 시나리오 플래닝, 전략 프레임워크 하네스. 사업계획서, 창업, 스타트업, 시장조사, TAM, 투자, IR, 피칭, 재무모델, SWOT, 경쟁분석."
---

# 비즈니스 & 전략 (② business-strategy)

> MoAI-Cowork v0.2.0 | 10 하네스

## 하네스 (전략 가이드)

| ID | 한국명 | 설명 |
|----|--------|------|
| startup-launcher | 스타트업 런처 | 사업계획서, 린 캔버스, MVP 전략 |
| market-research | 시장 조사 | TAM/SAM/SOM, 시장 트렌드, 고객 세그멘테이션 |
| financial-modeler | 재무 모델 | 매출 예측, 손익분석, 현금흐름 |
| pricing-strategy | 가격 전략 | 가격 모델, 탄력성 분석, 번들링 |
| investor-report | 투자자 보고서 | IR 자료, 피칭 덱, 투자 유치 전략 |
| competitive-analysis | 경쟁 분석 | 경쟁사 매핑, 차별화 전략, 포지셔닝 |
| business-model-canvas | 비즈니스 모델 캔버스 | 9블록 캔버스, 가치 제안 설계 |
| market-entry-strategy | 신시장 진출 전략 | 해외 진출, 시장 진입 장벽, 파트너 전략 |
| scenario-planner | 시나리오 플래닝 | 미래 시나리오 분석, 불확실성 대응 |
| strategy-framework | 전략 프레임워크 | SWOT, Porter's 5F, Blue Ocean, OKR |

→ 하네스 파일: `references/harness/{id}.md`

## 실행 규칙

1. 사용자 요청 수신 → 해당 하네스 판별
2. `references/harness/{id}.md` 로드 → 전략 가이드에 따라 실행
3. `--deepthink` 또는 복잡 전략 판단 → `mcp__sequential-thinking__sequentialthinking` 호출
4. 결과물 생성 후 사용자 검토 요청

※ 이 스킬은 전략 가이드 전용이며, 실행 스크립트는 포함하지 않는다.
