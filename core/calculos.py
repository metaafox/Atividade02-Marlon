import math
# Não é necessário 'json' ou 'os' aqui, pois os dados já chegam processados.

# --- FUNÇÃO PRINCIPAL DE CÁLCULO (WORKER PURO) ---
def lambda_calcular_distancia(dados: dict) -> list:
    """
    Recebe a lista de pontos e calcula a distância Euclidiana para cada par.
    Simula a Lambda de Cálculo.
    """
    resultados = []
    
    # Função auxiliar de cálculo matemático
    def calcula_distancia(p1: list, p2: list) -> float:
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    for ponto in dados.get('pontos', []):
        distancia = calcula_distancia(ponto['cliente_coord'], ponto['galpao_coord'])
        
        resultados.append({
            "id": ponto['galpao_id'],
            "nome": ponto['galpao_nome'],
            "distancia": round(distancia, 2)
        })

    return resultados


# --- FUNÇÃO DE DECISÃO FINAL (WORKER DECISOR) ---
def lambda_selecionar_vencedor(resultados_calculo: list) -> dict:
    """
    Recebe a lista de distâncias e seleciona o galpão com a menor distância.
    Simula a Lambda Decisora.
    """
    if not resultados_calculo:
        return {"erro": "Nenhum resultado de cálculo recebido."}
        
    # Encontra o galpão com a menor distância (Otimização: min() com chave lambda)
    melhor_galpao = min(resultados_calculo, key=lambda x: x['distancia'])
    
    return melhor_galpao