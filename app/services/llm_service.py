import json
import re
import time
import ollama
from app.config.settings import OLLAMA_BASE_URL, OLLAMA_MODEL

_client = None


def get_client() -> ollama.Client:
    global _client
    if _client is None:
        _client = ollama.Client(host=OLLAMA_BASE_URL)
    return _client


CATEGORIAS = [
    "consulta_general",
    "reclamo",
    "soporte_tecnico",
    "ventas",
]

PROMPT_SYSTEM = f"""
Eres un asistente de clasificación para atención al cliente.
Tu tarea: recibir una transcripción de audio de un cliente y devolver SOLO un JSON válido con dos claves:
- "categoria": una de {CATEGORIAS}
- "respuesta": una respuesta breve, profesional y empática (máx. 3 oraciones) que el agente pueda enviar al cliente.

Reglas estrictas:
1. La categoría DEBE ser exactamente una de la lista.
2. La respuesta NO debe incluir la categoría ni etiquetas, solo el texto de la respuesta.
3. Si la transcripción es ambigua, elige "consulta_general".
4. Salida: SOLO el JSON, sin markdown, sin explicaciones, sin texto extra.
"""

FEW_SHOT_EXAMPLES = [
    {
        "input": "Hola, quisiera saber el horario de atención de su oficina central.",
        "output": {"categoria": "consulta_general", "respuesta": "Nuestro horario de atención es de lunes a viernes de 9:00 a 18:00. ¿Hay algo más en lo que pueda ayudarle?"}
    },
    {
        "input": "Me llegó el producto roto, esto es inaceptable, quiero una solución ya.",
        "output": {"categoria": "reclamo", "respuesta": "Lamentamos mucho el inconveniente. Registramos su reclamo y le contactaremos en menos de 24 horas para gestionar el cambio o devolución."}
    },
    {
        "input": "La aplicación me da error 500 al intentar pagar, no puedo completar la compra.",
        "output": {"categoria": "soporte_tecnico", "respuesta": "Gracias por reportarlo. Nuestro equipo técnico ya está revisando el error 500 en el proceso de pago. Le avisaremos cuando esté solucionado."}
    },
    {
        "input": "Quiero contratar el plan premium para mi equipo de 10 personas, ¿cuánto cuesta?",
        "output": {"categoria": "ventas", "respuesta": "El plan premium para 10 usuarios tiene un costo de $X/mes. Un asesor comercial le contactará hoy para detallar beneficios y formas de pago."}
    },
]


def _build_prompt(transcripcion: str) -> str:
    examples = "\n".join(
        f"Entrada: {ex['input']}\nSalida: {json.dumps(ex['output'], ensure_ascii=False)}"
        for ex in FEW_SHOT_EXAMPLES
    )
    return f"{PROMPT_SYSTEM}\n\nEjemplos:\n{examples}\n\nEntrada: {transcripcion}\nSalida:"


def _extract_json(text: str) -> dict:
    """Extrae el primer JSON válido del texto."""
    # Intento directo
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Buscar bloque { ... }
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            pass
    raise ValueError("No se pudo parsear JSON válido de la respuesta del modelo")


def clasificar_y_responder(texto: str, max_reintentos: int = 2) -> dict:
    client = get_client()
    prompt = _build_prompt(texto)

    for intento in range(max_reintentos + 1):
        try:
            response = client.chat(
                model=OLLAMA_MODEL,
                messages=[
                    {"role": "system", "content": PROMPT_SYSTEM},
                    {"role": "user", "content": prompt},
                ],
                options={"temperature": 0.1, "num_predict": 200},
            )
            content = response["message"]["content"].strip()
            data = _extract_json(content)

            # Validar categoría
            cat = data.get("categoria", "").strip().lower()
            if cat not in CATEGORIAS:
                cat = "consulta_general"

            resp = data.get("respuesta", "").strip()
            if not resp:
                resp = "Gracias por su mensaje. Un agente revisará su caso y le responderá a la brevedad."

            return {"categoria": cat, "respuesta": resp}

        except Exception as e:
            if intento == max_reintentos:
                return {
                    "categoria": "consulta_general",
                    "respuesta": "Gracias por su mensaje. Un agente revisará su caso y le responderá a la brevedad.",
                }
            time.sleep(0.5 * (intento + 1))

    # Fallback (no debería llegar)
    return {"categoria": "consulta_general", "respuesta": "Gracias por su mensaje. Un agente revisará su caso y le responderá a la brevedad."}