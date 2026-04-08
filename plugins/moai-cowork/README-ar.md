<div align="center">

# 🗿 MoAI-Cowork

**100 حزام مجال ذاتي التطور - خبراؤك الشخصيون في الذكاء الاصطناعي**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [한국어](README.md) | [日本語](README-ja.md) | [Español](README-es.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## ما هو MoAI؟

**MoAI-Cowork** هو إضافة لـ Claude Cowork توفر 100 حزام خبير مجالي من خلال نظام مساعد ذكاء اصطناعي ذاتي التعلم.

الحزام هو وحدة خبير ذكاء اصطناعي تجمع المعرفة المتخصصة بالمجال وسير العمل وتنسيقات المخرجات وبروتوكولات جمع السياق في حزمة واحدة. بعد التثبيت، يتحول MoAI إلى خبير مجالي ويقدم نتائج منظمة.

**المميزات الرئيسية:**

- 10 فئات × 100 حزام - المحتوى والتسويق والأعمال والتعليم والقانون وأسلوب الحياة والتواصل والعمليات والتمويل والمنتج والابتكار
- معمارية ذاتية التعلم بـ 5 طبقات - تتطور وتتكيف مع المستخدم بمرور الوقت
- ملف تعريف عام - شارك المعلومات الشخصية وشركتك عبر الجلسات، بدون الحاجة إلى إعادة الإدخال
- دعم 17 لغة - مصدر واحد بالإنجليزية + محلية في وقت التشغيل
- دعم محلي عالمي - أدخل دولة عملك وسيقوم MoAI بجمع قوانين الضرائب والعمل وحماية البيانات والممارسات التجارية تلقائياً عبر البحث على الويب

---

## التثبيت

### الطريقة 1: التثبيت من سوق Claude Cowork (موصى به)

1. شغّل تطبيق **Claude Desktop**
2. ادخل وضع **Cowork** من الأسفل على اليسار
3. انقر على أيقونة **Plugin (🧩)** بجانب حقل الإدخال
4. ابحث عن `moai-cowork` في السوق
5. ابحث عن **MoAI-Cowork** وانقر على **Install**
6. بعد التثبيت، اكتب `/moai init` في الدردشة لبدء الإعداد الأولي

### الطريقة 2: التثبيت من سوق K-Harness

K-Harness هو السوق الذي يتضمن MoAI-Cowork.

```
# الخطوة 1: إضافة السوق
/plugin marketplace add modu-ai/k-harness

# الخطوة 2: تثبيت إضافة MoAI-Cowork
/plugin install moai-cowork@k-harness
```

### الطريقة 3: التثبيت مباشرة من GitHub

```
# استنساخ المستودع
git clone https://github.com/modu-ai/k-harness.git

# الانتقال إلى دليل الإضافة
cd k-harness/plugins/moai-cowork

# التحميل يدوياً في Claude Desktop
# وضع Cowork → Plugin (🧩) → "التثبيت من ملف" → حدد مجلد moai-cowork
```

### الطريقة 4: التثبيت اليدوي عبر ZIP

1. حمّل أحدث `moai-cowork-v0.1.3.zip` من صفحة [GitHub Releases](https://github.com/modu-ai/k-harness/releases)
2. افتح Claude Desktop → ادخل وضع Cowork
3. انقر على أيقونة Plugin (🧩) → **التثبيت من ملف**
4. اختر ملف ZIP المحمّل

---

## التحديث

### إذا تم التثبيت عبر السوق

```
# تحديث سوق K-Harness
/plugin marketplace update k-harness

# أو عبر واجهة Cowork:
# Plugin (🧩) → MoAI-Cowork → انقر على "تحديث"
```

### إذا تم التثبيت من GitHub

```
cd k-harness
git pull origin main
```

### إذا تم التثبيت عبر ZIP

1. أزل الإضافة الموجودة: Plugin (🧩) → MoAI-Cowork → **إزالة**
2. حمّل أحدث ملف ZIP
3. كرر عملية التثبيت اليدوي من الطريقة 4

### التحقق من الإصدار

اكتب `/moai status` في الدردشة للتحقق من الإصدار المثبت حالياً.

---

## استكشاف الأخطاء

### الإضافة غير معترف بها

1. أغلق وأعد تشغيل تطبيق Claude Desktop بالكامل
2. تحقق ما إذا كانت MoAI-Cowork تظهر في قائمة Plugin (🧩) في وضع Cowork
3. إن لم تظهر، حاول إعادة التثبيت

### خطأ عند `/moai init`

1. اكتب `/moai doctor` لتشغيل تشخيصات البيئة
2. إذا كان ملف التعريف العام الخاص بك تالفاً، أعد تعيينه باستخدام `/moai profile --reset`

### عدم تحميل الحزام

1. تحقق ما إذا كان ملف `.moai/config.json` موجوداً في مجلد المشروع
2. إن لم يكن موجوداً، أعد التهيئة باستخدام `/moai init`

### عدم جمع بيانات المحلية

- كوريا: استخدم البيانات المدمجة (بدون الحاجة إلى بحث على الويب)
- دول أخرى: يتطلب اتصال الإنترنت وأدوات البحث على الويب

---

## البدء السريع

### الخطوة 1: التهيئة

```
/moai init
```

يجري MoAI مقابلة تفاعلية لجمع ملفك الشخصي (الاسم والدور والشركة والمحلية).

### الخطوة 2: استعرض كتالوج الأحزمة

```
/moai catalog
```

اعرض القائمة الكاملة لـ 100 حزام عبر 10 فئات.

### الخطوة 3: قدم طلباً باللغة الطبيعية

```
ساعدني في إجراء بحث السوق
```

يكتشف MoAI تلقائياً حزام `market-research` ويعمل في وضع الخبير.

---

## كتالوج 100 حزام

| # | الفئة | العدد | نماذج الأحزمة |
|---|----------|-------|-----------------|
| 1 | المحتوى والإبداع | 10 | copywriting و youtube-production و podcast-studio و book-publishing |
| 2 | الأعمال والإستراتيجية | 10 | business-model-canvas و competitive-analysis و startup-launcher و pricing-strategy |
| 3 | التسويق والنمو | 10 | brand-identity و growth-hacking و social-media-manager و influencer-strategy |
| 4 | التعليم والبحث | 10 | course-builder و thesis-advisor و exam-prep و language-tutor |
| 5 | القانون والامتثال | 10 | contract-analyzer و compliance-checker و patent-drafter و privacy-engineer |
| 6 | أسلوب الحياة | 10 | travel-planner و wedding-planner و meal-planner و fitness-program |
| 7 | التواصل والمستندات | 10 | presentation-designer و report-generator و technical-writer و proposal-writer |
| 8 | العمليات والموارد البشرية | 10 | hiring-pipeline و onboarding-system و operations-manual و crisis-communication |
| 9 | التمويل والتجارة | 10 | accounting-tax و financial-modeler و import-export و invoice-mgmt |
| 10 | المنتج والابتكار | 10 | product-manager و ai-strategy و ux-research و sales-enablement |

اعرض القائمة الكاملة للـ 100 حزام باستخدام `/moai catalog`.

---

## الأوامر الرئيسية

| الأمر | الوصف |
|---------|-------------|
| `/moai init` | التهيئة - جمع الملف الشخصي وتثبيت الحزام |
| `/moai catalog` | استعرض كتالوج 100 حزام |
| `/moai status` | تحقق من الحزام المثبت وحالة التطور |
| `/moai evolve` | تشغيل دورة التطور ذاتي التعلم |
| `/moai profile` | عرض/تعديل الملف الشخصي العام |
| `/moai doctor` | تشغيل تشخيصات البيئة |
| `/moai help` | عرض الأوامر المتاحة |

---

## المعمارية

```
الطبقة 0: auto-memory (عام) - ملف المستخدم، سجل الأحزمة
الطبقة 1: plugin (قراءة فقط) - 100 حزام أساسي (مصدر واحد بـ en/ وتحويل محلي في وقت التشغيل)
الطبقة 2: .claude/CLAUDE.md + rules/ - الشخصية
الطبقة 3: .moai/ (قراءة/كتابة) - سياق المجال وبيانات التطور
الطبقة 4: auto-memory learning - تراكم التعليقات عبر الجلسات
```

---

## الترخيص

ترخيص MIT - مجاني للاستخدام والتعديل والتوزيع

---

## GitHub

- **المستودع**: [modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **المشاكل/الاقتراحات**: [GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork: التقِ بخبراء الذكاء الاصطناعي الخاصين بك.**

*الإصدار 0.1.3 | آخر تحديث: 2026-04-08*
