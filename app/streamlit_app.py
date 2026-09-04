import html
import os
from pathlib import Path
import tempfile
import streamlit as st

from app.config.settings import (
    ALLOWED_AUDIO_EXTENSIONS,
    MAX_AUDIO_DURATION_SECONDS,
    OLLAMA_MODEL,
    WHISPER_MODEL,
)
from app.services.llm_service import clasificar_y_responder
from app.services.supabase_service import (
    guardar_interaccion,
    obtener_interacciones,
)
from app.services.whisper_service import transcribir_audio
from app.ui.components import (
    render_category_badge,
    render_empty_state,
    render_flowing_waveform,
    render_processing_waveform,
    render_navbar,
    render_response_card,
    render_section_header,
    render_sidebar_telemetry,
)
from app.ui.styles import CUSTOM_CSS

# ===== CONFIGURACIÓN GLOBAL DE PÁGINA =====
st.set_page_config(
    page_title="Asistente de Voz — Análisis Acústico Inteligente",
    page_icon="🎙️",
    layout="wide",
)

# Inyección del sistema de diseño SAPO AI (Forest / Obsidian)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Hero Header superior
render_navbar()

# ===== SIDEBAR / TELEMETRÍA TÉCNICA =====
with st.sidebar:
    render_sidebar_telemetry(
        whisper_model=WHISPER_MODEL,
        ollama_model=OLLAMA_MODEL,
        max_duration=MAX_AUDIO_DURATION_SECONDS,
        formats=ALLOWED_AUDIO_EXTENSIONS,
    )

# ===== ETAPA 1: ENTRADA DE AUDIO =====
render_section_header(
    step_num=1,
    title="Captura Acústica de la Consulta",
    description="Sube un archivo de audio o graba directamente con tu micrófono para iniciar el procesamiento inteligente.",
)

tab_upload, tab_record = st.tabs(["Subir Archivo de Audio", "Grabar Micrófono"])

audio_file = None
audio_bytes = None

with tab_upload:
    audio_file = st.file_uploader(
        "Seleccionar archivo de audio",
        type=[ext[1:] for ext in ALLOWED_AUDIO_EXTENSIONS],
        accept_multiple_files=False,
        help=f"Formatos admitidos: {', '.join(sorted(ALLOWED_AUDIO_EXTENSIONS))}",
        label_visibility="collapsed",
    )

with tab_record:
    audio_bytes = st.audio_input(
        "Grabar consulta por micrófono",
        label_visibility="collapsed",
    )

# Procesamiento de archivo temporal + transcripción automática
audio_path = None
audio_key = None

if audio_file is not None:
    suffix = Path(audio_file.name).suffix
    # Usar nombre + tamaño como clave para detectar si el audio cambió
    audio_key = f"file::{audio_file.name}::{audio_file.size}"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(audio_file.read())
        audio_path = tmp.name
elif audio_bytes is not None:
    audio_key = f"mic::{len(audio_bytes.read())}"
    audio_bytes.seek(0)  # Rebobinar tras leer para obtener el tamaño
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes.read())
        audio_path = tmp.name

if audio_path and audio_key:
    # Si es un audio nuevo (distinto al último transcrito), transcribir automáticamente
    if st.session_state.get("ultimo_audio_key") != audio_key:
        # Mostrar el ecualizador animado (CSS puro → anima aunque Python esté bloqueado)
        render_processing_waveform()
        try:
            texto = transcribir_audio(audio_path)
            st.session_state["transcripcion"] = texto
            st.session_state["ultimo_audio_key"] = audio_key
            st.session_state.pop("clasificacion", None)
            st.toast("Transcripción acústica completada ✅")
            st.rerun()
        except Exception as e:
            st.error(f"Error en la transcripción: {e}")
        finally:
            if os.path.exists(audio_path):
                os.unlink(audio_path)
    else:
        # Audio ya transcrito: mostrar solo la onda visual animada
        render_flowing_waveform()
        if os.path.exists(audio_path):
            os.unlink(audio_path)

# Separación elegante por línea entre etapas
st.divider()

# ===== ETAPA 2: RESULTADOS Y CLASIFICACIÓN =====
render_section_header(
    step_num=2,
    title="Análisis Acústico & Clasificación",
    description="Revisa la transcripción obtenida, clasifica la intención del cliente con LLaMA 3.2 y genera la respuesta recomendada.",
)

