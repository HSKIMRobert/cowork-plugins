<div align="center">

# 🗿 MoAI-Cowork

**100 Selbstlernende Domain-Harnesses — Ihre persönlichen KI-Experten**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [한국어](README.md) | [日本語](README-ja.md) | [Español](README-es.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## Was ist MoAI?

**MoAI-Cowork** ist ein Plugin für Claude Cowork, das 100 Domain-Expert-Harnesses durch ein selbstlernendes KI-Assistenz-System bereitstellt.

Ein Harness ist ein KI-Experten-Modul, das domänenspezifisches Wissen, Workflows, Lieferformate und Kontext-Sammlungsprotokolle in einem Paket bündelt. Nach der Installation verwandelt sich MoAI in einen Domain-Experten und liefert strukturierte Ergebnisse.

**Wichtigste Merkmale:**

- 10 Kategorien × 100 Harnesses — Inhalte, Marketing, Business, Bildung, Recht, Lebensstil, Kommunikation, Betrieb, Finanzen und Produkt/Innovation
- 5-schichtiges Selbstlern-Architektur — entwickelt sich über die Zeit an den Benutzer an
- Globales Profil — teilen Sie persönliche + Unternehmensinformationen über Sessions hinweg, keine erneute Eingabe erforderlich
- 17 Sprachunterstützung — EN als einzige Quelle + Runtime-Lokalisierung
- Weltweite Locale-Unterstützung — geben Sie Ihr Arbeitsland ein und MoAI sammelt automatisch Steuerrecht, Arbeitsrecht, Datenschutz und Geschäftspraktiken durch Web-Suche

---

## Installation

### Methode 1: Installation aus Claude Cowork Marketplace (Empfohlen)

1. Starten Sie die **Claude Desktop** App
2. Geben Sie **Cowork** Modus unten links ein
3. Klicken Sie auf das **Plugin (🧩)** Symbol neben der Chat-Eingabe
4. Suchen Sie nach `moai-cowork` im Marketplace
5. Finden Sie **MoAI-Cowork** und klicken Sie auf **Install**
6. Geben Sie nach der Installation `/moai init` im Chat ein, um das initiale Setup zu starten

### Methode 2: Installation aus K-Harness Marketplace

K-Harness ist der Marketplace, der MoAI-Cowork enthält.

```
# Schritt 1: Marketplace hinzufügen
/plugin marketplace add modu-ai/k-harness

# Schritt 2: MoAI-Cowork Plugin installieren
/plugin install moai-cowork@k-harness
```

### Methode 3: Direkte Installation von GitHub

```
# Repository klonen
git clone https://github.com/modu-ai/k-harness.git

# Zum Plugin-Verzeichnis navigieren
cd k-harness/plugins/moai-cowork

# Manuell in Claude Desktop laden
# Cowork Modus → Plugin (🧩) → "Aus Datei installieren" → moai-cowork Ordner auswählen
```

### Methode 4: Manuelle Installation via ZIP

1. Laden Sie die neueste `moai-cowork-v0.1.3.zip` von der [GitHub Releases](https://github.com/modu-ai/k-harness/releases) Seite herunter
2. Öffnen Sie Claude Desktop → treten Sie in Cowork Modus ein
3. Klicken Sie auf das Plugin (🧩) Symbol → **Aus Datei installieren**
4. Wählen Sie die heruntergeladene ZIP-Datei aus

---

## Aktualisierung

### Falls über Marketplace installiert

```
# K-Harness Marketplace aktualisieren
/plugin marketplace update k-harness

# Oder über Cowork UI:
# Plugin (🧩) → MoAI-Cowork → klicken Sie auf "Update"
```

### Falls von GitHub installiert

```
cd k-harness
git pull origin main
```

### Falls via ZIP installiert

1. Entfernen Sie das vorhandene Plugin: Plugin (🧩) → MoAI-Cowork → **Remove**
2. Laden Sie die neueste ZIP-Datei herunter
3. Wiederholen Sie den Prozess der manuellen Installation aus Methode 4

### Version überprüfen

Geben Sie `/moai status` im Chat ein, um die derzeit installierte Version zu überprüfen.

---

## Fehlerbehebung

### Plugin nicht erkannt

1. Beenden Sie Claude Desktop vollständig und starten Sie es neu
2. Überprüfen Sie, ob MoAI-Cowork in der Plugin-Liste (🧩) im Cowork Modus angezeigt wird
3. Falls nicht, versuchen Sie eine Neuinstallation

### Fehler bei `/moai init`

1. Geben Sie `/moai doctor` ein, um die Umgebungsdiagnose auszuführen
2. Falls Ihr globales Profil beschädigt ist, setzen Sie es mit `/moai profile --reset` zurück

### Harness lädt nicht

1. Überprüfen Sie, ob `.moai/config.json` in Ihrem Projektordner existiert
2. Falls nicht, initialisieren Sie es erneut mit `/moai init`

### Lokalisierungsdaten nicht erfasst

- Südkorea: Verwendet integrierte Daten (keine Web-Suche erforderlich)
- Andere Länder: Benötigt Internetverbindung und Web-Such-Tools

---

## Schnelleinstieg

### Schritt 1: Initialisieren

```
/moai init
```

MoAI führt ein interaktives Interview durch, um Ihr Profil (Name, Rolle, Unternehmen, Locale) zu erfassen.

### Schritt 2: Harness-Katalog durchsuchen

```
/moai catalog
```

Sehen Sie sich die vollständige Liste der 100 Harnesses in 10 Kategorien an.

### Schritt 3: Machen Sie eine Anfrage in natürlicher Sprache

```
Hilf mir bei einer Marktforschung
```

MoAI erkennt automatisch den `market-research` Harness und läuft im Expert-Modus.

---

## 100 Harness-Katalog

| # | Kategorie | Anzahl | Beispiel-Harnesses |
|---|----------|-------|-----------------|
| 1 | Inhalte & Kreativität | 10 | copywriting, youtube-production, podcast-studio, book-publishing |
| 2 | Business & Strategie | 10 | business-model-canvas, competitive-analysis, startup-launcher, pricing-strategy |
| 3 | Marketing & Wachstum | 10 | brand-identity, growth-hacking, social-media-manager, influencer-strategy |
| 4 | Bildung & Forschung | 10 | course-builder, thesis-advisor, exam-prep, language-tutor |
| 5 | Recht & Compliance | 10 | contract-analyzer, compliance-checker, patent-drafter, privacy-engineer |
| 6 | Lebensstil | 10 | travel-planner, wedding-planner, meal-planner, fitness-program |
| 7 | Kommunikation & Dokumentation | 10 | presentation-designer, report-generator, technical-writer, proposal-writer |
| 8 | Betrieb & HR | 10 | hiring-pipeline, onboarding-system, operations-manual, crisis-communication |
| 9 | Finanzen & Handel | 10 | accounting-tax, financial-modeler, import-export, invoice-mgmt |
| 10 | Produkt & Innovation | 10 | product-manager, ai-strategy, ux-research, sales-enablement |

Siehe die vollständige Liste der 100 Harnesses mit `/moai catalog`.

---

## Wichtige Befehle

| Befehl | Beschreibung |
|---------|-------------|
| `/moai init` | Initialisieren — sammeln Sie das Profil und installieren Sie Harness |
| `/moai catalog` | Durchsuchen Sie den 100 Harness-Katalog |
| `/moai status` | Überprüfen Sie den installierten Harness und Evolve-Status |
| `/moai evolve` | Führen Sie einen Selbstlern-Evolve-Zyklus aus |
| `/moai profile` | Zeigen Sie an/bearbeiten Sie das globale Profil |
| `/moai doctor` | Führen Sie die Umgebungsdiagnose aus |
| `/moai help` | Zeigen Sie verfügbare Befehle an |

---

## Architektur

```
Layer 0: auto-memory (global) — Benutzerprofil, Harness-Verlauf
Layer 1: plugin (read-only) — 100 Basis-Harnesses (en/ einzige Quelle, Runtime-Lokalisierung)
Layer 2: .claude/CLAUDE.md + rules/ — Persona
Layer 3: .moai/ (read/write) — Domain-Kontext, Evolution-Daten
Layer 4: auto-memory learning — Sitzungsübergreifende Feedback-Akkumulation
```

---

## Lizenz

MIT License — frei nutzbar, modifizierbar und verteilbar

---

## GitHub

- **Repository**: [modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **Issues/Vorschläge**: [GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork: Treffen Sie Ihre KI-Experten.**

*Version 0.1.3 | Last Updated: 2026-04-08*
