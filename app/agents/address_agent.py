"""
Agente responsável por processar mensagens relacionadas a endereços.
"""

from app.models.address import (
    AddressErrorOutput,
    AddressInput,
    AddressOutput,
    AddressResponse,
)
from app.services.cep_service import get_info_by_cep, validate_cep


def process_address_request(cep: str) -> AddressResponse:
    """
    Processa uma solicitação de endereço com base no CEP fornecido.

    Args:
        cep (str): O CEP a ser consultado.

    Returns:
        AddressResponse: O modelo de sucesso ou erro do agente de endereço.
    """
    request = AddressInput(cep=cep)

    cep_validation = validate_cep(request.cep)
    if "error" in cep_validation:
        return AddressErrorOutput(message=cep_validation["error"])

    data = get_info_by_cep(cep_validation["cep"])

    if "error" in data:
        return AddressErrorOutput(message=data["error"])

    return AddressOutput(
        logradouro=data.get("street", ""),
        bairro=data.get("neighborhood", ""),
        cidade=data.get("city", ""),
        estado=data.get("state", ""),
        latitude=data.get("latitude"),
        longitude=data.get("longitude"),
    )