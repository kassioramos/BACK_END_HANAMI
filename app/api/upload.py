import os
import logging
from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/api", tags=["Upload"])
logger = logging.getLogger(__name__)

UPLOAD_DIR = "app/uploads"
ARQUIVO_CONTROLE = "app/storage/ultimo_arquivo.txt"

@router.post("/upload")
async def upload_arquivo(file: UploadFile = File(...)):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    if not os.path.exists("app/storage"):
        os.makedirs("app/storage")

    caminho_arquivo = os.path.join(UPLOAD_DIR, file.filename)

    with open(caminho_arquivo, "wb") as f:
        conteudo = await file.read()
        f.write(conteudo)

    with open(ARQUIVO_CONTROLE, "w", encoding="utf-8") as f:
        f.write(caminho_arquivo)

    logger.info(f"Upload realizado: {file.filename}")

    return {
        "status": "arquivo salvo com sucesso",
        "nome_arquivo": file.filename,
        "local_salvo": os.path.abspath(caminho_arquivo)
    }
