"""
Serviço que busca coordenadas geograficas a partir de um cep utilizando brazilapi..com.br
"""

import requests


def validate_cep(cep: object) -> dict:
    """
    Valida e normaliza CEP para o formato de 8 dígitos.

    Args:
    cep (object): O CEP a ser validado, pode ser de qualquer tipo.

    Returns:
    dict: Um dicionário contendo o CEP normalizado ou uma mensagem de erro se o
    CEP for inválido.

    """
    if not isinstance(cep, str) or not cep.strip():
        return {"error": "CEP inválido. Informe um CEP em formato texto."}

    normalized_cep = "".join(char for char in cep if char.isdigit())
    if len(normalized_cep) != 8:
        return {"error": "CEP inválido. O CEP deve conter 8 dígitos numéricos."}

    return {"cep": normalized_cep}


def get_info_by_cep(cep: str) -> dict:
    """
    Busca informações de endereço e coordenadas geográficas com base no CEP fornecido.

    Args:
        cep (str): O CEP a ser consultado.
    Returns:
        dict: Um dicionário contendo endereço, coordenadas ou uma mensagem de erro.
        Exemplo de resposta:
            {
                "cep": "89010025",
                "state": "SC",
                "city": "Blumenau",
                "neighborhood": "Centro",
                "street": "Rua Doutor Luiz de Freitas Melro",
                "location": {
                    "type": "Point",
                    "coordinates": {
                        "longitude": "-49.0629788",
                        "latitude": "-26.9244749"
                    }
                }
            }
    """

    url = f"https://brasilapi.com.br/api/cep/v2/{cep}"

    try:
        response = requests.get(
            url, timeout=5
        )  # Define um tempo limite para a requisição
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        data = response.json()
        location = data.get("location", {})
        coordinates = location.get("coordinates", {})

        latitude_raw = coordinates.get("latitude")
        longitude_raw = coordinates.get("longitude")

        latitude = None
        longitude = None

        if latitude_raw is not None and longitude_raw is not None:
            try:
                latitude = float(latitude_raw)
                longitude = float(longitude_raw)
            except (TypeError, ValueError):
                latitude = None
                longitude = None

        return {
            "cep": data.get("cep", cep),
            "street": data.get("street", ""),
            "neighborhood": data.get("neighborhood", ""),
            "city": data.get("city", ""),
            "state": data.get("state", ""),
            "latitude": latitude,
            "longitude": longitude,
        }
    except requests.RequestException as e:
        return {"error": f"Erro ao buscar dados de CEP: {e}"}
