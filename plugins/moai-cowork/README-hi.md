<div align="center">

# 🗿 MoAI-Cowork

**100 आत्म-विकसित डोमेन हार्नेस — आपके व्यक्तिगत AI विशेषज्ञ**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [한국어](README.md) | [日本語](README-ja.md) | [Español](README-es.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## MoAI क्या है?

**MoAI-Cowork** Claude Cowork के लिए एक प्लगइन है जो एक आत्म-शिक्षण AI सहायक प्रणाली के माध्यम से 100 डोमेन विशेषज्ञ हार्नेस प्रदान करता है।

एक हार्नेस एक AI विशेषज्ञ मॉड्यूल है जो डोमेन-विशिष्ट ज्ञान, वर्कफ़्लो, डिलीवरेबल प्रारूप और संदर्भ-संग्रह प्रोटोकॉल को एक पैकेज में बंडल करता है। एक बार इंस्टॉल होने के बाद, MoAI एक डोमेन विशेषज्ञ में रूपांतरित हो जाता है और संरचित परिणाम प्रदान करता है।

**मुख्य विशेषताएं:**

- 10 श्रेणियां × 100 हार्नेस — सामग्री, विपणन, व्यवसाय, शिक्षा, कानूनी, जीवनशैली, संचार, संचालन, वित्त और उत्पाद/नवाचार
- 5-स्तरीय आत्म-शिक्षण आर्किटेक्चर — समय के साथ उपयोगकर्ता के अनुकूल विकसित होता है
- वैश्विक प्रोफाइल — सत्र भर व्यक्तिगत + कंपनी जानकारी साझा करें, पुनः प्रविष्टि की आवश्यकता नहीं
- 17 भाषा समर्थन — EN एकल स्रोत + रनटाइम स्थानीयकरण
- विश्वव्यापी स्थान समर्थन — अपना कार्य देश दर्ज करें और MoAI स्वचालित रूप से वेब खोज के माध्यम से कर कानून, श्रम कानून, डेटा सुरक्षा और व्यावसायिक प्रथाएं एकत्र करता है

---

## स्थापना

### विधि 1: Claude Cowork मार्केटप्लेस से इंस्टॉल करें (अनुशंसित)

1. **Claude Desktop** ऐप लॉन्च करें
2. नीचे-बाएँ से **Cowork** मोड दर्ज करें
3. चैट इनपुट के आगे **Plugin (🧩)** आइकन पर क्लिक करें
4. मार्केटप्लेस में `moai-cowork` खोजें
5. **MoAI-Cowork** खोजें और **Install** पर क्लिक करें
6. इंस्टॉलेशन के बाद, प्रारंभिक सेटअप शुरू करने के लिए चैट में `/moai init` टाइप करें

### विधि 2: K-Harness मार्केटप्लेस से इंस्टॉल करें

K-Harness वह मार्केटप्लेस है जिसमें MoAI-Cowork शामिल है।

```
# चरण 1: मार्केटप्लेस जोड़ें
/plugin marketplace add modu-ai/k-harness

# चरण 2: MoAI-Cowork प्लगइन इंस्टॉल करें
/plugin install moai-cowork@k-harness
```

### विधि 3: GitHub से सीधे इंस्टॉल करें

```
# रिपोजिटरी क्लोन करें
git clone https://github.com/modu-ai/k-harness.git

# प्लगइन निर्देशिका में नेविगेट करें
cd k-harness/plugins/moai-cowork

# Claude Desktop में मैनुअल रूप से लोड करें
# Cowork mode → Plugin (🧩) → "Install from file" → moai-cowork फ़ोल्डर चुनें
```

### विधि 4: ZIP के माध्यम से मैनुअल इंस्टॉल करें

1. [GitHub Releases](https://github.com/modu-ai/k-harness/releases) पृष्ठ से नवीनतम `moai-cowork-v0.1.3.zip` डाउनलोड करें
2. Claude Desktop खोलें → Cowork मोड दर्ज करें
3. Plugin (🧩) आइकन पर क्लिक करें → **Install from file**
4. डाउनलोड की गई ZIP फ़ाइल चुनें

---

## अपडेट करना

### यदि मार्केटप्लेस के माध्यम से इंस्टॉल किया गया है

```
# K-Harness मार्केटप्लेस अपडेट करें
/plugin marketplace update k-harness

# या Cowork UI के माध्यम से:
# Plugin (🧩) → MoAI-Cowork → "Update" पर क्लिक करें
```

### यदि GitHub से इंस्टॉल किया गया है

```
cd k-harness
git pull origin main
```

### यदि ZIP के माध्यम से इंस्टॉल किया गया है

1. मौजूदा प्लगइन हटाएं: Plugin (🧩) → MoAI-Cowork → **Remove**
2. नवीनतम ZIP फ़ाइल डाउनलोड करें
3. विधि 4 मैनुअल इंस्टॉलेशन प्रक्रिया दोहराएं

### संस्करण जांचें

वर्तमान में इंस्टॉल किए गए संस्करण को सत्यापित करने के लिए चैट में `/moai status` टाइप करें।

---

## समस्या निवारण

### प्लगइन मान्यता प्राप्त नहीं है

1. Claude Desktop को पूरी तरह से बंद करें और पुनः शुरू करें
2. जांचें कि क्या Cowork मोड में Plugin (🧩) सूची में MoAI-Cowork दिखाई देता है
3. यदि नहीं, तो पुनः इंस्टॉल करने का प्रयास करें

### `/moai init` पर त्रुटि

1. पर्यावरण डायग्नोस्टिक्स चलाने के लिए `/moai doctor` टाइप करें
2. यदि आपकी वैश्विक प्रोफाइल खराब है, तो इसे `/moai profile --reset` के साथ रीसेट करें

### हार्नेस लोड नहीं हो रहा है

1. जांचें कि क्या `.moai/config.json` आपकी प्रोजेक्ट फ़ोल्डर में मौजूद है
2. यदि नहीं, तो `/moai init` के साथ पुनः शुरू करें

### स्थानीयकरण डेटा एकत्र नहीं किया जा रहा है

- दक्षिण कोरिया: अंतर्निहित डेटा का उपयोग करता है (वेब खोज की आवश्यकता नहीं)
- अन्य देश: इंटरनेट कनेक्शन और वेब खोज उपकरण की आवश्यकता है

---

## शीघ्र प्रारंभ

### चरण 1: आरंभीकरण करें

```
/moai init
```

MoAI आपकी प्रोफाइल (नाम, भूमिका, कंपनी, स्थान) एकत्र करने के लिए एक इंटरैक्टिव साक्षात्कार संचालित करता है।

### चरण 2: हार्नेस कैटलॉग ब्राउज़ करें

```
/moai catalog
```

10 श्रेणियों में 100 हार्नेस की पूरी सूची देखें।

### चरण 3: एक प्राकृतिक भाषा अनुरोध करें

```
मार्केट रिसर्च करने में मेरी मदद करो
```

MoAI स्वचालित रूप से `market-research` हार्नेस का पता लगाता है और विशेषज्ञ मोड में चलता है।

---

## 100 हार्नेस कैटलॉग

| # | श्रेणी | गिनती | नमूना हार्नेस |
|---|----------|-------|-----------------|
| 1 | सामग्री और रचनात्मक | 10 | copywriting, youtube-production, podcast-studio, book-publishing |
| 2 | व्यवसाय और रणनीति | 10 | business-model-canvas, competitive-analysis, startup-launcher, pricing-strategy |
| 3 | विपणन और विकास | 10 | brand-identity, growth-hacking, social-media-manager, influencer-strategy |
| 4 | शिक्षा और अनुसंधान | 10 | course-builder, thesis-advisor, exam-prep, language-tutor |
| 5 | कानूनी और अनुपालन | 10 | contract-analyzer, compliance-checker, patent-drafter, privacy-engineer |
| 6 | जीवनशैली | 10 | travel-planner, wedding-planner, meal-planner, fitness-program |
| 7 | संचार और दस्तावेज़ | 10 | presentation-designer, report-generator, technical-writer, proposal-writer |
| 8 | संचालन और HR | 10 | hiring-pipeline, onboarding-system, operations-manual, crisis-communication |
| 9 | वित्त और व्यापार | 10 | accounting-tax, financial-modeler, import-export, invoice-mgmt |
| 10 | उत्पाद और नवाचार | 10 | product-manager, ai-strategy, ux-research, sales-enablement |

`/moai catalog` के साथ सभी 100 हार्नेस की पूरी सूची देखें।

---

## मुख्य आदेश

| आदेश | विवरण |
|---------|-------------|
| `/moai init` | आरंभीकरण — प्रोफाइल एकत्र करें और हार्नेस इंस्टॉल करें |
| `/moai catalog` | 100 हार्नेस कैटलॉग ब्राउज़ करें |
| `/moai status` | इंस्टॉल किए गए हार्नेस और विकास स्थिति जांचें |
| `/moai evolve` | आत्म-शिक्षण विकास चक्र चलाएं |
| `/moai profile` | वैश्विक प्रोफाइल देखें/संपादित करें |
| `/moai doctor` | पर्यावरण डायग्नोस्टिक्स चलाएं |
| `/moai help` | उपलब्ध आदेश दिखाएं |

---

## आर्किटेक्चर

```
परत 0: auto-memory (वैश्विक) — उपयोगकर्ता प्रोफाइल, हार्नेस इतिहास
परत 1: प्लगइन (केवल पढ़ने के लिए) — 100 आधार हार्नेस (en/ एकल स्रोत, रनटाइम स्थानीयकरण)
परत 2: .claude/CLAUDE.md + नियम — व्यक्तित्व
परत 3: .moai/ (पढ़ना/लिखना) — डोमेन संदर्भ, विकास डेटा
परत 4: auto-memory शिक्षण — क्रॉस-सत्र प्रतिक्रिया संचय
```

---

## लाइसेंस

MIT लाइसेंस — उपयोग, संशोधन और वितरण के लिए स्वतंत्र

---

## GitHub

- **रिपोजिटरी**: [modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **समस्याएं/सुझाव**: [GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork: अपने AI विशेषज्ञों से मिलें।**

*संस्करण 0.1.3 | अंतिम अपडेट: 2026-04-08*
