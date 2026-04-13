"""
Schema de input e output dos agentes.
"""

from typing import Any

from pydantic import BaseModel


class AgentInput(BaseModel):
    """
    Esquema de input para o agente 'suporte' - simulando um atendimento ao usuário.
    """

    message: str
    # agent_type: str = "suporte"
    user_name: str | None = None
    # context: dict[str, Any] | None = None


class AgentOutput(BaseModel):
    """
    Esquema de output para o agente 'suporte' - simulando um atendimento ao usuário.
    """

    response: str
    # agent_type: str
    intent: str
