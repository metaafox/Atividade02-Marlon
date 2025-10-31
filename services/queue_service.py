# Simulação de uma Fila de Mensagens (Global)
FILA_DE_PROCESSAMENTO = []

def enviar_para_fila(dados: dict):
    """
    Simula o envio de uma mensagem para a fila (Producer).
    Em um ambiente real, usaria boto3 para AWS SQS ou RabbitMQ.
    """
    print(f"   [FILA] -> Novo trabalho adicionado à fila: {dados['cliente_id']}")
    FILA_DE_PROCESSAMENTO.append(dados)

def processar_proximo_item():
    """
    Simula um Worker (Consumer) lendo e processando o próximo item da fila.
    Em um ambiente real, o Worker estaria escutando a fila 24/7.
    """
    if not FILA_DE_PROCESSAMENTO:
        # print("   [FILA] -> Fila de processamento vazia.")
        return None

    # Simula a leitura FIFO (First In, First Out)
    trabalho = FILA_DE_PROCESSAMENTO.pop(0)
    print(f"   [FILA] <- Processando trabalho: {trabalho['cliente_id']}")
    return trabalho