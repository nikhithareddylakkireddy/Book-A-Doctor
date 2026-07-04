import sqlite3

DB_NAME = "appointment.db"


# ---------------------------------------
# Database Connection
# ---------------------------------------

def get_connection():
    return sqlite3.connect(DB_NAME)


# ---------------------------------------
# Book Appointment
# ---------------------------------------

def book_appointment(
    appointment_id,
    patient,
    age,
    gender,
    phone,
    email,
    symptom,
    department,
    doctor,
    date,
    time
):

    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        INSERT INTO appointments(
            appointment_id,
            patient,
            age,
            gender,
            phone,
            email,
            symptom,
            department,
            doctor,
            date,
            time,
            status
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        appointment_id,
        patient,
        age,
        gender,
        phone,
        email,
        symptom,
        department,
        doctor,
        date,
        time,
        "Pending"
    ))

    conn.commit()
    conn.close()


# ---------------------------------------
# Get All Appointments
# ---------------------------------------

def get_appointments():

    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        SELECT *
        FROM appointments
        ORDER BY id DESC
    """)

    data = c.fetchall()

    conn.close()

    return data


# ---------------------------------------
# Search Appointment By Email
# ---------------------------------------

def search_appointments(email):

    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        SELECT *
        FROM appointments
        WHERE email=?
        ORDER BY id DESC
    """, (email,))

    data = c.fetchall()

    conn.close()

    return data


# ---------------------------------------
# Search Appointment By ID
# ---------------------------------------

def search_appointment_by_id(appointment_id):

    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        SELECT *
        FROM appointments
        WHERE appointment_id=?
    """, (appointment_id,))

    data = c.fetchone()

    conn.close()

    return data


# ---------------------------------------
# Cancel Appointment
# ---------------------------------------

def cancel_appointment(appointment_id):

    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        UPDATE appointments
        SET status='Cancelled'
        WHERE appointment_id=?
    """, (appointment_id,))

    conn.commit()

    conn.close()


# ---------------------------------------
# Complete Appointment
# ---------------------------------------

def complete_appointment(appointment_id):

    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        UPDATE appointments
        SET status='Completed'
        WHERE appointment_id=?
    """, (appointment_id,))

    conn.commit()

    conn.close()


# ---------------------------------------
# Delete Appointment
# ---------------------------------------

def delete_appointment(appointment_id):

    conn = get_connection()
    c = conn.cursor()

    c.execute("""
        DELETE FROM appointments
        WHERE appointment_id=?
    """, (appointment_id,))

    conn.commit()

    conn.close()


# ---------------------------------------
# Dashboard Statistics
# ---------------------------------------

def get_statistics():

    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM appointments")
    total = c.fetchone()[0]

    c.execute("""
        SELECT COUNT(*)
        FROM appointments
        WHERE status='Pending'
    """)
    pending = c.fetchone()[0]

    c.execute("""
        SELECT COUNT(*)
        FROM appointments
        WHERE status='Completed'
    """)
    completed = c.fetchone()[0]

    c.execute("""
        SELECT COUNT(*)
        FROM appointments
        WHERE status='Cancelled'
    """)
    cancelled = c.fetchone()[0]

    conn.close()

    return {
        "total": total,
        "pending": pending,
        "completed": completed,
        "cancelled": cancelled
    }