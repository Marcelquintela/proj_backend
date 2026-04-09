"""Serviços relacionados a análise de intenção."""


def classify_intent(text: str) -> str:
    """
    Classifica a intenção principal a partir do texto informado.

    Args:
        text (str): Texto recebido para análise.

    Returns:
        str: Intenção identificada.
    """
    normalized_text = text.lower().strip()

    if any(word in normalized_text for word in ["compra", "comprar"]):
        return "compra"

    return "outro"
