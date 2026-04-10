"""
Criar o serviço de agente para lidar com a lógica de negócios relacionada aos agentes.
"""

async def process_message(message: str) -> str:
    """
    Processa a mensagem recebida e retorna uma resposta.
    
    Args:
        message (str): A mensagem a ser processada.

    Returns:
        str: A resposta gerada para a mensagem.

    """
    message = message.strip().lower()
    preco = ["preço", "valor", "custo", "quanto custa", "qual é o preço"]
    problema = ["problema", "erro", "bug", "falha", "dificuldade"]
    if any(p in message for p in preco):
        return "Vou te ajudar com a precificação."
    elif any(p in message for p in problema):
        return (
            "Lamento ouvir que você está enfrentando um problema."
            "\n Por favor, forneça mais detalhes para que eu possa ajudar."
        )

    response = (
        f"Não consegui entender muito bem o que você quis dizer com '{message}'"
        "\n Poderia fornecer mais detalhes?"
    )
    return response
