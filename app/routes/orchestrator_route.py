"""
Rota responsável por gerenciar solicitações relacionadas ao orquestrador.
"""

from fastapi import APIRouter

from app.agents.orchestrator_agent import orchestrate
from app.models.orchestrator_schema import OrchestratorInput, OrchestratorResponse

router = APIRouter()


@router.post("/orchestrator", response_model=OrchestratorResponse)
def run_orchestrator(payload: OrchestratorInput) -> OrchestratorResponse:
    return orchestrate(payload.model_dump())