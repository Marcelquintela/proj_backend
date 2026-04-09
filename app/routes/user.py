"""
Rotas relacionadas a usuário.
"""

from fastapi import APIRouter
from app.models.user import User

router = APIRouter()


@router.post("/users")
def create_user(user: User):
    """
    Cria um usuário.

    Args:
        user (User): dados do usuário

    Returns:
        dict: confirmação
    """
    return {
        "message": f"Usuário {user.name} criado com sucesso!",
        "data": user
    }