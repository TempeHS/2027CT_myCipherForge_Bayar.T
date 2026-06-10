"""CipherForge Flask Web Application.

Provides a web interface for the 5-phase encryption algorithm.
"""

from flask import Flask, render_template, request
from engine import encrypt, decrypt

app = Flask(__name__)
import os
from functools import wraps
from flask import session, redirect, url_for

app.secret_key = os.urandom(24)  # Required for sessions

# Store users (in real apps, use a database with hashed passwords!)
# SECURITY NOTE: Never store plain text passwords in production.
# Use werkzeug.security.generate_password_hash() to hash passwords.
USERS = {"admin": "supersecret", "student": "password123"}


def login_required(f):
    """Decorator that ensures user is logged in."""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated_function


@app.route("/")
def index():
    """Display the homepage."""
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Handle login form."""
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username in USERS and USERS[username] == password:
            session["logged_in"] = True
            session["username"] = username
            return redirect(url_for("workshop"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


@app.route("/logout")
def logout():
    """Log out the current user."""
    session.clear()
    return redirect(url_for("index"))


@app.route("/workshop", methods=["GET", "POST"])
@login_required  # ← NEW: must be AFTER @app.route, BEFORE def
def workshop():
    """Handle encryption and decryption requests."""
    result = ""
    original = ""

    if request.method == "POST":
        # Get form data
        original = request.form.get("message", "")
        action = request.form.get("action", "encrypt")

        # Build the key from form inputs
        key = {
            "shift": int(request.form.get("shift", 5)),
            "block_size": int(request.form.get("block_size", 4)),
            "password": request.form.get("password", "SECRET"),
            "noise_interval": int(request.form.get("noise_interval", 3)),
            "noise_char": request.form.get("noise_char", "~"),
        }

        # Perform the operation
        if action == "encrypt":
            result = encrypt(original, key)
        else:
            result = decrypt(original, key)

    return render_template("workshop.html", result=result, original=original)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
