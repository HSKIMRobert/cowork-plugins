<div align="center">

# 🗿 MoAI-Cowork

**100 Harnais Auto-Évolutifs — Vos Experts IA Personnels**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [한국어](README.md) | [日本語](README-ja.md) | [Español](README-es.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## Qu'est-ce que MoAI ?

**MoAI-Cowork** est un plugin pour Claude Cowork qui fournit 100 harnais d'experts de domaines à travers un système d'assistant IA auto-apprentissant.

Un harnais est un module expert IA qui regroupe des connaissances spécifiques au domaine, des flux de travail, des formats de livrables et des protocoles de collecte de contexte dans un seul package. Une fois installé, MoAI se transforme en expert du domaine et fournit des résultats structurés.

**Caractéristiques clés :**

- 10 catégories × 100 harnais — contenu, marketing, affaires, éducation, juridique, lifestyle, communication, opérations, finance et produit/innovation
- Architecture auto-apprentissante à 5 couches — évolue et s'adapte à l'utilisateur au fil du temps
- Profil global — partager les informations personnelles + entreprise entre les sessions, sans besoin de les re-saisir
- Support 17 langues — source unique EN + localisation en temps réel
- Support des paramètres régionaux mondiaux — entrez votre pays de travail et MoAI collecte automatiquement les lois fiscales, le droit du travail, la protection des données et les pratiques commerciales via recherche web

---

## Installation

### Méthode 1 : Installer depuis la Place de Marché Claude Cowork (Recommandé)

1. Lancez l'application **Claude Desktop**
2. Entrez le mode **Cowork** en bas à gauche
3. Cliquez sur l'icône **Plugin (🧩)** à côté de l'entrée de chat
4. Recherchez `moai-cowork` dans la marketplace
5. Trouvez **MoAI-Cowork** et cliquez sur **Install**
6. Après l'installation, tapez `/moai init` dans le chat pour commencer la configuration initiale

### Méthode 2 : Installer depuis la Place de Marché K-Harness

K-Harness est la marketplace qui inclut MoAI-Cowork.

```
# Étape 1 : Ajouter la marketplace
/plugin marketplace add modu-ai/k-harness

# Étape 2 : Installer le plugin MoAI-Cowork
/plugin install moai-cowork@k-harness
```

### Méthode 3 : Installer Directement depuis GitHub

```
# Cloner le référentiel
git clone https://github.com/modu-ai/k-harness.git

# Naviguer vers le répertoire du plugin
cd k-harness/plugins/moai-cowork

# Charger manuellement dans Claude Desktop
# Mode Cowork → Plugin (🧩) → "Install from file" → sélectionner le dossier moai-cowork
```

### Méthode 4 : Installation Manuelle via ZIP

1. Téléchargez le dernier `moai-cowork-v0.1.3.zip` depuis la page [GitHub Releases](https://github.com/modu-ai/k-harness/releases)
2. Ouvrez Claude Desktop → entrez le mode Cowork
3. Cliquez sur l'icône Plugin (🧩) → **Install from file**
4. Sélectionnez le fichier ZIP téléchargé

---

## Mise à Jour

### Si installé via la marketplace

```
# Mettre à jour la marketplace K-Harness
/plugin marketplace update k-harness

# Ou via l'interface Cowork :
# Plugin (🧩) → MoAI-Cowork → cliquez sur "Update"
```

### Si installé depuis GitHub

```
cd k-harness
git pull origin main
```

### Si installé via ZIP

1. Supprimez le plugin existant : Plugin (🧩) → MoAI-Cowork → **Remove**
2. Téléchargez le dernier fichier ZIP
3. Répétez le processus d'installation manuelle de la Méthode 4

### Vérifier la version

Tapez `/moai status` dans le chat pour vérifier la version actuellement installée.

---

## Dépannage

### Plugin non reconnu

1. Quittez complètement Claude Desktop et redémarrez-le
2. Vérifiez que MoAI-Cowork apparaît dans la liste Plugin (🧩) en mode Cowork
3. Si ce n'est pas le cas, essayez de réinstaller

### Erreur sur `/moai init`

1. Tapez `/moai doctor` pour exécuter les diagnostics d'environnement
2. Si votre profil global est corrompu, réinitialisez-le avec `/moai profile --reset`

### Harnais non chargé

1. Vérifiez que `.moai/config.json` existe dans votre dossier de projet
2. Si ce n'est pas le cas, réinitialisez avec `/moai init`

### Les données de localisation ne sont pas collectées

- Corée : Utilise les données intégrées (aucune recherche web requise)
- Autres pays : Nécessite une connexion Internet et les outils de recherche web

---

## Démarrage Rapide

### Étape 1 : Initialiser

```
/moai init
```

MoAI mène une interview interactive pour collecter votre profil (nom, rôle, entreprise, paramètres régionaux).

### Étape 2 : Parcourir le Catalogue de Harnais

```
/moai catalog
```

Consultez la liste complète des 100 harnais répartis sur 10 catégories.

### Étape 3 : Faire une Demande en Langage Naturel

```
Aide-moi à faire une étude de marché
```

MoAI détecte automatiquement le harnais `market-research` et s'exécute en mode expert.

---

## Catalogue des 100 Harnais

| # | Catégorie | Nombre | Exemples de Harnais |
|---|----------|--------|-------------------|
| 1 | Contenu & Créatif | 10 | copywriting, youtube-production, podcast-studio, book-publishing |
| 2 | Affaires & Stratégie | 10 | business-model-canvas, competitive-analysis, startup-launcher, pricing-strategy |
| 3 | Marketing & Croissance | 10 | brand-identity, growth-hacking, social-media-manager, influencer-strategy |
| 4 | Éducation & Recherche | 10 | course-builder, thesis-advisor, exam-prep, language-tutor |
| 5 | Juridique & Conformité | 10 | contract-analyzer, compliance-checker, patent-drafter, privacy-engineer |
| 6 | Lifestyle | 10 | travel-planner, wedding-planner, meal-planner, fitness-program |
| 7 | Communication & Docs | 10 | presentation-designer, report-generator, technical-writer, proposal-writer |
| 8 | Opérations & RH | 10 | hiring-pipeline, onboarding-system, operations-manual, crisis-communication |
| 9 | Finance & Commerce | 10 | accounting-tax, financial-modeler, import-export, invoice-mgmt |
| 10 | Produit & Innovation | 10 | product-manager, ai-strategy, ux-research, sales-enablement |

Voir la liste complète des 100 harnais avec `/moai catalog`.

---

## Commandes Clés

| Commande | Description |
|---------|-------------|
| `/moai init` | Initialiser — collecter le profil et installer le harnais |
| `/moai catalog` | Parcourir le catalogue de 100 harnais |
| `/moai status` | Vérifier le harnais installé et l'état d'évolution |
| `/moai evolve` | Exécuter le cycle d'évolution auto-apprentissant |
| `/moai profile` | Afficher/modifier le profil global |
| `/moai doctor` | Exécuter les diagnostics d'environnement |
| `/moai help` | Afficher les commandes disponibles |

---

## Architecture

```
Couche 0 : auto-memory (global) — profil utilisateur, historique des harnais
Couche 1 : plugin (lecture seule) — 100 harnais de base (source unique en/, localisation en temps réel)
Couche 2 : .claude/CLAUDE.md + rules/ — persona
Couche 3 : .moai/ (lecture/écriture) — contexte du domaine, données d'évolution
Couche 4 : auto-memory learning — accumulation des commentaires entre sessions
```

---

## Licence

Licence MIT — libre d'utilisation, de modification et de distribution

---

## GitHub

- **Référentiel** : [modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **Problèmes/Suggestions** : [GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork : Rencontrez vos experts IA.**

*Version 0.1.3 | Dernière mise à jour : 2026-04-08*
