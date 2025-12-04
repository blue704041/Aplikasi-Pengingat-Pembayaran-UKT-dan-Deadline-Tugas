from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

# Helper koneksi database
def db():
    conn = sqlite3.connect("database/db.sqlite3")
    conn.row_factory = sqlite3.Row
    return conn

# ---------------- LOGIN --------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Login dummy
        if username == "admin" and password == "123":
            session["user"] = username
            return redirect("/home")
        return render_template("login.html", error="Username/Password salah")
    return render_template("login.html")

# ---------------- DASHBOARD ----------------
@app.route("/home")
def home():
    if "user" not in session:
        return redirect("/")

    conn = db()
    payments = conn.execute("SELECT * FROM payments").fetchall()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()

    return render_template(
        "home.html",
        username=session["user"],
        payments=payments,
        tasks=tasks
    )

# ---------------- TAMBAH PEMBAYARAN ----------------
@app.route("/add_payment", methods=["POST"])
def add_payment():
    date = request.form["date"]
    title = request.form["title"]

    conn = db()
    conn.execute("INSERT INTO payments (date, title) VALUES (?,?)", (date, title))
    conn.commit()

    return redirect("/home")

# ---------------- TAMBAH TUGAS ----------------
@app.route("/add_task", methods=["POST"])
def add_task():
    date = request.form["date"]
    title = request.form["title"]

    conn = db()
    conn.execute("INSERT INTO tasks (date, title) VALUES (?,?)", (date, title))
    conn.commit()

    return redirect("/home")

# ---------------- DELETE ----------------
@app.route("/delete_payment/<int:id>")
def delete_payment(id):
    conn = db()
    conn.execute("DELETE FROM payments WHERE id=?", (id,))
    conn.commit()
    return redirect("/home")

@app.route("/delete_task/<int:id>")
def delete_task(id):
    conn = db()
    conn.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    return redirect("/home")


if __name__ == "__main__":
    app.run(debug=True)
