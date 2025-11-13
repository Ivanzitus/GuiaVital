from fastapi import APIRouter, HTTPException
from ..database import get_connection
from ..auth import criar_senha_hash, verificar_senha, criar_token
from ..schemas import UsuarioCreate, UsuarioLogin, UsuarioOut

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.post("/registrar")
def registrar(usuario: UsuarioCreate):
    try:
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT id FROM Usuario WHERE gmail = %s", (usuario.gmail,))
        if cur.fetchone():
            raise HTTPException(status_code=400, detail="Gmail já cadastrado")

        senha_hash = criar_senha_hash(usuario.senha)
        cur.execute(
            "INSERT INTO Usuario (nome, gmail, senhaHash) VALUES (%s, %s, %s)", 
            (usuario.nome, usuario.gmail, senha_hash)
        )
        conn.commit()
        return {"mensagem": "Usuário registrado com sucesso"}
    except Exception as e:
        print("ERRO AO REGISTRAR:", e)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login", response_model=dict)
def login(dados: UsuarioLogin):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM Usuario WHERE gmail = %s", (dados.gmail,))
    user = cur.fetchone()
    if not user or not verificar_senha(dados.senha, user["senhaHash"]):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = criar_token({"id": user["id"], "tipo": user["tipo"], "nome": user["nome"]})
    return {"token": token, "usuario": {"id": user["id"], "nome": user["nome"], "tipo": user["tipo"]}}
