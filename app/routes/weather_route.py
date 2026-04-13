"""
Rota responsável por lidar com solicitações relacionadas a informações meteorológicas.
"""

from fastapi import APIRouter

from app.agents.addres_agent import process_address_request
from app.agents.weather_agent import process_weather_request
from app.models.address import AddressErrorOutput, AddressOutput
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
    address_info = process_address_request(cep)

    if isinstance(address_info, AddressErrorOutput):
        return WeatherErrorOutput(message=address_info.message)

    if not isinstance(address_info, AddressOutput):
        return WeatherErrorOutput(message="Resposta inválida do agente de endereço.")

    if address_info.latitude is None or address_info.longitude is None:
        return WeatherErrorOutput(
            message=(
                "Não foi possível obter informações de "
                "clima para as coordenadas do CEP informado."
            )
        )

    return process_weather_request(address_info.latitude, address_info.longitude)
