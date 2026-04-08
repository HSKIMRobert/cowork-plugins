---
name: moai-marketing-growth
description: "마케팅 & 성장 — 브랜드 아이덴티티, CRM, 고객 여정, 그로스 해킹, 인플루언서, 퍼스널 브랜딩, A/B 테스트, 영업 지원 하네스 + SNS 콘텐츠, AI 이미지 생성(나노바나나/Imagen), 이커머스 상세페이지 실행. 마케팅, 브랜딩, SNS, 인스타, 네이버, 카카오, 이미지 생성, 상세페이지, 쿠팡, 스마트스토어, 그로스해킹."
---

# 마케팅 & 성장 (③ marketing-growth)

> MoAI-Cowork v0.2.0 | 10 하네스 + 3 실행 모듈

## 하네스 (전략 가이드)

| ID | 한국명 | 설명 |
|----|--------|------|
| brand-identity | 브랜드 아이덴티티 | 브랜드 전략, 로고 컨셉, CI/BI 가이드 |
| brand-voice-guide | 브랜드 보이스 가이드 | 톤 & 매너, 메시지 프레임워크 |
| crm-strategy | CRM 전략 | 고객 관계 관리, 리텐션, LTV 최적화 |
| customer-journey-map | 고객 여정 맵 | 터치포인트 매핑, 경험 최적화 |
| growth-hacking | 그로스 해킹 | 성장 실험, 바이럴 루프, 리퍼럴 |
| influencer-strategy | 인플루언서 전략 | 인플루언서 선정, 협찬 전략, ROI 측정 |
| content-repurposer | 콘텐츠 재활용 | 원 콘텐츠 → 다채널 변환, 리퍼포징 |
| personal-branding | 퍼스널 브랜딩 | 개인 브랜드 구축, 온라인 프레즌스 |
| ab-testing | A/B 테스트 설계 | 실험 설계, 통계적 유의성, 결과 분석 |
| sales-enablement | 영업 지원 | 세일즈 콘텐츠, 영업 프로세스 최적화 |

→ 하네스 파일: `references/harness/{id}.md`

## 실행 모듈 (코드 생성 가능)

### SNS 콘텐츠 제작
네이버 블로그, 인스타그램, 카카오 채널 등 한국 SNS 최적화 콘텐츠.
- 가이드: `references/sns-content/guide.md`

### AI 이미지 생성 (Nano Banana / Imagen)
Imagen API 기반 AI 이미지 생성.
- 가이드: `references/imagegen/guide.md`
- 스크립트: `${CLAUDE_SKILL_DIR}/scripts/imagegen/generate_image.py`

### 이커머스 상세페이지
쿠팡, 스마트스토어, 자사몰 상세페이지 제작.
- 가이드: `references/product-detail/guide.md`
- 참조: `references/product-detail/conversion-formulas.md`

## 실행 규칙

1. 사용자 요청 수신 → 하네스/실행 모듈 판별
2. 하네스 요청 → `references/harness/{id}.md` 로드 → 전략 가이드 실행
3. 실행 모듈 요청 → `references/{module}/guide.md` 로드 → 콘텐츠/이미지/코드 생성
4. `--deepthink` 또는 복잡 작업 → `mcp__sequential-thinking__sequentialthinking` 호출
5. 결과물 생성 후 사용자 검토 요청
