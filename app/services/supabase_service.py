import requests
from supabase import create_client, Client
from app.config.settings import SUPABASE_URL, SUPABASE_KEY, N8N_WEBHOOK_URL
from typing import Optional

_client: Optional[Client] = None


def get_client() -> Client:
    global _client
    if _client is None:
        if not SUPABASE_URL or not SUPABASE_KEY:
            raise ValueError("SUPABASE_URL y SUPABASE_KEY deben estar configurados en .env")
        _client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return _client


def _disparar_n8n(interaccion_id: str, transcripcion: str, categoria: str, respuesta: str) -> bool:
    """Dispara webhook a n8n con los datos de la interacción."""
    try:
        payload = {
            "id": interaccion_id,
            "fecha": None,  # n8n puede usar timestamp actual
            "texto_transcrito": transcripcion,
            "categoria": categoria,
            "respuesta_sugerida": respuesta,
            "estado": "nuevo"
        }
        response = requests.post(N8N_WEBHOOK_URL, json=payload, timeout=5)
        return response.status_code in (200, 201)
    except Exception:
        # No fallar el guardado si n8n no responde
        return False


def guardar_interaccion(transcripcion: str, categoria: str, respuesta: str) -> str:
    """
    Guarda una interacción en Supabase y dispara webhook a n8n.
    Retorna el ID del registro insertado.
    """
    client = get_client()
    
    data = {
        "texto_transcrito": transcripcion,
        "categoria": categoria,
        "respuesta_sugerida": respuesta,
        "estado": "nuevo"
    }
    
    response = client.table("interacciones").insert(data).execute()
    
    if response.data and len(response.data) > 0:
        interaccion_id = str(response.data[0]["id"])
        # Disparar n8n en background (no bloquear si falla)
        _disparar_n8n(interaccion_id, transcripcion, categoria, respuesta)
        return interaccion_id
    
    raise Exception("No se pudo guardar la interacción en Supabase")


def obtener_interacciones(limit: int = 50) -> list:
    """Obtiene las últimas interacciones guardadas."""
    client = get_client()
    response = client.table("interacciones").select("*").order("fecha", desc=True).limit(limit).execute()
    return response.data or []


def actualizar_estado(interaccion_id: str, nuevo_estado: str) -> bool:
    """Actualiza el estado de una interacción."""
    client = get_client()
    response = client.table("interacciones").update({"estado": nuevo_estado}).eq("id", interaccion_id).execute()
    return len(response.data) > 0