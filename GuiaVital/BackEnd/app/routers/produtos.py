from fastapi import APIRouter, Depends
from ..database import get_connection
from ..schemas import ProdutoBase
from ..auth import obter_usuario_token

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.get("/")
def listar_produtos():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT p.*, c.nome AS categoria
        FROM Produto p
        LEFT JOIN Categoria c ON c.id = p.fkCategoria
    """)
    return cur.fetchall()

@router.post("/")
def criar_produto(prod: ProdutoBase, usuario = Depends(obter_usuario_token)):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Produto (nome, descricao, tipo, fkCategoria) VALUES (%s, %s, %s, %s)",
        (prod.nome, prod.descricao, prod.tipo, prod.fkCategoria)
    )
    conn.commit()
    return {"mensagem": "Produto criado com sucesso"}
