"""Modelos de dados para análise."""

from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    """Dados recebidos para classificação de intenção."""

    text: str


class AnalyzeResponse(BaseModel):
    """Resultado da classificação de intenção."""

    intent: str
