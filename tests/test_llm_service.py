import pytest
from app.services.llm_service import clasificar_y_responder, CATEGORIAS


def test_llm_service_import():
    """Verifica que el servicio de LLM se importa correctamente."""
    assert clasificar_y_responder is not None


def test_categorias_definidas():
    """Verifica que las 4 categorías requeridas están definidas."""
    esperadas = {"consulta_general", "reclamo", "soporte_tecnico", "ventas"}
    assert set(CATEGORIAS) == esperadas


def test_categorias_no_vacias():
    """Verifica que no hay categorías vacías."""
    assert all(cat.strip() for cat in CATEGORIAS)