import os
from fastapi import APIRouter, UploadFile, File

router = APIRouter()

UPLOAD_DIR = "app/uploads"

@router.post("/upload")
async def upload_arquivo(file: UploadFile = File(...)):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

    caminho_arquivo = os.path.join(UPLOAD_DIR, file.filename)

    with open(caminho_arquivo, "wb") as f:
        conteudo = await file.read()
        f.write(conteudo)

    return {
        "status": "arquivo salvo com sucesso",
        "nome_arquivo": file.filename,
        "local_salvo": os.path.abspath(caminho_arquivo)
    }
