# Proj_Autocapacita

Autocapacitação em desenvolvimento backend em python e >net para desenvolvimento de agentes de inteligencia artificial.

Atividade 1: API simples em FastAPI para cadastro de usuários e análise de intenção de texto.

## Estrutura

- `app/main.py`: inicialização da aplicação
- `app/routes/`: rotas HTTP
- `app/models/`: modelos de entrada e saída
- `app/services/`: regras de negócio

## Requisitos

- Python 3.10+
- Git

## Como executar

### Bash

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Se estiver usando Git Bash no Windows, o comando de ativação acima funciona. Em Linux ou macOS, use:

```bash
source venv/bin/activate
```

## Endpoints

- `GET /`: valida se a API está no ar
- `POST /api/v1/users`: cria um usuário
- `POST /api/v1/analyze`: classifica a intenção de um texto

## Exemplo de request

### Análise de intenção

```json
{
  "text": "quero fazer uma compra hoje"
}
```

### Resposta

```json
{
  "intent": "compra"
}
```

## Documentação automática

Com a API rodando, acesse:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

