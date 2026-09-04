"""Sistema de diseño basado en la identidad visual de SAPO AI (https://sapo-ai.vercel.app).
Paleta Forest/Obsidian con acentos Emerald (#7bc090, #397b53), Manrope & DM Sans.
"""

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

:root {
    --bg: #0d1511;
    --bg-soft: #121d17;
    --surface: rgba(23, 34, 28, 0.84);
    --surface-solid: #17221c;
    --text: #edf5ef;
    --muted: #9eaca4;
    --line: rgba(219, 240, 225, 0.12);
    --accent: #7bc090;
    --accent-strong: #397b53;
    --accent-soft: #213c2a;
    --shadow: 0 24px 80px rgba(0, 0, 0, 0.32);

    --cat-reclamo-bg: rgba(239, 68, 68, 0.15);
    --cat-reclamo-text: #f87171;
    --cat-reclamo-border: rgba(239, 68, 68, 0.35);

    --cat-ventas-bg: rgba(34, 197, 94, 0.15);
    --cat-ventas-text: #4ade80;
    --cat-ventas-border: rgba(34, 197, 94, 0.35);

    --cat-soporte-bg: rgba(245, 158, 11, 0.15);
    --cat-soporte-text: #fbbf24;
    --cat-soporte-border: rgba(245, 158, 11, 0.35);

    --cat-consulta-bg: rgba(59, 130, 246, 0.15);
    --cat-consulta-text: #60a5fa;
    --cat-consulta-border: rgba(59, 130, 246, 0.35);

    --glow: 0 0 18px rgba(123, 192, 144, 0.18);
    --glow-strong: 0 0 28px rgba(123, 192, 144, 0.28);
    --radius-card: 18px;
}

/* =========================================================
   1. FONDO GLOBAL Y RESET
   ========================================================= */
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.main {
    background-color: var(--bg) !important;
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -15%, rgba(57, 123, 83, 0.22), transparent 70%),
        radial-gradient(circle at 10% 40%, rgba(123, 192, 144, 0.08), transparent 45%),
        radial-gradient(circle at 90% 85%, rgba(57, 123, 83, 0.12), transparent 50%) !important;
    background-attachment: fixed !important;
    color: var(--text) !important;
    font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
}

/* Encabezados y títulos con Manrope */
h1, h2, h3, h4, .brand, .hero-title, .section-title {
    font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif !important;
    letter-spacing: -0.035em !important;
}

/* Protección de fuentes de iconos nativos */
.material-symbols-rounded,
.material-symbols-outlined,
.material-icons,
[data-testid="stIconMaterial"],
[data-testid="stSidebarCollapseButton"] span,
[data-testid="stFileUploader"] span[class*="material"],
[data-testid="stFileUploader"] i {
    font-family: 'Material Symbols Rounded', 'Material Symbols Outlined', 'Material Icons' !important;
    font-feature-settings: 'liga' 1 !important;
    text-transform: none !important;
}

[data-testid="stSidebarCollapseButton"] {
    min-width: 32px !important;
    max-width: 38px !important;
    overflow: hidden !important;
}

/* Contenedor principal centrado */
[data-testid="block-container"] {
    padding-top: 1.5rem !important;
    padding-bottom: 4rem !important;
    max-width: 980px !important;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}

/* =========================================================
   2. SIDEBAR ESTILO SAPO AI
   ========================================================= */
[data-testid="stSidebar"] {
    background-color: var(--bg-soft) !important;
    border-right: 1px solid var(--line) !important;
}

[data-testid="stSidebarContent"] {
    padding: 1.5rem 1.25rem !important;
    box-sizing: border-box !important;
    overflow-x: hidden !important;
}

.sidebar-header-sapo {
    display: flex;
    align-items: center;
    gap: 12px;
    padding-bottom: 1.25rem;
    margin-bottom: 1.25rem;
    border-bottom: 1px solid var(--line);
}

.brand-mark {
    width: 36px;
    height: 36px;
    display: grid;
    place-items: center;
    border-radius: 12px;
    color: #fff;
    background: var(--accent-strong);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.35), 0 4px 14px rgba(57, 123, 83, 0.4);
}

.sidebar-title {
    font-family: 'Manrope', sans-serif !important;
    font-weight: 800;
    font-size: 1rem;
    letter-spacing: -0.03em;
    color: var(--text);
    margin: 0;
}

