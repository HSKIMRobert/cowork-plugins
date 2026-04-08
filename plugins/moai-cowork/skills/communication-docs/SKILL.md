---
name: moai-communication-docs
description: "커뮤니케이션 & 문서 — 제안서, 회의록, 보고서, SOP, 스피치, 위기 소통, 데이터 분석, 번역 하네스 + PPT 디자인(Pretendard+명조), 한글(HWPX) 문서 생성 실행. PPT, 슬라이드, 발표자료, 한글, hwpx, 아래한글, 한컴, 보고서, 제안서, 견적서, 회의록, SOP, 매뉴얼, 기안서."
---

# 커뮤니케이션 & 문서 (⑦ communication-docs)

> MoAI-Cowork v0.2.0 | 8 하네스 + 2 실행 모듈

## 하네스 (전략 가이드)

| ID | 한국명 | 설명 |
|----|--------|------|
| proposal-writer | 제안서 작성 | 사업 제안서, 견적서, RFP 응답 구성 |
| meeting-strategist | 회의 전략가 | 회의록 작성, 안건 관리, 후속 조치 |
| report-generator | 보고서 생성 | 주간/월간 보고서, 기안서, 업무 보고 |
| sop-writer | SOP 작성 | 표준 운영 절차, 매뉴얼, 가이드라인 |
| public-speaking | 퍼블릭 스피킹 | 발표 준비, 스피치 구성, 청중 분석 |
| crisis-communication | 위기 소통 | 사과문, 위기 대응 메시지, 미디어 대응 |
| data-analysis | 데이터 분석 | 데이터 인사이트, 시각화 전략, 보고 |
| translation-localization | 번역/현지화 | 다국어 번역, 현지화 전략 |

→ 하네스 파일: `references/harness/{id}.md`

## 실행 모듈 (코드 생성 가능)

### PPT 디자인 시스템
Pretendard + 명조 기반 한국형 PPT 디자인. pptxgenjs 코드 생성.
- 가이드: `references/ppt/guide.md`
- 참조: `references/ppt/pptxgen-code-patterns.md`

### 한글 문서 (HWPX)
OWPML 기반 한글 문서 생성/편집. python-hwpx + lxml 사용.
- 가이드: `references/hwpx/guide.md`
- 참조: `references/hwpx/owpml-spec.md`
- 스크립트:
  - `${CLAUDE_SKILL_DIR}/scripts/hwpx/create_hwpx.py` — HWPX 생성
  - `${CLAUDE_SKILL_DIR}/scripts/hwpx/extract_text.py` — 텍스트 추출
  - `${CLAUDE_SKILL_DIR}/scripts/hwpx/extract_hwp.py` — HWP 변환
  - `${CLAUDE_SKILL_DIR}/scripts/hwpx/pack.py` — HWPX 패킹
  - `${CLAUDE_SKILL_DIR}/scripts/hwpx/unpack.py` — HWPX 언패킹
  - `${CLAUDE_SKILL_DIR}/scripts/hwpx/validate.py` — HWPX 검증

## 실행 규칙

1. 사용자 요청 수신 → 하네스/실행 모듈 판별
2. 하네스 요청 → `references/harness/{id}.md` 로드 → 전략 가이드 실행
3. PPT 요청 → `references/ppt/guide.md` 로드 → pptxgenjs 코드 생성
4. 한글 문서 요청 → `references/hwpx/guide.md` 로드 → python-hwpx 스크립트 실행
5. `--deepthink` 또는 복잡 작업 → `mcp__sequential-thinking__sequentialthinking` 호출
6. 결과물 생성 후 사용자 검토 요청
