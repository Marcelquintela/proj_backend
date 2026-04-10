"""Testes do serviço de agente."""

from app.services.agent_service import process_message


def test_process_message_returns_precificacao_for_price_keywords() -> None:
    """Deve retornar resposta de precificação para termos de preço."""
    text = "Qual é o preço do plano?"

    response, intent = process_message(text)

    assert response == "vou te ajudar com a precificação."
    assert intent == "precificacao"


def test_process_message_returns_problem_response_for_problem_keywords() -> None:
    """Deve retornar resposta de suporte para termos de problema."""
    text = "Estou com erro no acesso"

    response, intent = process_message(text)

    assert "lamento ouvir" in response
    assert intent == "suporte_tecnico"


def test_process_message_returns_fallback_for_unknown_text() -> None:
    """Deve retornar fallback quando não houver correspondência."""
    text = "Bom dia"

    response, intent = process_message(text)

    assert "não consegui entender" in response
    assert intent == "geral"
