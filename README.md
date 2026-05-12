# 🏦 API Bancária Assíncrona - Desafio DIO

Este projeto é um microserviço para gerenciamento de contas e transações bancárias (saques e depósitos), desenvolvido com FastAPI, SQLAlchemy e autenticação JWT.

## 🚀 Como Executar

1. **Instale as dependências:**
   ```bash
   poetry install
   ```

2. **Crie as tabelas no Banco de Dados:**
   ```bash
   poetry run alembic upgrade head
   ```

3. **Inicie o servidor:**
   ```powershell
   $env:PYTHONPATH = "."; poetry run uvicorn src.main:app --reload
   ```

## 🔐 Guia de Login e Autenticação

Para testar os endpoints no Swagger (http://127.0.0.1:8000/docs), siga os passos:

1. **Credenciais de Teste:**
   - **Usuário:** admin@teste.com
   - **Senha:** admin123

2. **Passo a Passo:**
   - No Swagger, acesse o endpoint **POST /auth/login**.
   - Clique em **Try it out**, preencha os dados acima e clique em **Execute**.
   - Copie o código gerado em `access_token`.
   - Clique no botão **Authorize** (ícone de cadeado no topo da página).
   - Cole o token no campo **Value** e clique em **Authorize**.

## 📡 Endpoints Principais

- **POST /auth/login**: Realiza login e gera o token JWT.
- **POST /accounts/**: Cria uma nova conta bancária.
- **GET /accounts/**: Lista contas (Necessário estar Autorizado).
- **POST /transactions/**: Realiza Depósito ou Saque (Necessário estar Autorizado).
- **GET /accounts/{id}/transactions**: Histórico de transações/Extrato.

## 🛠️ Tecnologias
- **FastAPI** (Assíncrono)
- **SQLAlchemy & Alembic** (Banco de Dados)
- **SQLite (Aiosqlite)**
- **JWT** (Segurança)

---
🚀 Desafio de API Bancária finalizado com sucesso!
