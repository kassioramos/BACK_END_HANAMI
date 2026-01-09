# 📦 Kanban Backend — Sprint 1

Backend desenvolvido em **Python com FastAPI**, estruturado de forma incremental e orientado a boas práticas de organização, versionamento e design de **APIs REST**.

Esta primeira etapa (**Sprint 1**) tem como foco a **fundação do projeto**, criação de endpoints iniciais e estruturação dos módulos base para evolução futura.

---

## 🎯 Objetivo da Sprint 1

Construir a base sólida do backend, garantindo:

- Ambiente configurado corretamente
- Estrutura organizada de pastas e módulos
- Upload de arquivos funcional
- Endpoints iniciais de domínio (produtos, vendas e métricas)
- APIs documentadas automaticamente via Swagger

---

## 🧩 Escopo da Sprint 1 (Etapas 1 a 7)

A **Sprint 1** contempla exatamente os seguintes itens, conforme o Kanban do projeto:

### 1️⃣ Setup do Ambiente e Projeto
- Criação do ambiente virtual
- Instalação das dependências
- Inicialização do FastAPI

### 2️⃣ Módulo de Leitura e Validação de Dados
- Estrutura base para recebimento de dados
- Validações iniciais de payload

### 3️⃣ Endpoint POST `/upload`
- Recebimento de arquivos CSV
- Salvamento físico no servidor
- Retorno de metadados do arquivo

### 4️⃣ Configuração de Logging
- Estrutura preparada para observabilidade
- Base para logs de execução e erros

### 5️⃣ Módulo de Cálculos (Finanças e Vendas)
- Estrutura inicial para cálculos financeiros
- Preparação para análises futuras

### 6️⃣ Endpoints de Vendas e Produtos
- Cadastro e listagem de produtos
- Registro e listagem de vendas

### 7️⃣ Endpoint de Métricas Financeiras
- Endpoint dedicado a métricas consolidadas
- Base para relatórios financeiros

---

⚠️ **A Sprint 2 ainda não foi iniciada e não faz parte deste escopo.**
## 📁 Estrutura do Projeto

.
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── metrics.py
│   │   ├── products.py
│   │   ├── relatorios.py
│   │   ├── reports.py
│   │   ├── sales.py
│   │   └── upload.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   └── parser.py
│   ├── storage/
│   │   ├── uploads/
│   │   │   └── vendas_ficticias_10000_linhas (1).csv
│   │   ├── app.log
│   │   └── ultimo_arquivo.txt
│   ├── uploads/
│   ├── __init__.py
│   └── main.py
├── venv/
└── README.md
---

## 🚀 Como Executar o Projeto

### 1️⃣ Criar e ativar o ambiente virtual

python -m venv venv
venv\Scripts\activate

### 2️⃣ Instalar as dependências

pip install fastapi uvicorn

### 3️⃣ Executar a aplicação

uvicorn app.main:app --reload

---

## 🌐 Acessos

API:
http://127.0.0.1:8000

Documentação Swagger:
http://127.0.0.1:8000/docs

---

## 🔌 Endpoints Disponíveis (Sprint 1)

### 🔹 Home / Health Check
GET /

### 📤 Upload
POST /upload
Responsável por receber e salvar arquivos CSV no servidor.

### 📦 Produtos
GET /products
POST /products
GET /products/{product_id}

### 💰 Vendas
GET /sales
POST /sales

### 📊 Métricas Financeiras
GET /metrics/financeiras

---

## 🛠️ Tecnologias Utilizadas

Python 3.10+
FastAPI
Uvicorn
Git & GitHub

---

## 📌 Observações Importantes

A pasta uploads/ é ignorada pelo Git
O projeto segue evolução incremental por sprints
Commits são feitos de forma pequena e organizada
A Sprint 1 entrega apenas a base funcional, sem análises avançadas

---

## 👤 Autor
Kassio Ramos

Projeto desenvolvido com foco em aprendizado e aplicação prática de:

APIs REST
Organização de backend
Validação estrutural de dados
Boas práticas de versionamento
