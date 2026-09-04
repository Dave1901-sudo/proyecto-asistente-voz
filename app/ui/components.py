"""Componentes visuales de alta fidelidad inspirados en la interfaz de SAPO AI."""
import html
import streamlit as st


# SVGs vectoriales nítidos
SVG_MIC = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/></svg>"""

SVG_CHECK = """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>"""

SVG_ALERT = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" x2="12" y1="8" y2="12"/><line x1="12" x2="12.01" y1="16" y2="16"/></svg>"""

SVG_DATABASE = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/></svg>"""


def render_navbar():
    """Renderiza el Hero Header con estilo SAPO AI."""
    st.markdown(
        """
        <div class="sapo-hero">
            <div class="eyebrow">
                <span class="status-dot"></span>
                <span>Sistema Acústico de Atención al Cliente • IA Local</span>
            </div>
            <h1 class="hero-title">Asistente de Voz <span>Inteligente</span></h1>
            <p class="hero-intro hero-intro-centered">
                Transcripción acústica con Whisper y clasificación de intenciones con LLaMA 3.2 en tiempo real.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar_telemetry(whisper_model: str, ollama_model: str, max_duration: int, formats: list):
    """Renderiza el panel de telemetría lateral con diseño SAPO AI."""
    formatos_str = ", ".join(sorted(formats))

    st.sidebar.markdown(
        f"""
        <div class="sidebar-header-sapo">
            <div class="brand-mark">
                {SVG_MIC}
            </div>
            <div>
                <div class="sidebar-title">Asistente<span>Voz</span></div>
            </div>
        </div>

        <span class="sidebar-kicker">Arquitectura Local</span>

        <div class="telemetry-card">
            <div class="telemetry-label">Motor STT (Voz a Texto)</div>
            <div class="telemetry-value">faster-whisper : {html.escape(whisper_model)}</div>
        </div>

        <div class="telemetry-card">
            <div class="telemetry-label">Motor LLM (Inferencia)</div>
            <div class="telemetry-value">ollama : {html.escape(ollama_model)}</div>
        </div>

        <div class="telemetry-card">
            <div class="telemetry-label">Límite de Tiempo</div>
            <div class="telemetry-value">{max_duration} segundos</div>
        </div>

        <div class="telemetry-card">
            <div class="telemetry-label">Formatos Admitidos</div>
            <div class="telemetry-value" style="font-size: 0.74rem; word-break: break-all;">{html.escape(formatos_str)}</div>
        </div>

        <span class="sidebar-kicker">Flujo de Procesamiento</span>
        <div style="font-size: 0.8rem; color: var(--muted); line-height: 1.55; padding: 4px 2px;">
            1. Captura o sube consulta de audio.<br>
            2. Transcripción local con Whisper.<br>
            3. Clasificación inteligente con LLaMA.<br>
            4. Persistencia en BD y webhook n8n.
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_header(step_num: int, title: str, description: str):
    """Renderiza el encabezado de sección con kicker y título Manrope."""
    kickers = {
        1: "ETAPA 01 · ENTRADA ACÚSTICA",
        2: "ETAPA 02 · ANÁLISIS & RESPUESTA",
        3: "ETAPA 03 · REGISTRO & HISTORIAL",
    }
    kicker_text = kickers.get(step_num, f"ETAPA 0{step_num}")

    st.markdown(
        f"""
        <div>
            <span class="section-kicker">{kicker_text}</span>
            <h2 class="section-title-sapo">{html.escape(title)}</h2>
            <p class="section-desc-sapo">{html.escape(description)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_flowing_waveform():
    """Renderiza la onda acústica fluida estilo SAPO AI - versión refinada."""
    st.markdown(
        """
        <div class="signal-visual-sapo-refined">
            <svg class="waveform-svg-refined" viewBox="0 0 800 48" preserveAspectRatio="none">
                <defs>
                    <linearGradient id="waveGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stop-color="var(--accent)" stop-opacity="0.3"/>
                        <stop offset="50%" stop-color="var(--accent)" stop-opacity="0.8"/>
                        <stop offset="100%" stop-color="var(--accent)" stop-opacity="0.3"/>
                    </linearGradient>
                </defs>
                <path d="M0,24 Q80,8 160,24 T320,24 T480,24 T640,24 T800,24" fill="none" stroke="url(#waveGradient)" stroke-width="2" stroke-linecap="round"/>
                <path d="M0,24 Q80,36 160,24 T320,24 T480,24 T640,24 T800,24" fill="none" stroke="var(--accent-strong)" stroke-width="1.2" opacity="0.4"/>
            </svg>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_category_badge(categoria: str):
    """Renderiza el encabezado del resultado de clasificación al estilo SAPO AI."""
    cat_normalizada = categoria.strip().lower()
    etiquetas = {
        "reclamo": ("Reclamo Registrado", "🚨", "#ef4444"),
        "ventas": ("Oportunidad de Venta", "💼", "#22c55e"),
        "soporte_tecnico": ("Soporte Técnico", "🛠️", "#f59e0b"),
        "consulta_general": ("Consulta General", "💬", "#3b82f6"),
    }
    titulo, icono, color = etiquetas.get(cat_normalizada, (categoria.title(), "🏷️", "#7bc090"))

    st.markdown(
        f"""
        <div class="result-head-sapo">
            <div class="result-icon-badge" style="background: color-mix(in srgb, {color} 18%, transparent); color: {color};">
                {icono}
            </div>
            <div>
                <span class="section-kicker" style="color: {color};">INTENCIÓN DETECTADA</span>
                <h3 class="result-category-title">{html.escape(titulo)}</h3>
            </div>
        </div>

        <div class="result-meta-grid">
            <div class="result-meta-item">
                <div class="result-meta-label">Categoría</div>
                <div class="result-meta-val">{html.escape(categoria.upper())}</div>
            </div>
            <div class="result-meta-item">
                <div class="result-meta-label">Motor STT</div>
                <div class="result-meta-val">Whisper local</div>
            </div>
            <div class="result-meta-item">
                <div class="result-meta-label">Inferencia</div>
                <div class="result-meta-val">LLaMA 3.2 local</div>
            </div>
            <div class="result-meta-item">
                <div class="result-meta-label">Estado</div>
                <div class="result-meta-val">Completado</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_response_card(respuesta: str):
    """Renderiza la respuesta sugerida al estilo confidence-block de SAPO AI."""
    st.markdown(
        f"""
        <div class="confidence-response-box">
            <div class="response-kicker">Respuesta Sugerida para el Cliente</div>
            <div class="response-text-sapo">{html.escape(respuesta)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_empty_state(title: str, description: str, state_type: str = "audio"):
    """Renderiza un estado vacío limpio y elegante estilo SAPO AI."""
    svg_icon = SVG_MIC if state_type == "audio" else SVG_DATABASE
    st.markdown(
        f"""
        <div class="empty-state-sapo">
            <div class="empty-state-icon-sapo">
                {svg_icon}
            </div>
            <div>
                <div class="empty-state-title-sapo">{html.escape(title)}</div>
                <div class="empty-state-desc-sapo">{html.escape(description)}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
