# Mail Sender API
API para envio de campanhas de e-mail de forma assíncrona, permitindo que usuários autenticados criem campanhas e as enviem automaticamente para seus contatos cadastrados, utilizando filas para processamento em background.

## 🛠️ Tecnologias utilizadas

* Django
* Django REST Framework 
* djangorestframework-simplejwt
* PostgreSQL
* Celery
* Redis 
* Gmail SMTP 

---

## 🚀 Rodar o projeto em desenvolvimento (com logs no terminal)

### 🔧 Pré-requisitos

* Docker
* Docker Compose
* Make (opcional)

---

### Com Makefile

```bash
make build
make up-dev 
make migrate
make createsuperuser
```

Para parar os containers:

```bash
make down
```

---

### Sem Makefile

```bash
docker compose build
docker compose up 
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Para parar os containers:

```bash
docker compose down
```

---

## 🔐 Configuração de variáveis de ambiente

Crie um arquivo `.env` baseado no `.env.example`:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e preencha as variáveis necessárias.

---

## 📧 Configurando o Gmail para envio de e-mails

⚠️ Não utilize a senha normal da sua conta Gmail.  
É obrigatório usar uma **Senha de App**.


### 1️⃣ Verificação em duas etapas

* [https://myaccount.google.com/security](https://myaccount.google.com/security)
* Ative a **Verificação em duas etapas**


### 2️⃣ Crie uma Senha de App

* [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
* Crie o app
* Copie a senha gerada


### 3️⃣ Configure o `.env`

No arquivo `.env`, preencha:

```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=seu_email@gmail.com
EMAIL_HOST_PASSWORD=sua_senha_de_app
```
---

## 🔗 Endpoints disponíveis
```
POST /api/accounts/register/
POST /api/accounts/login/
POST /api/accounts/token/refresh/

GET /api/accounts/me
PATCH /api/accounts/me

GET /api/contacts/
GET /api/contacts/{id}
POST /api/contacts/
PATCH /api/contacts/{id}
DELETE /api/contacts/{id}

GET /api/campaigns/
GET /api/campaigns/{id}
POST /api/campaigns/
PATCH /api/campaigns/{id}
DELETE /api/campaigns/{id}

POST /api/campaigns/{id}/send/
```
