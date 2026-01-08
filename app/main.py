from fastapi import FastAPI
from app.api.upload import router as upload_router

app = FastAPI(
    title="Hanami Backend",
    description="API para upload e análise inicial de dados",
    version="0.1.0"
)

app.include_router(upload_router)

@app.get("/")
def home():
    return {
        "status": "ok",
        "mensagem": "Hanami Backend rodando"
    }
