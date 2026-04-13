"""Contratos de entrada e saída do agente de endereço."""

from typing import TypeAlias

from pydantic import BaseModel


class AddressInput(BaseModel):
    """Entrada do agente de endereço."""

    cep: str


class AddressOutput(BaseModel):
    """Saída de sucesso do agente de endereço."""

    logradouro: str
    bairro: str
    cidade: str
    estado: str
    latitude: float | None = None
    longitude: float | None = None


class AddressErrorOutput(BaseModel):
    """Saída de erro do agente de endereço."""

    message: str


AddressResponse: TypeAlias = AddressOutput | AddressErrorOutput
