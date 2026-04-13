# Proj_Autocapacita

Projeto de estudo em FastAPI com evolução incremental de uma API simples para uma arquitetura com agentes especializados e um orquestrador.

## Escopo Atual

- Dia 1: cadastro de usuários e análise de intenção de texto.
- Dia 2: endpoint legado de agente para respostas simples de suporte.
- Dia 3: fluxo multiagente com busca de endereço por CEP, consulta de clima por coordenadas e orquestração entre agentes.

## Arquitetura

O projeto segue a separação abaixo:

- routes: expõem os endpoints HTTP.
- services: integram APIs externas e executam regras operacionais.
- agents: tratam o caso de uso e coordenam a composição entre services.
- models: definem contratos de entrada e saída com Pydantic.

Fluxos principais do Dia 3:

- app/services/cep_service.py: valida CEP e consulta endereço/coordenadas.
- app/services/weather_service.py: consulta clima atual na Open-Meteo.
- app/agents/address_agent.py: trata o caso de uso de endereço.
- app/agents/weather_agent.py: trata o caso de uso de clima.
- app/agents/orchestrator_agent.py: decide e compõe os fluxos address, weather e all.

## Estrutura

- app/main.py: inicialização da aplicação e registro das rotas.
- app/routes/: endpoints HTTP.
- app/agents/: agentes especializados e orquestrador.
- app/services/: integração com APIs e regras operacionais.
- app/models/: contratos de entrada e saída.
- tests/: testes unitários e de rotas.

## Requisitos

- Python 3.10+
- Git

## Dependências

- requirements.txt: dependências da aplicação.
- requirements-dev.txt: ferramentas de desenvolvimento e testes.

## Como Executar

### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

### Linux ou macOS

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

## Qualidade e Testes

Ferramentas de desenvolvimento:

- black
- isort
- pydocstyle
- pytest

Fluxo recomendado antes de subir alterações:

```bash
black app tests
isort app tests
pydocstyle app
pytest tests -q
```

## Endpoints

### Gerais

- GET /: valida se a API está no ar.
- POST /api/v1/users: cria um usuário.
- POST /api/v1/analyze: classifica a intenção de um texto.

### Legado

- POST /api/v1/agent: endpoint legado de agente simples. Continua disponível por compatibilidade, mas não é o fluxo principal do Dia 3.

### Dia 3

- GET /address/{cep}: retorna endereço e coordenadas a partir do CEP.
- GET /weather?cep=89010025: retorna clima atual a partir do CEP.
- POST /orchestrator: executa um fluxo orquestrado com action address, weather ou all.

## Exemplos

### GET /

```json
{
  "message": "API funcionando!"
}
```

### GET /address/89010025

```json
{
  "logradouro": "Rua Doutor Luiz de Freitas Melro",
  "bairro": "Centro",
  "cidade": "Blumenau",
  "estado": "SC",
  "latitude": -26.9244749,
  "longitude": -49.0629788
}
```

### GET /weather?cep=89010025

Exemplo ilustrativo. Como o clima é consultado em tempo real, os valores podem variar.

```json
{
  "time": "2026-04-13T12:00",
  "interval": 900,
  "temperature": 22.8,
  "windspeed": 8.5,
  "winddirection": 190,
  "is_day": 1,
  "weathercode": 3
}
```

### POST /orchestrator

Exemplo ilustrativo. Como o clima é consultado em tempo real, os valores podem variar.

Request:

```json
{
  "action": "all",
  "cep": "89010025"
}
```

Response:

```json
{
  "result_type": "all",
  "address_info": {
    "logradouro": "Rua Doutor Luiz de Freitas Melro",
    "bairro": "Centro",
    "cidade": "Blumenau",
    "estado": "SC",
    "latitude": -26.9244749,
    "longitude": -49.0629788
  },
  "weather_info": {
    "time": "2026-04-13T12:00",
    "interval": 900,
    "temperature": 22.8,
    "windspeed": 8.5,
    "winddirection": 190,
    "is_day": 1,
    "weathercode": 3
  },
  "weather_error": null
}
```

## APIs Externas

- BrasilAPI: consulta de CEP.
- Open-Meteo: clima atual por coordenadas.

## Documentação Automática

Com a aplicação rodando:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc
