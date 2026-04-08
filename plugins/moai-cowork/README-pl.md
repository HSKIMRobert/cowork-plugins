<div align="center">

# 🗿 MoAI-Cowork

**100 Samorozwijających się Haranów Domenowych — Twoi Osobisty Eksperci AI**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [한국어](README.md) | [日本語](README-ja.md) | [Español](README-es.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## Co to jest MoAI?

**MoAI-Cowork** to plugin dla Claude Cowork, który zapewnia 100 haranów ekspertów domenowych poprzez system samorozwijającego się asystenta AI.

Haran to moduł eksperta AI, który łączy wiedzę specyficzną dla domeny, przepływy pracy, formaty wyników oraz protokoły gromadzenia kontekstu w jeden pakiet. Po zainstalowaniu MoAI przekształca się w eksperta domenowego i dostarcza strukturalne wyniki.

**Główne funkcje:**

- 10 kategorii × 100 haranów — treści, marketing, biznes, edukacja, prawo, styl życia, komunikacja, operacje, finanse oraz produkty/innowacje
- 5-warstwowa architektura samorozwojowa — ewoluuje i dostosowuje się do użytkownika w miarze upływu czasu
- Globalny profil — udostępniaj osobiste i firmowe informacje między sesjami, bez konieczności ponownego wpisywania
- Obsługa 17 języków — jedno źródło EN + lokalizacja w środowisku uruchomieniowym
- Obsługa światowych ustawień lokalnych — wprowadź kraj swojej pracy, a MoAI automatycznie zbiera prawo podatkowe, prawo pracy, ochronę danych i praktyki biznesowe poprzez wyszukiwanie w sieci

---

## Instalacja

### Metoda 1: Instalacja z Marketplace Claude Cowork (Rekomendowana)

1. Uruchom aplikację **Claude Desktop**
2. Wejdź w tryb **Cowork** z lewego dolnego rogu
3. Kliknij ikonę **Plugin (🧩)** obok wejścia czatu
4. Wyszukaj `moai-cowork` w marketplace
5. Znajdź **MoAI-Cowork** i kliknij **Install**
6. Po instalacji wpisz `/moai init` w czacie, aby rozpocząć wstępną konfigurację

### Metoda 2: Instalacja z K-Harness Marketplace

K-Harness to marketplace, który zawiera MoAI-Cowork.

```
# Krok 1: Dodaj marketplace
/plugin marketplace add modu-ai/k-harness

# Krok 2: Zainstaluj plugin MoAI-Cowork
/plugin install moai-cowork@k-harness
```

### Metoda 3: Instalacja bezpośrednio z GitHub

```
# Sklonuj repozytorium
git clone https://github.com/modu-ai/k-harness.git

# Przejdź do katalogu pluginu
cd k-harness/plugins/moai-cowork

# Załaduj ręcznie w Claude Desktop
# Tryb Cowork → Plugin (🧩) → "Install from file" → wybierz folder moai-cowork
```

### Metoda 4: Ręczna instalacja przez ZIP

1. Pobierz najnowszy plik `moai-cowork-v0.1.3.zip` ze strony [GitHub Releases](https://github.com/modu-ai/k-harness/releases)
2. Otwórz Claude Desktop → wejdź w tryb Cowork
3. Kliknij ikonę Plugin (🧩) → **Install from file**
4. Wybierz pobrany plik ZIP

---

## Aktualizacja

### Jeśli zainstalowano z marketplace

```
# Aktualizuj marketplace K-Harness
/plugin marketplace update k-harness

# Lub poprzez UI Cowork:
# Plugin (🧩) → MoAI-Cowork → kliknij "Update"
```

### Jeśli zainstalowano z GitHub

```
cd k-harness
git pull origin main
```

### Jeśli zainstalowano przez ZIP

1. Usuń istniejący plugin: Plugin (🧩) → MoAI-Cowork → **Remove**
2. Pobierz najnowszy plik ZIP
3. Powtórz proces instalacji ręcznej z Metody 4

### Sprawdź wersję

Wpisz `/moai status` w czacie, aby sprawdzić aktualnie zainstalowaną wersję.

---

## Rozwiązywanie problemów

### Plugin nie jest rozpoznawany

1. Całkowicie zamknij i ponownie uruchom Claude Desktop
2. Sprawdź, czy MoAI-Cowork pojawia się na liście Plugin (🧩) w trybie Cowork
3. Jeśli nie, spróbuj ponownie zainstalować

### Błąd podczas `/moai init`

1. Wpisz `/moai doctor`, aby uruchomić diagnostykę środowiska
2. Jeśli twój globalny profil jest uszkodzony, zresetuj go za pomocą `/moai profile --reset`

### Haran nie właduje się

1. Sprawdź, czy plik `.moai/config.json` istnieje w folderze projektu
2. Jeśli nie, ponownie zainicjuj za pomocą `/moai init`

### Dane lokalizacji nie są zbierane

- Korea: Używa wbudowanych danych (nie jest wymagane wyszukiwanie w sieci)
- Inne kraje: Wymaga połączenia internetowego i narzędzi wyszukiwania w sieci

---

## Szybki Start

### Krok 1: Inicjalizacja

```
/moai init
```

MoAI przeprowadza interaktywny wywiad, aby zebrać twój profil (imię, rolę, firmę, ustawienia lokalne).

### Krok 2: Przeglądaj Katalog Haranów

```
/moai catalog
```

Wyświetl pełną listę 100 haranów w 10 kategoriach.

### Krok 3: Złóż naturalny wniosek

```
Pomóż mi przeprowadzić badanie rynku
```

MoAI automatycznie wykrywa haran `market-research` i uruchamia się w trybie eksperta.

---

## Katalog 100 Haranów

| # | Kategoria | Liczba | Przykładowe Harany |
|---|----------|--------|-----------------|
| 1 | Treści & Kreatywność | 10 | copywriting, youtube-production, podcast-studio, book-publishing |
| 2 | Biznes & Strategia | 10 | business-model-canvas, competitive-analysis, startup-launcher, pricing-strategy |
| 3 | Marketing & Wzrost | 10 | brand-identity, growth-hacking, social-media-manager, influencer-strategy |
| 4 | Edukacja & Badania | 10 | course-builder, thesis-advisor, exam-prep, language-tutor |
| 5 | Prawo & Zgodność | 10 | contract-analyzer, compliance-checker, patent-drafter, privacy-engineer |
| 6 | Styl Życia | 10 | travel-planner, wedding-planner, meal-planner, fitness-program |
| 7 | Komunikacja & Dokumenty | 10 | presentation-designer, report-generator, technical-writer, proposal-writer |
| 8 | Operacje & HR | 10 | hiring-pipeline, onboarding-system, operations-manual, crisis-communication |
| 9 | Finanse & Handel | 10 | accounting-tax, financial-modeler, import-export, invoice-mgmt |
| 10 | Produkt & Innowacje | 10 | product-manager, ai-strategy, ux-research, sales-enablement |

Wyświetl pełną listę 100 haranów za pomocą `/moai catalog`.

---

## Główne Polecenia

| Polecenie | Opis |
|---------|-------------|
| `/moai init` | Inicjalizacja — zbierz profil i zainstaluj haran |
| `/moai catalog` | Przeglądaj katalog 100 haranów |
| `/moai status` | Sprawdź zainstalowany haran i stan ewolucji |
| `/moai evolve` | Uruchom cykl samorozwojowy ewolucji |
| `/moai profile` | Wyświetl/edytuj globalny profil |
| `/moai doctor` | Uruchom diagnostykę środowiska |
| `/moai help` | Pokaż dostępne polecenia |

---

## Architektura

```
Warstwa 0: auto-memory (globalna) — profil użytkownika, historia haranów
Warstwa 1: plugin (tylko do odczytu) — 100 bazowych haranów (źródło en/, lokalizacja w środowisku uruchomieniowym)
Warstwa 2: .claude/CLAUDE.md + rules/ — persona
Warstwa 3: .moai/ (odczyt/zapis) — kontekst domeny, dane ewolucji
Warstwa 4: auto-memory learning — akumulacja opinii między sesjami
```

---

## Licencja

MIT License — bezpłatne do użytku, modyfikacji i dystrybucji

---

## GitHub

- **Repozytorium**: [modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **Problemy/Sugestie**: [GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork: Poznaj swoich ekspertów AI.**

*Wersja 0.1.3 | Ostatnia aktualizacja: 2026-04-08*
