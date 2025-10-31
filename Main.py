from core.utilidades import carregar_dados_json
from services.queue_service import enviar_para_fila, processar_proximo_item
from services.worker_processador import processar_item_logistica

def rotear_assincrono(cliente_id: str):
    """
    Simula o fluxo de entrada que envia a solicitação para o processamento assíncrono.
    """
    try:
        clientes_db = carregar_dados_json('clientes.json')
        if cliente_id not in clientes_db:
            print(f"ERRO: Cliente '{cliente_id}' não encontrado.")
            return

        dados_cliente = clientes_db[cliente_id]
        
        # Prepara o "payload" da mensagem que será enviada para a fila
        payload = {
            "cliente_id": cliente_id,
            "coord_cliente": dados_cliente['coordenadas'],
            "timestamp": "simulação_data_hora"
        }
        
        # Envia a solicitação para a fila (Ação Assíncrona)
        enviar_para_fila(payload)
        
        print("\n[MAIN] Solicitação enviada. O processamento ocorrerá em segundo plano (assíncrono).")

    except Exception as e:
        print(f"ERRO durante o enfileiramento: {e}")

if __name__ == "__main__":
    print("--- 🚚 Sistema de Roteamento Logístico (Modelo Assíncrono) ---")
    
    CLIENTES_A_PROCESSAR = ["cliente_A03", "cliente_A08", "cliente_A04"]
    
    # 1. SIMULAÇÃO DA ENTRADA DE REQUISIÇÕES (API Gateway)
    print("\n[FASE 1: ENFILEIRAMENTO]")
    for cliente in CLIENTES_A_PROCESSAR:
        rotear_assincrono(cliente)
    
    # 2. SIMULAÇÃO DO PROCESSAMENTO EM SEGUNDO PLANO (Worker)
    print("\n[FASE 2: PROCESSAMENTO ASSÍNCRONO (CONSUMER)]")
    
    # Loop para processar todos os itens da fila simulada
    while True:
        item = processar_proximo_item()
        if item is None:
            break
        
        processar_item_logistica(item)

    print("\n--- Processamento Assíncrono Completo ---")