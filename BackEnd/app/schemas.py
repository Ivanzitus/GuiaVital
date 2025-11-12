from pydantic import BaseModel
from typing import Optional

# Usuário
class UsuarioBase(BaseModel):
    nome: str
    gmail: str

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioLogin(BaseModel):
    gmail: str
    senha: str

class UsuarioOut(UsuarioBase):
    id: int
    tipo: int
    class Config:
        orm_mode = True

# Categoria
class CategoriaBase(BaseModel):
    nome: str

class CategoriaOut(CategoriaBase):
    id: int

# Produto
class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str]
    tipo: str
    fkCategoria: Optional[int]

class ProdutoOut(ProdutoBase):
    id: int
    categoria: Optional[str]

# Comparação
class ComparacaoBase(BaseModel):
    fkProdutoA: int
    fkProdutoB: int
    tipoComparacao: Optional[str]
    resultado: Optional[str]
