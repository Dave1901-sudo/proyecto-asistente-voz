import pytest
from app.services.whisper_service import transcribir_audio


def test_whisper_service_import():
    """Verifica que el servicio de Whisper se importa correctamente."""
    assert transcribir_audio is not None


def test_whisper_service_callable():
    """Verifica que la función es invocable."""
    assert callable(transcribir_audio)