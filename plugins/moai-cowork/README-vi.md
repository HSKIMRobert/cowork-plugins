<div align="center">

# 🗿 MoAI-Cowork

**100 Harness Tự Tiến Hóa — Các Chuyên Gia AI Của Bạn**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [한국어](README.md) | [日本語](README-ja.md) | [Español](README-es.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## MoAI Là Gì?

**MoAI-Cowork** là một plugin cho Claude Cowork cung cấp 100 harness chuyên gia lĩnh vực thông qua hệ thống trợ lý AI tự học.

Harness là một mô-đun chuyên gia AI gói gọn kiến thức chuyên ngành, quy trình làm việc, định dạng kết quả và giao thức thu thập ngữ cảnh vào một gói duy nhất. Sau khi cài đặt, MoAI chuyển thành chuyên gia lĩnh vực và cung cấp kết quả có cấu trúc.

**Các tính năng chính:**

- 10 danh mục × 100 harness — nội dung, marketing, kinh doanh, giáo dục, pháp lý, lối sống, giao tiếp, vận hành, tài chính và sản phẩm/đổi mới
- Kiến trúc tự học 5 lớp — phát triển và thích ứng theo người dùng theo thời gian
- Hồ sơ toàn cầu — chia sẻ thông tin cá nhân + công ty trên các phiên, không cần nhập lại
- Hỗ trợ 17 ngôn ngữ — EN nguồn duy nhất + định địa phương trong thời gian chạy
- Hỗ trợ locale toàn thế giới — nhập đất nước làm việc của bạn và MoAI tự động thu thập luật thuế, luật lao động, bảo vệ dữ liệu và thực hành kinh doanh thông qua tìm kiếm web

---

## Cài Đặt

### Phương Pháp 1: Cài Đặt Từ Claude Cowork Marketplace (Được Khuyến Nghị)

1. Khởi chạy ứng dụng **Claude Desktop**
2. Nhập chế độ **Cowork** từ phía dưới bên trái
3. Nhấp vào biểu tượng **Plugin (🧩)** bên cạnh ô nhập liệu trò chuyện
4. Tìm kiếm `moai-cowork` trên marketplace
5. Tìm **MoAI-Cowork** và nhấp **Install**
6. Sau khi cài đặt, nhập `/moai init` trong trò chuyện để bắt đầu thiết lập ban đầu

### Phương Pháp 2: Cài Đặt Từ K-Harness Marketplace

K-Harness là marketplace bao gồm MoAI-Cowork.

```
# Bước 1: Thêm marketplace
/plugin marketplace add modu-ai/k-harness

# Bước 2: Cài đặt plugin MoAI-Cowork
/plugin install moai-cowork@k-harness
```

### Phương Pháp 3: Cài Đặt Trực Tiếp Từ GitHub

```
# Clone repository
git clone https://github.com/modu-ai/k-harness.git

# Điều hướng đến thư mục plugin
cd k-harness/plugins/moai-cowork

# Tải thủ công trong Claude Desktop
# Chế độ Cowork → Plugin (🧩) → "Install from file" → chọn thư mục moai-cowork
```

### Phương Pháp 4: Cài Đặt Thủ Công Qua ZIP

1. Tải xuống `moai-cowork-v0.1.3.zip` mới nhất từ trang [GitHub Releases](https://github.com/modu-ai/k-harness/releases)
2. Mở Claude Desktop → nhập chế độ Cowork
3. Nhấp vào biểu tượng Plugin (🧩) → **Install from file**
4. Chọn tệp ZIP đã tải xuống

---

## Cập Nhật

### Nếu cài đặt thông qua marketplace

```
# Cập nhật K-Harness marketplace
/plugin marketplace update k-harness

# Hoặc thông qua Cowork UI:
# Plugin (🧩) → MoAI-Cowork → nhấp "Update"
```

### Nếu cài đặt từ GitHub

```
cd k-harness
git pull origin main
```

### Nếu cài đặt qua ZIP

1. Xóa plugin hiện có: Plugin (🧩) → MoAI-Cowork → **Remove**
2. Tải xuống tệp ZIP mới nhất
3. Lặp lại quy trình cài đặt thủ công Phương Pháp 4

### Kiểm tra phiên bản

Nhập `/moai status` trong trò chuyện để xác minh phiên bản hiện được cài đặt.

---

## Khắc Phục Sự Cố

### Plugin không được nhận dạng

1. Thoát hoàn toàn và khởi động lại Claude Desktop
2. Kiểm tra xem MoAI-Cowork có xuất hiện trong danh sách Plugin (🧩) ở chế độ Cowork không
3. Nếu không, hãy thử cài đặt lại

### Lỗi khi `/moai init`

1. Nhập `/moai doctor` để chạy chẩn đoán môi trường
2. Nếu hồ sơ toàn cầu của bạn bị hỏng, đặt lại bằng `/moai profile --reset`

### Harness không tải

1. Kiểm tra xem `.moai/config.json` có tồn tại trong thư mục dự án của bạn không
2. Nếu không, hãy khởi tạo lại bằng `/moai init`

### Dữ liệu định địa phương không được thu thập

- Hàn Quốc: Sử dụng dữ liệu tích hợp (không cần tìm kiếm web)
- Các quốc gia khác: Cần kết nối Internet và công cụ tìm kiếm web

---

## Bắt Đầu Nhanh

### Bước 1: Khởi Tạo

```
/moai init
```

MoAI tiến hành phỏng vấn tương tác để thu thập hồ sơ của bạn (tên, vai trò, công ty, locale).

### Bước 2: Duyệt Danh Mục Harness

```
/moai catalog
```

Xem danh sách đầy đủ của 100 harness trên 10 danh mục.

### Bước 3: Gửi Yêu Cầu Bằng Ngôn Ngữ Tự Nhiên

```
Giúp tôi nghiên cứu thị trường
```

MoAI tự động phát hiện harness `market-research` và chạy ở chế độ chuyên gia.

---

## Danh Mục 100 Harness

| # | Danh Mục | Số Lượng | Harness Mẫu |
|---|----------|---------|-----------------|
| 1 | Nội Dung & Sáng Tạo | 10 | copywriting, youtube-production, podcast-studio, book-publishing |
| 2 | Kinh Doanh & Chiến Lược | 10 | business-model-canvas, competitive-analysis, startup-launcher, pricing-strategy |
| 3 | Marketing & Tăng Trưởng | 10 | brand-identity, growth-hacking, social-media-manager, influencer-strategy |
| 4 | Giáo Dục & Nghiên Cứu | 10 | course-builder, thesis-advisor, exam-prep, language-tutor |
| 5 | Pháp Lý & Tuân Thủ | 10 | contract-analyzer, compliance-checker, patent-drafter, privacy-engineer |
| 6 | Lối Sống | 10 | travel-planner, wedding-planner, meal-planner, fitness-program |
| 7 | Giao Tiếp & Tài Liệu | 10 | presentation-designer, report-generator, technical-writer, proposal-writer |
| 8 | Vận Hành & Nhân Sự | 10 | hiring-pipeline, onboarding-system, operations-manual, crisis-communication |
| 9 | Tài Chính & Thương Mại | 10 | accounting-tax, financial-modeler, import-export, invoice-mgmt |
| 10 | Sản Phẩm & Đổi Mới | 10 | product-manager, ai-strategy, ux-research, sales-enablement |

Xem danh sách đầy đủ 100 harness bằng `/moai catalog`.

---

## Các Lệnh Chính

| Lệnh | Mô Tả |
|---------|-------------|
| `/moai init` | Khởi tạo — thu thập hồ sơ và cài đặt harness |
| `/moai catalog` | Duyệt danh mục 100 harness |
| `/moai status` | Kiểm tra harness đã cài đặt và trạng thái phát triển |
| `/moai evolve` | Chạy chu kỳ phát triển tự học |
| `/moai profile` | Xem/chỉnh sửa hồ sơ toàn cầu |
| `/moai doctor` | Chạy chẩn đoán môi trường |
| `/moai help` | Hiển thị các lệnh khả dụng |

---

## Kiến Trúc

```
Layer 0: auto-memory (global) — hồ sơ người dùng, lịch sử harness
Layer 1: plugin (read-only) — 100 base harness (en/ nguồn duy nhất, bản địa hóa thời gian chạy)
Layer 2: .claude/CLAUDE.md + rules/ — nhân vật
Layer 3: .moai/ (read/write) — bối cảnh miền, dữ liệu tiến hóa
Layer 4: auto-memory learning — tích lũy phản hồi liên phiên
```

---

## Giấy Phép

MIT License — tự do sử dụng, sửa đổi và phân phối

---

## GitHub

- **Repository**: [modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **Issues/Suggestions**: [GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork: Gặp gỡ chuyên gia AI của bạn.**

*Version 0.1.3 | Last Updated: 2026-04-08*
