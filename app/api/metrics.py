from fastapi import APIRouter
from typing import List, Dict

router = APIRouter(
    prefix="/metrics",
    tags=["Métricas Financeiras"]
)

@router.get("/financeiras")
def metricas_financeiras():
    """
    Endpoint responsável por retornar métricas financeiras básicas.
    (Sprint 1 – versão inicial)
    """

    return {
        "faturamento_total": 150000.75,
        "ticket_medio": 250.50,
        "total_vendas": 599,
        "produto_mais_vendido": "Produto A",
        "periodo": "dados simulados (Sprint 1)"
    }
