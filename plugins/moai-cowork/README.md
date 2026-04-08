<div align="center">

# 🗿 MoAI-Cowork

**100개 자기진화 도메인 하네스 — 당신만의 AI 전문가**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [English](README-en.md) | [日本語](README-ja.md) | [Español](README-es.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## MoAI란?

**MoAI-Cowork**는 Claude Cowork용 플러그인으로, 100개 도메인 전문가 하네스를 제공하는 자기학습 AI 비서 시스템입니다.

하네스(Harness)란 특정 도메인의 전문 지식, 워크플로우, 산출물 형식, 맥락 수집 프로토콜을 하나로 묶은 AI 전문가 모듈입니다. 하네스를 설치하면 MoAI가 해당 도메인의 전문가로 전환되어 체계적인 결과물을 제공합니다.

**핵심 특징:**

- 10개 카테고리 × 100개 하네스 — 콘텐츠, 마케팅, 비즈니스, 교육, 법률, 라이프스타일, 커뮤니케이션, 운영, 재무, 제품/혁신
- 5계층 자기학습 아키텍처 — 사용할수록 사용자에게 맞춰 진화
- 글로벌 프로필 — 개인 + 회사 정보를 세션 간 공유, 매번 재입력 불필요
- 17개 언어 지원 — EN 단일 소스 + 런타임 현지화
- 전세계 로케일 지원 — 근무 국가 입력 시 웹검색으로 세법, 노동법, 데이터보호법, 비즈니스 관행 자동 수집

---

## 설치 방법

### 방법 1: Claude Cowork 마켓플레이스에서 설치 (권장)

1. **Claude Desktop** 앱을 실행합니다
2. 좌측 하단의 **Cowork** 모드로 진입합니다
3. 채팅 입력창 옆의 **플러그인(🧩)** 아이콘을 클릭합니다
4. **마켓플레이스 탐색** 또는 검색창에 `moai-cowork`를 검색합니다
5. **MoAI-Cowork** 플러그인을 찾아 **설치** 버튼을 클릭합니다
6. 설치 완료 후, 채팅에서 `/moai init`을 입력하여 초기 설정을 시작합니다

### 방법 2: K-Harness 마켓플레이스에서 설치

K-Harness는 MoAI-Cowork가 포함된 마켓플레이스입니다.

```
# 1단계: 마켓플레이스 추가
/plugin marketplace add modu-ai/k-harness

# 2단계: MoAI-Cowork 플러그인 설치
/plugin install moai-cowork@k-harness
```

### 방법 3: GitHub에서 직접 설치

```
# 리포지토리 클론
git clone https://github.com/modu-ai/k-harness.git

# 플러그인 디렉토리로 이동
cd k-harness/plugins/moai-cowork

# Claude Desktop에서 수동 로딩
# Cowork 모드 → 플러그인(🧩) → "파일에서 설치" → moai-cowork 폴더 선택
```

### 방법 4: ZIP 파일로 수동 설치

1. [GitHub Releases](https://github.com/modu-ai/k-harness/releases) 페이지에서 최신 `moai-cowork-v0.1.3.zip` 다운로드
2. Claude Desktop → Cowork 모드 진입
3. 플러그인(🧩) 아이콘 → **파일에서 설치** 클릭
4. 다운로드한 ZIP 파일을 선택

---

## 업데이트 방법

### 마켓플레이스로 설치한 경우

```
# K-Harness 마켓플레이스 업데이트
/plugin marketplace update k-harness

# 또는 Cowork UI에서
# 플러그인(🧩) → MoAI-Cowork → "업데이트" 버튼 클릭
```

### GitHub에서 직접 설치한 경우

```
cd k-harness
git pull origin main
```

### ZIP으로 설치한 경우

1. 기존 플러그인을 제거합니다: 플러그인(🧩) → MoAI-Cowork → **제거**
2. 최신 ZIP 파일을 다운로드합니다
3. 방법 4의 수동 설치 과정을 반복합니다

### 버전 확인

채팅에서 `/moai status`를 입력하면 현재 설치된 버전을 확인할 수 있습니다.

---

## 문제 해결 (Troubleshooting)

### 플러그인이 인식되지 않는 경우

1. Claude Desktop을 완전히 종료 후 재실행합니다
2. Cowork 모드에서 플러그인(🧩) 목록에 MoAI-Cowork가 있는지 확인합니다
3. 없다면 재설치를 시도합니다

### `/moai init` 실행 시 오류

1. `/moai doctor`를 입력하여 환경을 진단합니다
2. 글로벌 프로필이 손상된 경우 `/moai profile --reset`으로 초기화합니다

### 하네스가 로딩되지 않는 경우

1. 프로젝트 폴더에 `.moai/config.json`이 존재하는지 확인합니다
2. 없다면 `/moai init`으로 다시 초기화합니다

### 현지화 데이터가 수집되지 않는 경우

- 한국: 내장 데이터 사용 (웹검색 불필요)
- 기타 국가: 인터넷 연결과 웹검색 도구가 필요합니다

---

## 빠른 시작

### 1단계: 초기화

```
/moai init
```

MoAI가 대화형 인터뷰를 통해 사용자 프로필(이름, 역할, 회사, 로케일)을 수집합니다.

### 2단계: 하네스 카탈로그 조회

```
/moai catalog
```

10개 카테고리의 100개 하네스 목록을 확인할 수 있습니다.

### 3단계: 자연어로 요청

```
시장 조사 해줘
```

MoAI가 자동으로 `market-research` 하네스를 감지하여 전문가 모드로 실행합니다.

---

## 100개 하네스 카탈로그

| # | 카테고리 | 하네스 수 | 대표 하네스 |
|---|---------|---------|-----------|
| 1 | 콘텐츠 & 크리에이티브 | 10 | copywriting, youtube-production, podcast-studio, book-publishing |
| 2 | 비즈니스 & 전략 | 10 | business-model-canvas, competitive-analysis, startup-launcher, pricing-strategy |
| 3 | 마케팅 & 성장 | 10 | brand-identity, growth-hacking, social-media-manager, influencer-strategy |
| 4 | 교육 & 연구 | 10 | course-builder, thesis-advisor, exam-prep, language-tutor |
| 5 | 법률 & 컴플라이언스 | 10 | contract-analyzer, compliance-checker, patent-drafter, privacy-engineer |
| 6 | 라이프스타일 | 10 | travel-planner, wedding-planner, meal-planner, fitness-program |
| 7 | 커뮤니케이션 & 문서 | 10 | presentation-designer, report-generator, technical-writer, proposal-writer |
| 8 | 운영 & HR | 10 | hiring-pipeline, onboarding-system, operations-manual, crisis-communication |
| 9 | 재무 & 무역 | 10 | accounting-tax, financial-modeler, import-export, invoice-mgmt |
| 10 | 제품 & 혁신 | 10 | product-manager, ai-strategy, ux-research, sales-enablement |

전체 100개 하네스 목록은 `/moai catalog`에서 확인하세요.

---

## 주요 커맨드

| 커맨드 | 설명 |
|--------|------|
| `/moai init` | 초기화 — 프로필 수집 및 하네스 설치 |
| `/moai catalog` | 100개 하네스 카탈로그 조회 |
| `/moai status` | 설치된 하네스 및 진화 상태 확인 |
| `/moai evolve` | 자기학습 진화 사이클 실행 |
| `/moai profile` | 글로벌 프로필 조회/수정 |
| `/moai doctor` | 환경 진단 |
| `/moai help` | 사용 가능한 커맨드 표시 |

---

## 아키텍처

```
Layer 0: auto-memory (글로벌) — 사용자 프로필, 하네스 이력
Layer 1: plugin (읽기전용) — 100개 Base 하네스 (en/ 단일 소스, 런타임 현지화)
Layer 2: .claude/CLAUDE.md + rules/ — 페르소나
Layer 3: .moai/ (읽기/쓰기) — 도메인 맥락, 진화 데이터
Layer 4: auto-memory 학습 — 세션 간 피드백 누적
```

---

## 라이선스

MIT License — 자유롭게 사용, 수정, 배포 가능

---

## GitHub

- **리포지토리**: [modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **이슈/건의**: [GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork: 당신만의 AI 전문가를 만나세요.**

*Version 0.1.3 | Last Updated: 2026-04-08*
