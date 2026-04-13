"""Testes do agente de clima."""

from app.agents.weather_agent import process_weather_request
from app.models.weather import WeatherErrorOutput, WeatherOutput


def test_process_weather_request_returns_weather_output(monkeypatch) -> None:
    """Deve retornar model de sucesso quando o service responder com clima válido."""

    def fake_get_weather_by_coordinates(latitude: float, longitude: float) -> dict:
        assert latitude == -26.9244749
        assert longitude == -49.0629788
        return {
            "time": "2026-04-13T12:00",
            "interval": 900,
            "temperature": 22.8,
            "windspeed": 8.5,
            "winddirection": 190,
            "is_day": 1,
            "weathercode": 3,
        }

    monkeypatch.setattr(
        "app.agents.weather_agent.get_weather_by_coordinates",
        fake_get_weather_by_coordinates,
    )

    result = process_weather_request(-26.9244749, -49.0629788)

    assert isinstance(result, WeatherOutput)
    assert result.temperature == 22.8


def test_process_weather_request_returns_error_for_invalid_coordinates() -> None:
    """Deve retornar model de erro para coordenadas inválidas."""

    result = process_weather_request(-120.0, -49.0629788)

    assert isinstance(result, WeatherErrorOutput)
    assert "Coordenadas inválidas" in result.message