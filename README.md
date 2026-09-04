# 🎙️ Asistente de Voz para Atención al Cliente

**Proyecto Final — Herramientas de Desarrollo Profesional TIC**
Universidad Tecnológica del Perú (UTP)

Sistema inteligente end-to-end que recibe consultas de clientes en formato de audio (notas de voz, llamadas, buzones), las transcribe, clasifica, genera una respuesta sugerida y dispara acciones automáticas — todo con **IA local gratuita**.

---

## 📌 Tabla de Contenidos

1. [Descripción del Proyecto](#-descripción-del-proyecto)
2. [Flujo del Sistema](#-flujo-del-sistema)
3. [Tecnologías Utilizadas](#-tecnologías-utilizadas)
4. [Estructura del Proyecto](#-estructura-del-proyecto)
5. [Requisitos Previos](#-requisitos-previos)
6. [Instalación](#-instalación)
7. [Uso de la Aplicación](#-uso-de-la-aplicación)
8. [Automatización con n8n](#-automatización-con-n8n)
9. [CI/CD](#-cicd)
10. [Solución de Problemas](#-solución-de-problemas)

---

## 📝 Descripción del Proyecto

El **Asistente de Voz para Atención al Cliente** resuelve un problema real de las pequeñas y medianas empresas: recibir y gestionar consultas de clientes en formato de audio sin personal suficiente para procesarlas a tiempo.

### Problema que resuelve

- Demoras en la atención al cliente.
- Pérdida o mal registro de consultas por audio.
- Falta de criterio uniforme para derivar casos al área correcta.

### Solución

Un sistema que **automatiza** el proceso completo:

1. **Recibe** el audio del cliente.
2. **Transcribe** con Whisper (modelo local).
3. **Clasifica** la consulta en una categoría.
4. **Genera** una respuesta sugerida.
5. **Guarda** la interacción en la base de datos.
6. **Dispara** una acción automática según la categoría.

---

## 🔄 Flujo del Sistema

```
┌─────────────┐     ┌──────────────┐     ┌───────────────────┐
│  ENTRADA    │ ──▶ │ TRANSCRIPCIÓN │ ──▶ │  CLASIFICACIÓN    │
│ Audio del   │     │  Whisper      │     │  Ollama (LLM)     │
│ cliente     │     │  (local)      │     │  + Respuesta      │
└─────────────┘     └──────────────┘     └─────────┬─────────┘
                                                   │
                                                   ▼
┌─────────────┐     ┌──────────────┐     ┌───────────────────┐
│ AUTOMATIZACIÓN│ ◀── │  PERSISTENCIA │ ◀── │  RESPUESTA        │
│ n8n (webhook)│     │  Supabase     │     │  Texto + Voz TTS  │
└─────────────┘     └──────────────┘     └───────────────────┘
```

### Categorías de clasificación

| Categoría | Descripción |
|---|---|
| `reclamo` | Quejas, productos defectuosos, insatisfacción |
| `ventas` | Consultas comerciales, cotizaciones, planes |
| `soporte_tecnico` | Errores, bugs, problemas técnicos |
| `consulta_general` | Preguntas informativas, horarios, dudas |

---

## 🛠️ Tecnologías Utilizadas

| Componente | Tecnología | Rol |
|---|---|---|
| 🖥️ Interfaz web | **Streamlit** | Aplicación web responsiva |
| 🎙️ Transcripción | **faster-whisper** (modelo `small`) | Audio → texto (local, CPU) |
| 🧠 Clasificación + Respuesta | **Ollama** (`llama3.2:3b`) | Intención + respuesta sugerida |
| 🔊 Texto a voz | **gTTS** (Google TTS) | Respuesta hablada |
| 🗄️ Base de datos | **Supabase** (PostgreSQL) | Persistencia + historial |
| ⚡ Automatización | **n8n** (Docker) | Acciones según categoría |
| 🐍 Lenguaje | **Python 3.10+** | Base del sistema |
| 🔄 Control de versiones | **Git + GitHub** | Colaboración |
| 🚀 CI/CD | **GitHub Actions** | Lint + tests automáticos |

---

## 📂 Estructura del Proyecto

```
proyecto-asistente-voz/
├── app/
│   ├── streamlit_app.py              # Punto de entrada (UI principal)
│   ├── config/
│   │   └── settings.py               # Configuración desde .env
│   ├── services/
│   │   ├── whisper_service.py        # Transcripción de audio
│   │   ├── llm_service.py            # Clasificación + respuesta
│   │   ├── supabase_service.py       # Persistencia + webhook
│   │   └── tts_service.py            # Texto a voz (gTTS)
│   └── ui/
│       ├── components.py             # Componentes visuales
│       └── styles.py                 # Sistema de diseño CSS
├── n8n/
│   ├── docker-compose.yml            # n8n + PostgreSQL
│   └── workflows/
│       └── clasificacion.json        # Workflow de automatización
├── tests/
│   ├── test_whisper_service.py       # Tests de transcripción
│   └── test_llm_service.py           # Tests de clasificación
├── .github/
│   └── workflows/
│       └── ci.yml                    # Pipeline CI/CD
├── .streamlit/
│   └── config.toml                   # Tema de Streamlit
├── requirements.txt                  # Dependencias Python
├── .env.example                      # Plantilla de variables de entorno
├── .gitignore                        # Archivos excluidos de Git
└── muestras_demo.txt                 # Frases de prueba por categoría
```

---

## ✅ Requisitos Previos

| Requisito | Versión | Verificar |
|---|---|---|
| **Python** | 3.10+ | `python --version` |
| **Ollama** | Última | `ollama --version` |
| **Docker Desktop** | Última | `docker --version` |
| **Git** | Última | `git --version` |
| **Internet** | — | Para gTTS y Supabase |

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Dave1901-sudo/proyecto-asistente-voz.git
cd proyecto-asistente-voz
```

### 2. Crear entorno virtual e instalar dependencias

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
# python3 -m venv venv
# source venv/bin/activate

pip install -r requirements.txt
```

### 3. Instalar Ollama y el modelo LLM

```bash
# Windows: winget install Ollama.Ollama
# O descargar: https://ollama.com/download

ollama pull llama3.2:3b
```

### 4. Configurar variables de entorno

```bash
copy .env.example .env
# Editar .env con las credenciales (Supabase, n8n)
```

### 5. Levantar n8n (automatización)

```bash
cd n8n
docker compose up -d
# Abrir http://localhost:5678
```

---

## 🎮 Uso de la Aplicación

```bash
python -m streamlit run app/streamlit_app.py
```

Se abre en **http://localhost:8501**

### Pasos de uso

1. **Subir archivo de audio** o **grabar con micrófono** (pestañas).
2. La transcripción ocurre **automáticamente** con Whisper.
3. Clic en **"Clasificar Intención con LLaMA 3.2"** → categoría + respuesta.
4. Clic en **"🔊 Escuchar respuesta"** → la IA habla la respuesta.
5. Clic en **"Guardar Interacción en Base de Datos"** → se persiste en Supabase y se dispara n8n.
6. Revisa el **historial** de consultas guardadas.

---

## ⚡ Automatización con n8n

Cuando una consulta se guarda, la aplicación dispara un **webhook** a n8n. El workflow `clasificacion.json`:

```
Webhook → Switch (por categoría) → Respuesta según categoría
```

| Categoría | Acción en n8n |
|---|---|
| `reclamo` | "Reclamo registrado" |
| `ventas` | "Venta registrada" |
| `soporte_tecnico` | "Soporte registrado" |
| `consulta_general` | "Consulta general registrada" |

> **Nota:** n8n corre localmente en Docker (gratis, ilimitado). Si n8n no está activo, la app sigue funcionando (el guardado no falla).

---

## 🚀 CI/CD

El pipeline de **GitHub Actions** se ejecuta en cada push:

| Step | Qué hace |
|---|---|
| **Lint** | `flake8` (errores críticos: `--select=E9,F63,F7,F82`) |
| **Tests** | `pytest tests/ -v` (5 pruebas unitarias) |

Configuración: `.github/workflows/ci.yml`

---

## 🔧 Solución de Problemas

| Problema | Solución |
|---|---|
| `ModuleNotFoundError: app` | Ejecutar con `python -m streamlit run ...` |
| `ModuleNotFoundError: faster_whisper` | `pip install -r requirements.txt` con venv activado |
| `ollama: command not found` | Reiniciar terminal tras instalar Ollama |
| `Connection refused: localhost:11434` | `ollama serve` en otra terminal |
| Whisper lento / OOM | En `.env`: `WHISPER_MODEL=base` |
| Error 403 con TTS | Verificar conexión a internet (gTTS usa Google) |
| Puerto 8501 ocupado | `streamlit run ... --server.port 8502` |
| n8n no recibe webhook | Activar workflow (Publish) en n8n |
| Permiso denegado en Supabase | Ejecutar `grant select, insert, update on table interacciones to anon;` |

---

## 📄 Licencia

Proyecto académico — **Universidad Tecnológica del Perú (UTP)**.

**Curso:** Herramientas de Desarrollo Profesional TIC

---

*Documentación generada para el proyecto final.*