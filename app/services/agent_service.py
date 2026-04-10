"""
Criar o serviço de agente para lidar com a lógica de negócios relacionada aos agentes.
"""


def process_message(message: str, user_name: str | None = None) -> tuple[str, str]:
    """
    Processa a mensagem recebida e retorna uma resposta e a intenção.
    
    Args:
        message (str): A mensagem a ser processada.
        user_name (str | None): Nome opcional para personalizar a resposta.

    Returns:
        tuple[str, str]: Resposta gerada e intenção identificada.

    """
    message = message.strip().lower()
    greeting = f"{user_name}, " if user_name else ""

    preco = ["preço", "valor", "custo", "quanto custa", "qual é o preço"]
    problema = ["problema", "erro", "bug", "falha", "dificuldade"]

    if any(p in message for p in preco):
        return f"{greeting}vou te ajudar com a precificação.", "precificacao"

    if any(p in message for p in problema):
        response = (
            f"{greeting}lamento ouvir que você está enfrentando um problema."
            "\nPor favor, forneça mais detalhes para que eu possa ajudar."
        )
        return response, "suporte_tecnico"

    response = (
        f"{greeting}não consegui entender muito bem o que você quis dizer com "
        f"'{message}'.\nPoderia fornecer mais detalhes?"
    )
    return response, "geral"
