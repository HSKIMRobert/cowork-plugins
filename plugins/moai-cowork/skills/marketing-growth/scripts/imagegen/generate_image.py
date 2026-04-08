#!/usr/bin/env python3
"""
Nano Banana / Imagen 통합 이미지 생성 스크립트 v3.0.0
- Gemini 계열 (Nano Banana 2/Pro): :generateContent 엔드포인트
- Imagen 계열 (Imagen 4/Ultra/Fast): :predict 엔드포인트
- 서로게이트 문자 안전 패치 적용 (한글/이모지)

v3.0.0 변경사항:
- Imagen 3 → Imagen 4 모델 전환 (Imagen 3 서비스 종료)
- sampleCount → numberOfImages 파라미터 변경
- imageSize, personGeneration 파라미터 추가
- nano-banana-ultra 모델 별칭 추가
- 4:5 → 3:4 비율 자동 전환 (Imagen 4 미지원)
- Imagen 3 모델명 → Imagen 4 자동 매핑 + 경고
- Gemini generationConfig에 aspect_ratio, image_size 추가
- 타임아웃 90초 통일
"""

import os
import re
import sys
import json
import base64
import argparse
import time
import warnings
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

# ─── 모델 매핑 ───────────────────────────────────────────────
MODEL_ALIASES = {
    # Gemini 계열 (:generateContent)
    "nano-banana-2": "gemini-3.1-flash-image-preview",
    "nano-banana-pro": "gemini-3-pro-image-preview",
    "nano-banana": "gemini-2.5-flash-image",
    # Imagen 계열 (:predict) — Imagen 4
    "nano-banana-ultra": "imagen-4.0-ultra-generate-001",
    "imagen-4": "imagen-4.0-generate-001",
    "imagen-4-ultra": "imagen-4.0-ultra-generate-001",
    "imagen-4-fast": "imagen-4.0-fast-generate-001",
}

# Imagen 3 → Imagen 4 하위호환 매핑 (서비스 종료된 모델)
LEGACY_MODEL_MAP = {
    "imagen-3.0-generate-002": "imagen-4.0-generate-001",
    "imagen-3.0-generate-001": "imagen-4.0-generate-001",
    "imagen-3.0-fast-generate-001": "imagen-4.0-fast-generate-001",
}

IMAGEN_MODELS = {
    "imagen-4.0-generate-001",
    "imagen-4.0-ultra-generate-001",
    "imagen-4.0-fast-generate-001",
}

# Imagen 4 지원 비율 (공식 문서 기준)
IMAGEN4_SUPPORTED_RATIOS = {"1:1", "3:4", "4:3", "9:16", "16:9"}

# 비율 자동 전환 매핑 (미지원 → 지원)
RATIO_FALLBACK = {
    "4:5": "3:4",
    "5:4": "4:3",
}

DEFAULT_MODEL = "nano-banana-2"
DEFAULT_TIMEOUT = 90  # v3.0: 90초 통일

# ─── API 키 관리 ──────────────────────────────────────────────
def _find_key_file():
    """MoAI-Cowork 환경의 키 파일 자동 탐색"""
    candidates = [
        Path(__file__).parent.parent.parent.parent / "00_Context" / ".nano-banana-api-key",
        Path.home() / ".nano-banana-api-key",
    ]
    for p in candidates:
        if p.exists():
            return p
    return None


def load_api_key():
    """API 키 로드 (환경변수 > 파일 순서)"""
    key = os.environ.get("NANO_BANANA_API_KEY")
    if key:
        return key.strip()
    kf = _find_key_file()
    if kf:
        return kf.read_text().strip()
    return None


# ─── 서로게이트 안전 패치 ─────────────────────────────────────
def sanitize_text(text):
    """단독 서로게이트 문자(U+D800~U+DFFF) 제거"""
    return re.sub(r'[\ud800-\udfff]', '', text)


def safe_json_dumps(obj):
    """서로게이트 안전 JSON 직렬화"""
    text = json.dumps(obj, ensure_ascii=False)
    return sanitize_text(text)


# ─── 모델 해석 ────────────────────────────────────────────────
def resolve_model(model_name):
    """약칭을 실제 모델 ID로 변환. Imagen 3 모델은 자동으로 Imagen 4로 매핑."""
    model_id = MODEL_ALIASES.get(model_name, model_name)

    # Imagen 3 → 4 하위호환 매핑
    if model_id in LEGACY_MODEL_MAP:
        new_id = LEGACY_MODEL_MAP[model_id]
        print(f"[WARN] Imagen 3 모델 '{model_id}'은(는) 서비스 종료됨. "
              f"Imagen 4 '{new_id}'로 자동 전환합니다.", file=sys.stderr)
        model_id = new_id

    return model_id


