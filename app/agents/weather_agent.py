"""
Agente responsável por processar mensagens relacionadas a informações meteorológicas.
"""

from app.models.weather import (WeatherErrorOutput, WeatherInput,
                                WeatherOutput, WeatherResponse)
from app.services.weather_service import get_weather_by_coordinates


def process_weather_request(latitude: float, longitude: float) -> WeatherResponse:
    """
    Processa uma solicitação de informações meteorológicas com base nas coordenadas geográficas fornecidas.

    Args:
        latitude (float): A latitude do local a ser consultado.
        longitude (float): A longitude do local a ser consultado.

    Returns:
        WeatherResponse: O modelo de sucesso ou erro do agente de clima.
    """
    request = WeatherInput(latitude=latitude, longitude=longitude)

    if not (-90 <= request.latitude <= 90) or not (-180 <= request.longitude <= 180):
        return WeatherErrorOutput(
            message="Coordenadas inválidas. Latitude deve estar entre -90 e 90, e longitude entre -180 e 180."
        )

    weather_data = get_weather_by_coordinates(request.latitude, request.longitude)

    if "error" in weather_data:
        return WeatherErrorOutput(message=weather_data["error"])
    if "message" in weather_data:
        return WeatherErrorOutput(message=weather_data["message"])

    return WeatherOutput(**weather_data)
