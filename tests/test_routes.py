"""Testes das rotas HTTP principais."""

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_get_address_route_returns_address(monkeypatch) -> None:
    """Deve expor o retorno do agente de endereço na rota dedicada."""

    def fake_process_address_request(cep: str) -> dict:
        assert cep == "89010025"
        return {
            "logradouro": "Rua Doutor Luiz de Freitas Melro",
            "bairro": "Centro",
            "cidade": "Blumenau",
            "estado": "SC",
            "latitude": -26.9244749,
            "longitude": -49.0629788,
        }

    monkeypatch.setattr(
        "app.routes.address_route.process_address_request",
        fake_process_address_request,
    )

    response = client.get("/address/89010025")

    assert response.status_code == 200
    assert response.json()["cidade"] == "Blumenau"


def test_get_weather_route_returns_weather(monkeypatch) -> None:
    """Deve expor apenas os dados de clima quando o fluxo orquestrado for bem-sucedido."""

    class FakeResult:
        def __init__(self) -> None:
            self.data = {
                "time": "2026-04-13T12:00",
                "interval": 900,
                "temperature": 22.8,
                "windspeed": 8.5,
                "winddirection": 190,
                "is_day": 1,
                "weathercode": 3,
            }

    def fake_action_weather(payload: dict) -> FakeResult:
        assert payload == {"action": "weather", "cep": "89010025"}
        return FakeResult()

    monkeypatch.setattr("app.routes.weather_route.action_weather", fake_action_weather)

    response = client.get("/weather", params={"cep": "89010025"})

    assert response.status_code == 200
    assert response.json()["temperature"] == 22.8


def test_run_orchestrator_route_returns_response(monkeypatch) -> None:
    """Deve expor a resposta do orquestrador na rota dedicada."""

    def fake_orchestrate(payload: dict) -> dict:
        assert payload == {"action": "address", "cep": "89010025"}
        return {
            "result_type": "address",
            "data": {
                "logradouro": "Rua Doutor Luiz de Freitas Melro",
                "bairro": "Centro",
                "cidade": "Blumenau",
                "estado": "SC",
                "latitude": -26.9244749,
                "longitude": -49.0629788,
            },
        }

    monkeypatch.setattr("app.routes.orchestrator_route.orchestrate", fake_orchestrate)

    response = client.post(
        "/orchestrator",
        json={"action": "address", "cep": "89010025"},
    )

    assert response.status_code == 200
    assert response.json()["result_type"] == "address"