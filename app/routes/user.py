"""Rotas relacionadas a usuário."""

from fastapi import APIRouter

from app.models.user import CreateUserResponse, CreateUser
from app.services.user import create_user_service

router = APIRouter()


@router.post("/users", response_model=CreateUserResponse)
def create_user(user: CreateUser) -> CreateUserResponse:
    """
    Cria um usuário.

    Args:
        user (CreateUser): dados do usuário

    Returns:
        CreateUserResponse: confirmação da criação
    """
    return create_user_service(user)