def is_imagen(model_id):
    """Imagen 계열 모델인지 판별"""
    return model_id in IMAGEN_MODELS or model_id.startswith("imagen-")


def validate_imagen_ratio(aspect_ratio):
    """Imagen 4 지원 비율 검증 및 자동 전환"""
    if aspect_ratio in IMAGEN4_SUPPORTED_RATIOS:
        return aspect_ratio

    if aspect_ratio in RATIO_FALLBACK:
        new_ratio = RATIO_FALLBACK[aspect_ratio]
        print(f"[WARN] Imagen 4는 '{aspect_ratio}' 비율을 지원하지 않습니다. "
              f"'{new_ratio}'로 자동 전환합니다.", file=sys.stderr)
        return new_ratio

    print(f"[WARN] Imagen 4 미지원 비율 '{aspect_ratio}'. "
          f"지원 비율: {', '.join(sorted(IMAGEN4_SUPPORTED_RATIOS))}. "
          f"기본값 '1:1'로 대체합니다.", file=sys.stderr)
    return "1:1"


# ─── Gemini 계열 생성 (:generateContent) ─────────────────────
def generate_gemini(prompt, output_path, model_id, api_key,
                    aspect_ratio=None, image_size=None):
    """Nano Banana 2/Pro 등 Gemini 계열 이미지 생성"""
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
           f"{model_id}:generateContent?key={api_key}")

    gen_config = {
        "responseModalities": ["TEXT", "IMAGE"],
        "temperature": 1.0,
    }
    # v3.0: generationConfig에 aspect_ratio, image_size 추가
    if aspect_ratio:
        gen_config["aspect_ratio"] = aspect_ratio
    if image_size:
        gen_config["image_size"] = image_size

    payload = {
        "contents": [{"parts": [{"text": sanitize_text(prompt)}]}],
        "generationConfig": gen_config,
    }
    req = Request(url, data=safe_json_dumps(payload).encode("utf-8"),
                  headers={"Content-Type": "application/json"}, method="POST")

    with urlopen(req, timeout=DEFAULT_TIMEOUT) as resp:
        result = json.loads(resp.read().decode("utf-8"))

    for candidate in result.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            if "inlineData" in part:
                out = Path(output_path)
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_bytes(base64.b64decode(part["inlineData"]["data"]))
                return {"success": True, "path": str(out), "model": model_id}

    return {"success": False,
            "error": f"응답에 이미지가 없습니다: {json.dumps(result)[:300]}"}


# ─── Imagen 계열 생성 (:predict) ─────────────────────────────
def generate_imagen(prompt, output_path, model_id, api_key,
                    aspect_ratio="1:1", num_images=1,
                    image_size=None, person_generation=None):
    """Imagen 4/Ultra/Fast 이미지 생성"""
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/"
           f"{model_id}:predict?key={api_key}")

    # v3.0: 비율 검증
    aspect_ratio = validate_imagen_ratio(aspect_ratio)

    parameters = {
        "aspectRatio": aspect_ratio,
        "numberOfImages": num_images,  # v3.0: sampleCount → numberOfImages
    }
    # v3.0: 선택적 파라미터
    if image_size:
        parameters["imageSize"] = image_size
    if person_generation:
        parameters["personGeneration"] = person_generation

    payload = {
        "instances": [{"prompt": sanitize_text(prompt)}],
        "parameters": parameters,
    }

    req = Request(url, data=safe_json_dumps(payload).encode("utf-8"),
                  headers={"Content-Type": "application/json"}, method="POST")

    with urlopen(req, timeout=DEFAULT_TIMEOUT) as resp:
        result = json.loads(resp.read().decode("utf-8"))

    predictions = result.get("predictions", [])
    if predictions and predictions[0].get("bytesBase64Encoded"):
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(base64.b64decode(predictions[0]["bytesBase64Encoded"]))
        return {"success": True, "path": str(out), "model": model_id}

    return {"success": False,
            "error": f"응답에 이미지가 없습니다: {json.dumps(result)[:300]}"}


