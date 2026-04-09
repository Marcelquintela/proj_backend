"""
Arquivo principal da aplicação FastAPI.
Responsável por inicializar a API e registrar rotas.
"""

from fastapi import FastAPI
from app.routes.user import router as user_router
from app.routes.analyze import router as analyze_router

app = FastAPI()

app.include_router(user_router, prefix="/api/v1")
app.include_router(analyze_router, prefix="/api/v1")

@app.get("/")
def read_root():
    """
    Endpoint inicial para teste da API.

    Returns:
        dict: mensagem simples de validação
    """
    return {"message": "API funcionando!"}
