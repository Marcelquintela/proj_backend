"""Testes do serviço de clima."""

import requests

from app.services.weather_service import get_weather_by_coordinates


def test_get_weather_by_coordinates_calls_open_meteo_with_current_weather(
    monkeypatch,
) -> None:
    """Deve chamar a Open-Meteo com os parâmetros esperados."""

    class FakeResponse:
        def raise_for_status(self) -> None:
            return None

        def json(self) -> dict:
            return {
                "current_weather": {
                    "temperature": 22.8,
                    "windspeed": 8.5,
                }
            }

    def fake_get(url: str, params: dict, timeout: int) -> FakeResponse:
        assert url == "https://api.open-meteo.com/v1/forecast"
        assert params == {
            "latitude": -26.9244749,
            "longitude": -49.0629788,
            "current_weather": "true",
        }
        assert timeout == 5
        return FakeResponse()

    monkeypatch.setattr("app.services.weather_service.requests.get", fake_get)

    result = get_weather_by_coordinates(-26.9244749, -49.0629788)

    assert result == {"temperature": 22.8, "windspeed": 8.5}


def test_get_weather_by_coordinates_returns_message_when_api_has_no_current_weather(
    monkeypatch,
) -> None:
    """Deve retornar mensagem amigável quando a API não trouxer clima atual."""

    class FakeResponse:
        def raise_for_status(self) -> None:
            return None

        def json(self) -> dict:
            return {}

    def fake_get(url: str, params: dict, timeout: int) -> FakeResponse:
        return FakeResponse()

    monkeypatch.setattr("app.services.weather_service.requests.get", fake_get)

    result = get_weather_by_coordinates(-26.9244749, -49.0629788)

    assert result == {
        "message": "Informações meteorológicas não encontradas para as coordenadas fornecidas."
    }


def test_get_weather_by_coordinates_returns_message_on_request_failure(
    monkeypatch,
) -> None:
    """Deve encapsular falhas de rede em mensagem de erro."""

    def fake_get(url: str, params: dict, timeout: int) -> None:
        raise requests.RequestException("timeout")

    monkeypatch.setattr("app.services.weather_service.requests.get", fake_get)

    result = get_weather_by_coordinates(-26.9244749, -49.0629788)

    assert result == {"message": "Erro ao buscar informações meteorológicas: timeout"}