"""Rotas relacionadas a análise."""

from fastapi import APIRouter

from app.models.analyze import AnalyzeRequest, AnalyzeResponse
from app.services.analyze import classify_intent

router = APIRouter()


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_text(analyze: AnalyzeRequest) -> AnalyzeResponse:
    """Recebe um texto e retorna a intenção classificada."""

    intent = classify_intent(analyze.text)
    return AnalyzeResponse(intent=intent)
