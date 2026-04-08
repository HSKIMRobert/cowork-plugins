---
name: moai-content-creative
description: "콘텐츠 & 크리에이티브 — 유튜브 프로덕션, 뉴스레터, 카피라이팅, 팟캐스트, 출판, 광고 캠페인 하네스 + Remotion 영상 제작, 랜딩 페이지, 인스타 카드뉴스 실행. 영상, 콘텐츠, 유튜브, 뉴스레터, 카피, 팟캐스트, 출판, 광고, Remotion, 랜딩페이지, 카드뉴스, 캐러셀, 콘텐츠 캘린더, 비주얼 스토리텔링."
---

# 콘텐츠 & 크리에이티브 (① content-creative)

> MoAI-Cowork v0.2.0 | 8 하네스 + 3 실행 모듈

## 하네스 (전략 가이드)

| ID | 한국명 | 설명 |
|----|--------|------|
| youtube-production | 유튜브 프로덕션 | 채널 기획, 콘텐츠 전략, 촬영/편집 가이드, 알고리즘 최적화 |
| newsletter-engine | 뉴스레터 엔진 | 뉴스레터 기획~발행, 구독자 확보 전략 |
| content-calendar | 콘텐츠 캘린더 | 월간/주간 콘텐츠 일정 수립 및 관리 |
| copywriting | 카피라이팅 | 마케팅 카피, 헤드라인, CTA 전문 |
| podcast-studio | 팟캐스트 스튜디오 | 팟캐스트 기획, 녹음, 편집, 배포 |
| book-publishing | 출판 기획 | 원고 기획, 출판 프로세스, 전자책 |
| visual-storytelling | 비주얼 스토리텔링 | 시각 내러티브, 인포그래픽, 스토리보드 |
| advertising-campaign | 광고 캠페인 | 미디어 플랜, 크리에이티브 전략, 성과 분석 |

→ 하네스 파일: `references/harness/{id}.md`

## 실행 모듈 (코드 생성 가능)

### Remotion 영상 제작
React 기반 프로그래매틱 영상 생성 프레임워크.
- 가이드: `references/remotion-video/guide.md`
- 참조: `references/remotion-video/core-animation-rules.md`, `advanced-rules.md`, `media-rules.md`, `utility-rules.md`

### 랜딩 페이지 빌더
고전환율 원페이지 랜딩 설계.
- 가이드: `references/landing-page/guide.md`
- 참조: `references/landing-page/design-principles.md`

### 인스타 카드뉴스
AI 이미지 생성 기반 캐러셀 카드뉴스 제작.
- 가이드: `references/card-news/guide.md`
- 참조: `references/card-news/anti-ai-writing.md`, `magazine-sop.md`, `design-guide.md`
- 스크립트: `${CLAUDE_SKILL_DIR}/scripts/card-news/generate_image.py`

## 실행 규칙

1. 사용자 요청 수신 → 하네스/실행 모듈 판별
2. 하네스 요청 → 해당 `references/harness/{id}.md` 로드 → 전략 가이드 실행
3. 실행 모듈 요청 → 해당 `references/{module}/guide.md` 로드 → 코드/파일 생성
4. `--deepthink` 또는 복잡 작업 → `mcp__sequential-thinking__sequentialthinking` 호출
5. 결과물 생성 후 사용자 검토 요청
