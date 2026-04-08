<div align="center">

# 🗿 MoAI-Cowork

**100 Self-Evolving Domain Harnesses — Your Personal AI Experts**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [한국어](README.md) | [日本語](README-ja.md) | [Español](README-es.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## What is MoAI?

**MoAI-Cowork** is a plugin for Claude Cowork that provides 100 domain expert harnesses through a self-learning AI assistant system.

A harness is an AI expert module that bundles domain-specific knowledge, workflows, deliverable formats, and context-collection protocols into one package. Once installed, MoAI transforms into a domain expert and delivers structured results.

**Key features:**

- 10 categories × 100 harnesses — content, marketing, business, education, legal, lifestyle, communication, operations, finance, and product/innovation
- 5-layer self-learning architecture — evolves and adapts to the user over time
- Global profile — share personal + company info across sessions, no re-entry needed
- 17 language support — EN single source + runtime localization
- Worldwide locale support — enter your work country and MoAI auto-collects tax law, labor law, data protection, and business practices via web search

---

## Installation

### Method 1: Install from Claude Cowork Marketplace (Recommended)

1. Launch the **Claude Desktop** app
2. Enter **Cowork** mode from the bottom-left
3. Click the **Plugin (🧩)** icon next to the chat input
4. Search for `moai-cowork` in the marketplace
5. Find **MoAI-Cowork** and click **Install**
6. After installation, type `/moai init` in chat to start the initial setup

### Method 2: Install from K-Harness Marketplace

K-Harness is the marketplace that includes MoAI-Cowork.

```
# Step 1: Add the marketplace
/plugin marketplace add modu-ai/k-harness

# Step 2: Install MoAI-Cowork plugin
/plugin install moai-cowork@k-harness
```

### Method 3: Install Directly from GitHub

```
# Clone the repository
git clone https://github.com/modu-ai/k-harness.git

# Navigate to the plugin directory
cd k-harness/plugins/moai-cowork

# Load manually in Claude Desktop
# Cowork mode → Plugin (🧩) → "Install from file" → select the moai-cowork folder
```

### Method 4: Manual Install via ZIP

1. Download the latest `moai-cowork-v0.1.3.zip` from the [GitHub Releases](https://github.com/modu-ai/k-harness/releases) page
2. Open Claude Desktop → enter Cowork mode
3. Click the Plugin (🧩) icon → **Install from file**
4. Select the downloaded ZIP file

---

## Updating

### If installed via marketplace

```
# Update K-Harness marketplace
/plugin marketplace update k-harness

# Or via Cowork UI:
# Plugin (🧩) → MoAI-Cowork → click "Update"
```

### If installed from GitHub

```
cd k-harness
git pull origin main
```

### If installed via ZIP

1. Remove the existing plugin: Plugin (🧩) → MoAI-Cowork → **Remove**
2. Download the latest ZIP file
3. Repeat the Method 4 manual installation process

### Check version

Type `/moai status` in chat to verify the currently installed version.

---

## Troubleshooting

### Plugin not recognized

1. Fully quit and restart Claude Desktop
2. Check if MoAI-Cowork appears in the Plugin (🧩) list in Cowork mode
3. If not, try reinstalling

### Error on `/moai init`

1. Type `/moai doctor` to run environment diagnostics
2. If your global profile is corrupted, reset it with `/moai profile --reset`

### Harness not loading

1. Check if `.moai/config.json` exists in your project folder
2. If not, re-initialize with `/moai init`

### Localization data not collected

- Korea: Uses built-in data (no web search needed)
- Other countries: Requires internet connection and web search tools

---

## Quick Start

### Step 1: Initialize

```
/moai init
```

MoAI conducts an interactive interview to collect your profile (name, role, company, locale).

### Step 2: Browse the Harness Catalog

```
/moai catalog
```

View the full list of 100 harnesses across 10 categories.

### Step 3: Make a Natural Language Request

```
Help me do market research
```

MoAI automatically detects the `market-research` harness and runs in expert mode.

---

## 100 Harness Catalog

| # | Category | Count | Sample Harnesses |
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

See the full list of 100 harnesses with `/moai catalog`.

---

## Key Commands

| Command | Description |
|---------|-------------|
| `/moai init` | Initialize — collect profile and install harness |
| `/moai catalog` | Browse 100 harness catalog |
| `/moai status` | Check installed harness and evolution state |
| `/moai evolve` | Run self-learning evolution cycle |
| `/moai profile` | View/edit global profile |
| `/moai doctor` | Run environment diagnostics |
| `/moai help` | Show available commands |

---

## Architecture

```
Layer 0: auto-memory (global) — user profile, harness history
Layer 1: plugin (read-only) — 100 base harnesses (en/ single source, runtime localization)
Layer 2: .claude/CLAUDE.md + rules/ — persona
Layer 3: .moai/ (read/write) — domain context, evolution data
Layer 4: auto-memory learning — cross-session feedback accumulation
```

---

## License

MIT License — free to use, modify, and distribute

---

## GitHub

- **Repository**: [modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **Issues/Suggestions**: [GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork: Meet Your AI Experts.**

*Version 0.1.3 | Last Updated: 2026-04-08*
