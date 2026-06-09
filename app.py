"""CipherForge Flask Web Application.

Provides a web interface for the 5-phase encryption algorithm.
"""

from flask import Flask, render_template, request
from engine import encrypt, decrypt

app = Flask(__name__)


@app.route("/")
def index():
    """Display the homepage."""
    return render_template("index.html")


@app.route("/workshop", methods=["GET", "POST"])
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
