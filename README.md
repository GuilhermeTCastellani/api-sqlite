# 📦 API de Cadastro de Clientes - FastAPI + PostgreSQL (Docker Compose)

Este projeto é uma API REST simples para cadastro de clientes, desenvolvida com **Python (FastAPI)**, utilizando **PostgreSQL** como banco de dados e **Docker Compose** para orquestração dos containers.

## 🧰 Tecnologias Utilizadas

- 🐍 Python 3.11 + FastAPI
- 🐘 PostgreSQL 14
- 🐳 Docker + Docker Compose
- 🧪 HTTPie (para testes de API)
- 🛠️ Adminer (cliente web para o banco de dados)

## 🚀 Como Executar o Projeto

### 1. Clone o repositório

git clone https://github.com/GuilhermeTCastellani/api-sqlite.git

Suba os containers com o comando:
  docker compose up --build

Certifique-se de que o Docker e o Docker Compose estão instalados corretamente na sua máquina ou VM.

# E para facilitar os comandos instale o HTTPIE
pip install httpie 

# Criar cliente
http POST http://localhost:8000/clientes nome="Carlos" email="carlos@example.com"

# Listar todos os clientes
http GET http://localhost:8000/clientes

# Buscar cliente por ID
http GET http://localhost:8000/clientes/1

# Atualizar cliente
http PUT http://localhost:8000/clientes/1 nome="Carlos Silva" email="carlos.silva@example.com"

# Deletar cliente
http DELETE http://localhost:8000/clientes/1




# Integrantes do grupo:
Alessandro da Rosa, Arthur B. Spada, Guilherme T. Castellai, Isadora Aguirre, Maria Eduarda B. Schulze, Mariana Melara

