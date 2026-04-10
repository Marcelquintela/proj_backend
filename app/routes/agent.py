"""
Rota dos agentes.
"""

from fastapi import APIRouter
from app.models.schemas import AgentInput, AgentOutput
from app.services.agent_service import process_message

router = APIRouter()

@router.post("/agent", response_model=AgentOutput)
async def agent_endpoint(input: AgentInput) -> AgentOutput:
    """
    Endpoint para processar mensagens dos agentes.

    Args:
        input (AgentInput): O input contendo a mensagem a ser processada.

    Returns:
        AgentOutput: O output contendo a resposta gerada para a mensagem.
    """
    response = await process_message(input.message)
    return AgentOutput(response=response)
