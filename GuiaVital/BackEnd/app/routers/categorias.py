from fastapi import APIRouter, Depends
from ..database import get_connection
from ..schemas import CategoriaBase
from ..auth import obter_usuario_token

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.get("/")
def listar_categorias():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM Categoria ORDER BY nome")
    return cur.fetchall()

@router.post("/")
def criar_categoria(cat: CategoriaBase, usuario = Depends(obter_usuario_token)):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Categoria (nome) VALUES (%s)", (cat.nome,))
    conn.commit()
    return {"mensagem": "Categoria criada"}
