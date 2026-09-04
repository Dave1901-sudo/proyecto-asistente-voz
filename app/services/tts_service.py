"""Servicio de Text-to-Speech con gTTS (Google TTS) - requiere internet, compatible Python 3.14+."""

import io
from pathlib import Path
from gtts import gTTS


def sintetizar_a_bytes(texto: str, lang: str = "es") -> bytes:
    """
    Convierte texto a audio usando gTTS (Google TTS) y retorna bytes WAV.
    Requiere conexión a internet.
    """
    tts = gTTS(text=texto, lang="es", slow=False)
    buf = io.BytesIO()
    tts.write_to_fp(buf)
    buf.seek(0)
    return buf.read()


def sintetizar_voz(texto: str, salida: str | Path = "respuesta.wav") -> str:
    """
    Convierte texto a audio WAV y lo guarda en disco.
    Retorna la ruta del archivo generado.
    """
    from gtts import gTTS
    tts = gTTS(text=texto, lang="es", slow=False)
    tts.save(str(salida))
    return str(salida)