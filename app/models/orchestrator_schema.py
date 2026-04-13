"""Contratos de entrada e saída do orquestrador."""

from typing import Annotated, Literal, TypeAlias

from pydantic import BaseModel, Field

from app.models.address import AddressOutput
from app.models.weather import WeatherOutput


class OrchestratorInput(BaseModel):
    """Entrada padronizada para o orquestrador."""

    action: Literal[
        "address",
        "endereco",
        "endereço",
        "weather",
        "clima",
        "tempo",
        "all",
        "todos",
        "tudo",
    ]
    cep: str


class OrchestratorAddressOutput(BaseModel):
    """Saída da action de endereço do orquestrador."""

    result_type: Literal["address"] = "address"
    data: AddressOutput


class OrchestratorWeatherOutput(BaseModel):
    """Saída da action de clima do orquestrador."""

    result_type: Literal["weather"] = "weather"
    data: WeatherOutput


class OrchestratorAllOutput(BaseModel):
    """Saída da action combinada de endereço e clima."""

    result_type: Literal["all"] = "all"

    address_info: AddressOutput
    weather_info: WeatherOutput | None = None
    weather_error: str | None = None


class OrchestratorErrorOutput(BaseModel):
    """Saída padrão para erros do orquestrador."""

    result_type: Literal["error"] = "error"
    message: str


OrchestratorResponse: TypeAlias = Annotated[
    OrchestratorAddressOutput
    | OrchestratorWeatherOutput
    | OrchestratorAllOutput
    | OrchestratorErrorOutput,
    Field(discriminator="result_type"),
]
