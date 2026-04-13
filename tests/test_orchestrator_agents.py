"""Testes do orquestrador de agentes."""

from app.agents.orchestrator_agents import orchestrate


def test_orchestrate_address_returns_address_data(monkeypatch) -> None:
	"""Deve retornar dados de endereço com coordenadas para action address."""

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
		"app.agents.orchestrator_agents.process_address_request",
		fake_process_address_request,
	)

	result = orchestrate({"action": "address", "cep": "89010025"})

	assert result.result_type == "address"
	assert result.data.logradouro == "Rua Doutor Luiz de Freitas Melro"
	assert result.data.latitude == -26.9244749
	assert result.data.longitude == -49.0629788


def test_orchestrate_weather_uses_cep_coordinates(monkeypatch) -> None:
	"""Deve retornar clima para action weather usando CEP válido."""

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

	def fake_process_weather_request(latitude: float, longitude: float) -> dict:
		assert latitude == -26.9244749
		assert longitude == -49.0629788
		return {"temperature": 22.8, "windspeed": 8.5}

	monkeypatch.setattr(
		"app.agents.orchestrator_agents.process_address_request",
		fake_process_address_request,
	)
	monkeypatch.setattr(
		"app.agents.orchestrator_agents.process_weather_request",
		fake_process_weather_request,
	)

	result = orchestrate({"action": "weather", "cep": "89010025"})

	assert result.result_type == "weather"
	assert result.data.temperature == 22.8


def test_orchestrate_weather_returns_error_for_invalid_cep() -> None:
	"""Deve falhar para action weather quando CEP for inválido."""

	result = orchestrate({"action": "weather", "cep": "123"})

	assert result.result_type == "error"
	assert result.message == "CEP inválido. O CEP deve conter 8 dígitos numéricos."


def test_orchestrate_all_returns_address_and_weather(monkeypatch) -> None:
	"""Deve retornar endereço e clima para action all a partir do CEP."""

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

	def fake_process_weather_request(latitude: float, longitude: float) -> dict:
		assert latitude == -26.9244749
		assert longitude == -49.0629788
		return {"temperature": 22.8, "windspeed": 8.5}

	monkeypatch.setattr(
		"app.agents.orchestrator_agents.process_address_request",
		fake_process_address_request,
	)
	monkeypatch.setattr(
		"app.agents.orchestrator_agents.process_weather_request",
		fake_process_weather_request,
	)

	result = orchestrate({"action": "all", "cep": "89010025"})

	assert result.result_type == "all"
	assert result.address_info.cidade == "Blumenau"
	assert result.weather_info is not None
	assert result.weather_info.temperature == 22.8


def test_orchestrate_all_returns_error_when_coordinates_missing(monkeypatch) -> None:
	"""Deve retornar endereço e erro de clima quando não houver coordenadas válidas."""

	def fake_process_address_request(_: str) -> dict:
		return {
			"logradouro": "Rua X",
			"bairro": "Centro",
			"cidade": "Cidade",
			"estado": "SC",
			"latitude": None,
			"longitude": None,
		}

	monkeypatch.setattr(
		"app.agents.orchestrator_agents.process_address_request",
		fake_process_address_request,
	)

	result = orchestrate({"action": "all", "cep": "89010025"})

	assert result.result_type == "all"
	assert result.address_info.cidade == "Cidade"
	assert result.weather_info is None
	assert result.weather_error == "Não foi possível obter coordenadas para o CEP informado."
