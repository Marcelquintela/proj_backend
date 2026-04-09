"""Serviços relacionados a análise de intenção."""


def classify_intent(text: str) -> str:
    """Classifica a intenção principal a partir do texto informado."""

    normalized_text = text.lower()

    if "compra" in normalized_text:
        return "compra"

    return "outro"