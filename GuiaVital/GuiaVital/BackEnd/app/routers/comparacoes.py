from fastapi import APIRouter, Depends
from ..database import get_connection
from ..schemas import ComparacaoBase
from ..auth import obter_usuario_token

router = APIRouter(prefix="/comparacoes", tags=["Comparações"])

@router.get("/")
def listar_comparacoes():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT cmp.*, a.nome AS produtoA, b.nome AS produtoB
        FROM Comparacao cmp
        JOIN Produto a ON cmp.fkProdutoA = a.id
        JOIN Produto b ON cmp.fkProdutoB = b.id
    """)
    return cur.fetchall()

@router.post("/")
def criar_comparacao(cmp: ComparacaoBase, usuario = Depends(obter_usuario_token)):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Comparacao (fkProdutoA, fkProdutoB, tipoComparacao, resultado)
        VALUES (%s, %s, %s, %s)
    """, (cmp.fkProdutoA, cmp.fkProdutoB, cmp.tipoComparacao, cmp.resultado))
    conn.commit()
    return {"mensagem": "Comparação registrada"}
