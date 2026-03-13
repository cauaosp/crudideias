# 💡 Lista de Ideias

Um **CRUD de ideias** desenvolvido com **Flask + PostgreSQL + Docker**.

---

## 🤖 Tecnologias utilizadas

* Flask
* SQLAlchemy
* PostgreSQL
* Docker

---

## 📦 Como rodar o projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/crudideias.git
cd crudideias
```

### 2️⃣ Configure as variáveis de ambiente

Crie seu arquivo `.env` a partir do exemplo:

```bash
cp .env.example .env
```

Se quiser, altere os valores conforme necessário.

### 3️⃣ Inicie os containers

```bash
docker compose up --build
```

Criará e inicializará os 2 contêineres:

* 🐘 PostgreSQL (banco de dados)
* 🌐 Aplicação Flask

### 4️⃣ Acesse a aplicação

Abra no navegador:

```
http://localhost:4949
```
---

## 🛠 Funcionalidades

* ➕ Adicionar ideia
* 📄 Visualizar ideia
* ✏️ Editar ideia
* ❌ Remover ideia

---

## 📂 Estrutura do projeto

```
crudideias
│
├── app.py
├── Dockerfile
├── compose.yml
├── requirements.txt
├── templates/
├── static/
├── .env.example
└── README.md
```
