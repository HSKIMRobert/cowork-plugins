<div align="center">

# 🗿 MoAI-Cowork

**100 Harness ที่พัฒนาตัวเองอย่างอิสระ — ผู้เชี่ยวชาญ AI ส่วนตัวของคุณ**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [한국어](README.md) | [日本語](README-ja.md) | [Español](README-es.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## MoAI คืออะไร?

**MoAI-Cowork** เป็น Plugin สำหรับ Claude Cowork ที่มอบ 100 Harness ผู้เชี่ยวชาญด้านต่างๆ ผ่านระบบผู้ช่วยอัจฉริยะที่เรียนรู้ด้วยตัวเอง

Harness คือโมดูลผู้เชี่ยวชาญ AI ที่รวมความรู้เฉพาะด้าน เวิร์กโฟลว์ รูปแบบผลลัพธ์ และโพรโทคอลการรวบรวมบริบทเข้าไว้ในแพ็คเกจเดียว เมื่อติดตั้งแล้ว MoAI จะเปลี่ยนเป็นผู้เชี่ยวชาญด้านหนึ่งและให้ผลลัพธ์ที่มีโครงสร้าง

**คุณสมบัติหลัก:**

- 10 หมวดหมู่ × 100 Harness — เนื้อหา การตลาด ธุรกิจ การศึกษา กฎหมาย ไลฟ์สไตล์ การสื่อสาร การดำเนินงาน การเงิน และผลิตภัณฑ์/นวัตกรรม
- สถาปัตยกรรม 5 ชั้นที่เรียนรู้ด้วยตัวเอง — พัฒนาและปรับตัวให้เข้ากับผู้ใช้เมื่อเวลาผ่านไป
- โปรไฟล์โลก — แชร์ข้อมูลส่วนตัวและบริษัททั่วทุกเซสชัน ไม่ต้องป้อนข้อมูลซ้ำ
- รองรับ 17 ภาษา — EN เดียวรวมทั้งการแปลทันที
- รองรับพื้นที่ทั่วโลก — ป้อนประเทศที่คุณทำงานและ MoAI จะรวบรวมกฎหมายภาษี กฎหมายแรงงาน การปกป้องข้อมูล และแนวปฏิบัติทางธุรกิจโดยอัตโนมัติผ่านการค้นหาเว็บ

---

## การติดตั้ง

### วิธีที่ 1: ติดตั้งจาก Claude Cowork Marketplace (แนะนำ)

1. เปิด **Claude Desktop** app
2. เข้า **Cowork** โหมดจากด้านล่างซ้าย
3. คลิกไอคอน **Plugin (🧩)** ข้างๆ ช่องอินพุตแชท
4. ค้นหา `moai-cowork` ใน Marketplace
5. หา **MoAI-Cowork** และคลิก **Install**
6. หลังจากติดตั้ง พิมพ์ `/moai init` ในแชทเพื่อเริ่มการตั้งค่าเบื้องต้น

### วิธีที่ 2: ติดตั้งจาก K-Harness Marketplace

K-Harness เป็น Marketplace ที่รวม MoAI-Cowork

```
# ขั้นตอนที่ 1: เพิ่ม Marketplace
/plugin marketplace add modu-ai/k-harness

# ขั้นตอนที่ 2: ติดตั้ง MoAI-Cowork Plugin
/plugin install moai-cowork@k-harness
```

### วิธีที่ 3: ติดตั้งโดยตรงจาก GitHub

```
# Clone Repository
git clone https://github.com/modu-ai/k-harness.git

# ไปยังไดเรกทอรี่ Plugin
cd k-harness/plugins/moai-cowork

# โหลดด้วยตนเองใน Claude Desktop
# Cowork mode → Plugin (🧩) → "Install from file" → เลือกโฟลเดอร์ moai-cowork
```

### วิธีที่ 4: ติดตั้งด้วยตนเองผ่าน ZIP

1. ดาวน์โหลด `moai-cowork-v0.1.3.zip` ล่าสุดจากหน้า [GitHub Releases](https://github.com/modu-ai/k-harness/releases)
2. เปิด Claude Desktop → เข้าโหมด Cowork
3. คลิกไอคอน Plugin (🧩) → **Install from file**
4. เลือกไฟล์ ZIP ที่ดาวน์โหลด

---

## การอัปเดต

### หากติดตั้งผ่าน Marketplace

```
# อัปเดต K-Harness Marketplace
/plugin marketplace update k-harness

# หรือผ่าน Cowork UI:
# Plugin (🧩) → MoAI-Cowork → คลิก "Update"
```

### หากติดตั้งจาก GitHub

```
cd k-harness
git pull origin main
```

### หากติดตั้งผ่าน ZIP

1. ลบ Plugin ที่มีอยู่: Plugin (🧩) → MoAI-Cowork → **Remove**
2. ดาวน์โหลดไฟล์ ZIP ล่าสุด
3. ทำตามขั้นตอนการติดตั้งด้วยตนเองจากวิธีที่ 4 อีกครั้ง

### ตรวจสอบเวอร์ชัน

พิมพ์ `/moai status` ในแชทเพื่อยืนยันเวอร์ชันที่ติดตั้งในปัจจุบัน

---

## แก้ไขปัญหา

### ไม่รู้จัก Plugin

1. ปิด Claude Desktop อย่างสมบูรณ์และเปิดใหม่
2. ตรวจสอบว่า MoAI-Cowork ปรากฏในรายการ Plugin (🧩) ในโหมด Cowork หรือไม่
3. หากไม่มี ให้พยายามติดตั้งใหม่

### ข้อผิดพลาดใน `/moai init`

1. พิมพ์ `/moai doctor` เพื่อเรียกใช้การวินิจฉัยสภาพแวดล้อม
2. หากโปรไฟล์โลกของคุณเสียหาย ให้รีเซ็ตด้วย `/moai profile --reset`

### Harness ไม่โหลด

1. ตรวจสอบว่า `.moai/config.json` มีอยู่ในโฟลเดอร์โครงการของคุณหรือไม่
2. หากไม่มี ให้สร้างใหม่ด้วย `/moai init`

### ไม่รวบรวมข้อมูลท้องถิ่น

- เกาหลี: ใช้ข้อมูลในตัว (ไม่ต้องค้นหาเว็บ)
- ประเทศอื่นๆ: ต้องการการเชื่อมต่ออินเทอร์เน็ตและเครื่องมือค้นหาเว็บ

---

## เริ่มต้นอย่างรวดเร็ว

### ขั้นตอนที่ 1: เริ่มต้น

```
/moai init
```

MoAI ทำการสัมภาษณ์แบบโต้ตอบเพื่อรวบรวมโปรไฟล์ของคุณ (ชื่อ บทบาท บริษัท พื้นที่)

### ขั้นตอนที่ 2: เรียกดูแคตตาล็อก Harness

```
/moai catalog
```

ดูรายการ 100 Harness ทั้งหมดทั่วทั้ง 10 หมวดหมู่

### ขั้นตอนที่ 3: ทำการร้องขอภาษาธรรมชาติ

```
ช่วยทำวิจัยตลาดให้หน่อย
```

MoAI จะตรวจจับ Harness `market-research` โดยอัตโนมัติและรันในโหมดผู้เชี่ยวชาญ

---

## แคตตาล็อก 100 Harness

| # | หมวดหมู่ | จำนวน | Harness ตัวอย่าง |
|---|----------|-------|-----------------|
| 1 | Content & Creative | 10 | copywriting, youtube-production, podcast-studio, book-publishing |
| 2 | Business & Strategy | 10 | business-model-canvas, competitive-analysis, startup-launcher, pricing-strategy |
| 3 | Marketing & Growth | 10 | brand-identity, growth-hacking, social-media-manager, influencer-strategy |
| 4 | Education & Research | 10 | course-builder, thesis-advisor, exam-prep, language-tutor |
| 5 | Legal & Compliance | 10 | contract-analyzer, compliance-checker, patent-drafter, privacy-engineer |
| 6 | Lifestyle | 10 | travel-planner, wedding-planner, meal-planner, fitness-program |
| 7 | Communication & Docs | 10 | presentation-designer, report-generator, technical-writer, proposal-writer |
| 8 | Operations & HR | 10 | hiring-pipeline, onboarding-system, operations-manual, crisis-communication |
| 9 | Finance & Trade | 10 | accounting-tax, financial-modeler, import-export, invoice-mgmt |
| 10 | Product & Innovation | 10 | product-manager, ai-strategy, ux-research, sales-enablement |

ดูรายการ Harness ทั้ง 100 รายการด้วย `/moai catalog`

---

## คำสั่งหลัก

| คำสั่ง | คำอธิบาย |
|---------|-------------|
| `/moai init` | เริ่มต้น — รวบรวมโปรไฟล์และติดตั้ง Harness |
| `/moai catalog` | เรียกดูแคตตาล็อก 100 Harness |
| `/moai status` | ตรวจสอบ Harness ที่ติดตั้งและสถานะการพัฒนา |
| `/moai evolve` | รันรอบวงจรการพัฒนาตัวเองอย่างอิสระ |
| `/moai profile` | ดู/แก้ไขโปรไฟล์โลก |
| `/moai doctor` | รันการวินิจฉัยสภาพแวดล้อม |
| `/moai help` | แสดงคำสั่งที่มีอยู่ |

---

## สถาปัตยกรรม

```
Layer 0: auto-memory (global) — โปรไฟล์ผู้ใช้ ประวัติ Harness
Layer 1: Plugin (read-only) — 100 Harness ฐาน (en/ เดียวรวมทั้งการแปลทันที)
Layer 2: .claude/CLAUDE.md + rules/ — บุคลิกภาพ
Layer 3: .moai/ (read/write) — บริบทโดเมน ข้อมูลการพัฒนา
Layer 4: auto-memory learning — การสะสมความเห็นข้ามเซสชัน
```

---

## ใบอนุญาต

MIT License — สามารถใช้งาน แก้ไข และแจกจ่ายได้ฟรี

---

## GitHub

- **Repository**: [modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **Issues/Suggestions**: [GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork: พบกับผู้เชี่ยวชาญ AI ของคุณ**

*Version 0.1.3 | Last Updated: 2026-04-08*
