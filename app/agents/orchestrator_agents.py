"""
Agente orquestrador responsável por decidir qual agente executar
"""

from collections.abc import Mapping
from typing import Any

from pydantic import BaseModel

from app.agents.addres_agent import process_address_request
from app.agents.weather_agent import process_weather_request
from app.models.address import AddressErrorOutput, AddressOutput
from app.models.orchestrator_schema import (OrchestratorAddressOutput,
                                            OrchestratorAllOutput,
                                            OrchestratorErrorOutput,
                                            OrchestratorResponse,
                                            OrchestratorWeatherOutput)
from app.models.weather import WeatherErrorOutput, WeatherOutput


def _error_response(message: str) -> OrchestratorErrorOutput:
    """Gera saída padronizada de erro."""
    return OrchestratorErrorOutput(message=message)


def _to_dict(data: BaseModel | Mapping[str, object] | dict) -> dict:
    """Normaliza models e mappings para dict comum."""
    if isinstance(data, BaseModel):
        return data.model_dump()
    return dict(data)


def _normalize_address_response(
    data: BaseModel | Mapping[str, object] | dict,
) -> AddressOutput | AddressErrorOutput:
    """Converte resposta do agente de endereço em model tipado."""
    if isinstance(data, (AddressOutput, AddressErrorOutput)):
        return data

    normalized = _to_dict(data)
    if "message" in normalized:
        return AddressErrorOutput(message=str(normalized["message"]))

    return AddressOutput(**normalized)


def _normalize_weather_response(
    data: BaseModel | Mapping[str, object] | dict,
) -> WeatherOutput | WeatherErrorOutput:
    """Converte resposta do agente de clima em model tipado."""
    if isinstance(data, (WeatherOutput, WeatherErrorOutput)):
        return data

    normalized = _to_dict(data)
    if "message" in normalized:
        return WeatherErrorOutput(message=str(normalized["message"]))

    return WeatherOutput(**normalized)


def action_address(
    payload: dict[str, Any],
) -> OrchestratorAddressOutput | OrchestratorErrorOutput:
    """Executa a action de endereço."""
    info = _normalize_address_response(process_address_request(payload.get("cep", "")))

    if isinstance(info, AddressErrorOutput):
        return _error_response(info.message)

    return OrchestratorAddressOutput(data=info)


def _weather_from_address_info(
    address_info: AddressOutput,
) -> OrchestratorWeatherOutput | OrchestratorErrorOutput:
    """Executa agente de clima usando latitude/longitude vindos do agente de endereço."""
    latitude = address_info.latitude
    longitude = address_info.longitude

    if not isinstance(latitude, (int, float)) or not isinstance(
        longitude, (int, float)
    ):
        return _error_response(
            "Não foi possível obter coordenadas para o CEP informado."
        )

    weather_info = _normalize_weather_response(
        process_weather_request(latitude, longitude)
    )

    if isinstance(weather_info, WeatherErrorOutput):
        return _error_response(weather_info.message)

    return OrchestratorWeatherOutput(data=weather_info)


def action_weather(
    payload: dict[str, Any],
) -> OrchestratorWeatherOutput | OrchestratorErrorOutput:
    """Executa a action de clima."""
    address_info = action_address(payload)

    if isinstance(address_info, OrchestratorErrorOutput):
        return address_info

    return _weather_from_address_info(address_info.data)


def action_all(
    payload: dict[str, Any],
) -> OrchestratorAllOutput | OrchestratorErrorOutput:
    """Executa a action combinada de endereço e clima."""
    address_info = action_address(payload)

    if isinstance(address_info, OrchestratorErrorOutput):
        return address_info

    weather_info = _weather_from_address_info(address_info.data)

    if isinstance(weather_info, OrchestratorErrorOutput):
        return OrchestratorAllOutput(
            address_info=address_info.data,
            weather_error=weather_info.message,
        )

    return OrchestratorAllOutput(
        address_info=address_info.data,
        weather_info=weather_info.data,
    )


def orchestrate(payload: dict[str, Any]) -> OrchestratorResponse:
    """
    Decide qual agente executar com base na mensagem recebida e retorna a resposta gerada.

    args:
    payload (dict): O dicionário contendo a ação e os dados necessários para processar

    Returns:
    OrchestratorResponse: A resposta gerada pelo agente selecionado ou uma saída de erro.

    """
    action = payload.get("action")

    if action in {"address", "endereco", "endereço"}:
        return action_address(payload)

    if action in {"weather", "clima", "tempo"}:
        return action_weather(payload)

    if action in {"all", "todos", "tudo"}:
        return action_all(payload)

    return _error_response(
        "Ação não reconhecida. Por favor, forneça uma ação válida.\n"
        " ---- \n"
        "Ações válidas: 'address', 'weather', 'all' ou \n"
        "seus equivalentes em português."
    )
