from flask import Flask, request, session
import bcrypt

app = Flask(__name__)
app.secret_key = "secret_key_123"

users = {}

@app.route("/")
def home():
    return """
    <h1>Secure Login System</h1>
    <p>Application Running Successfully</p>
    """

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return "Username and Password required"

    if username in users:
        return "User already exists"

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    users[username] = hashed_password

    return "Registration Successful"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username not in users:
        return "User not found"

    if bcrypt.checkpw(
        password.encode("utf-8"),
        users[username]
    ):
        session["user"] = username
        return "Login Successful"

    return "Invalid Password"

@app.route("/logout")
def logout():
    session.pop("user", None)
    return "Logged Out Successfully"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)