if "transcripcion" in st.session_state and st.session_state["transcripcion"]:
    st.text_area(
        "Texto Transcrito por Whisper",
        st.session_state["transcripcion"],
        height=120,
        help="Texto extraído del audio mediante el motor Whisper local",
    )

    col_btn_copy, col_btn_classify = st.columns([1, 2])

    with col_btn_copy:
        if st.button("Copiar Transcripción", use_container_width=True):
            texto_escaped = st.session_state["transcripcion"].replace("'", "\\'")
            st.components.v1.html(
                f"""
                <script>
                navigator.clipboard.writeText('{texto_escaped}');
                </script>
                """,
                height=0,
            )
            st.toast("Texto copiado al portapapeles")

    with col_btn_classify:
        if st.button("Clasificar Intención con LLaMA 3.2", type="secondary", use_container_width=True):
            with st.spinner("Ejecutando inferencia local con Ollama..."):
                try:
                    resultado = clasificar_y_responder(st.session_state["transcripcion"])
                    st.session_state["clasificacion"] = resultado
                    st.toast("Clasificación completada con éxito")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error durante la inferencia: {e}")

    if "clasificacion" in st.session_state:
        cl = st.session_state["clasificacion"]
        render_category_badge(cl["categoria"])
        render_response_card(cl["respuesta"])

        col_save, col_clear = st.columns([3, 1])

        with col_save:
            if st.button("Guardar Interacción en Base de Datos", type="primary", use_container_width=True):
                with st.spinner("Guardando en Supabase y activando webhook n8n..."):
                    try:
                        interaccion_id = guardar_interaccion(
                            st.session_state["transcripcion"],
                            cl["categoria"],
                            cl["respuesta"],
                        )
                        st.session_state["ultimo_guardado_id"] = interaccion_id
                        st.toast("Interacción registrada en Supabase")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error guardando en Supabase: {e}")

        with col_clear:
            if st.button("Limpiar Todo", use_container_width=True):
                for key in ["transcripcion", "clasificacion", "ultimo_guardado_id"]:
                    st.session_state.pop(key, None)
                st.rerun()

        if "ultimo_guardado_id" in st.session_state:
            ultimo_id = html.escape(str(st.session_state['ultimo_guardado_id']))
            st.markdown(
                f"""
                <div style="background: color-mix(in srgb, var(--accent-soft) 40%, transparent); border: 1px solid color-mix(in srgb, var(--accent) 35%, transparent); border-radius: 12px; padding: 10px 16px; margin-top: 10px; font-size: 0.84rem; color: var(--accent);">
                    ✓ Consulta persistida exitosamente en Supabase · ID: <code>{ultimo_id}</code>
                </div>
                """,
                unsafe_allow_html=True,
            )

    else:
        col_clear_only, _ = st.columns([1, 4])
        with col_clear_only:
            if st.button("Limpiar transcripción", use_container_width=True):
                st.session_state.pop("transcripcion", None)
                st.rerun()
else:
    render_empty_state(
        title="Sin señal acústica procesada",
        description="Carga o graba una consulta en el paso anterior y presiona \"Transcribir y Analizar Audio\" para comenzar.",
        state_type="audio",
    )

# Separación elegante por línea entre etapas
st.divider()

# ===== ETAPA 3: HISTORIAL RECIENTE =====
render_section_header(
    step_num=3,
    title="Historial de Consultas Registradas",
    description="Explora las últimas interacciones persistidas en Supabase con su categorización y estado de atención.",
)

col_refresh, _ = st.columns([2, 4])
with col_refresh:
    btn_historial = st.button("Sincronizar Historial", use_container_width=True)

if btn_historial or "historial_cache" not in st.session_state:
    try:
        st.session_state["historial_cache"] = obtener_interacciones(limit=10)
    except Exception as e:
        st.session_state["historial_cache"] = []
        st.warning(f"No se pudo sincronizar el historial: {e}")

historial = st.session_state.get("historial_cache", [])

if historial:
    for item in historial:
        fecha_raw = item.get("fecha", "") or ""
        fecha_fmt = fecha_raw[:19].replace("T", " ") if fecha_raw else "Fecha no registrada"
        categoria = item.get("categoria", "consulta_general")
        inter_id = str(item.get("id", ""))
        estado = item.get("estado", "nuevo")

        header_title = f"{fecha_fmt} • [{categoria.upper()}] • ID: #{inter_id[:8]}"

        with st.expander(header_title):
            st.markdown(
                f"""
                <div style="font-size: 0.85rem; margin-bottom: 8px; color: var(--text);">
                    <strong style="color: var(--accent);">Transcripción Acústica:</strong><br>
                    {html.escape(item.get('texto_transcrito', ''))}
                </div>
                <div style="font-size: 0.85rem; margin-bottom: 8px; color: var(--text);">
                    <strong style="color: var(--accent);">Respuesta Generada:</strong><br>
                    {html.escape(item.get('respuesta_sugerida', ''))}
                </div>
                <div style="font-size: 0.74rem; color: var(--muted); margin-top: 10px; border-top: 1px solid var(--line); padding-top: 6px;">
                    Estado: <code>{html.escape(estado)}</code> | ID Completo: <code>{html.escape(inter_id)}</code>
                </div>
                """,
                unsafe_allow_html=True,
            )
else:
    render_empty_state(
        title="No se encontraron registros previos",
        description="Presiona \"Sincronizar Historial\" o procesa y guarda una consulta para ver las interacciones registradas.",
        state_type="history",
    )

st.markdown(
    """
    <div style="text-align: center; color: var(--muted); font-size: 0.75rem; padding: 1.5rem 0 0.5rem 0;">
        Sistema Acústico de Atención al Cliente — UTP 2026 · Basado en arquitectura SAPO AI
    </div>
    """,
    unsafe_allow_html=True,
)
