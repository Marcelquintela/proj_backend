"""Serviços relacionados a usuário."""

from app.models.user import CreateUser, CreateUserResponse


def create_user_service(user: CreateUser) -> CreateUserResponse:
    """Cria o payload de resposta para criação de usuário."""
    return CreateUserResponse(
        message=f"Usuário {user.name} criado com sucesso!",
        data=user,
    )