.sidebar-title span {
    color: var(--accent);
}

.sidebar-kicker {
    display: block;
    color: var(--accent);
    font-size: 0.68rem;
    font-weight: 800;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin: 1.25rem 0 0.6rem 0;
}

.telemetry-card {
    box-sizing: border-box;
    width: 100%;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 14px;
    padding: 11px 14px;
    margin-bottom: 9px;
    backdrop-filter: blur(16px);
    transition: all 0.2s ease;
}

.telemetry-card:hover {
    border-color: rgba(123, 192, 144, 0.3);
    transform: translateY(-1px);
}

.telemetry-label {
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--muted);
    margin-bottom: 2px;
}

.telemetry-value {
    font-size: 0.86rem;
    font-weight: 700;
    color: var(--text);
}

/* =========================================================
   3. HERO / HEADER ESTILO SAPO AI
   ========================================================= */
.sapo-hero {
    text-align: center;
    padding: 1.75rem 1rem 2rem 1rem;
    margin-bottom: 1.25rem;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
}

/* Resplandor ambiental detrás del hero */
.sapo-hero::before {
    content: '';
    position: absolute;
    top: 0; left: 50%;
    transform: translateX(-50%);
    width: 600px;
    height: 180px;
    background: radial-gradient(ellipse at center top, rgba(57, 123, 83, 0.18) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
}

.sapo-hero > * { position: relative; z-index: 1; }

.eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 16px;
    border: 1px solid rgba(123, 192, 144, 0.22);
    border-radius: 99px;
    color: var(--accent);
    background: rgba(33, 60, 42, 0.6);
    font-size: 0.73rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-bottom: 0.9rem;
    backdrop-filter: blur(8px);
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.eyebrow:hover {
    border-color: rgba(123, 192, 144, 0.45);
    box-shadow: var(--glow);
}

.status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #5ac77b;
    box-shadow: 0 0 0 3px rgba(90, 199, 123, 0.2), 0 0 10px rgba(90, 199, 123, 0.4);
    animation: statusPulse 2s infinite ease-in-out;
}

@keyframes statusPulse {
    0%, 100% { opacity: 1; transform: scale(1); box-shadow: 0 0 0 3px rgba(90, 199, 123, 0.2), 0 0 10px rgba(90, 199, 123, 0.4); }
    50% { opacity: 0.5; transform: scale(0.82); box-shadow: 0 0 0 5px rgba(90, 199, 123, 0.08); }
}

.hero-title {
    font-size: clamp(2rem, 3.8vw, 2.9rem) !important;
    font-weight: 800 !important;
    letter-spacing: -0.055em !important;
    color: var(--text) !important;
    margin: 0 0 0.6rem 0 !important;
    line-height: 1.1 !important;
}

