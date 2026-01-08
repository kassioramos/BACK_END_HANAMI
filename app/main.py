from fastapi import FastAPI

app = FastAPI(
    title="Hanami Backend",
    description="API para upload e análise inicial de dados",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "status": "ok",
        "mensagem": "Hanami Backend rodando"
    }
