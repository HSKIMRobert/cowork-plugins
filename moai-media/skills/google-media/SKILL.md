---
name: google-media
description: >
  Google Gemini API 기반 통합 미디어 생성 스킬. **Nano Banana Pro (gemini-3-pro-image-preview)**,
  Nano Banana 2 (gemini-3.1-flash-image-preview), Veo 3.1 영상(8초·1080p·오디오 포함)을
  하나의 API 키로 사용합니다.
  '나노바나나 이미지 생성', '구글 이미지 만들어줘', 'Veo 영상', '프리미엄 영상', '카드뉴스 이미지',
  '/moai-media google-media'로 호출하세요.
  한국어 텍스트 렌더링 SOTA, 최대 4K 이미지, 최대 14장 블렌딩 지원.
user-invocable: true
metadata:
  version: "1.1.0"
  status: "stable"
  updated: "2026-04-14"
  tags: "google,gemini,nano-banana,imagen,veo,image,video,1080p,4k,korean"
---

# Google Media — Gemini API 통합 이미지/영상 생성

> moai-media v1.1.0 | Gemini API 공식 (Nano Banana Pro + Veo 3.1 + Flash Image)

## 개요

Google이 2026년 1분기 "Nano Banana" 브랜드를 **Imagen 4에서 Gemini 3 Image 계열로 완전히 재정의**했습니다.
기존 `imagen-4.0-*` 매핑은 레거시 호환용이며, **신규 프로젝트는 Gemini 3 Image Preview** 모델을 사용해야 합니다.

이 스킬 하나로:
- **이미지** — Nano Banana Pro (`gemini-3-pro-image-preview`), Nano Banana 2 (`gemini-3.1-flash-image-preview`)
- **영상** — Veo 3.1 Standard/Fast (`veo-3.1-generate-preview` / `veo-3.1-fast-generate-preview`)
- **단일 API 키** — `GEMINI_API_KEY` 하나로 전부 호출

## 모델 선택 가이드

### 이미지

| Alias | 실제 모델 ID | 용도 | 속도 | 비용 |
|---|---|---|---|---|
| `nano-banana-pro` (기본) | `gemini-3-pro-image-preview` | 카드뉴스·포스터·광고 (텍스트 렌더링 SOTA) | 보통 | 표준 ($12/M output) |
| `nano-banana-2` | `gemini-3.1-flash-image-preview` | 초안·대량 A/B 테스트 | 빠름 | 낮음 |
| `nano-banana-ultra` | `gemini-3-pro-image-preview` + `image_size=4K` | 대형 인쇄·광고 마스터 | 느림 | 높음 |
| `imagen-4` (레거시) | `imagen-4.0-generate-001` | 하위호환용, 신규 사용 비권장 | - | - |

**주요 특징**:
- 최대 **4K 해상도** (`image_size`: `"1K"` / `"2K"` / `"4K"`)
- **14장 이미지 블렌딩** 지원 (참조 이미지로 스타일·구성 혼합)
- **SOTA 텍스트 렌더링** — 한국어·영문 타이포그래피 품질 최상
- **SynthID 워터마크** 자동 삽입

### 영상 (Veo 3.1)

| Alias | 모델 ID | 용도 | 비용 |
|---|---|---|---|
| `veo-3.1` (기본) | `veo-3.1-generate-preview` | 프리미엄 광고·브랜드 영상 | $0.40/sec (오디오 포함) |
| `veo-3.1-fast` | `veo-3.1-fast-generate-preview` | 시안·빠른 반복 | $0.15/sec |

**제약**:
- 최대 클립 **8초** (`durationSeconds`: `"4"` / `"6"` / `"8"`)
- 해상도: `720p` (기본) / `1080p` / `4k`
- 화면비: `16:9` (기본) / `9:16`
- 오디오는 **항상 생성됨** (Standard 모델, off 불가)

## 호출 방식

### Python (공식 SDK 권장)

```python
from google import genai
from google.genai import types

client = genai.Client()  # GEMINI_API_KEY 환경변수 자동 인식

# 1) 이미지 — Nano Banana Pro
resp = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="'오늘의 인사이트' 한글 타이틀, 미니멀 배경, 파스텔",
    config=types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        image_config=types.ImageConfig(
            aspect_ratio="3:4",
            image_size="2K",
        ),
    ),
)
# resp.candidates[0].content.parts 에서 이미지 bytes 추출

# 2) 영상 — Veo 3.1
import time
op = client.models.generate_videos(
    model="veo-3.1-generate-preview",
    prompt="한국 카페에서 바리스타가 핸드드립을 내리는 슬로우모션, 따뜻한 조명",
)
while not op.done:
    time.sleep(10)
    op = client.operations.get(op)

video = op.response.generated_videos[0]
client.files.download(file=video.video)
video.video.save("output.mp4")
```

### CLI (간편 스크립트)

```bash
# 이미지
python "${CLAUDE_PLUGIN_ROOT}/scripts/generate_image.py" \
  "미니멀 카페 인테리어, 원목 가구, 따뜻한 조명" \
  output/slide_01.png 3:4 nano-banana-pro

# 영상 (추후 추가 예정: generate_video.py)
```

### 엔드포인트 참고 (REST 직접 호출 시)

