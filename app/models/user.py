"""Modelos de dados para usuário."""

from pydantic import BaseModel


class CreateUser(BaseModel):
    """Representa um usuário no sistema."""

    name: str
    age: int


class CreateUserResponse(BaseModel):
    """Representa a resposta de criação de usuário."""

    message: str
    data: CreateUser
