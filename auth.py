import sqlite3
import bcrypt


DB_NAME = "appointment.db"


def register_user(username, password):

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Check duplicate username
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    existing = c.fetchone()

    if existing:
        conn.close()
        raise Exception("Username already exists!")

    # Encrypt password
    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    c.execute(
        """
        INSERT INTO users(username,password)
        VALUES(?,?)
        """,
        (
            username,
            hashed_password.decode()
        )
    )

    conn.commit()
    conn.close()


def login_user(username, password):

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    user = c.fetchone()

    conn.close()

    if user:

        stored_password = user[2]

        if bcrypt.checkpw(
            password.encode(),
            stored_password.encode()
        ):
            return user

    return None