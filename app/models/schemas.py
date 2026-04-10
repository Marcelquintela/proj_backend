"""
Schema de input e output dos agentes.
"""

from pydantic import BaseModel

class AgentInput(BaseModel):
    """
    Esquema de input para os agentes.
    """
    message: str

class AgentOutput(BaseModel):
    """
    Esquema de output para os agentes.
    """
    response: str

