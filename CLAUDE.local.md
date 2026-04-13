# CLAUDE.local.md — cowork-plugins 저장소 로컬 지침

이 파일은 이 저장소에서 Claude Code가 작업할 때 반드시 지켜야 할 로컬 규칙입니다.

---

## 1. 버저닝 정책 (HARD)

**단일 진실 원칙**: cowork-plugins 저장소의 모든 버전 표기는 **완전히 동일**해야 합니다.

### 동기화 대상 (총 82개 지점)

| 범주 | 경로 | 필드 | 개수 |
|---|---|---|---|
| 마켓플레이스 | `.claude-plugin/marketplace.json` | `metadata.version` | 1 |
| 플러그인 매니페스트 | `<plugin>/.claude-plugin/plugin.json` | `version` | 16 |
| 스킬 frontmatter | `<plugin>/skills/<skill>/SKILL.md` | `metadata.version` | 65 |

### [HARD] 버전 변경 절차

릴리스 버전을 올릴 때는 **반드시 아래 4단계를 함께 실행**합니다. 일부만 올리는 것은 금지.

1. **3곳 동시 업데이트** (위 표의 82개 지점 전부)
   ```bash
   NEW="1.0.4"
   # marketplace
   sed -i '' -E 's/"version": *"[0-9]+\.[0-9]+\.[0-9]+"/"version": "'$NEW'"/' .claude-plugin/marketplace.json
   # 모든 plugin.json
   find . -path "*/.claude-plugin/plugin.json" -not -path "*/.git/*" -exec \
     sed -i '' -E 's/"version": *"[0-9]+\.[0-9]+\.[0-9]+"/"version": "'$NEW'"/' {} +
   # 모든 SKILL.md metadata.version
   find . -name "SKILL.md" -not -path "*/.git/*" -exec \
     sed -i '' -E 's/^(  version: *)"[0-9]+\.[0-9]+\.[0-9]+"/\1"'$NEW'"/' {} +
   ```

2. **CHANGELOG.md 항목 추가**: `## [NEW] - YYYY-MM-DD` 섹션, Added/Changed/Fixed/Removed 분류

3. **커밋**: `chore(release): vX.Y.Z — 요약` 형식의 단일 릴리스 커밋

4. **태그 생성·푸시**: `git tag vX.Y.Z && git push origin vX.Y.Z`
   - 태그는 `vX.Y.Z` 형식 (v 접두어 필수)
   - 태그 값과 파일 내 버전은 **반드시 동일**

### [HARD] 금지 사항

- 일부 파일만 버전 올리기 (예: marketplace.json만 bump, SKILL.md 방치)
- 태그 형식 불일치 (예: `v1.1.0` 태그인데 marketplace.json은 `1.0.3`)
- 버전 번호와 무관한 마이너 수정에 버전 bump
- 이미 배포된 태그를 force-push로 덮어쓰기 (사용자 캐시 손상)

### 검증 명령

커밋 전 반드시 실행:
```bash
# 모든 버전이 동일한지 확인 (한 줄만 출력되어야 통과)
{ grep -h '"version"' .claude-plugin/marketplace.json moai-*/.claude-plugin/plugin.json | grep -oE '[0-9]+\.[0-9]+\.[0-9]+'; \
  grep -h "^  version:" moai-*/skills/*/SKILL.md | grep -oE '[0-9]+\.[0-9]+\.[0-9]+'; } \
  | sort -u
```

---

## 2. 플러그인 컴포넌트 규격 (HARD)

### Skill 슬래시 자동완성 노출

`/<skill-name>` Tab 자동완성에 노출하려면 SKILL.md frontmatter에 다음 필드 **필수**:

```yaml
---
name: <skill-name>
description: >
  ...
user-invocable: true        # ← 슬래시 메뉴 노출 스위치
metadata:
  version: "X.Y.Z"
  status: "active" | "stable" | "experimental"
  updated: "YYYY-MM-DD"
  tags: "tag1,tag2,tag3"
---
```

- `user-invocable` 누락 시 → Tab 자동완성 불가, 모델 자동 호출만 가능
- `keywords` 필드는 **비표준**이므로 사용 금지 (`metadata.tags`로 대체)

### Plugin 매니페스트

`<plugin>/.claude-plugin/plugin.json` 필수 필드:
```json
{
  "name": "plugin-name",
  "version": "1.0.3",
  "description": "...",
  "author": { "name": "..." },
  "keywords": ["..."],
  "license": "MIT"
}
```

---

## 3. 릴리스 후 사용자 안내

신버전 배포 후 사용자 측 캐시 갱신 필요:
```
/plugin marketplace update cowork-plugins
```
이후 플러그인 상세 재진입 시 반영됨. README나 릴리스 노트에 해당 안내 포함.

---

## 4. 태그 히스토리

- **v1.0.3** (2026-04-14): `/moai` 자동완성 수정 + 전체 버전 통일 + 태그 정책 확립
- 이전 로컬 태그(v1.1.0, v1.2.0, v1.3.0)는 marketplace 버전과 불일치하여 v1.0.3에서 정리·삭제함

---

Version: 1.0.0
Last Updated: 2026-04-14
