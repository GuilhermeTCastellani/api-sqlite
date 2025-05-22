from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./clientes.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100))

Base.metadata.create_all(bind=engine)

app = FastAPI()

class ClienteSchema(BaseModel):
    nome: str
    email: str

@app.get("/clientes")
def listar_clientes():
    db = SessionLocal()
    clientes = db.query(Cliente).all()
    db.close()
    return clientes

@app.get("/clientes/{id}")
def buscar_cliente(id: int):
    db = SessionLocal()
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    db.close()
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@app.post("/clientes", status_code=201)
def criar_cliente(cliente: ClienteSchema):
    db = SessionLocal()
    novo = Cliente(nome=cliente.nome, email=cliente.email)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    db.close()
    return novo

@app.put("/clientes/{id}")
def atualizar_cliente(id: int, dados: ClienteSchema):
    db = SessionLocal()
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if cliente is None:
        db.close()
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    cliente.nome = dados.nome
    cliente.email = dados.email
    db.commit()
    db.refresh(cliente)
    db.close()
    return cliente

@app.delete("/clientes/{id}")
def deletar_cliente(id: int):
    db = SessionLocal()
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if cliente is None:
        db.close()
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    db.delete(cliente)
    db.commit()
    db.close()
    return {"mensagem": "Cliente excluído com sucesso"}