| 작업 | 엔드포인트 |
|---|---|
| 이미지 | `https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent` |
| 영상 (long-running) | `https://generativelanguage.googleapis.com/v1beta/models/{model}:predictLongRunning` |
| 작업 폴링 | `https://generativelanguage.googleapis.com/v1beta/{operation_name}` |

**중요 변경점 (이전 버전 대비)**:
- 이미지 엔드포인트: `:predict` → **`:generateContent`**
- 파라미터: `numberOfImages` + top-level `aspectRatio` → **`imageConfig.aspect_ratio`** + `imageConfig.image_size`
- 응답: `predictions[].bytesBase64Encoded` → `candidates[].content.parts[].inline_data.data`

## 화면비 지원 (이미지, 14종)

Nano Banana Pro는 광범위한 비율 지원:
`1:1`, `9:16`, `16:9`, `21:9`, `4:5`, `5:4`, `3:4`, `4:3`, `2:3`, `3:2`,
`1:2`, `2:1`, `9:21`, `3:5`

카드뉴스는 `3:4` (구 `4:5` 대체), 릴스/쇼츠는 `9:16`, 유튜브는 `16:9` 사용.

## 프롬프트 팁

### 한국어 텍스트 렌더링 (Nano Banana Pro 강점)

- 텍스트는 **큰따옴표**로 감싸기: `"완벽한 주말" 이라는 제목`
- 폰트 스타일 명시: `깔끔한 고딕`, `진한 세리프`, `손글씨 느낌`
- 크기·위치 지시: `상단 중앙에 큰 글씨로`
- 줄바꿈: `두 줄로 나눠서`

### 영상 (Veo 3.1)

- **카메라 워크**: `슬로우 줌인`, `돌리샷`, `좌에서 우로 팬`
- **오디오 명시**: `잔잔한 피아노 BGM`, `"안녕하세요"라고 말하는 여성 내레이션`
- **한 장면 원칙**: 8초 안에 과도한 전환 금지
- **브랜드 요소**: `브랜드 컬러(#FF6B35)가 중심에`

## API 키 설정

- 환경변수: **`GEMINI_API_KEY`** (권장)
  - 레거시 호환: `NANO_BANANA_API_KEY` 도 인식 (기존 사용자 마이그레이션용)
- 발급처: [ai.google.dev/gemini-api/docs/api-key](https://ai.google.dev/gemini-api/docs/api-key)
- **Nano Banana Pro/2 및 Veo 3.1은 유료 플랜 필요** (무료 티어 호출 불가, 2026-02 Google 공지)

### 대체 구독 옵션

| 플랜 | 가격 | 포함 |
|---|---|---|
| Google AI Plus | $7.99/mo | Veo 3.1 Fast 제한 사용 |
| Google AI Pro | $19.99/mo | Veo 3.1 Standard 제한 |
| Google AI Ultra | $249.99/mo | 무제한급 |

## 비용 가이드 (Pay-as-you-go)

| 작업 | 예상 비용 |
|---|---|
| 카드뉴스 이미지 1장 (Nano Banana Pro, 2K) | ~$0.12 |
| 숏폼 썸네일 1장 (Nano Banana 2) | ~$0.03 |
| Veo 3.1 Fast 8초 (720p) | $1.20 |
| Veo 3.1 Standard 8초 (1080p+오디오) | $3.20 |

**월 예산 예시**: 카드뉴스 10장/주 + Veo 시안 3개/주 = 약 $25/월

## 이관 이력 (v1.1.0)

이전 `moai-content/scripts/card-news/generate_image.py`가 `moai-media/scripts/`로 이관되었으며,
기존 Imagen 4 기반 매핑을 Gemini 3 Image Preview로 업그레이드했습니다.

| v1.0.x (구) | v1.1.0 (신) |
|---|---|
| `imagen-4.0-generate-001` | `gemini-3-pro-image-preview` |
| `imagen-4.0-fast-generate-001` | `gemini-3.1-flash-image-preview` |
| `:predict` 엔드포인트 | `:generateContent` |
| `numberOfImages` 파라미터 | `imageConfig.aspect_ratio` + `image_size` |
| `NANO_BANANA_API_KEY` | `GEMINI_API_KEY` (레거시 이름 호환 유지) |

## 연계 스킬

- `ideogram` (moai-media) — Nano Banana Pro 텍스트 렌더링이 부족할 때 대체
- `kling` (moai-media) — Veo보다 저렴한 숏폼 영상 (립싱크 특화)
- `elevenlabs` (moai-media) — Veo 내장 오디오 대신 더 자연스러운 TTS 사용
- `fal-gateway` (moai-media) — Flux·Recraft 등 non-Google 모델
- `card-news` (moai-content) — 본 스킬 호출로 이미지 생성

## 참고 (공식 문서)

- [Nano Banana Pro 공식 소개](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-3-pro-image-developers/)
- [Gemini 3 Pro Image Preview API 문서](https://ai.google.dev/gemini-api/docs/models/gemini-3-pro-image-preview)
- [Imagen/Image Generation 문서](https://ai.google.dev/gemini-api/docs/image-generation)
- [Veo 영상 생성 문서](https://ai.google.dev/gemini-api/docs/video)
- [DeepMind Gemini Image Pro](https://deepmind.google/models/gemini-image/pro/)
