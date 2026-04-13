"""
Serviço de busca de informações meteorológicas utilizando a API Open-Meteo.
"""

import requests


def get_weather_by_coordinates(latitude: float, longitude: float) -> dict:
    """
    Busca informações meteorológicas com base nas coordenadas geográficas fornecidas.

    Args:
        latitude (float): A latitude do local a ser consultado.
        longitude (float): A longitude do local a ser consultado.

    Returns:
        dict: Um dicionário contendo as informações meteorológicas ou uma mensagem de erro.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true",
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        data = response.json()
        if "current_weather" in data:
            return data["current_weather"]
        else:
            return {
                "message": "Informações meteorológicas não encontradas para as coordenadas fornecidas."
            }
    except requests.RequestException as e:
        return {"message": f"Erro ao buscar informações meteorológicas: {e}"}
