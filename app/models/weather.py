"""Contratos de entrada e saída do agente de clima."""

from typing import TypeAlias

from pydantic import BaseModel


class WeatherInput(BaseModel):
    """Entrada do agente de clima baseada em coordenadas."""

    latitude: float
    longitude: float


class WeatherOutput(BaseModel):
    """Saída de sucesso do agente de clima."""

    time: str | None = None
    interval: int | None = None
    temperature: float | None = None
    windspeed: float | None = None
    winddirection: int | None = None
    is_day: int | None = None
    weathercode: int | None = None


class WeatherErrorOutput(BaseModel):
    """Saída de erro do agente de clima."""

    message: str


WeatherResponse: TypeAlias = WeatherOutput | WeatherErrorOutput
