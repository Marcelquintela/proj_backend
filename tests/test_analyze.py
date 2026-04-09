"""Testes da classificação de intenção."""

from app.services.analyze import classify_intent


def test_classify_intent_returns_compra_for_compra_keyword() -> None:
    """Deve retornar compra quando o texto contiver a palavra compra."""

    text = "Quero fazer uma compra hoje"

    result = classify_intent(text)

    assert result == "compra"


def test_classify_intent_returns_compra_for_comprar_keyword() -> None:
    """Deve retornar compra quando o texto contiver a palavra comprar."""

    text = "Estou pensando em comprar um curso"

    result = classify_intent(text)

    assert result == "compra"


def test_classify_intent_returns_outro_for_non_purchase_text() -> None:
    """Deve retornar outro quando não houver indicação de compra."""

    text = "Hoje vou caminhar no parque"

    result = classify_intent(text)

    assert result == "outro"