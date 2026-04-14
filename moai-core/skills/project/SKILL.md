---
name: project
description: |
  Claude Cowork 프로젝트 초기화와 작업 지침(CLAUDE.md) 자동 생성 스킬.
  사용자의 업무 워크플로우를 인터뷰하고, 설치된 moai-* 플러그인을 기반으로
  **스킬 체이닝 워크플로우**가 포함된 CLAUDE.md를 생성합니다.

  다음과 같은 요청 시 반드시 이 스킬을 사용하세요:
  - "/project init", "/project catalog", "/project status", "/project apikey"
  - "새 프로젝트 시작", "Cowork 프로젝트 초기 설정", "CLAUDE.md 만들어줘"
  - "이 프로젝트에 어울리는 워크플로우 설계해줘"
  - "도메인 라우팅 설정", "플러그인 연결", "API 키 등록"
  - 사업계획, 마케팅, 계약서, 세무, 인사, 콘텐츠, 운영, PM 등
    자연어 요청이 들어왔을 때 적합한 도메인 플러그인으로 라우팅해야 할 때

  이 스킬은 **이름·회사 같은 글로벌 프로필을 재질문하지 않습니다.**
  프로젝트마다 "이번에 뭘 할 건지, 어떻게 처리하고 싶은지"만 인터뷰해서
  스킬 체인(예: strategy-planner → docx-generator → ai-slop-reviewer)을 설계하고
  사용자 확인을 받은 뒤 CLAUDE.md를 최적화합니다.
user-invocable: true
---

# project — Cowork 프로젝트 초기화 & 스킬 체이닝 워크플로우 설계

사용자는 이 프로젝트에서 무엇을 할지 말해주면 됩니다. 나머지(플러그인 선택, 스킬 체인 설계, 산출물 규칙, 검수 파이프라인)는 MoAI가 설계·정리합니다.

## 커맨드

| 커맨드 | 동작 |
|--------|------|
| `/project init` | **워크플로우 인터뷰 → 스킬 체인 설계 → 확인 → CLAUDE.md 생성** |
| `/project catalog` | 설치된 플러그인 + 스킬 목록 표시 |
| `/project status` | 현재 프로젝트 설정(CLAUDE.md, 플러그인, API 키) 상태 확인 |
| `/project apikey` | API 키 조회/추가/변경 |
| `/project feedback` | 버그/기능 요청 → GitHub Issues 자동 등록 (`feedback` 스킬) |

## /project init — 새 워크플로우 (v1.3)

**글로벌 프로필 시스템을 제거**했습니다. 매번 이름·회사·역할을 되묻지 않습니다. 대신 이 프로젝트의 **업무 맥락**만 수집하고, 그에 맞는 **스킬 체인**을 설계합니다.

```
1. [Interview] 3단계 소크라테스 인터뷰 (최대 3질문)
     ① 이 프로젝트에서 어떤 일을 하시나요?
     ② 주로 만드는 산출물은 무엇인가요? (블로그/사업계획서/계약서/…)
     ③ 특별히 지키고 싶은 톤·형식·제약이 있나요?

2. [Detect] 설치된 moai-* 플러그인 자동 감지 + 인터뷰 답변 기반 매칭

3. [Chain Design] 산출물별 스킬 체인 설계 (핵심)
     - 각 산출물마다 [기획 → 생성 → 포맷 변환 → AI 슬롭 검수] 파이프라인 정의
     - 체인의 각 단계를 실존하는 moai 스킬로 매핑
     - 예:
       • 사업계획서: strategy-planner → docx-generator → ai-slop-reviewer
       • 블로그 발행: blog → ai-slop-reviewer → (선택) 이미지는 nano-banana
       • 제품 랜딩: copywriting → landing-page → ai-slop-reviewer
       • IR 피칭덱: investor-relations → pptx-designer → ai-slop-reviewer
       • 법무 NDA: nda-triage → docx-generator → ai-slop-reviewer
       • 카드뉴스: card-news → nano-banana → ai-slop-reviewer
     - 텍스트 산출물 체인은 **항상 ai-slop-reviewer로 종료**
     - 비텍스트 산출물(차트/데이터/숫자)은 ai-slop 단계 생략

4. [Confirm] AskUserQuestion으로 체인 설계 승인 (수정 / 승인 / 취소)

5. [Generate] 프로젝트 루트에 CLAUDE.md 생성 (≤ 200라인)
     - references/templates/CLAUDE.md.tmpl 기반
     - Interview 결과를 페르소나·워크플로우 섹션에 주입
     - 승인된 스킬 체인을 "워크플로우" 섹션에 명시
     - office/web/ai-slop HARD 규칙 고정 포함

6. [APIKey] 선택된 플러그인이 요구하는 API 키만 선택적으로 등록 (필요 시)

7. [First Run] 첫 작업 예시 3개를 스킬 체인 기반으로 동적 생성 후 안내
```

