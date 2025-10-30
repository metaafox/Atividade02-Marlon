import json
from core.calculos import encontra_melhor_galpao

# Ponto de entrada da aplicação
if __name__ == "__main__":
    print("--- 🚚 Sistema de Roteamento Logístico ---")
    
    # IDs a serem processados
    CLIENTE_ALVO = "cliente_A08"
    
    # Chama a Função 2
    resultado = encontra_melhor_galpao(CLIENTE_ALVO)
    
    if "erro" in resultado:
        print(f"\nERRO: {resultado['erro']}")
    else:
        print(f"\n📍 Cliente Alvo: {CLIENTE_ALVO}")
        print("\n✅ Decisão de Roteamento:")
        print(f"O produto deve ser direcionado para o:")
        print(f"-> **{resultado['nome']}** ({resultado['id']})")
        