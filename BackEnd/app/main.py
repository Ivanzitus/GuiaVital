from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import usuarios, categorias, produtos, comparacoes

app = FastAPI(title="API Saúde DB")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Rotas
app.include_router(usuarios.router)
app.include_router(categorias.router)
app.include_router(produtos.router)
app.include_router(comparacoes.router)

@app.get("/")
def raiz():
    return {"mensagem": "API Saúde DB rodando!"}
