<div align="center">

# 🗿 MoAI-Cowork

**84개 도메인 하네스 + 10개 한국 특화 실행 스킬 — 당신만의 AI 전문가**

[![Version](https://img.shields.io/badge/version-0.2.0-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-84-orange)]()
[![Skills](https://img.shields.io/badge/skills-11-purple)]()

</div>

---

## MoAI란?

**MoAI-Cowork**는 Claude Cowork용 플러그인으로, 84개 도메인 전문가 하네스와 10개 한국 특화 실행 스킬을 제공하는 자기학습 AI 비서 시스템입니다.

하네스(Harness)란 특정 도메인의 전문 지식, 워크플로우, 산출물 형식을 하나로 묶은 AI 전문가 모듈입니다. 하네스를 설치하면 MoAI가 해당 도메인의 전문가로 전환되어 체계적인 결과물을 제공합니다.

**v0.2.0 핵심 특징:**

- **11개 스킬** — moai(코어) + 10개 카테고리 도메인 스킬
- **84개 하네스** — 콘텐츠, 마케팅, 비즈니스, 교육, 법률, 라이프스타일, 문서, 운영, 재무, 제품/혁신
- **10개 한국 특화 실행 스킬** — PPT, 한글(HWPX), 카드뉴스, Remotion 영상, 랜딩 페이지, SNS, AI 이미지, 상세페이지, 계약서 검토, 세무
- **4계층 자기학습 아키텍처** — 사용할수록 사용자에게 맞춰 진화
- **글로벌 프로필** — 개인 + 회사 정보를 세션 간 공유
- **자연어 라우팅** — 스킬명을 외울 필요 없이 자연어로 요청
- **딥씽킹 모드** — 복잡 작업 시 sequential-thinking MCP 활용

---

## 빠른 시작

### 1. 플러그인 설치
Cowork에서 `moai-cowork.plugin` 파일을 설치합니다.

### 2. 하네스 설치
```
/moai init
```
대화형 설문을 통해 맞춤형 CLAUDE.md가 생성됩니다.

### 3. 사용
자연어로 요청하면 MoAI가 자동으로 적합한 스킬과 하네스를 트리거합니다.
```
"유튜브 영상 기획해줘"     → content-creative 스킬 → youtube-production 하네스
"계약서 검토해줘"          → legal-compliance 스킬 → contract 실행 모듈
"PPT 만들어줘"            → communication-docs 스킬 → ppt 실행 모듈
```

---

## 커맨드

| 커맨드 | 설명 |
|--------|------|
| `/moai init` | 하네스 설치 → CLAUDE.md 맞춤 생성 |
| `/moai init --harness {id}` | 특정 하네스 직접 설치 |
| `/moai catalog` | 84개 하네스 카탈로그 조회 |
| `/moai status` | 설치된 하네스 + 진화 상태 |
| `/moai evolve` | 자기 개선 사이클 실행 |
| `/moai profile` | 글로벌 프로필 조회/수정 |
| `/moai doctor` | 환경 진단 |
| `/moai help` | 사용 가능한 커맨드 표시 |

---

## 스킬 구조 (11개)

| # | 스킬 | 하네스 | 실행 모듈 | 설명 |
|---|------|--------|----------|------|
| ★ | moai | — | — | 코어 (프로젝트 관리 + 라우터) |
| ① | content-creative | 8 | 3 | 콘텐츠 & 크리에이티브 |
| ② | business-strategy | 10 | — | 비즈니스 & 전략 |
| ③ | marketing-growth | 10 | 3 | 마케팅 & 성장 |
| ④ | education-research | 7 | — | 교육 & 연구 |
| ⑤ | legal-compliance | 7 | 1 | 법률 & 컴플라이언스 |
| ⑥ | lifestyle | 10 | — | 라이프스타일 |
| ⑦ | communication-docs | 8 | 2 | 커뮤니케이션 & 문서 |
| ⑧ | operations-hr | 8 | — | 운영 & HR |
| ⑨ | finance-trade | 7 | 1 | 재무 & 무역 |
| ⑩ | product-innovation | 9 | — | 제품 & 혁신 |

---

## 한국 특화 실행 스킬 (10개)

| # | 실행 모듈 | 배치 스킬 | 기능 |
|---|----------|----------|------|
| 1 | Remotion 영상 | content-creative | React 기반 프로그래매틱 영상 생성 |
| 2 | 랜딩 페이지 | content-creative | 고전환율 원페이지 랜딩 설계 |
| 3 | 인스타 카드뉴스 | content-creative | AI 이미지 기반 캐러셀 카드뉴스 |
| 4 | SNS 콘텐츠 | marketing-growth | 네이버/인스타/카카오 최적화 |
| 5 | AI 이미지 생성 | marketing-growth | Imagen API 기반 이미지 생성 |
| 6 | 이커머스 상세페이지 | marketing-growth | 쿠팡/스마트스토어 상세페이지 |
| 7 | 계약서 검토 | legal-compliance | 한국 민법/상법 기반 리스크 분석 |
| 8 | PPT 디자인 | communication-docs | Pretendard+명조 한국형 디자인 |
| 9 | 한글 문서 (HWPX) | communication-docs | python-hwpx 기반 한글 생성 |
| 10 | 세무 도우미 | finance-trade | 3.3%/부가세/종소세/홈택스 |

---

## 아키텍처 (4계층)

```
계층 0: auto-memory (글로벌) — 사용자 프로필, 하네스 이력
    ↓
계층 1: 플러그인 (read-only) — 11개 스킬 + 하네스 + 실행 코드
    ↓
계층 2: .claude/CLAUDE.md (자동 로딩) — 맞춤형 페르소나 + 라우팅
    ↓
계층 3: .moai/ (R/W) — 도메인 맥락, 진화 데이터
```

---

## 버전 이력

| 버전 | 날짜 | 변경 내용 |
|------|------|----------|
| v0.2.0 | 2026-04-08 | 한국 전용 재설계: 11 스킬, 84 하네스, 10 실행 스킬, 4계층, sequential-thinking |
| v0.1.3 | 2026-04-08 | 풀스펙 하네스 병합 + EN 단일 소스 |
| v0.1.2 | 2026-04-08 | verification-protocol, 에이전트 디렉터 UX |
| v0.1.0 | 2026-04-04 | 초기 릴리스: 글로벌 100 하네스, 17개 언어 |

---

## 라이선스

MIT License — [LICENSE](LICENSE) 참조

---

<div align="center">

**모두의AI (MoAI)** | 제작: GOOS

</div>
