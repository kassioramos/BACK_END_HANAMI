from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.api.relatorios import router as relatorios_router
from app.core.logger import configurar_logger
import logging

configurar_logger()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Hanami Backend",
    description="API para upload e análise inicial de dados",
    version="0.1.0"
)

app.include_router(upload_router)
app.include_router(relatorios_router)

@app.get("/")
def home():
    logger.info("Endpoint / acessado")
    return {
        "status": "ok",
        "mensagem": "Hanami Backend rodando"
    }
