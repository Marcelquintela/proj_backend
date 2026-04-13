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
    intent = ["compra", "comprar"]

    if any(word in normalized_text for word in intent):
        return "compra"

    return "outro"
