"""Testes do serviço de CEP."""

import requests

from app.services.cep_service import get_info_by_cep, validate_cep


def test_validate_cep_normalizes_digits() -> None:
    """Deve remover caracteres não numéricos e retornar CEP com 8 dígitos."""

    result = validate_cep("89010-025")

    assert result == {"cep": "89010025"}


def test_validate_cep_rejects_invalid_input_types() -> None:
    """Deve rejeitar CEP ausente ou fora do formato esperado."""

    assert validate_cep(None) == {
        "error": "CEP inválido. Informe um CEP em formato texto."
    }
    assert validate_cep("123") == {
        "error": "CEP inválido. O CEP deve conter 8 dígitos numéricos."
    }


def test_get_info_by_cep_returns_address_and_coordinates(monkeypatch) -> None:
    """Deve converter coordenadas da API para float."""

    class FakeResponse:
        def raise_for_status(self) -> None:
            return None

        def json(self) -> dict:
            return {
                "cep": "89010025",
                "street": "Rua Doutor Luiz de Freitas Melro",
                "neighborhood": "Centro",
                "city": "Blumenau",
                "state": "SC",
                "location": {
                    "coordinates": {
                        "longitude": "-49.0629788",
                        "latitude": "-26.9244749",
                    }
                },
            }

    def fake_get(url: str, timeout: int) -> FakeResponse:
        assert url.endswith("/89010025")
        assert timeout == 5
        return FakeResponse()

    monkeypatch.setattr("app.services.cep_service.requests.get", fake_get)

    result = get_info_by_cep("89010025")

    assert result["cep"] == "89010025"
    assert result["city"] == "Blumenau"
    assert result["latitude"] == -26.9244749
    assert result["longitude"] == -49.0629788


def test_get_info_by_cep_returns_error_on_request_failure(monkeypatch) -> None:
    """Deve encapsular falhas de rede em mensagem de erro."""

    def fake_get(url: str, timeout: int) -> None:
        raise requests.RequestException("timeout")

    monkeypatch.setattr("app.services.cep_service.requests.get", fake_get)

    result = get_info_by_cep("89010025")

    assert result == {"error": "Erro ao buscar dados de CEP: timeout"}