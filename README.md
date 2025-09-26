# 📝 FastAPI Blog API  

A simple and secure **Blog API** built with **FastAPI**, featuring:  
- 🔐 JWT Authentication (login required for blog actions)  
- ✍️ Create, Read, Update, Delete (CRUD) blogs  
- 👤 User-based authentication with protected routes  
- ⚡ High performance powered by FastAPI  

---

## 🚀 Features  
- User Login with JWT Authentication  
- Only authenticated users can **create, update, or delete** blogs  
- Unauthorized access returns `401 Unauthorized`  
- Clean and modular project structure  
- For database I have using postgresql and alchemy

---

## 📂 Project Structure  
```
fastapi-blog/

backend
 │── main.py 
 │── auth_token.py
 │── models.py 
 │── schemas.py
 │── crud.py 
 │── database.py 
 │── requirements.txt

```

## ⚙️ Installation  

```
### 1️ Clone Repository

git clone https://github.com/SHIVA-SINGHx/Fast-Api-Blog
cd backend

### 2 Create Virtual Environment

python -m venv venv
source venv/bin/activate   # On Linux/Mac

venv\Scripts\activate      # On Windows

### 3 Install Dependencies

pip install -r requirements.txt

### 4 Run Server

uvicorn main:app --reload

Server will start at 👉 http://127.0.0.1:8000

```
```
📌 ### API Endpoints


POST /login → Login & get JWT token

Blogs (Protected)

GET /blogs/ → Get all blogs

POST /blogs/ → Create new blog

PUT /blogs/{id} → Update blog

DELETE /blogs/{id} → Delete blog
```
```
🛠 Tech Stack

FastAPI – Web framework

JWT – Authentication

PostgreSQL – Database

SQLAlchemy – ORM

Pydantic – Data validation
