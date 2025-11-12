import jwt, os
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jwt import PyJWTError
from passlib.hash import bcrypt

JWT_SECRET = os.getenv("JWT_SECRET", "segredo123")
auth_scheme = HTTPBearer()

def criar_senha_hash(senha: str):
    """Cria hash seguro da senha (garantindo limite de 72 bytes)"""
    if not senha:
        raise ValueError("Senha não pode ser vazia")
    senha = str(senha).strip()[:72]  # 🔥 força string e limita
    print(f"🔍 [DEBUG] Criando hash da senha: '{senha}' (len={len(senha)})")
    return bcrypt.hash(senha)

def verificar_senha(senha: str, senha_hash: str):
    """Verifica se a senha fornecida é igual ao hash armazenado"""
    if not senha:
        return False
    senha = str(senha).strip()[:72]
    try:
        return bcrypt.verify(senha, senha_hash)
    except Exception:
        return False

def criar_token(dados: dict):
    """Cria token JWT válido por 8 horas"""
    dados_copy = dados.copy()
    dados_copy.update({"exp": datetime.utcnow() + timedelta(hours=8)})
    return jwt.encode(dados_copy, JWT_SECRET, algorithm="HS256")

def obter_usuario_token(credentials = Depends(auth_scheme)):
    """Decodifica e valida o token JWT"""
    token = credentials.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except PyJWTError:
        raise HTTPException(status_code=403, detail="Token inválido ou expirado")