.hero-title span {
    background: linear-gradient(135deg, #7bc090 0%, #a8dbb8 50%, #7bc090 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 14px rgba(123, 192, 144, 0.35));
}

.hero-intro {
    font-size: 0.96rem;
    color: var(--muted);
    max-width: 520px;
    margin: 0 auto;
    line-height: 1.6;
    letter-spacing: 0.01em;
}

.hero-intro-centered {
    font-size: 1rem;
    font-weight: 500;
    color: var(--text);
    max-width: 640px;
    margin: 0.75rem auto 0 auto;
    line-height: 1.6;
    text-align: center;
    background: linear-gradient(90deg, var(--muted) 0%, var(--accent) 50%, var(--muted) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    opacity: 0.92;
}

/* =========================================================
   4. LÍNEAS DIVISORIAS ENTRE SECCIONES (SIN RECTÁNGULOS)
   ========================================================= */
hr, [data-testid="stDivider"], .section-divider {
    border: none !important;
    height: 1px !important;
    background: linear-gradient(
        to right,
        transparent 0%,
        var(--line) 20%,
        rgba(123, 192, 144, 0.18) 50%,
        var(--line) 80%,
        transparent 100%
    ) !important;
    margin: 2.5rem 0 !important;
    opacity: 1 !important;
}

/* =========================================================
   5. ENCABEZADOS DE ETAPA Y KICKERS
   ========================================================= */
.section-kicker {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: var(--accent);
    font-size: 0.7rem;
    font-weight: 800;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-bottom: 5px;
    opacity: 0.85;
}

.section-kicker::before {
    content: '';
    display: inline-block;
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: var(--accent);
    box-shadow: 0 0 6px rgba(123, 192, 144, 0.5);
    flex-shrink: 0;
}

.section-title-sapo {
    font-size: 1.4rem;
    font-weight: 800;
    letter-spacing: -0.045em;
    color: var(--text);
    margin: 0 0 0.35rem 0;
}

.section-desc-sapo {
    font-size: 0.87rem;
    color: var(--muted);
    margin: 0 0 1.3rem 0;
    line-height: 1.55;
    max-width: 620px;
}

/* =========================================================
   6. PESTAÑAS (TABS) MODERNAS SAPO AI
   ========================================================= */
[data-testid="stTabs"] [data-baseweb="tab-list"],
.stTabs [data-baseweb="tab-list"] {
    gap: 8px !important;
    border-bottom: 1px solid var(--line) !important;
    padding-bottom: 6px !important;
    margin-bottom: 1.25rem !important;
}

[data-testid="stTabs"] button[role="tab"],
.stTabs button[role="tab"],
.stTabs [data-baseweb="tab"] {
    border-radius: 12px !important;
    font-size: 0.86rem !important;
    font-weight: 700 !important;
    padding: 8px 18px !important;
    color: var(--muted) !important;
    background: transparent !important;
    border: 1px solid transparent !important;
    transition: all 0.2s ease !important;
}

[data-testid="stTabs"] button[role="tab"][aria-selected="true"],
.stTabs button[role="tab"][aria-selected="true"],
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    color: var(--text) !important;
    background: var(--surface-solid) !important;
    border: 1px solid var(--line) !important;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2) !important;
}

[data-testid="stTabs"] [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-highlight"] {
    background-color: var(--accent) !important;
    height: 2px !important;
}

[data-testid="stTabs"] [data-baseweb="tab-border"],
.stTabs [data-baseweb="tab-border"] {
    background-color: var(--line) !important;
}

/* =========================================================
   7. DROP-ZONE / FILE UPLOADER SAPO AI
   ========================================================= */
[data-testid="stFileUploader"] {
    border: 1.5px dashed color-mix(in srgb, var(--accent) 35%, transparent) !important;
    border-radius: 18px !important;
    background: color-mix(in srgb, var(--accent-soft) 25%, transparent) !important;
    padding: 14px !important;
    transition: all 0.2s ease !important;
}

[data-testid="stFileUploader"]:hover {
    border-color: var(--accent) !important;
    background: color-mix(in srgb, var(--accent-soft) 40%, transparent) !important;
}

[data-testid="stFileUploaderFileData"] {
    background: var(--surface-solid) !important;
    border: 1px solid var(--line) !important;
    border-radius: 14px !important;
    padding: 10px 14px !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25) !important;
}

[data-testid="stAudioInput"] {
    background: color-mix(in srgb, var(--accent-soft) 22%, transparent) !important;
    border: 1px solid var(--line) !important;
    border-radius: 18px !important;
    padding: 12px !important;
}

/* =========================================================
    8. VISUALIZACIÓN DE ONDA ACÚSTICA (WAVEFORM)
    ========================================================= */
.signal-visual-sapo {
    height: 56px;
    margin: 1rem 0;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 14px;
    background: linear-gradient(145deg, color-mix(in srgb, var(--accent-soft) 45%, transparent), color-mix(in srgb, var(--surface-solid) 80%, transparent));
    border: 1px solid var(--line);
    overflow: hidden;
    padding: 0 16px;
}

.waveform-svg {
    width: 100%;
    height: 100%;
    stroke: var(--accent);
    filter: drop-shadow(0 0 8px rgba(123, 192, 144, 0.4));
}

/* Waveform refinada - más sutil y elegante */
.signal-visual-sapo-refined {
    height: 48px;
    margin: 0.75rem 0 1rem 0;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
    background: color-mix(in srgb, var(--accent-soft) 18%, transparent);
    border: 1px solid color-mix(in srgb, var(--accent) 20%, transparent);
    overflow: hidden;
}

.waveform-svg-refined {
    width: 100%;
    height: 100%;
    filter: drop-shadow(0 0 6px rgba(123, 192, 144, 0.25));
}

