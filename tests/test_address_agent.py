"""Testes do agente de endereço."""

from app.agents.address_agent import process_address_request
from app.models.address import AddressErrorOutput, AddressOutput


def test_process_address_request_returns_address_output(monkeypatch) -> None:
    """Deve mapear a resposta do serviço para o model de saída."""

    def fake_validate_cep(cep: str) -> dict:
        assert cep == "89010-025"
        return {"cep": "89010025"}

    def fake_get_info_by_cep(cep: str) -> dict:
        assert cep == "89010025"
        return {
            "street": "Rua Doutor Luiz de Freitas Melro",
            "neighborhood": "Centro",
            "city": "Blumenau",
            "state": "SC",
            "latitude": -26.9244749,
            "longitude": -49.0629788,
        }

    monkeypatch.setattr("app.agents.address_agent.validate_cep", fake_validate_cep)
    monkeypatch.setattr("app.agents.address_agent.get_info_by_cep", fake_get_info_by_cep)

    result = process_address_request("89010-025")

    assert isinstance(result, AddressOutput)
    assert result.logradouro == "Rua Doutor Luiz de Freitas Melro"
    assert result.latitude == -26.9244749


def test_process_address_request_returns_error_for_invalid_cep(monkeypatch) -> None:
    """Deve retornar erro quando a validação do CEP falhar."""

    def fake_validate_cep(cep: str) -> dict:
        return {"error": "CEP inválido."}

    monkeypatch.setattr("app.agents.address_agent.validate_cep", fake_validate_cep)

    result = process_address_request("123")

    assert isinstance(result, AddressErrorOutput)
    assert result.message == "CEP inválido."