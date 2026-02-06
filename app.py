from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# -------------------- DATABASE --------------------

def get_db():
    return sqlite3.connect("library.db")

def init_db():
    conn = get_db()
    cur = conn.cursor()

    # BOOKS TABLE (quantity >= 0 enforced)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        quantity INTEGER CHECK(quantity >= 0)
    )
    """)

    # STUDENTS TABLE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

# -------------------- ROUTES --------------------

# HOME
@app.route('/')
def index():
    return render_template('index.html')

# -------------------- BOOKS --------------------

# ADD BOOK
@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']

    try:
        quantity = int(request.form['quantity'])
    except:
        quantity = 0

    if quantity < 0:
        quantity = 0

    conn = get_db()
    conn.execute(
        "INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)",
        (title, author, quantity)
    )
    conn.commit()
    conn.close()
    return redirect('/books')

# VIEW BOOKS
@app.route('/books')
def books():
    conn = get_db()
    data = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return render_template('books.html', books=data)

# DELETE BOOK
@app.route('/delete_book/<int:id>')
def delete_book(id):
    conn = get_db()
    conn.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/books')

# EDIT BOOK PAGE
@app.route('/edit_book/<int:id>')
def edit_book(id):
    conn = get_db()
    book = conn.execute(
        "SELECT * FROM books WHERE id=?", (id,)
    ).fetchone()
    conn.close()
    return render_template('edit_book.html', book=book)

# UPDATE BOOK
@app.route('/update_book/<int:id>', methods=['POST'])
def update_book(id):
    title = request.form['title']
    author = request.form['author']

    try:
        quantity = int(request.form['quantity'])
    except:
        quantity = 0

    if quantity < 0:
        quantity = 0

    conn = get_db()
    conn.execute("""
        UPDATE books
        SET title=?, author=?, quantity=?
        WHERE id=?
    """, (title, author, quantity, id))
    conn.commit()
    conn.close()
    return redirect('/books')

# -------------------- STUDENTS --------------------

# ADD STUDENT
@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    department = request.form['department']

    conn = get_db()
    conn.execute(
        "INSERT INTO students (name, department) VALUES (?, ?)",
        (name, department)
    )
    conn.commit()
    conn.close()
    return redirect('/students')

# VIEW STUDENTS
@app.route('/students')
def students():
    conn = get_db()
    data = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template('students.html', students=data)

# -------------------- RUN --------------------

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
