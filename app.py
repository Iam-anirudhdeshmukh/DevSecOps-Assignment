from flask import Flask, request, render_template_string, make_response
import sqlite3
import os

app = Flask(__name__)

# Hardcoded secret (vulnerability)
SECRET_KEY = "12345-plain-secret"
app.config['SECRET_KEY'] = SECRET_KEY

# Database setup
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return "Welcome to the Vulnerable Flask App!"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # SQL Injection vulnerability
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()

        if result:
            return "Logged in successfully"
        else:
            return "Login failed"
    return '''
        <form method="post">
            <input name="username" placeholder="Username" />
            <input name="password" placeholder="Password" type="password" />
            <input type="submit" />
        </form>
    '''

@app.route("/xss")
def xss():
    # Reflected XSS vulnerability
    name = request.args.get("name", "")
    return render_template_string(f"<h1>Hello {name}</h1>")

@app.route("/readfile")
def readfile():
    # Arbitrary file read vulnerability
    filename = request.args.get("file", "app.py")
    try:
        with open(filename, "r") as f:
            return f"<pre>{f.read()}</pre>"
    except Exception as e:
        return f"Error: {str(e)}"

@app.after_request
def set_response_headers(response):
    # Missing security headers (vulnerability)
    response.headers['Server'] = 'Python-Flask-TestServer'
    return response

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
