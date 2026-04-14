# moai-media

> AI 미디어 스튜디오 — 이미지·영상·음성 통합 생성 플러그인

[![버전](https://img.shields.io/badge/version-1.1.0-blue)](../CHANGELOG.md)
[![라이선스](https://img.shields.io/badge/license-MIT-green)](../LICENSE)

## 개요

`moai-media`는 AI 크리에이터·마케터를 위한 **미디어 생성 단일 창구**입니다.
카드뉴스·인스타 피드·숏폼 영상·팟캐스트·브랜드 캠페인에 필요한 이미지·영상·음성을
하나의 플러그인에서 해결합니다.

## 스킬 카탈로그 (5종)

| 스킬 | 한글명 | 백엔드 | 용도 |
|---|---|---|---|
| [`google-media`](skills/google-media/SKILL.md) | 구글 미디어 | Gemini 3 Image Preview + Veo 3.1 | **나노바나나 Pro 이미지 + Veo 영상** (단일 Gemini 키) |
| [`ideogram`](skills/ideogram/SKILL.md) | 아이디오그램 | Ideogram 3.0 via fal.ai | 한국어 타이포 특화 이미지 |
| [`kling`](skills/kling/SKILL.md) | 클링 | Kling 3.0 via fal.ai | 숏폼 영상 (릴스·쇼츠·틱톡) |
| [`elevenlabs`](skills/elevenlabs/SKILL.md) | 일레븐랩스 | ElevenLabs 공식 MCP | AI 음성·TTS·다국어 더빙 |
| [`fal-gateway`](skills/fal-gateway/SKILL.md) | 팔게이트웨이 | fal.ai MCP | Flux·Recraft·Hailuo·Luma·Pika·MiniMax Music 통합 |

## 스킬 선택 가이드

### 이미지

| 상황 | 우선 스킬 |
|---|---|
| 범용 고품질 이미지 (텍스트 포함도 SOTA) | **`google-media`** (Nano Banana Pro) |
| 한국어 대형 타이포그래피가 핵심 | `ideogram` |
| 로고·벡터·브랜드 일관 컬러 | `fal-gateway` (Recraft V3) |
| 오픈소스 Flux 선호 | `fal-gateway` (Flux 1.1 Pro) |

### 영상

| 상황 | 우선 스킬 |
|---|---|
| 프리미엄 브랜드 광고 (1080p + 오디오) | **`google-media`** (Veo 3.1) |
| 인스타 릴스·유튜브 쇼츠·틱톡 (가성비) | `kling` |
| 립싱크 캐릭터 숏폼 | `kling` |
| 저가 시안·대량 A/B 테스트 | `fal-gateway` (Hailuo 2.3) |

### 음성·음악

| 상황 | 스킬 |
|---|---|
| TTS·내레이션·다국어 더빙 | `elevenlabs` |
| BGM·효과음·오리지널 음악 | `fal-gateway` (MiniMax Music, Stable Audio) |

## API 키 설정 (총 3개)

| 키 | 발급처 | 공유 대상 스킬 |
|---|---|---|
| `GEMINI_API_KEY` | [ai.google.dev](https://ai.google.dev/) | `google-media` (이미지 + 영상 모두) |
| `FAL_KEY` | [fal.ai/dashboard/keys](https://fal.ai/dashboard/keys) | `ideogram`, `kling`, `fal-gateway` |
| `ELEVENLABS_API_KEY` | [elevenlabs.io](https://elevenlabs.io/app/settings/api-keys) | `elevenlabs` |

`/moai init` 또는 `/moai apikey`로 통합 등록.

### 레거시 호환

- `NANO_BANANA_API_KEY` 환경변수는 `GEMINI_API_KEY`의 별칭으로 계속 인식됩니다 (v1.0.x 사용자 마이그레이션용).

## MCP 서버 자동 등록

`moai-media/.mcp.json`이 다음 2개 MCP를 자동 등록합니다:

1. **fal-ai** (hosted MCP): `https://mcp.fal.ai/mcp`
2. **elevenlabs** (local MCP): `uvx elevenlabs-mcp`

플러그인 설치 시 자동 활성화. `google-media`는 MCP 불필요 (REST/Python SDK 직접 호출).

## 월 예상 비용 (한국 크리에이터 기준)

| 용도 | 월 예산 | 산출물 |
|---|---|---|
| 입문 (포트폴리오 1~2편/주) | **$10~15** | Nano Banana 2 위주, 영상 시안 소량 |
| 중급 (브랜드 3개, 주 3편) | **$45~60** | 이미지 500장 + Kling 영상 20편 + TTS 30분 |
| 고급 (에이전시 수준) | **$200+** | Veo 3.1 Standard 활용, 일 10편 다채널 배포 |

## 관련 플러그인

- `moai-content` — 카드뉴스·블로그·랜딩페이지 기획 (`moai-media` 스킬을 호출하여 에셋 생성)
- `moai-marketing` — SNS 캠페인·광고 소재 기획
- `moai-office` — PPT·Word·Excel 문서 생성

## v1.1.0 주요 변경 (2026-04-14)

- **신규 플러그인**: `moai-media`를 독립 플러그인으로 분리
- **Google Nano Banana 재정의 반영**: Imagen 4 → **Gemini 3 Image Preview** (모델 ID, 엔드포인트, 파라미터 스키마 전면 마이그레이션)
- **이미지 + 영상 통합**: Nano Banana Pro와 Veo 3.1을 `google-media` 단일 스킬로 묶음
- **스크립트 이관**: `moai-content/scripts/card-news/generate_image.py` → `moai-media/scripts/generate_image.py` (v3.0 → v4.0 마이그레이션 포함)

자세한 변경 내역: [CHANGELOG.md](../CHANGELOG.md)

## 라이선스

MIT · [CHANGELOG](../CHANGELOG.md) · [CLAUDE.local.md](../CLAUDE.local.md)
