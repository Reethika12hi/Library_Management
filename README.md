# 📚 Library Management System

A simple **Library Management System** built using **Python (Flask)** and **SQLite**, designed to perform basic **CRUD operations** for managing books and students.  
This project is suitable for **freshers**, **internships**, and **academic mini-projects**.

---

## 🚀 Features

### 📖 Book Management
- Add new books
- View all books
- Update book details
- Delete books
- Quantity validation (cannot be negative)

### 👩‍🎓 Student Management
- Add students
- View student list

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS  
- **Database:** SQLite  
- **Tools:** Git, GitHub, VS Code  

---

## 📂 Project Structure

Library_Management/
│
├── app.py
├── library.db
├── static/
│ └── style.css
├── templates/
│ ├── index.html
│ ├── books.html
│ ├── students.html
│ └── edit_book.html
└── README.md

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Reethika12hi/Library_Management.git
Navigate to the project folder
cd Library_Management

install Flask
pip install flask
Run the application
python app.py
Open in browser
http://127.0.0.1:500
Database

Uses SQLite

Database file: library.db

Tables:

books (id, title, author, quantity)

students (id, name, department)

🎯 Learning Outcomes

Flask routing and templates

CRUD operations

SQLite database integration

Form handling

Git & GitHub workflow
