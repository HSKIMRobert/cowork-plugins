<div align="center">

# 🗿 MoAI-Cowork

**100 Harnesses Auto-Evolucionarios — Tus Expertos Personales en IA**

[![Version](https://img.shields.io/badge/version-0.1.3-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Harnesses](https://img.shields.io/badge/harnesses-100-orange)]()
[![Languages](https://img.shields.io/badge/languages-17-purple)]()

🌐 [한국어](README.md) | [English](README-en.md) | [日本語](README-ja.md) | [Français](README-fr.md) | [Deutsch](README-de.md) | [Português](README-pt-BR.md) | [中文](README-zh-CN.md) | [Bahasa](README-id.md) | [हिन्दी](README-hi.md) | [Tiếng Việt](README-vi.md) | [ภาษาไทย](README-th.md) | [Italiano](README-it.md) | [Nederlands](README-nl.md) | [Polski](README-pl.md) | [العربية](README-ar.md) | [עברית](README-he.md)

</div>

---

## ¿Qué es MoAI?

**MoAI-Cowork** es un plugin para Claude Cowork que proporciona 100 harnesses de expertos de dominio a través de un sistema de asistente de IA auto-aprendizaje.

Un harness es un módulo de experto en IA que agrupa conocimiento específico de dominio, flujos de trabajo, formatos de entregables y protocolos de recopilación de contexto en un solo paquete. Una vez instalado, MoAI se transforma en un experto de dominio y entrega resultados estructurados.

**Características clave:**

- 10 categorías × 100 harnesses — contenido, marketing, negocios, educación, legal, estilo de vida, comunicación, operaciones, finanzas e innovación de productos
- Arquitectura de auto-aprendizaje de 5 capas — evoluciona y se adapta al usuario en el tiempo
- Perfil global — comparte información personal + empresarial en sesiones, sin necesidad de re-entrada
- Soporte de 17 idiomas — EN fuente única + localización en tiempo de ejecución
- Soporte de localidad mundial — introduce tu país de trabajo y MoAI auto-recopila ley tributaria, ley laboral, protección de datos y prácticas comerciales mediante búsqueda web

---

## Instalación

### Método 1: Instalar desde Claude Cowork Marketplace (Recomendado)

1. Abre la aplicación **Claude Desktop**
2. Ingresa en modo **Cowork** desde la esquina inferior izquierda
3. Haz clic en el icono **Plugin (🧩)** junto a la entrada de chat
4. Busca `moai-cowork` en el marketplace
5. Encuentra **MoAI-Cowork** y haz clic en **Install**
6. Después de la instalación, escribe `/moai init` en el chat para comenzar la configuración inicial

### Método 2: Instalar desde K-Harness Marketplace

K-Harness es el marketplace que incluye MoAI-Cowork.

```
# Paso 1: Agregar el marketplace
/plugin marketplace add modu-ai/k-harness

# Paso 2: Instalar plugin MoAI-Cowork
/plugin install moai-cowork@k-harness
```

### Método 3: Instalar Directamente desde GitHub

```
# Clonar el repositorio
git clone https://github.com/modu-ai/k-harness.git

# Navegar al directorio del plugin
cd k-harness/plugins/moai-cowork

# Cargar manualmente en Claude Desktop
# Cowork mode → Plugin (🧩) → "Install from file" → selecciona la carpeta moai-cowork
```

### Método 4: Instalación Manual mediante ZIP

1. Descarga el último `moai-cowork-v0.1.3.zip` desde la página de [GitHub Releases](https://github.com/modu-ai/k-harness/releases)
2. Abre Claude Desktop → ingresa en modo Cowork
3. Haz clic en el icono Plugin (🧩) → **Install from file**
4. Selecciona el archivo ZIP descargado

---

## Actualizando

### Si se instaló a través del marketplace

```
# Actualizar marketplace K-Harness
/plugin marketplace update k-harness

# O a través de la interfaz de Cowork:
# Plugin (🧩) → MoAI-Cowork → haz clic en "Update"
```

### Si se instaló desde GitHub

```
cd k-harness
git pull origin main
```

### Si se instaló mediante ZIP

1. Elimina el plugin existente: Plugin (🧩) → MoAI-Cowork → **Remove**
2. Descarga el archivo ZIP más reciente
3. Repite el proceso de instalación manual del Método 4

### Verificar versión

Escribe `/moai status` en el chat para verificar la versión actualmente instalada.

---

## Solución de Problemas

### Plugin no reconocido

1. Cierra completamente y reinicia Claude Desktop
2. Verifica si MoAI-Cowork aparece en la lista Plugin (🧩) en modo Cowork
3. Si no aparece, intenta reinstalar

### Error en `/moai init`

1. Escribe `/moai doctor` para ejecutar diagnósticos del entorno
2. Si tu perfil global está dañado, reinicialo con `/moai profile --reset`

### Harness no se carga

1. Verifica que `.moai/config.json` exista en tu carpeta del proyecto
2. Si no existe, reinicializa con `/moai init`

### Datos de localización no recopilados

- Korea: Utiliza datos integrados (no se necesita búsqueda web)
- Otros países: Requiere conexión a internet y herramientas de búsqueda web

---

## Inicio Rápido

### Paso 1: Inicializar

```
/moai init
```

MoAI realiza una entrevista interactiva para recopilar tu perfil (nombre, rol, empresa, localidad).

### Paso 2: Explorar el Catálogo de Harnesses

```
/moai catalog
```

Ver la lista completa de 100 harnesses en 10 categorías.

### Paso 3: Hacer una Solicitud en Lenguaje Natural

```
Ayúdame con una investigación de mercado
```

MoAI detecta automáticamente el harness `market-research` y ejecuta en modo experto.

---

## Catálogo de 100 Harnesses

| # | Categoría | Cantidad | Harnesses de Ejemplo |
|---|----------|----------|-----------------|
| 1 | Contenido y Creatividad | 10 | copywriting, youtube-production, podcast-studio, book-publishing |
| 2 | Negocios y Estrategia | 10 | business-model-canvas, competitive-analysis, startup-launcher, pricing-strategy |
| 3 | Marketing y Crecimiento | 10 | brand-identity, growth-hacking, social-media-manager, influencer-strategy |
| 4 | Educación e Investigación | 10 | course-builder, thesis-advisor, exam-prep, language-tutor |
| 5 | Legal y Cumplimiento | 10 | contract-analyzer, compliance-checker, patent-drafter, privacy-engineer |
| 6 | Estilo de Vida | 10 | travel-planner, wedding-planner, meal-planner, fitness-program |
| 7 | Comunicación y Documentos | 10 | presentation-designer, report-generator, technical-writer, proposal-writer |
| 8 | Operaciones y RRHH | 10 | hiring-pipeline, onboarding-system, operations-manual, crisis-communication |
| 9 | Finanzas y Comercio | 10 | accounting-tax, financial-modeler, import-export, invoice-mgmt |
| 10 | Productos e Innovación | 10 | product-manager, ai-strategy, ux-research, sales-enablement |

Ver la lista completa de 100 harnesses con `/moai catalog`.

---

## Comandos Clave

| Comando | Descripción |
|---------|-------------|
| `/moai init` | Inicializar — recopilar perfil e instalar harness |
| `/moai catalog` | Explorar catálogo de 100 harnesses |
| `/moai status` | Verificar harness instalado y estado de evolución |
| `/moai evolve` | Ejecutar ciclo de evolución de auto-aprendizaje |
| `/moai profile` | Ver/editar perfil global |
| `/moai doctor` | Ejecutar diagnósticos del entorno |
| `/moai help` | Mostrar comandos disponibles |

---

## Arquitectura

```
Capa 0: auto-memory (global) — perfil de usuario, historial de harness
Capa 1: plugin (solo lectura) — 100 harnesses base (fuente única en/ localización en tiempo de ejecución)
Capa 2: .claude/CLAUDE.md + rules/ — persona
Capa 3: .moai/ (lectura/escritura) — contexto de dominio, datos de evolución
Capa 4: auto-memory learning — acumulación de retroalimentación entre sesiones
```

---

## Licencia

MIT License — libre para usar, modificar y distribuir

---

## GitHub

- **Repositorio**: [modu-ai/k-harness](https://github.com/modu-ai/k-harness)
- **Problemas/Sugerencias**: [GitHub Issues](https://github.com/modu-ai/k-harness/issues)

---

**MoAI-Cowork: Conoce a tus expertos en IA.**

*Versión 0.1.3 | Última actualización: 2026-04-08*
