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
    padding: 1.5rem 1rem 1.75rem 1rem;
    margin-bottom: 1.25rem;
}

.eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 14px;
    border: 1px solid var(--line);
    border-radius: 99px;
    color: var(--accent);
    background: color-mix(in srgb, var(--accent-soft) 55%, transparent);
    font-size: 0.74rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.85rem;
}

.status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #5ac77b;
    box-shadow: 0 0 0 4px rgba(90, 199, 123, 0.22);
    animation: statusPulse 2s infinite ease-in-out;
}

@keyframes statusPulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.35; transform: scale(0.85); }
}

.hero-title {
    font-size: clamp(2rem, 3.8vw, 2.75rem) !important;
    font-weight: 800 !important;
    letter-spacing: -0.05em !important;
    color: var(--text) !important;
    margin: 0 0 0.5rem 0 !important;
    line-height: 1.15 !important;
}

.hero-title span {
    color: var(--accent);
}

.hero-intro {
    font-size: 0.95rem;
    color: var(--muted);
    max-width: 580px;
    margin: 0 auto;
    line-height: 1.55;
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
    border-top: 1px solid var(--line) !important;
    margin: 2.25rem 0 !important;
    opacity: 0.9 !important;
}

/* =========================================================
   5. ENCABEZADOS DE ETAPA Y KICKERS
   ========================================================= */
.section-kicker {
    display: block;
    color: var(--accent);
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 4px;
}

.section-title-sapo {
    font-size: 1.35rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    color: var(--text);
    margin: 0 0 0.4rem 0;
}

.section-desc-sapo {
    font-size: 0.88rem;
    color: var(--muted);
    margin: 0 0 1.25rem 0;
    line-height: 1.5;
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
</style>
"""
