📋 ToDo App
A simple and intuitive ToDo list web application built with HTML, CSS, Python (Flask), and a SQLite database. This app helps users manage their tasks efficiently.

🚀 Features
✅ Add new tasks

🗑️ Delete completed tasks

📝 Update task status (completed/incomplete)

🗂️ Persistent storage using SQLite

🖥️ User-friendly web interface

🛠️ Tech Stack
Frontend: HTML, CSS

Backend: Python with Flask

Database: SQLite (via SQLAlchemy)

🧑‍💻 How to Run Locally
Clone the repository

bash
Copy
Edit
git clone https://github.com/Bhavaniputti/todo_app.git
cd todo_app
Create virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
python app.py
Open in browser
Navigate to http://localhost:5000

📁 Folder Structure
csharp
Copy
Edit
todo_app/
│
├── app.py                # Main Flask app
├── templates/
│   └── index.html        # HTML for UI
├── static/               # CSS/JS (if added)
├── __pycache__/          # Python cache
├── Todo.db               # SQLite database file
└── README.md             # Project documentation
