from fastapi import APIRouter

router = APIRouter(prefix="/reports", tags=["Relatórios"])

@router.get("/sales-summary")
def sales_summary():
    return {
        "status": "ok",
        "mensagem": "Relatório de vendas - em construção"
    }

@router.get("/regional-performance")
def regional_performance():
    return {
        "status": "ok",
        "mensagem": "Relatório regional - em construção"
    }

@router.get("/product-analysis")
def product_analysis():
    return {
        "status": "ok",
        "mensagem": "Relatório de produtos - em construção"
    }

@router.get("/customer-profile")
def customer_profile():
    return {
        "status": "ok",
        "mensagem": "Relatório de clientes - em construção"
    }

@router.get("/financial-metrics")
def financial_metrics():
    return {
        "status": "ok",
        "mensagem": "Métricas financeiras - em construção"
    }
