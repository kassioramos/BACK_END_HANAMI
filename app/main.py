from fastapi import FastAPI

from app.api.products import router as products_router
from app.api.sales import router as sales_router

app = FastAPI(
    title="Kanban Backend",
    version="1.0.0",
    description="Backend do projeto Kanban – Sprint 1"
)

# Registro dos endpoints
app.include_router(products_router)
app.include_router(sales_router)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "API Kanban Backend rodando corretamente"
    }
