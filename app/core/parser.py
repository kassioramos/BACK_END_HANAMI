import os
from datetime import datetime


def analisar_arquivo(caminho_arquivo: str) -> dict:
    """
    Analisa o arquivo de forma básica:
    - verifica se existe
    - conta linhas
    - conta colunas (CSV)
    - captura tamanho e data de criação
    """

    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError("Arquivo não encontrado")

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    total_linhas = len(linhas)

    if total_linhas == 0:
        total_colunas = 0
    else:
        total_colunas = len(linhas[0].strip().split(","))

    tamanho_bytes = os.path.getsize(caminho_arquivo)
    criado_em = datetime.fromtimestamp(
        os.path.getctime(caminho_arquivo)
    ).strftime("%d/%m/%Y %H:%M:%S")

    return {
        "total_linhas": total_linhas,
        "total_colunas": total_colunas,
        "tamanho_bytes": tamanho_bytes,
        "criado_em": criado_em
    }