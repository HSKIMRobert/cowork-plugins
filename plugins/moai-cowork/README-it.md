<div align="center">

# 🗿 MoAI-Cowork

**100 Self-Evolving Domain Harnesses — I tuoi esperti personali in IA**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [한국어](README.md) | [日本語](README-ja.md) | [Español](README-es.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## Cos'è MoAI?

**MoAI-Cowork** è un plugin per Claude Cowork che fornisce 100 harness di esperti di dominio attraverso un sistema di assistente IA auto-apprendente.

Un harness è un modulo esperto in IA che raggruppa conoscenze specifiche del dominio, flussi di lavoro, formati consegnabili e protocolli di raccolta del contesto in un unico pacchetto. Una volta installato, MoAI si trasforma in un esperto di dominio e fornisce risultati strutturati.

**Caratteristiche principali:**

- 10 categorie × 100 harness — contenuti, marketing, affari, educazione, legale, stile di vita, comunicazione, operazioni, finanza e prodotto/innovazione
- Architettura auto-apprendente a 5 livelli — evolve e si adatta all'utente nel tempo
- Profilo globale — condividi informazioni personali e aziendali tra le sessioni, senza necessità di reinserimento
- Supporto per 17 lingue — singola fonte EN + localizzazione runtime
- Supporto internazionale — inserisci il tuo paese di lavoro e MoAI raccoglie automaticamente leggi fiscali, leggi sul lavoro, protezione dei dati e pratiche commerciali tramite ricerca web

---

## Installazione

### Metodo 1: Installa dal Claude Cowork Marketplace (Consigliato)

1. Avvia l'app **Claude Desktop**
2. Accedi alla modalità **Cowork** dal basso a sinistra
3. Fai clic sull'icona **Plugin (🧩)** accanto all'input della chat
4. Cerca `moai-cowork` nel marketplace
5. Trova **MoAI-Cowork** e fai clic su **Install**
6. Dopo l'installazione, digita `/moai init` nella chat per avviare la configurazione iniziale

### Metodo 2: Installa dal K-Harness Marketplace

K-Harness è il marketplace che include MoAI-Cowork.

```
# Passaggio 1: Aggiungi il marketplace
/plugin marketplace add modu-ai/k-harness

# Passaggio 2: Installa il plugin MoAI-Cowork
/plugin install moai-cowork@k-harness
```

### Metodo 3: Installa direttamente da GitHub

```
# Clona il repository
git clone https://github.com/modu-ai/k-harness.git

# Naviga nella directory del plugin
cd k-harness/plugins/moai-cowork

# Carica manualmente in Claude Desktop
# Modalità Cowork → Plugin (🧩) → "Install from file" → seleziona la cartella moai-cowork
```

### Metodo 4: Installazione manuale tramite ZIP

1. Scarica il file `moai-cowork-v0.1.3.zip` più recente dalla pagina [GitHub Releases](https://github.com/modu-ai/k-harness/releases)
2. Apri Claude Desktop → accedi alla modalità Cowork
3. Fai clic sull'icona Plugin (🧩) → **Install from file**
4. Seleziona il file ZIP scaricato

---

## Aggiornamento

### Se installato tramite marketplace

```
# Aggiorna il marketplace K-Harness
/plugin marketplace update k-harness

# Oppure tramite interfaccia Cowork:
# Plugin (🧩) → MoAI-Cowork → fai clic su "Update"
```

### Se installato da GitHub

```
cd k-harness
git pull origin main
```

### Se installato tramite ZIP

1. Rimuovi il plugin esistente: Plugin (🧩) → MoAI-Cowork → **Remove**
2. Scarica il file ZIP più recente
3. Ripeti il processo di installazione manuale del Metodo 4

### Verifica versione

Digita `/moai status` nella chat per verificare la versione attualmente installata.

---

## Risoluzione dei problemi

### Plugin non riconosciuto

1. Esci completamente e riavvia Claude Desktop
2. Verifica se MoAI-Cowork appare nell'elenco Plugin (🧩) in modalità Cowork
3. Se no, prova a reinstallare

### Errore su `/moai init`

1. Digita `/moai doctor` per eseguire diagnostica ambientale
2. Se il tuo profilo globale è corrotto, ripristinalo con `/moai profile --reset`

### Harness non si carica

1. Verifica se `.moai/config.json` esiste nella cartella del tuo progetto
2. Se no, reinizializza con `/moai init`

### Dati di localizzazione non raccolti

- Corea: Utilizza dati integrati (non richiede ricerca web)
- Altri paesi: Richiede connessione internet e strumenti di ricerca web

---

## Avvio rapido

### Passaggio 1: Inizializza

```
/moai init
```

MoAI conduce un'intervista interattiva per raccogliere il tuo profilo (nome, ruolo, azienda, localizzazione).

### Passaggio 2: Sfoglia il catalogo Harness

```
/moai catalog
```

Visualizza l'elenco completo di 100 harness in 10 categorie.

### Passaggio 3: Effettua una richiesta in linguaggio naturale

```
Aiutami a fare una ricerca di mercato
```

MoAI rileva automaticamente l'harness `market-research` e viene eseguito in modalità esperto.

---

## Catalogo 100 Harness

| # | Categoria | Numero | Harness di esempio |
|---|----------|--------|-----------------|
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

Visualizza l'elenco completo di 100 harness con `/moai catalog`.

---

## Comandi chiave

| Comando | Descrizione |
|---------|-------------|
| `/moai init` | Inizializza — raccogli profilo e installa harness |
| `/moai catalog` | Sfoglia il catalogo 100 harness |
| `/moai status` | Verifica l'harness installato e lo stato di evoluzione |
| `/moai evolve` | Esegui il ciclo di evoluzione auto-apprendente |
| `/moai profile` | Visualizza/modifica il profilo globale |
| `/moai doctor` | Esegui la diagnostica ambientale |
| `/moai help` | Mostra i comandi disponibili |

---

## Architettura

```
Layer 0: auto-memory (globale) — profilo utente, cronologia harness
Layer 1: plugin (sola lettura) — 100 harness di base (en/ singola fonte, localizzazione runtime)
Layer 2: .claude/CLAUDE.md + rules/ — persona
Layer 3: .moai/ (lettura/scrittura) — contesto di dominio, dati di evoluzione
Layer 4: auto-memory learning — accumulo di feedback tra sessioni
```

---

## Licenza

MIT License — libero da usare, modificare e distribuire

---

## GitHub

- **Repository**: [modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **Issues/Suggestions**: [GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork: Incontra i tuoi esperti IA.**

*Version 0.1.3 | Last Updated: 2026-04-08*
