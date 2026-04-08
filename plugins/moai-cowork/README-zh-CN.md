<div align="center">

# 🗿 MoAI-Cowork

**100个自我进化的领域框架 — 您的个人AI专家**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [한국어](README.md) | [日本語](README-ja.md) | [Español](README-es.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## 什么是 MoAI？

**MoAI-Cowork** 是一款 Claude Cowork 插件，通过自学型AI助手系统提供100个领域专家框架。

框架是一个AI专家模块，将特定领域的知识、工作流程、交付物格式和上下文收集协议打包在一起。安装后，MoAI将转变为领域专家，提供结构化的结果。

**主要特性：**

- 10个类别 × 100个框架 — 内容、营销、商业、教育、法律、生活方式、沟通、运营、财务和产品/创新
- 5层自学架构 — 随时间推移不断进化和适应用户
- 全球档案 — 跨会话共享个人和公司信息，无需重新输入
- 支持17种语言 — 单一英文源 + 运行时本地化
- 全球地区支持 — 输入您的工作国家，MoAI将自动通过网络搜索收集税法、劳动法、数据保护和商业惯例

---

## 安装

### 方法1：从 Claude Cowork Marketplace 安装（推荐）

1. 启动 **Claude Desktop** 应用
2. 从左下角进入 **Cowork** 模式
3. 点击聊天输入框旁的 **Plugin（🧩）** 图标
4. 在marketplace中搜索 `moai-cowork`
5. 找到 **MoAI-Cowork** 并点击 **Install**
6. 安装后，在聊天中输入 `/moai init` 开始初始设置

### 方法2：从 K-Harness Marketplace 安装

K-Harness 是包含 MoAI-Cowork 的marketplace。

```
# 步骤1：添加marketplace
/plugin marketplace add modu-ai/k-harness

# 步骤2：安装 MoAI-Cowork 插件
/plugin install moai-cowork@k-harness
```

### 方法3：直接从 GitHub 安装

```
# 克隆仓库
git clone https://github.com/modu-ai/k-harness.git

# 导航到插件目录
cd k-harness/plugins/moai-cowork

# 在 Claude Desktop 中手动加载
# Cowork 模式 → Plugin（🧩）→ "Install from file" → 选择 moai-cowork 文件夹
```

### 方法4：通过 ZIP 手动安装

1. 从 [GitHub Releases](https://github.com/modu-ai/k-harness/releases) 页面下载最新的 `moai-cowork-v0.1.3.zip`
2. 打开 Claude Desktop → 进入 Cowork 模式
3. 点击 Plugin（🧩）图标 → **Install from file**
4. 选择下载的 ZIP 文件

---

## 更新

### 如果通过marketplace安装

```
# 更新 K-Harness marketplace
/plugin marketplace update k-harness

# 或通过 Cowork UI：
# Plugin（🧩）→ MoAI-Cowork → 点击 "Update"
```

### 如果从 GitHub 安装

```
cd k-harness
git pull origin main
```

### 如果通过 ZIP 安装

1. 删除现有插件：Plugin（🧩）→ MoAI-Cowork → **Remove**
2. 下载最新的 ZIP 文件
3. 重复方法4的手动安装流程

### 检查版本

在聊天中输入 `/moai status` 以验证当前安装的版本。

---

## 故障排除

### 插件未被识别

1. 完全关闭并重启 Claude Desktop
2. 检查 MoAI-Cowork 是否出现在 Cowork 模式中的 Plugin（🧩）列表中
3. 如果没有，请尝试重新安装

### `/moai init` 出现错误

1. 输入 `/moai doctor` 运行环境诊断
2. 如果您的全局档案已损坏，使用 `/moai profile --reset` 重置

### 框架未加载

1. 检查项目文件夹中是否存在 `.moai/config.json`
2. 如果没有，使用 `/moai init` 重新初始化

### 本地化数据未收集

- 韩国：使用内置数据（无需网络搜索）
- 其他国家：需要互联网连接和网络搜索工具

---

## 快速开始

### 步骤1：初始化

```
/moai init
```

MoAI进行交互式访谈，收集您的档案（名字、角色、公司、地区）。

### 步骤2：浏览框架目录

```
/moai catalog
```

查看跨越10个类别的完整100个框架列表。

### 步骤3：发出自然语言请求

```
帮我做市场调研
```

MoAI自动检测 `market-research` 框架并以专家模式运行。

---

## 100个框架目录

| # | 类别 | 数量 | 示例框架 |
|---|------|------|---------|
| 1 | 内容与创意 | 10 | copywriting, youtube-production, podcast-studio, book-publishing |
| 2 | 商业与战略 | 10 | business-model-canvas, competitive-analysis, startup-launcher, pricing-strategy |
| 3 | 营销与增长 | 10 | brand-identity, growth-hacking, social-media-manager, influencer-strategy |
| 4 | 教育与研究 | 10 | course-builder, thesis-advisor, exam-prep, language-tutor |
| 5 | 法律与合规 | 10 | contract-analyzer, compliance-checker, patent-drafter, privacy-engineer |
| 6 | 生活方式 | 10 | travel-planner, wedding-planner, meal-planner, fitness-program |
| 7 | 沟通与文档 | 10 | presentation-designer, report-generator, technical-writer, proposal-writer |
| 8 | 运营与人力资源 | 10 | hiring-pipeline, onboarding-system, operations-manual, crisis-communication |
| 9 | 财务与贸易 | 10 | accounting-tax, financial-modeler, import-export, invoice-mgmt |
| 10 | 产品与创新 | 10 | product-manager, ai-strategy, ux-research, sales-enablement |

使用 `/moai catalog` 查看完整的100个框架列表。

---

## 关键命令

| 命令 | 描述 |
|------|------|
| `/moai init` | 初始化 — 收集档案并安装框架 |
| `/moai catalog` | 浏览100个框架目录 |
| `/moai status` | 检查已安装框架和进化状态 |
| `/moai evolve` | 运行自学型进化周期 |
| `/moai profile` | 查看/编辑全球档案 |
| `/moai doctor` | 运行环境诊断 |
| `/moai help` | 显示可用命令 |

---

## 架构

```
第0层：auto-memory（全局）— 用户档案、框架历史
第1层：plugin（只读）— 100个基础框架（en/单一源、运行时本地化）
第2层：.claude/CLAUDE.md + rules/ — 人设
第3层：.moai/（读/写）— 领域上下文、进化数据
第4层：auto-memory learning — 跨会话反馈累积
```

---

## 许可证

MIT 许可证 — 可自由使用、修改和分发

---

## GitHub

- **仓库**：[modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **问题/建议**：[GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork：遇见您的AI专家。**

*版本 0.1.3 | 最后更新：2026-04-08*
