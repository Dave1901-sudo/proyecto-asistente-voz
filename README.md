# Asistente de Voz para Atención al Cliente

Proyecto para el curso: Herramientas de Desarrollo Profesional TIC
Universidad Tecnológica del Perú (UTP)

Sistema que recibe consultas de clientes en formato de audio, las transcribe, clasifica, genera una respuesta sugerida y dispara acciones automáticas. Utiliza modelos de IA locales.

---

## Funcionalidad

1. El cliente sube o graba un audio de consulta.
2. Whisper transcribe el audio a texto.
3. Ollama clasifica la consulta en una categoría y genera una respuesta sugerida.
4. La interacción se guarda en la base de datos.
5. Se dispara una acción automática en n8n según la categoría.

### Categorías

- `reclamo`
- `ventas`
- `soporte_tecnico`
- `consulta_general`

---

## Tecnologías

| Componente | Tecnología |
|---|---|
| Interfaz web | Streamlit |
| Transcripción | faster-whisper (modelo small) |
| Clasificación y respuesta | Ollama (llama3.2:3b) |
| Texto a voz | gTTS |
| Base de datos | Supabase (PostgreSQL) |
| Automatización | n8n (Docker) |
| Lenguaje | Python 3.10+ |
| Control de versiones | Git + GitHub |
| CI/CD | GitHub Actions |

---

## Estructura

```
app/
├── streamlit_app.py          # Interfaz principal
├── config/settings.py        # Configuración
├── services/
│   ├── whisper_service.py    # Transcripción
│   ├── llm_service.py        # Clasificación + respuesta
│   ├── supabase_service.py   # Persistencia + webhook
│   └── tts_service.py        # Texto a voz
└── ui/
    ├── components.py         # Componentes visuales
    └── styles.py             # Estilos CSS

n8n/
├── docker-compose.yml
└── workflows/clasificacion.json

tests/                        # Pruebas unitarias
.github/workflows/ci.yml      # CI/CD
requirements.txt
.env.example
```

---

## Requisitos

- Python 3.10+
- Ollama
- Docker Desktop
- Git
- Conexión a internet (para gTTS y Supabase)

---

## Instalación

```bash
git clone https://github.com/Dave1901-sudo/proyecto-asistente-voz.git
cd proyecto-asistente-voz

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

ollama pull llama3.2:3b

copy .env.example .env
# Editar .env con las credenciales

cd n8n
docker compose up -d
```

---

## Ejecución

```bash
python -m streamlit run app/streamlit_app.py
```

La aplicación se abre en `http://localhost:8501`.

---

## CI/CD

El pipeline de GitHub Actions ejecuta `flake8` y `pytest` en cada push.

---

## Solución de problemas

| Problema | Solución |
|---|---|
| `ModuleNotFoundError: app` | Usar `python -m streamlit run ...` |
| `ollama: command not found` | Reiniciar terminal tras instalar Ollama |
| `Connection refused: localhost:11434` | Ejecutar `ollama serve` |
| Puerto 8501 ocupado | `streamlit run ... --server.port 8502` |
| Whisper lento | Cambiar `WHISPER_MODEL=base` en `.env` |

---

## Licencia

Proyecto académico — Universidad Tecnológica del Perú (UTP).

**Curso:** Herramientas de Desarrollo Profesional TIC
