from pydantic import BaseModel
from typing import Optional

# Usuário
class UsuarioCreate(BaseModel):
    nome: str
    gmail: str
    senha: str
    tipo: Optional[int] = 0  # 0 = comum, 1 = admin/profissional

class UsuarioLogin(BaseModel):
    gmail: str
    senha: str

class UsuarioOut(BaseModel):
    id: int
    nome: str
    gmail: str
    tipo: int

# Produto
class ProdutoCreate(BaseModel):
    nome: str
    descricao: Optional[str]
    tipo: str  # 'natural' ou 'industrial'
    fkCategoria: int
