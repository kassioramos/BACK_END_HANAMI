import os
from fastapi import APIRouter, HTTPException
from app.core.parser import analisar_arquivo

router = APIRouter()

ARQUIVO_CONTROLE = "app/storage/ultimo_arquivo.txt"

@router.get("/relatorios/arquivo-atual")
def relatorio_arquivo_atual():
    if not os.path.exists(ARQUIVO_CONTROLE):
        raise HTTPException(
            status_code=400,
            detail="Nenhum upload realizado ainda"
        )

    with open(ARQUIVO_CONTROLE, "r", encoding="utf-8") as f:
        caminho_arquivo = f.read().strip()

    dados = analisar_arquivo(caminho_arquivo)

    return {
        "nome_arquivo": os.path.basename(caminho_arquivo),
        "local_salvo": os.path.abspath(caminho_arquivo),
        **dados
    }
