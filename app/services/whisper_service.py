from faster_whisper import WhisperModel
from app.config.settings import WHISPER_MODEL, WHISPER_DEVICE, WHISPER_COMPUTE_TYPE

_model = None


def get_model() -> WhisperModel:
    global _model
    if _model is None:
        _model = WhisperModel(
            WHISPER_MODEL,
            device=WHISPER_DEVICE,
            compute_type=WHISPER_COMPUTE_TYPE,
        )
    return _model


def transcribir_audio(ruta_audio: str, modelo: str = None) -> str:
    model = get_model()
    segments, info = model.transcribe(ruta_audio, language="es", beam_size=5)
    texto = " ".join([seg.text for seg in segments]).strip()
    return texto