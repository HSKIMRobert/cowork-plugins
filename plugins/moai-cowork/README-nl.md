<div align="center">

# 🗿 MoAI-Cowork

**100 Zelf-Evoluerende Domein Harnesses — Uw Persoonlijke AI-Experts**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [한국어](README.md) | [日本語](README-ja.md) | [Español](README-es.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## Wat is MoAI?

**MoAI-Cowork** is een plugin voor Claude Cowork die 100 domein-expert harnesses levert via een zelf-lerend AI-assistent systeem.

Een harness is een AI-expert module die domeinspecifieke kennis, workflows, deliverable-formaten en context-verzamelingsprotocollen in één pakket bundelt. Nadat het is geïnstalleerd, transformeert MoAI in een domein-expert en levert gestructureerde resultaten.

**Sleutelfuncties:**

- 10 categorieën × 100 harnesses — inhoud, marketing, zaken, onderwijs, juridisch, levensstijl, communicatie, operaties, financiën en product/innovatie
- 5-laags zelf-lerend architectuur — evolueert en past zich aan de gebruiker aan over tijd
- Globaal profiel — deel persoonlijke + bedrijfsinformatie over sessies heen, geen herboeking nodig
- Ondersteuning voor 17 talen — EN enkele bron + runtime-lokalisatie
- Wereldwijde locale-ondersteuning — voer uw werkland in en MoAI verzamelt automatisch belastingwetgeving, arbeidswetgeving, gegevensbescherming en bedrijfspraktijken via websearch

---

## Installatie

### Methode 1: Installeer vanuit Claude Cowork Marketplace (Aanbevolen)

1. Start de **Claude Desktop** app
2. Ga naar **Cowork** modus vanuit de onderste linkerkant
3. Klik op het **Plugin (🧩)** pictogram naast de chat-invoer
4. Zoek naar `moai-cowork` in de marketplace
5. Zoek **MoAI-Cowork** en klik op **Install**
6. Na installatie, typ `/moai init` in de chat om de initiële setup te starten

### Methode 2: Installeer vanuit K-Harness Marketplace

K-Harness is de marketplace die MoAI-Cowork bevat.

```
# Stap 1: Voeg de marketplace toe
/plugin marketplace add modu-ai/k-harness

# Stap 2: Installeer MoAI-Cowork plugin
/plugin install moai-cowork@k-harness
```

### Methode 3: Installeer rechtstreeks vanuit GitHub

```
# Kloon de repository
git clone https://github.com/modu-ai/k-harness.git

# Navigeer naar de plugin directory
cd k-harness/plugins/moai-cowork

# Laad handmatig in Claude Desktop
# Cowork modus → Plugin (🧩) → "Install from file" → selecteer de moai-cowork map
```

### Methode 4: Handmatige installatie via ZIP

1. Download de meest recente `moai-cowork-v0.1.3.zip` van de [GitHub Releases](https://github.com/modu-ai/k-harness/releases) pagina
2. Open Claude Desktop → ga naar Cowork modus
3. Klik op het Plugin (🧩) pictogram → **Install from file**
4. Selecteer het gedownloade ZIP-bestand

---

## Bijwerken

### Indien geïnstalleerd via marketplace

```
# Update K-Harness marketplace
/plugin marketplace update k-harness

# Of via Cowork UI:
# Plugin (🧩) → MoAI-Cowork → klik op "Update"
```

### Indien geïnstalleerd vanuit GitHub

```
cd k-harness
git pull origin main
```

### Indien geïnstalleerd via ZIP

1. Verwijder de bestaande plugin: Plugin (🧩) → MoAI-Cowork → **Remove**
2. Download het meest recente ZIP-bestand
3. Herhaal het handmatige installatieproces van Methode 4

### Check versie

Typ `/moai status` in de chat om de momenteel geïnstalleerde versie te verifiëren.

---

## Problemen oplossen

### Plugin niet herkend

1. Sluit Claude Desktop volledig af en start opnieuw
2. Controleer of MoAI-Cowork in de Plugin (🧩) lijst in Cowork modus verschijnt
3. Indien niet, probeer reinstallatie

### Fout op `/moai init`

1. Typ `/moai doctor` om omgevingsdiagnostiek uit te voeren
2. Indien uw globale profiel is beschadigd, stel het opnieuw in met `/moai profile --reset`

### Harness laadt niet

1. Controleer of `.moai/config.json` bestaat in uw projectmap
2. Indien niet, herinitialiseer met `/moai init`

### Lokalisatiegegevens niet verzameld

- Korea: Gebruikt ingebouwde gegevens (geen websearch nodig)
- Andere landen: Vereist internetverbinding en websearch-tools

---

## Snelle Start

### Stap 1: Initialiseer

```
/moai init
```

MoAI voert een interactief interview uit om uw profiel in te vullen (naam, functie, bedrijf, locale).

### Stap 2: Blader door de Harness-catalogus

```
/moai catalog
```

Bekijk de volledige lijst van 100 harnesses in 10 categorieën.

### Stap 3: Doen een Natuurlijke Taal Verzoek

```
Help me met een marktonderzoek
```

MoAI detecteert automatisch de `market-research` harness en draait in expert modus.

---

## 100 Harness-catalogus

| # | Categorie | Aantal | Voorbeeldharnessen |
|---|----------|--------|-----------------|
| 1 | Inhoud & Creatief | 10 | copywriting, youtube-production, podcast-studio, book-publishing |
| 2 | Zaken & Strategie | 10 | business-model-canvas, competitive-analysis, startup-launcher, pricing-strategy |
| 3 | Marketing & Groei | 10 | brand-identity, growth-hacking, social-media-manager, influencer-strategy |
| 4 | Onderwijs & Onderzoek | 10 | course-builder, thesis-advisor, exam-prep, language-tutor |
| 5 | Juridisch & Compliance | 10 | contract-analyzer, compliance-checker, patent-drafter, privacy-engineer |
| 6 | Levensstijl | 10 | travel-planner, wedding-planner, meal-planner, fitness-program |
| 7 | Communicatie & Documenten | 10 | presentation-designer, report-generator, technical-writer, proposal-writer |
| 8 | Operaties & HR | 10 | hiring-pipeline, onboarding-system, operations-manual, crisis-communication |
| 9 | Financiën & Handel | 10 | accounting-tax, financial-modeler, import-export, invoice-mgmt |
| 10 | Product & Innovatie | 10 | product-manager, ai-strategy, ux-research, sales-enablement |

Bekijk de volledige lijst van 100 harnesses met `/moai catalog`.

---

## Sleutelcommando's

| Commando | Beschrijving |
|---------|-------------|
| `/moai init` | Initialiseer — verzamel profiel en installeer harness |
| `/moai catalog` | Blader door 100 harness-catalogus |
| `/moai status` | Controleer geïnstalleerde harness en evolutietoestand |
| `/moai evolve` | Voer zelf-lerend evolutiecyclus uit |
| `/moai profile` | Bekijk/bewerk globaal profiel |
| `/moai doctor` | Voer omgevingsdiagnostiek uit |
| `/moai help` | Toon beschikbare commando's |

---

## Architectuur

```
Laag 0: auto-memory (globaal) — gebruikersprofiel, harness-historie
Laag 1: plugin (alleen-lezen) — 100 basisharnesses (en/ enkele bron, runtime-lokalisatie)
Laag 2: .claude/CLAUDE.md + rules/ — persona
Laag 3: .moai/ (lezen/schrijven) — domeincontext, evolutiegegevens
Laag 4: auto-memory learning — cross-session feedbackaccumulatie
```

---

## Licentie

MIT License — vrij te gebruiken, aanpassen en distribueren

---

## GitHub

- **Repository**: [modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **Issues/Suggesties**: [GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork: Ontmoet uw AI-experts.**

*Version 0.1.3 | Last Updated: 2026-04-08*
