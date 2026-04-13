"""
Rota dos agentes.
"""

from fastapi import APIRouter

from app.models.schemas import AgentInput, AgentOutput
from app.services.agent_service import process_message

router = APIRouter(prefix="/api/v1", tags=["agent"])


@router.post(
    "/agent",
    response_model=AgentOutput,
    deprecated=True,
    summary="Endpoint legado de agente",
)
def agent_endpoint(payload: AgentInput) -> AgentOutput:
    """
    Endpoint para processar mensagens dos agentes.

    Args:
        payload (AgentInput): mensagem a ser processada.

    Returns:
        AgentOutput: O output contendo a resposta gerada para a mensagem.
    """
    response, intent = process_message(payload.message, payload.user_name)
    return AgentOutput(response=response, intent=intent)
