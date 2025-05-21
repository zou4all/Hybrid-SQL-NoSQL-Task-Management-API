# Hybrid SQL + NoSQL Task Management API

This project is a full-stack API using **FastAPI** that integrates both **PostgreSQL** (Relational Database) and **MongoDB** (NoSQL) to manage tasks and their details.

---

## ✨ Features

* Create and list users (PostgreSQL)
* Create tasks linked to users (PostgreSQL)
* Add task details such as comments and history (MongoDB)
* Retrieve task and its NoSQL details together
* Interact with both SQL and NoSQL data visually using **pgAdmin** and **MongoDB Compass**

---

## 📁 Project Structure

```
project_databases/
├── app/
│   ├── api/endpoints/
│   │   ├── users.py
│   │   └── tasks.py
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   ├── crud/
│   │   ├── sql_crud.py
│   │   └── mongo_crud.py
│   ├── models/
│   │   └── sql_models.py
│   └── main.py
└── README.md
```

---

## 🌐 Technologies Used

* FastAPI
* SQLAlchemy + PostgreSQL
* Motor (MongoDB async client)
* Pydantic
* pgAdmin for PostgreSQL GUI
* MongoDB Compass for MongoDB GUI

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <repo_url>
cd project_databases
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. PostgreSQL Setup

* Make sure PostgreSQL is running on `localhost:5432`
* Create a database named `hybrid_db`
* Update the URL in `app/core/config.py`:

```python
DATABASE_URL = "postgresql+psycopg2://postgres:<password>@localhost:5432/hybrid_db"
```

### 5. MongoDB Setup

* Option 1: Install MongoDB locally

  * Use the installer from [mongodb.com](https://www.mongodb.com/try/download/community)
  * Ensure MongoDB service is running



* Update `MONGO_URI` in `app/core/config.py`:

```python
MONGO_URI = "mongodb://localhost:27017"
```

### 6. Create SQL tables (if not done already)

```python
# init_db.py
from app.models.sql_models import Base
from app.core.database import engine
Base.metadata.create_all(bind=engine)
```

```bash
python init_db.py
```

### 7. Run the server

```bash
uvicorn app.main:app --reload
```

Open your browser at:

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔢 Example API Usage

### Create a user

```
POST /users/?username=alice&email=alice@example.com
```

### Create a task

```json
POST /tasks/
{
  "title": "Prepare Meeting",
  "status": "to-do",
  "user_id": 1
}
```

### Add task details

```json
POST /tasks/1/details
{
  "task_id": 1,
  "comments": [
    { "author": "Bob", "text": "Add slides", "timestamp": "2024-05-18T10:00:00" }
  ],
  "history": [
    { "status": "to-do", "timestamp": "2024-05-17T08:00:00" }
  ],
  "attachments": ["http://example.com/file.pdf"]
}
```

### Retrieve a task with details

```
GET /tasks/1
```

Returns combined SQL (task) and MongoDB (details).

---

## 📃 Database Interaction via pgAdmin and MongoDB Compass

### PostgreSQL with pgAdmin

* Connect to your PostgreSQL server on `localhost`
* Explore your `hybrid_db` database
* Query your `users` and `tasks` tables easily via the Query Tool

### MongoDB with Compass

* Open **MongoDB Compass**
* Connect to `mongodb://localhost:27017`
* Select the `hybrid_app` or default database
* Open the `task_details` collection
* View and edit your MongoDB documents visually, including `comments`, `history`, and `attachments`


### 🔀 Example: Unified API to Combine SQL + NoSQL Task Data

Your project exposes an endpoint that merges data from **PostgreSQL (`tasks`)** and **MongoDB (`task_details`)** in one API call:

#### 📥 Route

```http
GET /hybrid/tasks/{task_id}
```

#### 📤 Example Response

```json
{
  "task": {
    "id": 1,
    "title": "Prepare Meeting",
    "status": "to-do"
  },
  "details": {
    "_id": "661a99ef1234567890abcde1",
    "task_id": 1,
    "comments": [
      {
        "author": "sara",
        "text": "Add slide deck",
        "timestamp": "2024-05-18T10:00:00"
      }
    ],
    "history": [
      {
        "status": "to-do",
        "timestamp": "2024-05-17T09:00:00"
      }
    ],
    "attachments": [
      "http://example.com/slides.pdf"
    ]
  }
}
```

> This simulates a hybrid join between a relational and a NoSQL document — powered by FastAPI.

