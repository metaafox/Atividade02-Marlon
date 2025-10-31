import json
import os

BASE_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def carregar_dados_json(filename: str) -> dict:
    """Função de ajuda para carregar dados dos arquivos JSON."""
    filepath = os.path.join(BASE_DIR, filename)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        raise FileNotFoundError(f"Erro ao carregar {filename}: {e}")