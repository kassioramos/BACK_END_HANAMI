from fastapi import FastAPI

from app.api.upload import router as upload_router
from app.api.products import router as products_router
from app.api.sales import router as sales_router
from app.api.metrics import router as metrics_router

app = FastAPI(
    title="Kanban Backend",
    version="1.0.0",
    description="Backend do projeto Kanban – Sprint 1"
)

# Home / Health Check
@app.get("/", tags=["default"])
def home():
    return {
        "status": "ok",
        "message": "API Kanban Backend rodando corretamente"
    }

# Routers
app.include_router(upload_router, tags=["Upload"])
app.include_router(products_router, tags=["Produtos"])
app.include_router(sales_router, tags=["Vendas"])
app.include_router(metrics_router, tags=["Métricas Financeiras"])
