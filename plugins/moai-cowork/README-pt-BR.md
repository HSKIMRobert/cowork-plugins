<div align="center">

# 🗿 MoAI-Cowork

**100 Harnesses de Domínio Auto-Evoluíveis — Seus Especialistas em IA Pessoais**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [한국어](README.md) | [日本語](README-ja.md) | [Español](README-es.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## O que é MoAI?

**MoAI-Cowork** é um Plugin para Claude Cowork que fornece 100 harnesses de especialistas de domínio através de um sistema de assistente IA com aprendizado automático.

Um harness é um módulo especialista de IA que agrupa conhecimento específico de domínio, fluxos de trabalho, formatos de entrega e protocolos de coleta de contexto em um único pacote. Uma vez instalado, o MoAI se transforma em um especialista de domínio e oferece resultados estruturados.

**Recursos principais:**

- 10 categorias × 100 harnesses — conteúdo, marketing, negócios, educação, jurídico, estilo de vida, comunicação, operações, finanças e produto/inovação
- Arquitetura de aprendizado automático em 5 camadas — evolui e se adapta ao usuário ao longo do tempo
- Perfil global — compartilhe informações pessoais e da empresa em todas as sessões, sem necessidade de re-entrada
- Suporte para 17 idiomas — fonte única EN + localização em tempo de execução
- Suporte de localidade mundial — insira seu país de trabalho e o MoAI coleta automaticamente leis fiscais, leis trabalhistas, proteção de dados e práticas comerciais via busca na web

---

## Instalação

### Método 1: Instalar do Marketplace Claude Cowork (Recomendado)

1. Inicie o aplicativo **Claude Desktop**
2. Entre no modo **Cowork** no canto inferior esquerdo
3. Clique no ícone **Plugin (🧩)** ao lado da entrada de chat
4. Procure por `moai-cowork` no marketplace
5. Encontre **MoAI-Cowork** e clique em **Install**
6. Após a instalação, digite `/moai init` no chat para iniciar a configuração inicial

### Método 2: Instalar do Marketplace K-Harness

K-Harness é o marketplace que inclui MoAI-Cowork.

```
# Passo 1: Adicionar o marketplace
/plugin marketplace add modu-ai/k-harness

# Passo 2: Instalar plugin MoAI-Cowork
/plugin install moai-cowork@k-harness
```

### Método 3: Instalar Diretamente do GitHub

```
# Clonar o repositório
git clone https://github.com/modu-ai/k-harness.git

# Navegar para o diretório do Plugin
cd k-harness/plugins/moai-cowork

# Carregar manualmente em Claude Desktop
# Cowork mode → Plugin (🧩) → "Install from file" → selecione a pasta moai-cowork
```

### Método 4: Instalação Manual via ZIP

1. Baixe o arquivo `moai-cowork-v0.1.3.zip` mais recente da página [GitHub Releases](https://github.com/modu-ai/k-harness/releases)
2. Abra Claude Desktop → entre no modo Cowork
3. Clique no ícone Plugin (🧩) → **Install from file**
4. Selecione o arquivo ZIP baixado

---

## Atualização

### Se instalado via marketplace

```
# Atualizar marketplace K-Harness
/plugin marketplace update k-harness

# Ou via Cowork UI:
# Plugin (🧩) → MoAI-Cowork → clique em "Update"
```

### Se instalado do GitHub

```
cd k-harness
git pull origin main
```

### Se instalado via ZIP

1. Remova o Plugin existente: Plugin (🧩) → MoAI-Cowork → **Remove**
2. Baixe o arquivo ZIP mais recente
3. Repita o processo de instalação manual do Método 4

### Verificar versão

Digite `/moai status` no chat para verificar a versão atualmente instalada.

---

## Solução de Problemas

### Plugin não reconhecido

1. Saia completamente e reinicie Claude Desktop
2. Verifique se MoAI-Cowork aparece na lista Plugin (🧩) no modo Cowork
3. Se não aparecer, tente reinstalar

### Erro em `/moai init`

1. Digite `/moai doctor` para executar diagnósticos de ambiente
2. Se seu perfil global estiver corrompido, redefina com `/moai profile --reset`

### Harness não carregando

1. Verifique se `.moai/config.json` existe na pasta do seu projeto
2. Se não, reinicialize com `/moai init`

### Dados de localização não coletados

- Coréia: Usa dados incorporados (sem necessidade de busca na web)
- Outros países: Requer conexão com internet e ferramentas de busca na web

---

## Guia de Início Rápido

### Etapa 1: Inicializar

```
/moai init
```

MoAI realiza uma entrevista interativa para coletar seu perfil (nome, função, empresa, localidade).

### Etapa 2: Procurar no Catálogo de Harnesses

```
/moai catalog
```

Visualize a lista completa de 100 harnesses em 10 categorias.

### Etapa 3: Fazer uma Solicitação em Linguagem Natural

```
Me ajude a fazer uma pesquisa de mercado
```

MoAI detecta automaticamente o harness `market-research` e executa em modo especialista.

---

## Catálogo de 100 Harnesses

| # | Categoria | Quantidade | Harnesses de Exemplo |
|---|-----------|-----------|----------------------|
| 1 | Conteúdo & Criatividade | 10 | copywriting, youtube-production, podcast-studio, book-publishing |
| 2 | Negócios & Estratégia | 10 | business-model-canvas, competitive-analysis, startup-launcher, pricing-strategy |
| 3 | Marketing & Crescimento | 10 | brand-identity, growth-hacking, social-media-manager, influencer-strategy |
| 4 | Educação & Pesquisa | 10 | course-builder, thesis-advisor, exam-prep, language-tutor |
| 5 | Jurídico & Conformidade | 10 | contract-analyzer, compliance-checker, patent-drafter, privacy-engineer |
| 6 | Estilo de Vida | 10 | travel-planner, wedding-planner, meal-planner, fitness-program |
| 7 | Comunicação & Documentos | 10 | presentation-designer, report-generator, technical-writer, proposal-writer |
| 8 | Operações & RH | 10 | hiring-pipeline, onboarding-system, operations-manual, crisis-communication |
| 9 | Finanças & Comércio | 10 | accounting-tax, financial-modeler, import-export, invoice-mgmt |
| 10 | Produto & Inovação | 10 | product-manager, ai-strategy, ux-research, sales-enablement |

Veja a lista completa de 100 harnesses com `/moai catalog`.

---

## Comandos Principais

| Comando | Descrição |
|---------|-----------|
| `/moai init` | Inicializar — coletar perfil e instalar harness |
| `/moai catalog` | Procurar catálogo de 100 harnesses |
| `/moai status` | Verificar harness instalado e estado de evolução |
| `/moai evolve` | Executar ciclo de evolução com aprendizado automático |
| `/moai profile` | Visualizar/editar perfil global |
| `/moai doctor` | Executar diagnósticos de ambiente |
| `/moai help` | Mostrar comandos disponíveis |

---

## Arquitetura

```
Layer 0: auto-memory (global) — perfil do usuário, histórico de harness
Layer 1: plugin (somente leitura) — 100 harnesses base (fonte única en/, localização em tempo de execução)
Layer 2: .claude/CLAUDE.md + rules/ — persona
Layer 3: .moai/ (leitura/escrita) — contexto de domínio, dados de evolução
Layer 4: auto-memory learning — acumulação de feedback entre sessões
```

---

## Licença

Licença MIT — livre para usar, modificar e distribuir

---

## GitHub

- **Repositório**: [modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **Problemas/Sugestões**: [GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork: Conheça seus especialistas em IA.**

*Versão 0.1.3 | Última atualização: 2026-04-08*
