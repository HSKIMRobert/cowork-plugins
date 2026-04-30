---
title: "moai-cost — 원가 분석"
weight: 15
description: "협력업체 견적서, BOM, 생산공장 원가, 전체 프로젝트 원가를 2025/2026 기준으로 비교 분석하는 플러그인입니다."
tags: ["moai-cost"]
---

# moai-cost

`moai-cost`는 협력업체 견적서, 내부 BOM, 생산공장 원가, 전체 프로젝트 원가를 2025/2026 기준으로 비교 분석하는 원가 분석 플러그인입니다.

## 설치

1. Cowork에서 `modu-ai/cowork-plugins` 마켓플레이스를 추가합니다.
2. `moai-core` 설치 후 `moai-cost` 옆의 **+** 버튼을 눌러 설치합니다.
3. 원가 자료 파일을 업로드하고 자연어로 분석을 요청합니다.

## Skills

| 스킬 | 목적 | 대표 입력 |
|---|---|---|
| `supplier-quote-cost-analysis` | 협력업체 견적서 세부 원가 분석 | 견적서, target price, 업체별 단가 |
| `bom-cost-rollup` | 내부 BOM 가격 roll-up | BOM, 2025/2026 단가표, 소요량 |
| `factory-cost-comparison` | 제품별·공장별 제조원가 비교 | 공장 원가자료, 생산량, 불량률 |
| `project-cost-variance` | 전체 프로젝트 원가 2025/2026 비교 | 프로젝트 원가, BOM 분석, 견적 분석, 공장 분석 |

## 추천 흐름

```mermaid
flowchart LR
  A[협력업체 견적 분석] --> B[BOM 원가 Roll-up]
  B --> C[공장별 제품 원가 비교]
  C --> D[프로젝트 전체 원가 Bridge]
```

## 사용 예시

```text
협력업체 견적서 원가 분석해줘. 업체별 단가, target price gap, 이상치, 협상 우선순위를 뽑아줘.
```

```text
프로젝트 전체 원가를 2025/2026년 기준으로 비교해줘. 제품별·공장별·협력업체별 증감 기여도와 원가 bridge를 만들어줘.
```

## 연계 플러그인

- [`moai-data`](../moai-data/) — CSV/Excel 프로파일링, 데이터 품질 검사
- [`moai-finance`](../moai-finance/) — 예산 대비 실적, 재무 KPI, 수익성 분석
- [`moai-operations`](../moai-operations/) — 벤더 평가, 구매/조달 리스크 관리

## Sources

- [modu-ai/cowork-plugins](https://github.com/modu-ai/cowork-plugins)
- [moai-cost 디렉터리](https://github.com/modu-ai/cowork-plugins/tree/main/moai-cost)
