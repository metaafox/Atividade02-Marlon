import math
import json
import os

# --- FUNÇÃO 1: CÁLCULO MATEMÁTICO ---
def calcula_distancia(ponto_a: list, ponto_b: list) -> float:
    distancia_quadrada = (ponto_a[0] - ponto_b[0])**2 + \
                         (ponto_a[1] - ponto_b[1])**2
    return math.sqrt(distancia_quadrada)

# --- FUNÇÃO 2: LÓGICA DE NEGÓCIO ---
def encontra_melhor_galpao(cliente_id: str) -> dict:
    base_dir = os.path.dirname(os.path.dirname(__file__))
    
    try:
        with open(os.path.join(base_dir, 'data', 'clientes.json'), 'r') as f:
            clientes_db = json.load(f)
        with open(os.path.join(base_dir, 'data', 'galpoes.json'), 'r') as f:
            galpoes_db = json.load(f)
    except FileNotFoundError:
        return {"erro": "Arquivos de dados não encontrados."}
        
    # 2. Obter coordenadas do cliente
    if cliente_id not in clientes_db:
        return {"erro": f"Cliente '{cliente_id}' não encontrado."}

    coords_cliente = clientes_db[cliente_id]['coordenadas']
    
    # 3. Iterar sobre galpões e encontrar o mais próximo
    melhor_distancia = float('inf')
    galpao_selecionado = None
    
    for id_galpao, dados_galpao in galpoes_db.items():
        coords_galpao = dados_galpao['coordenadas']
        
        # Chama a Função 1
        distancia = calcula_distancia(coords_cliente, coords_galpao)
        
        if distancia < melhor_distancia:
            melhor_distancia = distancia
            galpao_selecionado = {
                "id": id_galpao,
                "nome": dados_galpao['nome'],
                "distancia": round(melhor_distancia, 2)
            }

    return galpao_selecionado