/* =========================================================
   9. BOTONES ESTILO SAPO AI (MÁXIMA PRIORIDAD CSS)
   ========================================================= */
/* Primario: Verde Esmeralda SAPO AI */
button[data-testid="stBaseButton-primary"],
button[data-testid="baseButton-primary"],
div[data-testid="stButton"] > button[kind="primary"],
div[data-testid="stButton"] > button:first-child:not([kind="secondary"]) {
    background: var(--accent-strong) !important;
    background: linear-gradient(145deg, #3f875c 0%, #266440 100%) !important;
    border: 1px solid rgba(158, 210, 173, 0.35) !important;
    border-radius: 14px !important;
    color: #ffffff !important;
    font-family: 'Manrope', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    min-height: 48px !important;
    padding: 0 24px !important;
    box-shadow: 0 10px 26px color-mix(in srgb, var(--accent) 26%, transparent) !important;
    cursor: pointer !important;
    transition: transform 0.22s ease, box-shadow 0.22s ease, background 0.22s ease !important;
}

button[data-testid="stBaseButton-primary"]:hover,
button[data-testid="baseButton-primary"]:hover,
div[data-testid="stButton"] > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    background: linear-gradient(145deg, #489b6a 0%, #2d744b 100%) !important;
    box-shadow: 0 14px 32px color-mix(in srgb, var(--accent) 38%, transparent) !important;
}

button[data-testid="stBaseButton-primary"]:active,
button[data-testid="baseButton-primary"]:active {
    transform: translateY(1px) !important;
}

/* Secundario: Superficie de Cristal SAPO AI */
button[data-testid="stBaseButton-secondary"],
button[data-testid="baseButton-secondary"],
div[data-testid="stButton"] > button[kind="secondary"] {
    background: var(--surface) !important;
    border: 1px solid var(--line) !important;
    border-radius: 14px !important;
    color: var(--text) !important;
    font-family: 'Manrope', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    min-height: 44px !important;
    padding: 0 20px !important;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2) !important;
    transition: transform 0.22s ease, border-color 0.22s ease, background 0.22s ease !important;
}

button[data-testid="stBaseButton-secondary"]:hover,
button[data-testid="baseButton-secondary"]:hover,
div[data-testid="stButton"] > button[kind="secondary"]:hover {
    transform: translateY(-2px) !important;
    background: var(--surface-solid) !important;
    border-color: rgba(123, 192, 144, 0.35) !important;
}

/* =========================================================
   10. RESULTADOS: TARJETA DE ANÁLISIS SAPO AI
   ========================================================= */
.result-head-sapo {
    display: flex;
    align-items: center;
    gap: 16px;
    padding-bottom: 1.25rem;
    margin-bottom: 1.25rem;
    border-bottom: 1px solid var(--line);
}

.result-icon-badge {
    width: 50px;
    height: 50px;
    display: grid;
    place-items: center;
    border-radius: 16px;
    font-size: 1.4rem;
    background: var(--accent-soft);
    color: var(--accent);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.25);
}

.result-category-title {
    font-family: 'Manrope', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    margin: 2px 0 0 0;
}

/* Grid de Metadatos (result-meta) */
.result-meta-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    border: 1px solid var(--line);
    border-radius: 16px;
    overflow: hidden;
    margin: 1.25rem 0;
    background: color-mix(in srgb, var(--surface-solid) 60%, transparent);
}

.result-meta-item {
    padding: 13px 16px;
    border-right: 1px solid var(--line);
}

.result-meta-item:last-child {
    border-right: none;
}

.result-meta-label {
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--muted);
    margin-bottom: 3px;
}

.result-meta-val {
    font-size: 0.84rem;
    font-weight: 700;
    color: var(--text);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* Respuesta Sugerida (confidence-block) */
.confidence-response-box {
    background: color-mix(in srgb, var(--accent-soft) 40%, transparent);
    border: 1px solid color-mix(in srgb, var(--accent) 30%, transparent);
    border-radius: 18px;
    padding: 1.25rem 1.5rem;
    margin: 1rem 0 1.5rem 0;
}

.response-kicker {
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 8px;
}

.response-text-sapo {
    font-size: 0.94rem;
    color: var(--text);
    line-height: 1.6;
}

/* Textarea del editor */
.stTextArea textarea {
    background: var(--surface-solid) !important;
    border: 1px solid var(--line) !important;
    border-radius: 14px !important;
    color: var(--text) !important;
    font-size: 0.92rem !important;
    line-height: 1.6 !important;
    box-shadow: inset 0 2px 6px rgba(0, 0, 0, 0.25) !important;
}

.stTextArea textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(123, 192, 144, 0.25) !important;
}

