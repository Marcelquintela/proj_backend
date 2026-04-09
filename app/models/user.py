"""
Modelos de dados para usuário.
"""

from pydantic import BaseModel


class User(BaseModel):
    """
    Representa um usuário no sistema.
    """
    name: str
    age: int