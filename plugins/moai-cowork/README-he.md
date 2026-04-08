<div align="center">

# 🗿 MoAI-Cowork

**100 Harnesses בעלי ביקורת עצמית - מומחי ה-AI האישיים שלך**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [한국어](README.md) | [日本語](README-ja.md) | [Español](README-es.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## מה זה MoAI?

**MoAI-Cowork** הוא תוסף ל-Claude Cowork המספק 100 harness מומחים בתחומים שונים דרך מערכת סייע AI שמתפתחת בעצמה.

Harness הוא מודול מומחה AI המקבץ ידע ספציפי לתחום, זרימות עבודה, פורמטי deliverable וממסכי האסיף קשר בחבילה אחת. לאחר התקנה, MoAI הופך למומחה בתחום ומספק תוצאות מובנות.

**תכונות עיקריות:**

- 10 קטגוריות × 100 harnesses - תוכן, שיווק, עסקים, חינוך, משפט, אורח חיים, תקשורת, פעולות, כספים וקונספט/חדשנות
- ארכיטקטורת אימון עצמי בעומק 5 שכבות - מתפתחת והסתגלת למשתמש לאורך זמן
- פרופיל גלובלי - שיתוף של פרטים אישיים וחברתיים בהפעלות, ללא צורך בהזנה מחודשת
- תמיכה בחרי שפות - EN מקור יחיד + התאמה מקום בזמן ריצה
- תמיכת אזור עולמית - הזן את מדינת העבודה שלך ו-MoAI אוטומטית אוסף חוקי מס, חוקי עבודה, הגנת נתונים ועוסקי של באמצעות חיפוש באינטרנט

---

## התקנה

### שיטה 1: התקנה מ-Claude Cowork Marketplace (מומלץ)

1. הפעל את אפליקציית **Claude Desktop**
2. כנס ל-**Cowork** מהפינה השמאלית התחתונה
3. לחץ על סמל **Plugin (🧩)** ליד קלט הצ'אט
4. חפש את `moai-cowork` ב-Marketplace
5. מצא את **MoAI-Cowork** ולחץ על **Install**
6. לאחר התקנה, הקלד `/moai init` בצ'אט כדי להתחיל את ההתקנה הראשונית

### שיטה 2: התקנה מ-K-Harness Marketplace

K-Harness הוא ה-Marketplace המכיל את MoAI-Cowork.

```
# שלב 1: הוסף את ה-Marketplace
/plugin marketplace add modu-ai/k-harness

# שלב 2: התקן את התוסף MoAI-Cowork
/plugin install moai-cowork@k-harness
```

### שיטה 3: התקנה ישירה מ-GitHub

```
# שבור את המאגר
git clone https://github.com/modu-ai/k-harness.git

# נווט לספרית התוסף
cd k-harness/plugins/moai-cowork

# טען ידנית ב-Claude Desktop
# Cowork mode → Plugin (🧩) → "Install from file" → בחר את תיקיית moai-cowork
```

### שיטה 4: התקנה ידנית דרך ZIP

1. הורד את ה-`moai-cowork-v0.1.3.zip` האחרון מדף [GitHub Releases](https://github.com/modu-ai/k-harness/releases)
2. פתח Claude Desktop → כנס ל-Cowork mode
3. לחץ על סמל Plugin (🧩) → **Install from file**
4. בחר את קובץ ZIP שהורדת

---

## עדכון

### אם התוקנה דרך Marketplace

```
# עדכן את K-Harness Marketplace
/plugin marketplace update k-harness

# או דרך Cowork UI:
# Plugin (🧩) → MoAI-Cowork → לחץ על "Update"
```

### אם התוקנה מ-GitHub

```
cd k-harness
git pull origin main
```

### אם התוקנה דרך ZIP

1. הסר את התוסף הקיים: Plugin (🧩) → MoAI-Cowork → **Remove**
2. הורד את קובץ ZIP האחרון
3. חזור על תהליך ההתקנה הידנית של שיטה 4

### בדוק את הגרסה

הקלד `/moai status` בצ'אט כדי לאמת את הגרסה שהתוקנה כרגע.

---

## פתרון בעיות

### התוסף לא מזוהה

1. סגור לחלוטין והפעל מחדש את Claude Desktop
2. בדוק אם MoAI-Cowork מופיע ברשימת Plugin (🧩) ב-Cowork mode
3. אם לא, נסה להתקין מחדש

### שגיאה ב-`/moai init`

1. הקלד `/moai doctor` כדי להפעיל אבחוני סביבה
2. אם הפרופיל הגלובלי שלך פגום, אפס אותו עם `/moai profile --reset`

### Harness לא נטוען

1. בדוק אם `.moai/config.json` קיים בתיקיית הפרויקט שלך
2. אם לא, אתחול מחדש עם `/moai init`

### נתוני התאמה מקום לא אוספים

- קוריאה: משתמשת בנתונים מובנים (אין צורך בחיפוש באינטרנט)
- מדינות אחרות: דורש חיבור לאינטרנט וכלי חיפוש באינטרנט

---

## התחלה מהירה

### שלב 1: אתחול

```
/moai init
```

MoAI מערך ראיון אינטראקטיבי כדי לאסוף את הפרופיל שלך (שם, תפקיד, חברה, אזור).

### שלב 2: עיין בקטלוג Harness

```
/moai catalog
```

צפה ברשימה המלאה של 100 harnesses על פני 10 קטגוריות.

### שלב 3: בצע בקשה בשפה טבעית

```
עזור לי לעשות מחקר שוק
```

MoAI אוטומטית מזהה את ה-`market-research` harness ופועל במצב מומחה.

---

## קטלוג 100 Harness

| # | קטגוריה | ספירה | דוגמאות Harnesses |
|---|----------|-------|-----------------|
| 1 | תוכן ויצירה | 10 | copywriting, youtube-production, podcast-studio, book-publishing |
| 2 | עסקים וסטרטגיה | 10 | business-model-canvas, competitive-analysis, startup-launcher, pricing-strategy |
| 3 | שיווק וגדילה | 10 | brand-identity, growth-hacking, social-media-manager, influencer-strategy |
| 4 | חינוך מחקר | 10 | course-builder, thesis-advisor, exam-prep, language-tutor |
| 5 | משפט ציות | 10 | contract-analyzer, compliance-checker, patent-drafter, privacy-engineer |
| 6 | אורח חיים | 10 | travel-planner, wedding-planner, meal-planner, fitness-program |
| 7 | תקשורת מסמכים | 10 | presentation-designer, report-generator, technical-writer, proposal-writer |
| 8 | פעולות וموארד אנוש | 10 | hiring-pipeline, onboarding-system, operations-manual, crisis-communication |
| 9 | כספים וסחר | 10 | accounting-tax, financial-modeler, import-export, invoice-mgmt |
| 10 | קונספט וחדשנות | 10 | product-manager, ai-strategy, ux-research, sales-enablement |

ראה את הרשימה המלאה של 100 harnesses עם `/moai catalog`.

---

## פקודות עיקריות

| פקודה | תיאור |
|---------|-------------|
| `/moai init` | אתחול - אסוף פרופיל והתקן harness |
| `/moai catalog` | עיין בקטלוג harness של 100 |
| `/moai status` | בדוק את ה-harness המותקן ומצב ההתפתחות |
| `/moai evolve` | הפעל מחזור התפתחות של אימון עצמי |
| `/moai profile` | צפה/ערוך בפרופיל גלובלי |
| `/moai doctor` | הפעל אבחוני סביבה |
| `/moai help` | הצג פקודות זמינות |

---

## ארכיטקטורה

```
Layer 0: auto-memory (global) — פרופיל משתמש, היסטוריית harness
Layer 1: plugin (read-only) — 100 base harnesses (en/ מקור יחיד, התאמה מקום בזמן ריצה)
Layer 2: .claude/CLAUDE.md + rules/ — persona
Layer 3: .moai/ (read/write) — תוכן תחום, נתוני התפתחות
Layer 4: auto-memory learning — צבירת משוב בחתך הפעלות
```

---

## רישיון

MIT License - חופשי לשימוש, שינוי והפצה

---

## GitHub

- **Repository**: [modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **Issues/Suggestions**: [GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork: פגשו את מומחי ה-AI שלכם.**

*Version 0.1.3 | Last Updated: 2026-04-08*
