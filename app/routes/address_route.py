"""
Rota responsável por gerenciar solicitações relacionadas a endereços.
"""

from fastapi import APIRouter

from app.agents.addres_agent import process_address_request
from app.models.address import AddressResponse

router = APIRouter()


@router.get("/address/{cep}", response_model=AddressResponse)
def get_address(cep: str) -> AddressResponse:
    """
    Endpoint para obter informações de endereço com base no CEP fornecido.

    Args:
        cep (str): O CEP a ser consultado.

    Returns:
        dict: Um dicionário contendo as informações do endereço ou uma mensagem de erro.
    """
    return process_address_request(cep)
