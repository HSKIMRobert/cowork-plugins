# moai-cost — 원가 분석

`moai-cost`는 협력업체 견적서, 내부 BOM, 생산공장 원가, 전체 프로젝트 원가를 2025/2026 기준으로 비교 분석하는 플러그인입니다.

## Skills

| 스킬 | 한글명 | 기능 |
|------|--------|------|
| [supplier-quote-cost-analysis](./skills/supplier-quote-cost-analysis/) | 협력업체 견적 원가 분석 | 견적서 세부 내역을 재료비·가공비·노무비·경비·물류비·관리비·이윤으로 분해하고 target price gap을 분석 |
| [bom-cost-rollup](./skills/bom-cost-rollup/) | BOM 원가 roll-up | 제품별 BOM 원가를 계산하고 2025/2026 단가·수량·BOM 변경 효과를 분해 |
| [factory-cost-comparison](./skills/factory-cost-comparison/) | 공장 원가 비교 | 제품별·공장별 제조원가를 2025/2026 기준으로 비교하고 원가 경쟁력 순위를 산출 |
| [project-cost-variance](./skills/project-cost-variance/) | 프로젝트 원가 차이 분석 | 전체 프로젝트 원가를 제품·공장·협력업체·BOM 영향으로 통합 비교 |

## Recommended Flow

```text
supplier-quote-cost-analysis → bom-cost-rollup → factory-cost-comparison → project-cost-variance
```

## Example Prompts

```text
협력업체 견적서 원가 분석해줘. 업체별 단가, target price gap, 이상치, 협상 우선순위를 뽑아줘.
```

```text
프로젝트 전체 원가를 2025/2026년 기준으로 비교해줘. 제품별·공장별·협력업체별 증감 기여도와 원가 bridge를 만들어줘.
```
