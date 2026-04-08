# MoAI Core Protocol — v0.2.0 인덱스

## 개요
MoAI-Cowork v0.2.0의 핵심 프로토콜 10개 파일 인덱스.
v0.1.3 대비 변경: localization-protocol, rules-generator, verification-protocol 제거.
모든 파일은 한국어로 작성. 4계층 아키텍처 반영.

**버전**: v0.2.0
**생성일**: 2026-04-08

---

## 10개 파일 목록

### 1. router.md — 자연어 → 스킬 라우팅 프로토콜
사용자의 자연어 요청을 분석하여 10개 도메인 스킬 중 적합한 스킬로 라우팅.
키워드 매핑, 모호성 해소, 복합 요청 분기.

### 2. init-protocol.md — /moai init 전체 플로우
5단계 Phase: 프로필 감지 → 기본 프로필 → 카테고리 선택 → 하네스 선택 → CLAUDE.md 생성.
rules/ 제거, CLAUDE.md에 모든 내용 통합.

### 3. context-collector.md — 맥락 수집 프로토콜
맥락 충분성 등급 (A/B/C), 모호성 감지, AskUserQuestion 전략.

### 4. profile-manager.md — 글로벌 프로필 관리
/mnt/.auto-memory/moai-profile.md 중심. 개인 + 회사 프로필 CRUD.

### 5. claudemd-generator.md — CLAUDE.md 생성 프로토콜
하네스 레퍼런스 기반 맞춤형 CLAUDE.md 자동 생성. 하네스 전체 복사 원칙.

### 6. execution-protocol.md — 하네스 실행 프로토콜
스킬 트리거 → 레퍼런스 로드 → 산출물 생성 → 검토.

### 7. evaluation-protocol.md — 평가 프로토콜
5개 차원 평가: 정확성, 완전성, 실용성, 톤 적합성, 도메인 적합성.

### 8. evolution-protocol.md — 자기학습 진화 프로토콜
Self-Refine 사이클: 반성 → 피드백 → 패턴 → 업데이트 → 학습.

### 9. diagnostic-protocol.md — 진단 프로토콜
/moai doctor, /moai status 명령어. 환경 상태 진단.

### 10. .mcp.json — sequential-thinking MCP 설정
복잡 작업, --deepthink 시 mcp__sequential-thinking__sequentialthinking 호출.

---

## 파일 간 의존성

```
router.md → init-protocol.md → profile-manager.md → context-collector.md
    ↓
claudemd-generator.md → execution-protocol.md → evaluation-protocol.md
    ↓
evolution-protocol.md ← diagnostic-protocol.md
```

## v0.1.3 대비 제거 항목

| 제거 파일 | 이유 |
|----------|------|
| localization-protocol.md | 한국 전용 — 다국어 불필요 |
| rules-generator.md | CLAUDE.md에 통합 — rules/ 미생성 |
| verification-protocol.md | evaluation-protocol에 통합 |

## 4계층 아키텍처

```
계층 0: auto-memory (글로벌) — 프로필, 하네스 이력
계층 1: 플러그인 (read-only) — 11개 스킬 + 레퍼런스 + 스크립트
계층 2: .claude/CLAUDE.md (자동 로딩) — 맞춤형 페르소나 + 워크플로우
계층 3: .moai/ (R/W) — 도메인 맥락, 진화 데이터
계층 4: auto-memory 학습 — 세션 간 피드백 누적
```