상세: `references/core/init-protocol.md`

### 인터뷰 질문 설계 원칙

- **이름/회사/역할을 묻지 않는다.** 필요하면 사용자가 CLAUDE.md를 직접 편집한다.
- **프로필 저장 파일(`moai-profile.md`)을 생성하지 않는다.**
- 모든 사용자 정보는 **이 프로젝트의 CLAUDE.md 한 곳에만** 기록된다.
- Interview는 **이번 프로젝트에서 뭘 어떻게 할지**에만 집중한다.

## 스킬 체이닝 설계 원칙

CLAUDE.md는 단순한 라우팅 테이블이 아니라 **실행 가능한 파이프라인 스펙**을 포함해야 합니다.

### 체인 구성 요소

1. **기획·분석 스킬** — strategy-planner, market-analyst, ux-researcher 등
2. **생성·제작 스킬** — blog, copywriting, card-news, spec-writer 등
3. **포맷 변환 스킬** — docx-generator, pptx-designer, xlsx-creator, hwpx-writer, landing-page
4. **미디어 스킬** (선택) — nano-banana(이미지), ideogram, kling(영상), elevenlabs(음성)
5. **후처리 스킬** — `ai-slop-reviewer` (텍스트 산출물 체인의 **필수 마지막 단계**)

### 체인 표기 규약 (CLAUDE.md에 기록될 형식)

```
[산출물명]
  요청 예시: "..."
  체인: skill-A → skill-B → skill-C → ai-slop-reviewer
  입력/출력: A가 받는 입력과 C가 내는 출력 형식을 한 줄로 기록
  제외 조건: 스킵해야 할 상황 명시 (예: 데이터 시각화는 ai-slop 생략)
```

### 체인 실행 계약

- 각 단계 스킬은 다음 스킬이 소비 가능한 **구조화된 출력**을 반환한다.
- 사용자 확인 없이 체인 전체를 한 번에 실행하되, **각 단계 완료 시 요약을 보고**한다.
- 마지막 단계가 `ai-slop-reviewer`인 경우, **진단 → 수정 → 주요 변경사항** 3블록을 함께 출력한다.

## CLAUDE.md에 항상 포함되는 HARD 규칙

`/project init`이 생성하는 CLAUDE.md에는 다음 규칙이 **반드시** 포함됩니다:

### 1. 문서·콘텐츠 생성 우선순위 (HARD)

Claude 기본 artifacts·도구보다 moai 스킬을 우선 사용한다.

| 산출물 | 사용 스킬 |
|---|---|
| DOCX / Word 문서 | `moai-office:docx-generator` |
| PPTX / 발표자료 | `moai-office:pptx-designer` |
| XLSX / Excel | `moai-office:xlsx-creator` |
| HWPX / 한글 | `moai-office:hwpx-writer` |
| HTML / 웹페이지 / 랜딩 | `moai-content:landing-page` |
| 블로그 포스트 | `moai-content:blog` |
| 카드뉴스 | `moai-content:card-news` |
| 뉴스레터 | `moai-content:newsletter` |
| SNS 콘텐츠 | `moai-content:social-media` |
| 카피·광고 문구 | `moai-content:copywriting` |
| 상세페이지 | `moai-content:product-detail` |
| 영상·이미지·음성 | `moai-media:*` |

해당 스킬이 설치되어 있으면 기본 artifacts로 직접 생성하지 않는다.

### 2. AI 슬롭 후처리 (HARD)

**모든 텍스트 산출물 워크플로우(=스킬 체인)의 마지막 단계**에 `ai-slop-reviewer` 스킬을 호출해 AI 패턴을 제거하고 인간적인 톤으로 검수한다.

- 대상: 블로그, 뉴스레터, 카피, 사업계획서, 계약서·공문 초안, 제안서, 보고서, 이메일, 랜딩 카피, 사업보고, 특허 초안 등 **모든 텍스트 산출물**
- 제외: 코드, JSON/CSV 데이터, 차트·표, 단순 조회 응답, 숫자 리포트
- 산출 형식: 진단 요약 → 수정 텍스트 → 주요 변경사항

### 3. 실행 플로우 (Interview → Plan → Confirm → Execute)

멀티스텝 작업은 반드시 다음 4단계를 따른다:

1. [Interview] 소크라테스 인터뷰로 빠진 맥락 수집 (최대 3질문)
2. [Summary] 수집한 맥락을 구조화하여 확인 요약
3. [Plan+Confirm] 스킬 체인 실행 계획 제시 → AskUserQuestion으로 최종 승인
4. [Execute] 체인 순차 실행 → 품질 검증 → **ai-slop-reviewer 검수** → 전달

스킵 조건: 단순 조회, 이미 상세 지시, "빠르게" 명시, 후속 요청

## 라우팅 (자연어 → 플러그인)

| 키워드 | 플러그인 |
|--------|---------|
| 사업계획, 스타트업, 투자, IR, 시장조사 | moai-business |
| 마케팅, SEO, SNS, 브랜드, 캠페인 | moai-marketing |
| 계약서, 컴플라이언스, 법률, NDA | moai-legal |
| 세금, 부가세, 홈택스, K-IFRS | moai-finance |
| 채용, 면접, 근로계약, 4대보험 | moai-hr |
| 카드뉴스, 블로그, 뉴스레터, 카피, 랜딩 | moai-content |
| 운영, 결재, 조달, SOP | moai-operations |
| 강의, 커리큘럼, 시험 | moai-education |
| 여행, 건강, 웨딩, 이벤트 | moai-lifestyle |
| PM, 로드맵, UX, 스프린트 | moai-product |
| 고객지원, CS, 티켓 | moai-support |
| PPT, 한글, Word, Excel | moai-office |
| 이력서, 면접, 포트폴리오 | moai-career |
| 데이터, CSV, 차트, 통계, 공공데이터 | moai-data |
| 논문, 특허, KIPRIS, 연구비, 출원 | moai-research |
| 이미지, 영상, 음성, AI 생성 미디어 | moai-media |

2개+ 플러그인 매칭 시 AskUserQuestion으로 선택 요청.
상세 키워드 매핑: `references/core/router.md`

## 저장 위치

- **프로젝트 작업 지침**: `./CLAUDE.md` (≤ 200라인)
- **프로젝트 설정**: `./.moai/config.json`
- **API 키**: `./.moai/credentials.env` (프로젝트 격리)
- **~~글로벌 프로필~~**: v1.3.0에서 **제거됨**. 이름·역할은 CLAUDE.md에 기록.

## 딥씽킹

`--deepthink`, `ultrathink` 키워드 포함 시 단계별 심층 분석 수행.
자동 트리거: 법률/세무 판단, 2개+ 플러그인 복합 작업, 전략적 의사결정.

## 사용하지 말아야 할 때

- 특정 도메인 작업이 명확한 경우 → 해당 플러그인 직접 호출
- 단순 질문이나 일반 대화 → 별도 스킬 없이 직접 대화
- 코드 개발 → Claude Code 기본 기능 활용
