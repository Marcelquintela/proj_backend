"""Testes do serviço de agente."""

import asyncio

from app.services.agent_service import process_message


def test_process_message_returns_precificacao_for_price_keywords() -> None:
    """Deve retornar resposta de precificação para termos de preço."""
    text = "Qual é o preço do plano?"

    result = asyncio.run(process_message(text))

    assert result == "Vou te ajudar com a precificação."


def test_process_message_returns_problem_response_for_problem_keywords() -> None:
    """Deve retornar resposta de suporte para termos de problema."""
    text = "Estou com erro no acesso"

    result = asyncio.run(process_message(text))

    assert "Lamento ouvir" in result


def test_process_message_returns_fallback_for_unknown_text() -> None:
    """Deve retornar fallback quando não houver correspondência."""
    text = "Bom dia"

    result = asyncio.run(process_message(text))

    assert "Não consegui entender" in result
