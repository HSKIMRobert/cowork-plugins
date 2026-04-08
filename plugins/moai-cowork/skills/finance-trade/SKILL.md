---
name: moai-finance-trade
description: "재무 & 무역 — 청구서 관리, 보조금 신청서, 수출입, 공급망, RFP 응답, 비영리 관리, 이커머스 런처 하네스 + 세무 도우미(한국 3.3%/홈택스) 실행. 세금, 부가세, 3.3%, 종소세, 홈택스, 청구서, 인보이스, 보조금, 수출입, 무역, 통관, 공급망, RFP, 입찰."
---

# 재무 & 무역 (⑨ finance-trade)

> MoAI-Cowork v0.2.0 | 7 하네스 + 1 실행 모듈

## 하네스 (전략 가이드)

| ID | 한국명 | 설명 |
|----|--------|------|
| invoice-mgmt | 청구서 관리 | 인보이스 작성, 수금 관리, 미수금 추적 |
| grant-writer | 보조금 신청서 | 정부 지원사업, 보조금 신청, 사업계획 |
| import-export | 수출입 | 무역 실무, 통관, HS 코드, 인코텀즈 |
| supply-chain | 공급망 관리 | SCM 최적화, 재고 관리, 물류 전략 |
| rfp-responder | RFP 응답 | 입찰 제안서, 기술 평가, 가격 전략 |
| nonprofit-management | 비영리 관리 | 비영리 운영, 기부금 관리, 보고 의무 |
| ecommerce-launcher | 이커머스 런처 | 온라인 쇼핑몰 개설, 운영, 마케팅 |

→ 하네스 파일: `references/harness/{id}.md`

## 실행 모듈 (코드 생성 가능)

### 세무 도우미 (한국 3.3%/홈택스)
한국 세법 기반 세무 상담. 3.3% 원천징수, 종합소득세, 부가가치세, 홈택스 안내.
- 가이드: `references/tax/guide.md`

## 실행 규칙

1. 사용자 요청 수신 → 하네스/실행 모듈 판별
2. 하네스 요청 → `references/harness/{id}.md` 로드 → 전략 가이드 실행
3. 세무 요청 → `references/tax/guide.md` 로드 → 한국 세법 기반 분석
4. **세무/재무 판단은 항상** `mcp__sequential-thinking__sequentialthinking` 호출
5. 결과물 생성 후 사용자 검토 요청

⚠️ 면책 고지: MoAI는 AI 어시스턴트이며 공인 세무/회계 자문을 대체하지 않습니다. 중요한 세무 사안은 반드시 세무사와 상담하세요.
