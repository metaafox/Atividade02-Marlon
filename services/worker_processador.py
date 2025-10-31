from core.calculos import lambda_calcular_distancia, lambda_selecionar_vencedor
from core.utilidades import carregar_dados_json

# A Lambda aqui simula o Processamento Pesado.

def processar_item_logistica(dados_trabalho: dict):
    """
    Executa a lógica de roteamento (cálculo e decisão) para o item recebido da fila.
    """
    cliente_id = dados_trabalho.get('cliente_id')
    coord_cliente = dados_trabalho.get('coord_cliente')
    
    # Simula o Step 1 (Buscar e Filtrar) que foi enviado para a fila
    # Carregando dados novamente para simplificar a simulação de um Worker independente
    try:
        galpoes_db = carregar_dados_json('galpoes.json')
    except:
        print(f"   [WORKER] Erro: Não foi possível carregar o DB de galpões.")
        return

    # Preparar dados para o cálculo
    pontos_para_calcular = []
    for galpao_id, dados_galpao in galpoes_db.items():
        if dados_galpao.get('status') == 'Livre':
            pontos_para_calcular.append({
                "cliente_coord": coord_cliente,
                "galpao_id": galpao_id,
                "galpao_nome": dados_galpao['nome'],
                "galpao_coord": dados_galpao['coordenadas']
            })
            
    if not pontos_para_calcular:
        print(f"   [WORKER] Aviso: Nenhum galpão livre encontrado para {cliente_id}.")
        return

    # SIMULAÇÃO STEP 2: CALCULAR DISTÂNCIAS
    resultados_calculo = lambda_calcular_distancia({"pontos": pontos_para_calcular})
    
    # SIMULAÇÃO STEP 3: SELECIONAR VENCEDOR
    resultado_final = lambda_selecionar_vencedor(resultados_calculo)
    
    # Saída do Worker
    print("\n✅ Decisão de Roteamento Assíncrono Concluída:")
    print(f"  -> Cliente: {cliente_id}")
    print(f"  -> Galpão Selecionado: **{resultado_final['nome']}** ({resultado_final['id']})")