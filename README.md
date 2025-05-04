
# 📝 Taskify - Task Management App

**Taskify** is a simple task management application built using:

- 🚀 **FastAPI** for the backend  
- 🌐 **Flask** for the frontend  
- 🗄️ **SQLite** with **SQLAlchemy** for database storage  
- 📄 HTML (Jinja2 templates) for rendering tasks

---

## 📦 Features

- Add new tasks with a title and description  
- View all tasks  
- Mark tasks as **Completed**  
- Delete tasks  
- Tasks persist using a **SQLite database**

---

## 🛠️ Technologies Used

| Layer       | Technology       |
|-------------|------------------|
| Frontend    | Flask + Jinja2   |
| Backend     | FastAPI          |
| Database    | SQLite (via SQLAlchemy) |
| API Communication | REST via `requests` |

---

## 📁 Project Structure

```
taskify/
│
├── flask_app.py           # Flask frontend
├── fastapi_app.py         # FastAPI backend
├── database.py            # SQLAlchemy DB setup
├── tasks.db               # SQLite database file (auto-generated)
├── templates/
│   └── index.html         # Task list HTML template
└── README.md              # Project documentation
```

---

## ▶️ Getting Started

### 1️⃣ Clone the repo

```bash
git clone https://github.com/yourusername/taskify.git
cd taskify
```

### 2️⃣ Install dependencies

```bash
pip install fastapi uvicorn flask sqlalchemy jinja2
```

### 3️⃣ Run FastAPI backend

```bash
uvicorn fastapi_app:app --reload
```

> Backend will be available at: `http://127.0.0.1:8000`

### 4️⃣ Run Flask frontend

Open a **new terminal** and run:

```bash
python flask_app.py
```

> Frontend available at: `http://127.0.0.1:5000`

---

## 🖼️ Preview

![Taskify Screenshot](https://via.placeholder.com/800x400?text=Taskify+App+Preview)

---

## 🔧 API Endpoints (FastAPI)

| Method | Endpoint         | Description            |
|--------|------------------|------------------------|
| GET    | `/tasks`         | Get all tasks          |
| POST   | `/tasks`         | Add a new task         |
| PUT    | `/tasks/{id}`    | Update task by ID      |
| DELETE | `/tasks/{id}`    | Delete task by ID      |

---

## ✅ Example Task JSON

```json
{
  "title": "Write README",
  "description": "Create documentation for Taskify app",
  "status": "In-progress"
}
```

---

## 🙌 Contributions

Feel free to fork the repo, suggest improvements, or open pull requests!

---

## 📄 License

MIT License – free to use and modify.
