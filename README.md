# Proj_Autocapacita

Autocapacitação em desenvolvimento backend em Python e .NET para criação de APIs e agentes de inteligência artificial.

Atividade 1: API simples em FastAPI para cadastro de usuários e análise de intenção de texto.

## Estrutura

- `app/main.py`: inicialização da aplicação
- `app/routes/`: rotas HTTP
- `app/models/`: modelos de entrada e saída
- `app/services/`: regras de negócio
- `tests/`: testes automatizados

## Requisitos

- Python 3.10+
- Git

## Dependências

- `requirements.txt`: dependências da aplicação em execução
- `requirements-dev.txt`: ferramentas de desenvolvimento e qualidade

## Como executar localmente

### Git Bash no Windows

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

### Linux ou macOS

```bash
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

## Ferramentas de qualidade

### Black

Formata o código Python automaticamente para manter um padrão visual único no projeto.

Uso:

```bash
black app
```

### isort

Organiza os imports automaticamente, agrupando e ordenando as importações.

Uso:

```bash
isort app
```

### pydocstyle

Valida se módulos, classes e funções seguem um padrão consistente de docstrings.

Uso:

```bash
pydocstyle app
```

### Fluxo recomendado

Antes de subir alterações, rode:

```bash
black app
isort app
pydocstyle app
pytest tests -q
```

## Testes automatizados

Os testes da regra de análise ficam em `tests/test_analyze.py`.

Eles cobrem, no mínimo:

- intenção `compra` quando houver `compra`
- intenção `compra` quando houver `comprar`
- intenção `outro` para textos sem intenção de compra

Para executar:

```bash
pytest tests -q
```

## Endpoints

- `GET /`: valida se a API está no ar
- `POST /api/v1/users`: cria um usuário
- `POST /api/v1/analyze`: classifica a intenção de um texto

## Exemplos de uso

### GET /

Resposta:

```json
{
  "message": "API funcionando!"
}
```

### POST /api/v1/users

Request:

```json
{
  "name": "Maria",
  "age": 28
}
```

Response:

```json
{
  "message": "Usuário Maria criado com sucesso!",
  "data": {
    "name": "Maria",
    "age": 28
  }
}
```

### POST /api/v1/analyze

Request:

```json
{
  "text": "quero fazer uma compra hoje"
}
```

Response:

```json
{
  "intent": "compra"
}
```

## Documentação automática

Com a API rodando, acesse:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`
