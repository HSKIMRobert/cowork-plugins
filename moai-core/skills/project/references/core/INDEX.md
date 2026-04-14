# project Core Protocol — v1.3.0 인덱스

## 개요

Cowork 프로젝트 초기화 + 스킬 체이닝 워크플로우 설계 스킬(`/project`)의 핵심 프로토콜 파일 인덱스.

**v1.3.0 주요 변경:**
- `/moai init` → `/project init` 커맨드 이름 변경
- **글로벌 프로필 시스템 제거** (`profile-manager.md` 삭제)
- 스킬 체이닝 기반 워크플로우 설계(Phase 3) 신규 도입
- CLAUDE.md 외부 템플릿화 (`references/templates/CLAUDE.md.tmpl`)
- HARD 규칙: office/web 스킬 우선 + AI 슬롭 후처리 고정 포함

**버전**: v1.3.0
**최종 업데이트**: 2026-04-14

---

## 파일 목록 (9개)

### 1. router.md — 자연어 → 플러그인 라우팅
16개 플러그인 키워드 매핑, 모호성 해소, 복합 요청 분기.

### 2. init-protocol.md — /project init 전체 플로우 (v1.3)
Phase 1 인터뷰 → Phase 2 감지 → Phase 3 체인 설계 → Phase 4 확인 → Phase 5 CLAUDE.md 생성 → Phase 6 API 키 → Phase 7 안내.

### 3. context-collector.md — 맥락 수집 프로토콜
맥락 충분성 등급(A/B/C), 모호성 감지, AskUserQuestion 전략.

### 4. claudemd-generator.md — CLAUDE.md 생성 프로토콜
`references/templates/CLAUDE.md.tmpl` 변수 치환 규칙, 200라인 예산, HARD 규칙 고정 블록.

### 5. execution-protocol.md — 스킬 체인 실행 프로토콜
플러그인 트리거 → 체인 순차 실행 → 단계별 요약 → ai-slop-reviewer 종료.

### 6. evaluation-protocol.md — 평가 프로토콜
5개 차원 평가: 정확성, 완전성, 실용성, 톤 적합성, 도메인 적합성.

### 7. evolution-protocol.md — 자기학습 진화 프로토콜
Self-Refine 사이클: 반성 → 피드백 → 패턴 → 업데이트 → 학습.

### 8. diagnostic-protocol.md — 진단 프로토콜
`/project doctor`, `/project status` 커맨드. 환경 상태 진단.

### 9. quality-evaluator.md — 품질 자동 평가
산출물 품질 자동 검증, AI 슬롭 체크리스트 포함.

### (삭제됨) profile-manager.md
v1.3.0에서 **전면 제거**. 이름·회사·역할을 프로젝트마다 묻지 않는 정책으로 전환.

---

## templates/

- `CLAUDE.md.tmpl` — `/project init` Phase 5에서 로드되는 CLAUDE.md 생성 템플릿.

---

## 파일 간 의존성

```
router.md → init-protocol.md → context-collector.md
                ↓
    claudemd-generator.md (templates/CLAUDE.md.tmpl 로드)
                ↓
    execution-protocol.md → evaluation-protocol.md
                ↓
    evolution-protocol.md ← diagnostic-protocol.md ← quality-evaluator.md
```

---

## 스킬 체이닝 핵심 원칙

1. 텍스트 산출물 체인은 **반드시 `ai-slop-reviewer`로 종료**한다.
2. 체인은 [기획/분석 → 생성 → 포맷 변환 → 검수] 구조를 기본으로 한다.
3. 비텍스트 산출물(차트·데이터·숫자·음성)은 ai-slop 단계를 생략한다.
4. 체인 정의는 `/project init` Phase 3에서 생성되어 CLAUDE.md에 기록된다.
5. DOCX/PPTX/XLSX/HWPX/HTML 포맷은 Claude 기본 artifacts가 아닌 **moai-office/moai-content 스킬 우선**.

---

## 17개 플러그인 목록 (moai-core 오케스트레이터 + 16 도메인 플러그인)

| 플러그인 | 도메인 |
|---------|--------|
| moai-core | 초기화, 라우팅, AI 슬롭 검수, 피드백 |
| moai-business | 비즈니스 전략, 스타트업, 시장조사 |
| moai-marketing | 마케팅, SEO, SNS, 광고 |
| moai-legal | 법률, 계약서, 컴플라이언스 |
| moai-finance | 재무, 세무, 부가세, 홈택스 |
| moai-hr | 인사, 노무, 채용, 퇴직금 |
| moai-content | 콘텐츠, 카드뉴스, 블로그, 뉴스레터, 랜딩 |
| moai-operations | 운영, 결재, 조달, SOP |
| moai-education | 교육, 커리큘럼, 평가 |
| moai-lifestyle | 여행, 건강, 웨딩, 이벤트 |
| moai-product | 제품, PM, UX, 로드맵 |
| moai-support | 고객지원, CS, 티켓 |
| moai-office | 문서, PPT, 한글, 엑셀 |
| moai-career | 이력서, 면접, 포트폴리오, 취업 |
| moai-data | 데이터 분석, 공공데이터, 시각화 |
| moai-research | 논문, 특허, 연구비, 선행기술 |
| moai-media | AI 이미지·영상·음성 생성 |

---

## 2계층 아키텍처 (v1.3.0)

```
계층 1: 플러그인 (Read-Only) — 17개 플러그인 (moai-core + moai-media 포함) + 스킬
계층 2: ./CLAUDE.md (자동 로딩) — 프로젝트별 맞춤형 페르소나 + 스킬 체인 정의
         + ./.moai/ — 설정, 컨텍스트, API 키
         + auto-memory — Claude 자율 저장 (세션 간 학습 누적)

❌ 제거됨: 글로벌 프로필 계층 (moai-profile.md, [MoAI 프로필])
```
