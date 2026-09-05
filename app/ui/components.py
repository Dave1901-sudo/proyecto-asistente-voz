"""Componentes visuales de alta fidelidad"""
import html
import streamlit as st


# SVGs vectoriales nítidos
SVG_MIC = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/></svg>"""

SVG_CHECK = """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>"""

SVG_ALERT = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" x2="12" y1="8" y2="12"/><line x1="12" x2="12.01" y1="16" y2="16"/></svg>"""

SVG_DATABASE = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/></svg>"""


def render_navbar():
    """Renderiza el Hero Header"""
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
    """Renderiza el panel de telemetría lateral"""
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
    """Renderiza la onda acústica con animación CSS (fluye aunque Python esté ocupado)."""
    st.markdown(
        """
        <style>
        @keyframes waveShift {
            0%   { stroke-dashoffset: 0; }
            100% { stroke-dashoffset: -800; }
        }
        @keyframes wavePulse {
            0%, 100% { opacity: 0.7; }
            50%       { opacity: 1; }
        }
        .signal-visual-sapo {
            height: 56px;
            margin: 1rem 0;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 14px;
            background: linear-gradient(145deg, rgba(33, 60, 42, 0.55), rgba(23, 34, 28, 0.7));
            border: 1px solid var(--line);
            overflow: hidden;
            padding: 0 16px;
        }
        .waveform-svg {
            width: 100%;
            height: 100%;
            overflow: visible;
        }
        .wave-path-main {
            fill: none;
            stroke: var(--accent);
            stroke-width: 2.2;
            stroke-dasharray: 800;
            stroke-linecap: round;
            animation: waveShift 3s linear infinite, wavePulse 2s ease-in-out infinite;
            filter: drop-shadow(0 0 6px rgba(123, 192, 144, 0.5));
        }
        .wave-path-shadow {
            fill: none;
            stroke: var(--accent-strong);
            stroke-width: 1.4;
            stroke-dasharray: 800;
            stroke-dashoffset: 100;
            stroke-linecap: round;
            opacity: 0.45;
            animation: waveShift 4.5s linear infinite reverse;
        }
        </style>
        <div class="signal-visual-sapo">
            <svg class="waveform-svg" viewBox="0 0 800 56" preserveAspectRatio="none">
                <defs>
                    <linearGradient id="waveGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%"   stop-color="var(--accent)" stop-opacity="0.2"/>
                        <stop offset="50%"  stop-color="var(--accent)" stop-opacity="1"/>
                        <stop offset="100%" stop-color="var(--accent)" stop-opacity="0.2"/>
                    </linearGradient>
                </defs>
                <path class="wave-path-main"
                    d="M0,28 Q50,8 100,28 T200,28 T300,28 T400,28 T500,28 T600,28 T700,28 T800,28"
                    stroke="url(#waveGrad)"/>
                <path class="wave-path-shadow"
                    d="M0,28 Q50,42 100,28 T200,28 T300,28 T400,28 T500,28 T600,28 T700,28 T800,28"/>
            </svg>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_processing_waveform():
    """Visualizador animado tipo ecualizador durante el procesamiento con Whisper.
    Usa CSS puro para animar → funciona aunque Python esté bloqueado.
    """
    st.markdown(
        """
        <style>
        @keyframes equalize {
            0%   { transform: scaleY(0.15); }
            100% { transform: scaleY(1); }
        }
        .proc-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 12px;
            padding: 18px 0 14px 0;
        }
        .proc-eq {
            display: flex;
            align-items: flex-end;
            justify-content: center;
            gap: 5px;
            height: 52px;
        }
        .proc-bar {
            width: 5px;
            height: 44px;
            border-radius: 3px;
            background: var(--accent);
            transform-origin: bottom;
            animation: equalize 0.7s ease-in-out infinite alternate;
            box-shadow: 0 0 8px rgba(123, 192, 144, 0.4);
        }
        .proc-bar:nth-child(1)  { animation-delay: 0.00s; height: 24px; }
        .proc-bar:nth-child(2)  { animation-delay: 0.07s; height: 38px; }
        .proc-bar:nth-child(3)  { animation-delay: 0.14s; height: 44px; background: color-mix(in srgb, var(--accent) 90%, #fff 10%); }
        .proc-bar:nth-child(4)  { animation-delay: 0.21s; height: 32px; }
        .proc-bar:nth-child(5)  { animation-delay: 0.28s; height: 44px; background: color-mix(in srgb, var(--accent) 90%, #fff 10%); }
        .proc-bar:nth-child(6)  { animation-delay: 0.35s; height: 38px; }
        .proc-bar:nth-child(7)  { animation-delay: 0.42s; height: 44px; background: color-mix(in srgb, var(--accent) 90%, #fff 10%); }
        .proc-bar:nth-child(8)  { animation-delay: 0.49s; height: 28px; }
        .proc-bar:nth-child(9)  { animation-delay: 0.56s; height: 44px; }
        .proc-bar:nth-child(10) { animation-delay: 0.63s; height: 36px; }
        .proc-bar:nth-child(11) { animation-delay: 0.70s; height: 44px; background: color-mix(in srgb, var(--accent) 90%, #fff 10%); }
        .proc-bar:nth-child(12) { animation-delay: 0.77s; height: 20px; }
        .proc-bar:nth-child(13) { animation-delay: 0.56s; height: 38px; }
        .proc-bar:nth-child(14) { animation-delay: 0.35s; height: 44px; }
        .proc-bar:nth-child(15) { animation-delay: 0.14s; height: 28px; }
        .proc-label {
            font-family: 'Manrope', sans-serif;
            font-size: 0.82rem;
            font-weight: 600;
            letter-spacing: 0.06em;
            color: var(--accent);
            margin: 0;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        @keyframes dotBlink {
            0%, 100% { opacity: 0.2; }
            50%       { opacity: 1; }
        }
        .proc-dot {
            display: inline-block;
            width: 5px;
            height: 5px;
            border-radius: 50%;
            background: var(--accent);
            animation: dotBlink 1.2s ease-in-out infinite;
        }
        .proc-dot:nth-child(2) { animation-delay: 0.2s; }
        .proc-dot:nth-child(3) { animation-delay: 0.4s; }
        </style>

        <div class="proc-container">
            <div class="proc-eq">
                <div class="proc-bar"></div>
                <div class="proc-bar"></div>
                <div class="proc-bar"></div>
                <div class="proc-bar"></div>
                <div class="proc-bar"></div>
                <div class="proc-bar"></div>
                <div class="proc-bar"></div>
                <div class="proc-bar"></div>
                <div class="proc-bar"></div>
                <div class="proc-bar"></div>
                <div class="proc-bar"></div>
                <div class="proc-bar"></div>
                <div class="proc-bar"></div>
                <div class="proc-bar"></div>
                <div class="proc-bar"></div>
            </div>
            <p class="proc-label">
                Procesando señal acústica con Whisper
                <span class="proc-dot"></span>
                <span class="proc-dot"></span>
                <span class="proc-dot"></span>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )




def render_category_badge(categoria: str):
    """Renderiza el encabezado del resultado de clasificación."""
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
    """Renderiza la respuesta sugerida."""
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
    """Renderiza un estado vacío limpio y elegante."""
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
