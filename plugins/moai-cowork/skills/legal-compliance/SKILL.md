---
name: moai-legal-compliance
description: "법률 & 컴플라이언스 — 컴플라이언스 체커, 감사 보고서, ESG 보고, 법률 리서치, 지적재산 포트폴리오, 규제 서류, 서비스 법률 문서 하네스 + 계약서 검토(한국 민법/상법 기반) 실행. 계약서, 법률, 컴플라이언스, 규제, 감사, ESG, 지적재산, 특허, 이용약관, 개인정보처리방침, 계약 검토, 위험 조항."
---

# 법률 & 컴플라이언스 (⑤ legal-compliance)

> MoAI-Cowork v0.2.0 | 7 하네스 + 1 실행 모듈

## 하네스 (전략 가이드)

| ID | 한국명 | 설명 |
|----|--------|------|
| compliance-checker | 컴플라이언스 체커 | 규제 준수 점검, 갭 분석, 시정 계획 |
| audit-report | 감사 보고서 | 내부 감사, 보고서 구성, 개선 권고 |
| esg-reporting | ESG 보고 | ESG 지표 수집, 보고서 프레임워크 |
| legal-research | 법률 리서치 | 판례 검색, 법률 해석, 쟁점 분석 |
| ip-portfolio | 지적재산 포트폴리오 | 특허/상표/저작권 관리, IP 전략 |
| regulatory-filing | 규제 서류 | 인허가 신청, 규제 대응 문서 |
| service-legal-docs | 서비스 법률 문서 | 이용약관, 개인정보처리방침, SLA |

→ 하네스 파일: `references/harness/{id}.md`

## 실행 모듈 (코드 생성 가능)

### 계약서 검토 (한국법 기반)
한국 민법/상법 기반 계약서 검토, 10대 리스크 패턴 분석.
- 가이드: `references/contract/guide.md`

## 실행 규칙

1. 사용자 요청 수신 → 하네스/실행 모듈 판별
2. 하네스 요청 → `references/harness/{id}.md` 로드 → 전략 가이드 실행
3. 계약서 검토 요청 → `references/contract/guide.md` 로드 → 한국법 기반 분석
4. **법률/규제 판단은 항상** `mcp__sequential-thinking__sequentialthinking` 호출
5. 결과물 생성 후 사용자 검토 요청

⚠️ 면책 고지: MoAI는 AI 어시스턴트이며 공인 법률 자문을 대체하지 않습니다. 중요한 법률 사안은 반드시 전문 법률가와 상담하세요.