# ─── 통합 생성 함수 ──────────────────────────────────────────
def generate_image(prompt, output_path, model=DEFAULT_MODEL,
                   aspect_ratio="1:1", api_key=None,
                   image_size=None, person_generation=None):
    """
    모델 계열을 자동 판별하여 적절한 API로 이미지를 생성한다.

    Args:
        prompt: 영어 프롬프트 (권장) 또는 한국어
        output_path: 저장 경로 (.png)
        model: 모델 약칭 또는 전체 ID
        aspect_ratio: 비율 (Imagen: 1:1/3:4/4:3/9:16/16:9, Gemini: 14종)
        api_key: API 키 (None이면 자동 로드)
        image_size: 해상도 (Imagen: "1K"/"2K", Gemini: "512"/"1K"/"2K"/"4K")
        person_generation: 인물 생성 정책 (Imagen: "dont_allow"/"allow_adult"/"allow_all")

    Returns:
        dict: {"success": bool, "path": str, "model": str, "error": str}
    """
    if not api_key:
        api_key = load_api_key()
    if not api_key:
        return {"success": False,
                "error": "API 키가 없습니다. NANO_BANANA_API_KEY 환경변수를 설정하세요."}

    model_id = resolve_model(model)

    try:
        if is_imagen(model_id):
            return generate_imagen(
                prompt, output_path, model_id, api_key,
                aspect_ratio=aspect_ratio,
                image_size=image_size,
                person_generation=person_generation,
            )
        else:
            return generate_gemini(
                prompt, output_path, model_id, api_key,
                aspect_ratio=aspect_ratio,
                image_size=image_size,
            )
    except HTTPError as e:
        body = ""
        if hasattr(e, "read"):
            body = e.read().decode("utf-8", errors="replace")[:300]
        return {"success": False, "error": f"HTTP {e.code}: {body}",
                "model": model_id}
    except Exception as e:
        return {"success": False, "error": str(e), "model": model_id}


def generate_batch(jobs, output_dir="./images", model=DEFAULT_MODEL,
                   api_key=None, delay=2):
    """
    여러 이미지를 순차 생성한다. 레이트 제한 방지를 위해 delay초 간격을 둔다.

    Args:
        jobs: [{"prompt": "...", "filename": "img.png", "ratio": "16:9",
                "model": "...", "image_size": "2K"}, ...]
        output_dir: 출력 디렉토리
        model: 기본 모델 (개별 job에서 override 가능)
        api_key: API 키
        delay: 생성 간 대기 시간(초)

    Returns:
        dict: {filename: result_dict, ...}
    """
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    results = {}

    for job in jobs:
        fp = str(out / job["filename"])
        m = job.get("model", model)
        r = job.get("ratio", "1:1")
        img_size = job.get("image_size", None)
        person_gen = job.get("person_generation", None)

        result = generate_image(
            job["prompt"], fp, model=m, aspect_ratio=r,
            api_key=api_key, image_size=img_size,
            person_generation=person_gen,
        )
        results[job["filename"]] = result

        status = "OK" if result["success"] else "FAIL"
        print(f"  [{status}] {job['filename']}: "
              f"{result.get('error', result.get('path', ''))}")

        if len(jobs) > 1:
            time.sleep(delay)

    return results


# ─── CLI ──────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Nano Banana / Imagen 통합 이미지 생성 (v3.0.0)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
모델 약칭:
  nano-banana-2     → gemini-3.1-flash-image-preview (기본값)
  nano-banana-pro   → gemini-3-pro-image-preview
  nano-banana       → gemini-2.5-flash-image
  nano-banana-ultra → imagen-4.0-ultra-generate-001 (신규)
  imagen-4          → imagen-4.0-generate-001
  imagen-4-ultra    → imagen-4.0-ultra-generate-001
  imagen-4-fast     → imagen-4.0-fast-generate-001

Imagen 4 지원 비율: 1:1, 3:4, 4:3, 9:16, 16:9
  (4:5 → 3:4 자동 전환)
        """
    )
    parser.add_argument("--prompt", "-p", required=True,
                        help="이미지 생성 프롬프트")
    parser.add_argument("--output", "-o", default="output.png",
                        help="저장 경로 (기본: output.png)")
    parser.add_argument("--model", "-m", default=DEFAULT_MODEL,
                        help="모델 약칭 또는 ID (기본: nano-banana-2)")
    parser.add_argument("--ratio", "-r", default="1:1",
                        help="비율 (기본: 1:1)")
    parser.add_argument("--image-size", "-s", default=None,
                        choices=["512", "1K", "2K", "4K"],
                        help="해상도 (Imagen: 1K/2K, Gemini: 512/1K/2K/4K)")
    parser.add_argument("--person-generation", default=None,
                        choices=["dont_allow", "allow_adult", "allow_all"],
                        help="인물 생성 정책 (Imagen 전용)")
    parser.add_argument("--api-key", help="API 키 (없으면 환경변수/파일에서 로드)")

    args = parser.parse_args()

    result = generate_image(
        prompt=args.prompt,
        output_path=args.output,
        model=args.model,
        aspect_ratio=args.ratio,
        api_key=args.api_key,
        image_size=args.image_size,
        person_generation=args.person_generation,
    )

    if result["success"]:
        print(f"이미지 생성 완료: {result['path']} (모델: {result['model']})")
    else:
        print(f"오류: {result['error']}")
        exit(1)
