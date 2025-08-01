# 📝 ToDo App

A simple and lightweight web-based ToDo list application that helps you keep track of your tasks. Built using **Python (Flask)** and **SQLite**.

---

## 🚀 Features

- ➕ Add new tasks
- ✅ Mark tasks as completed
- 🗑️ Delete tasks
- 📦 Persistent task storage using SQLite
- 🖥️ Clean and minimal web UI

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS (via Flask templates)
- **Backend**: Python, Flask
- **Database**: SQLite (managed with SQLAlchemy)

---

## 📂 Project Structure

notes_app/
│
├── app.py # Main Flask application
├── templates/
│ └── index.html # HTML template for the app
├── static/ # Optional: for CSS or JS
├── Todo.db # SQLite database
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🧑‍💻 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Bhavaniputti/todo_app.git
cd todo_app

pip install -r requirements.txt

python app.py

Go to: http://localhost:5000
