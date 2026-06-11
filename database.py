"""Database setup for user authentication."""

import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

DATABASE = "users.db"


def get_db():
    """Get a database connection."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn


def init_db():
    """Create the users table if it doesn't exist."""
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()
    print("Database initialized!")


def register_user(username, password):
    """Register a new user with hashed password.

    Args:
        username: The username to register
        password: The plain text password (will be hashed)

    Returns:
        True if successful, False if username already exists
    """
    conn = get_db()
    try:
        # generate_password_hash creates a secure hash
        password_hash = generate_password_hash(password)
        conn.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash),
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        # Username already exists (UNIQUE constraint failed)
        return False
    finally:
        conn.close()


def verify_user(username, password):
    """Check if username and password are correct.

    Args:
        username: The username to check
        password: The plain text password to verify

    Returns:
        True if credentials are valid, False otherwise
    """
    conn = get_db()
    user = conn.execute(
        "SELECT password_hash FROM users WHERE username = ?", (username,)
    ).fetchone()
    conn.close()

    if user is None:
        return False

    # check_password_hash compares the entered password with stored hash
    return check_password_hash(user["password_hash"], password)


def get_all_users():
    """Get list of all usernames (for admin purposes)."""
    conn = get_db()
    users = conn.execute("SELECT username, created_at FROM users").fetchall()
    conn.close()
    return [(row["username"], row["created_at"]) for row in users]