/* =========================================================
   11. HISTORIAL RECIENTE / EXPANDERS SAPO AI
   ========================================================= */
[data-testid="stExpander"] {
    background: var(--surface) !important;
    border: 1px solid var(--line) !important;
    border-radius: 14px !important;
    margin-bottom: 0.65rem !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.18) !important;
    transition: all 0.2s ease !important;
}

[data-testid="stExpander"]:hover {
    border-color: rgba(123, 192, 144, 0.3) !important;
    transform: translateY(-1px) !important;
}

/* Estado vacío limpio */
.empty-state-sapo {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 1.35rem 1.6rem;
    background: color-mix(in srgb, var(--accent-soft) 22%, transparent);
    border: 1.5px dashed var(--line);
    border-radius: 18px;
    margin: 0.75rem 0;
}

.empty-state-icon-sapo {
    width: 44px;
    height: 44px;
    display: grid;
    place-items: center;
    border-radius: 14px;
    background: var(--surface-solid);
    color: var(--accent);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    flex-shrink: 0;
}

.empty-state-title-sapo {
    font-family: 'Manrope', sans-serif;
    font-size: 0.98rem;
    font-weight: 700;
    color: var(--text);
    margin: 0 0 2px 0;
}

.empty-state-desc-sapo {
    font-size: 0.84rem;
    color: var(--muted);
    margin: 0;
}

/* =========================================================
   12. RETOQUES DE POLISH
   ========================================================= */

/* Telemetry card: micro-glow verde al hover */
.telemetry-card:hover {
    border-color: rgba(123, 192, 144, 0.35) !important;
    box-shadow: var(--glow) !important;
    transform: translateY(-2px) !important;
}

/* Expander historial: left-border accent + glow al hover */
[data-testid="stExpander"]:hover {
    border-color: rgba(123, 192, 144, 0.3) !important;
    border-left-color: rgba(123, 192, 144, 0.55) !important;
    border-left-width: 2px !important;
    box-shadow: var(--glow), 0 6px 20px rgba(0, 0, 0, 0.22) !important;
    transform: translateY(-1px) !important;
}

/* Textarea: transición más suave + ligero glow en focus */
.stTextArea textarea {
    transition: border-color 0.25s ease, box-shadow 0.25s ease !important;
    font-family: 'DM Sans', sans-serif !important;
}

.stTextArea textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(123, 192, 144, 0.18), 0 0 14px rgba(123, 192, 144, 0.1) !important;
}

/* Scrollbar personalizada (Chrome/Edge/Safari) */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: var(--bg-soft);
    border-radius: 3px;
}
::-webkit-scrollbar-thumb {
    background: var(--accent-strong);
    border-radius: 3px;
    opacity: 0.7;
}
::-webkit-scrollbar-thumb:hover {
    background: var(--accent);
}

/* Toast de Streamlit: fondo más integrado */
[data-testid="stToast"] {
    background: var(--surface-solid) !important;
    border: 1px solid rgba(123, 192, 144, 0.25) !important;
    border-radius: 14px !important;
    box-shadow: var(--shadow), var(--glow) !important;
    backdrop-filter: blur(16px) !important;
}

/* Botones secundarios: micro-glow en hover */
button[data-testid="stBaseButton-secondary"]:hover,
div[data-testid="stButton"] > button[kind="secondary"]:hover {
    box-shadow: var(--glow) !important;
}

/* Tabs: tab activo con glow sutil */
[data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2), var(--glow) !important;
}

/* Spinner del expander (▶ ▼) */
[data-testid="stExpander"] summary {
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    color: var(--text) !important;
    padding: 0.65rem 0.75rem !important;
    transition: color 0.2s ease !important;
}

[data-testid="stExpander"] summary:hover {
    color: var(--accent) !important;
}
</style>
"""
