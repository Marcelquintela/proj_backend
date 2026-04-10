"""
Rota dos agentes.
"""

from fastapi import APIRouter
from app.models.schemas import AgentInput, AgentOutput
from app.services.agent_service import process_message

router = APIRouter(prefix="/api/v1", tags=["agent"])

@router.post("/agent", response_model=AgentOutput)
def agent_endpoint(input: AgentInput) -> AgentOutput:
    """
    Endpoint para processar mensagens dos agentes.

    Args:
        input (AgentInput): O input contendo a mensagem a ser processada.

    Returns:
        AgentOutput: O output contendo a resposta gerada para a mensagem.
    """
    response, intent = process_message(input.message, input.user_name)
    return AgentOutput(response=response, agent_type=input.agent_type, intent=intent)
