import streamlit as st
import tempfile
import os
from pathlib import Path
from app.services.whisper_service import transcribir_audio
from app.services.llm_service import clasificar_y_responder
from app.config.settings import ALLOWED_AUDIO_EXTENSIONS, MAX_AUDIO_DURATION_SECONDS

st.set_page_config(page_title="Asistente de Voz", page_icon="🎙️", layout="wide")

st.title("🎙️ Asistente de Voz para Atención al Cliente")
st.caption("Sube o graba un audio → Transcripción → Clasificación + Respuesta")

with st.sidebar:
    st.header("⚙️ Configuración")
    st.info(f"Modelo Whisper: `small` (local)")
    st.info(f"Modelo LLM: `llama3.2:3b` (Ollama local)")
    st.info(f"Duración máx: {MAX_AUDIO_DURATION_SECONDS}s")
    st.info(f"Formatos: {', '.join(sorted(ALLOWED_AUDIO_EXTENSIONS))}")

st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📤 Entrada de Audio")
    audio_file = st.file_uploader(
        "Subir archivo de audio",
        type=[ext[1:] for ext in ALLOWED_AUDIO_EXTENSIONS],
        accept_multiple_files=False,
    )

    audio_bytes = st.audio_input("O graba directamente")

    audio_path = None
    if audio_file is not None:
        suffix = Path(audio_file.name).suffix
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(audio_file.read())
            audio_path = tmp.name
    elif audio_bytes is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_bytes.read())
            audio_path = tmp.name

    if audio_path and st.button("🔄 Transcribir", type="primary"):
        with st.spinner("Transcribiendo con Whisper..."):
            try:
                texto = transcribir_audio(audio_path)
                st.session_state["transcripcion"] = texto
                st.session_state.pop("clasificacion", None)
                st.success("✅ Transcripción completada")
            except Exception as e:
                st.error(f"Error: {e}")
            finally:
                if os.path.exists(audio_path):
                    os.unlink(audio_path)

    if "transcripcion" in st.session_state:
        st.divider()
        if st.button("🎯 Clasificar y Generar Respuesta", type="secondary"):
            with st.spinner("Clasificando con LLM local..."):
                try:
                    resultado = clasificar_y_responder(st.session_state["transcripcion"])
                    st.session_state["clasificacion"] = resultado
                    st.success("✅ Clasificación completada")
                except Exception as e:
                    st.error(f"Error: {e}")

with col2:
    st.subheader("📝 Resultados")
    if "transcripcion" in st.session_state:
        st.text_area("Transcripción", st.session_state["transcripcion"], height=150)

    if "clasificacion" in st.session_state:
        cl = st.session_state["clasificacion"]
        st.markdown(f"**Categoría:** `{cl['categoria']}`")
        st.text_area("Respuesta sugerida", cl["respuesta"], height=100)
    elif "transcripcion" in st.session_state:
        st.info("Presiona \"Clasificar y Generar Respuesta\" para analizar la transcripción")
    else:
        st.empty()

st.divider()
st.caption("Asistente de Voz para Atención al Cliente — UTP")