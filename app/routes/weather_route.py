"""
Rota responsável por lidar com solicitações relacionadas a informações meteorológicas.
"""

from fastapi import APIRouter

from app.agents.orchestrator_agent import action_weather
from app.models.orchestrator_schema import OrchestratorErrorOutput
from app.models.weather import WeatherErrorOutput, WeatherResponse

router = APIRouter()


@router.get("/weather")
def get_weather(cep: str) -> WeatherResponse:
    """
    Endpoint para obter informações meteorológicas com base nas coordenadas geográficas
    fornecidas pelo CEP.

    Args:
        cep (str): O CEP a ser consultado.

    Returns:
        WeatherResponse: O modelo de sucesso ou erro do agente de clima.
    """
    result = action_weather({"action": "weather", "cep": cep})

    if isinstance(result, OrchestratorErrorOutput):
        return WeatherErrorOutput(message=result.message)

    return result.data
