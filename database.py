import sqlite3


DB_NAME = "appointment.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():

    conn = get_connection()
    c = conn.cursor()

    # ================= USERS ================= #

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        full_name TEXT,

        email TEXT,

        phone TEXT,

        role TEXT DEFAULT 'Patient',

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    # ================= APPOINTMENTS ================= #

    c.execute("""
    CREATE TABLE IF NOT EXISTS appointments(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        appointment_id TEXT UNIQUE,

        patient TEXT,

        age INTEGER,

        gender TEXT,

        phone TEXT,

        email TEXT,

        symptom TEXT,

        department TEXT,

        doctor TEXT,

        date TEXT,

        time TEXT,

        status TEXT DEFAULT 'Pending',

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()
    conn.close()