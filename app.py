import streamlit as st
import random

from database import init_db
from auth import register_user, login_user

from appointment import (
    book_appointment,
    get_appointments,
    search_appointments,
    cancel_appointment
)

from admin import admin_panel

from email_service import send_confirmation_email


# ==========================================
# DATABASE
# ==========================================

init_db()


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="MediSync Hospital",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main{
    background:#f6fbff;
}

h1,h2,h3{
    color:#0d6efd;
}

.stButton>button{
    background:#0d6efd;
    color:white;
    border-radius:10px;
    border:none;
    font-weight:bold;
    padding:10px;
}

.stButton>button:hover{
    background:#084298;
}

.footer{
    text-align:center;
    color:gray;
}

</style>
""",unsafe_allow_html=True)


# ==========================================
# TITLE
# ==========================================

st.title("🏥 MediSync Hospital")

st.caption(
    "Professional Doctor Appointment Booking System"
)


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🏥 MediSync")

st.sidebar.success("🟢 System Online")

menu=[
    "🏠 Home",
    "👤 Register",
    "🔐 Login",
    "📅 Book Appointment",
    "📋 My Appointments",
    "🏥 Departments",
    "🛠 Admin"
]

choice=st.sidebar.radio(
    "Navigation",
    menu
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 👩‍💻 Developer

**Nikhitha**

Artificial Intelligence & Data Science

Version 1.0
""")


# ==========================================
# HOME
# ==========================================

if choice=="🏠 Home":

    st.header("Welcome to MediSync Hospital")

    st.write("""
Book doctor appointments online in just a few clicks.

✅ Experienced Doctors

✅ Online Booking

✅ Email Confirmation

✅ Appointment Cancellation

✅ Secure Patient Records

✅ Professional Admin Dashboard
""")

    st.divider()

    c1,c2,c3,c4=st.columns(4)

    c1.metric("👨‍⚕ Doctors","25+")

    c2.metric("😊 Patients","500+")

    c3.metric("📅 Appointments","1200+")

    c4.metric("🏥 Departments","10+")

    st.divider()

    st.subheader("🏥 Departments")

    a,b,c=st.columns(3)

    with a:

        st.success("❤️ Cardiology")

        st.success("🧠 Neurology")

    with b:

        st.info("🦷 Dentistry")

        st.info("🦴 Orthopedics")

    with c:

        st.warning("🩺 General Medicine")

        st.warning("👶 Pediatrics")

    st.divider()

    st.subheader("Hospital Facilities")

    st.write("✔ 24×7 Emergency")

    st.write("✔ Experienced Doctors")

    st.write("✔ Online Appointment Booking")

    st.write("✔ Email Confirmation")

    st.write("✔ Appointment Cancellation")

    st.write("✔ Secure Database")

    st.divider()

    col1,col2=st.columns(2)

    with col1:

        st.info("📞 Emergency : +91 9876543210")

        st.info("📧 Email : nikhithareddylakkireddy@gmail.com")

    with col2:

        st.info("📍 Tirupati")

        st.info("🕒 Open : 24 Hours")
        # ==========================================
# REGISTER
# ==========================================

elif choice == "👤 Register":

    st.header("👤 Patient Registration")

    col1, col2 = st.columns(2)

    with col1:
        username = st.text_input("👤 Username")

    with col2:
        password = st.text_input(
            "🔒 Password",
            type="password"
        )

    st.markdown("---")

    if st.button("✅ Register"):

        if username.strip() == "" or password.strip() == "":

            st.warning("⚠ Please fill all the fields.")

        else:

            try:

                register_user(
                    username,
                    password
                )

                st.success("🎉 Registration Successful!")

                st.balloons()

            except Exception as e:

                st.error(str(e))


# ==========================================
# LOGIN
# ==========================================

elif choice == "🔐 Login":

    st.header("🔐 Patient Login")

    st.info("Please login using your registered username and password.")

    username = st.text_input("👤 Username")

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    remember = st.checkbox("Remember Me")

    if st.button("🚀 Login"):

        if username.strip() == "" or password.strip() == "":

            st.warning("⚠ Please enter username and password.")

        else:

            user = login_user(
                username,
                password
            )

            if user:

                st.success("✅ Login Successful!")

                st.balloons()

                st.session_state["logged_in"] = True
                st.session_state["username"] = username

            else:

                st.error("❌ Invalid Username or Password")

    st.markdown("---")

    st.info(
        "💡 New User? Please Register First."
    )
    # ==========================================
# BOOK APPOINTMENT
# ==========================================

elif choice == "📅 Book Appointment":

    st.header("📅 Book Doctor Appointment")

    st.info("Fill the details below to book your appointment.")

    col1, col2 = st.columns(2)

    with col1:

        patient = st.text_input("👤 Patient Name")

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            step=1
        )

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female",
                "Other"
            ]
        )

        phone = st.text_input("📱 Phone Number")

        email = st.text_input("📧 Email Address")

    with col2:

        symptom = st.text_area("🤒 Symptoms")

        department = st.selectbox(
            "🏥 Department",
            [
                "General Medicine",
                "Cardiology",
                "Dentistry",
                "Neurology",
                "Orthopedics"
            ]
        )

        doctors = {
            "General Medicine": [
                "Dr. Reddy",
                "Dr. Kumar"
            ],
            "Cardiology": [
                "Dr. Priya"
            ],
            "Dentistry": [
                "Dr. John"
            ],
            "Neurology": [
                "Dr. Smith"
            ],
            "Orthopedics": [
                "Dr. Rajesh"
            ]
        }

        doctor = st.selectbox(
            "👨‍⚕ Select Doctor",
            doctors[department]
        )

        date = st.date_input(
            "📅 Appointment Date"
        )

        time = st.time_input(
            "⏰ Appointment Time"
        )

    st.markdown("---")

    if st.button("✅ Confirm Appointment"):

        # Validation

        if patient.strip() == "":
            st.error("Patient Name is required.")

        elif phone.strip() == "":
            st.error("Phone Number is required.")

        elif len(phone) != 10 or not phone.isdigit():
            st.error("Enter a valid 10-digit phone number.")

        elif email.strip() == "":
            st.error("Email Address is required.")

        elif "@" not in email:
            st.error("Enter a valid email address.")

        elif symptom.strip() == "":
            st.error("Symptoms cannot be empty.")

        else:

            appointment_id = f"APT{random.randint(1000,9999)}"

            try:

                book_appointment(
                    appointment_id,
                    patient,
                    age,
                    gender,
                    phone,
                    email,
                    symptom,
                    department,
                    doctor,
                    str(date),
                    str(time)
                )

                email_sent = send_confirmation_email(
                    email,
                    patient,
                    appointment_id,
                    symptom,
                    department,
                    doctor,
                    str(date),
                    str(time)
                )

                st.success("🎉 Appointment Booked Successfully!")

                st.balloons()

                st.markdown("---")

                st.subheader("📋 Appointment Summary")

                st.success(f"Appointment ID : {appointment_id}")

                st.write(f"👤 Patient : {patient}")
                st.write(f"👨‍⚕ Doctor : {doctor}")
                st.write(f"🏥 Department : {department}")
                st.write(f"📅 Date : {date}")
                st.write(f"⏰ Time : {time}")

                if email_sent:

                    st.success("📧 Confirmation Email Sent Successfully")

                else:

                    st.warning("Appointment booked, but email could not be sent.")

            except Exception as e:

                st.error(str(e))
                # ==================================================
# MY APPOINTMENTS
# ==================================================

elif choice == "📋 My Appointments":

    st.header("📋 My Appointments")

    st.info("Search your appointments using your registered email address.")

    email = st.text_input("📧 Registered Email")

    if st.button("🔍 Search Appointments"):

        appointments = search_appointments(email)

        if appointments:

            st.success(
                f"Total Appointments Found : {len(appointments)}"
            )

            st.markdown("---")

            for row in appointments:

                with st.container():

                    st.markdown(
                    """
                    <div style="
                    border:1px solid #dbeafe;
                    border-radius:10px;
                    padding:15px;
                    margin-bottom:20px;
                    background:#ffffff;
                    ">
                    """,
                    unsafe_allow_html=True)

                    col1, col2 = st.columns([3,1])

                    with col1:

                        st.subheader(f"🆔 {row[1]}")

                        st.write(f"👤 Patient : **{row[2]}**")

                        st.write(f"🏥 Department : **{row[8]}**")

                        st.write(f"👨‍⚕ Doctor : **{row[9]}**")

                        st.write(f"🤒 Symptoms : **{row[7]}**")

                        st.write(f"📅 Date : **{row[10]}**")

                        st.write(f"⏰ Time : **{row[11]}**")

                        if row[12] == "Pending":

                            st.warning("🟡 Status : Pending")

                        elif row[12] == "Completed":

                            st.success("🟢 Status : Completed")

                        elif row[12] == "Cancelled":

                            st.error("🔴 Status : Cancelled")

                    with col2:

                        if row[12] == "Pending":

                            if st.button(
                                "❌ Cancel",
                                key=f"cancel_{row[1]}"
                            ):

                                cancel_appointment(row[1])

                                st.success(
                                    "Appointment Cancelled Successfully!"
                                )

                                st.rerun()

                    st.markdown("</div>", unsafe_allow_html=True)

        else:

            st.error("No Appointment Found.")
            # ==================================================
# DEPARTMENTS
# ==================================================

elif choice == "🏥 Departments":

    st.header("🏥 Hospital Departments")

    col1, col2 = st.columns(2)

    with col1:

        st.success("❤️ Cardiology")
        st.write("Heart related diseases and treatments.")

        st.success("🧠 Neurology")
        st.write("Brain and nervous system specialists.")

        st.success("🩺 General Medicine")
        st.write("General health consultation.")

    with col2:

        st.info("🦷 Dentistry")
        st.write("Dental care and oral health.")

        st.info("🦴 Orthopedics")
        st.write("Bone and joint specialists.")

        st.info("👶 Pediatrics")
        st.write("Children healthcare specialists.")

    st.divider()

    st.subheader("🏥 Hospital Facilities")

    st.write("✅ 24 x 7 Emergency Services")
    st.write("✅ ICU Available")
    st.write("✅ Laboratory")
    st.write("✅ Pharmacy")
    st.write("✅ Ambulance Facility")
    st.write("✅ Online Appointment Booking")
    st.write("✅ Email Notification System")



# ==================================================
# ADMIN LOGIN
# ==================================================

elif choice == "🛠 Admin":

    if "admin_logged" not in st.session_state:
        st.session_state.admin_logged = False

    if st.session_state.admin_logged == False:

        st.title("🔐 Admin Login")

        st.info("Authorized Personnel Only")

        username = st.text_input(
            "Admin Username"
        )

        password = st.text_input(
            "Admin Password",
            type="password"
        )

        if st.button("Login as Admin"):

            if username == "admin" and password == "admin123":

                st.session_state.admin_logged = True

                st.success("Welcome Admin 👨‍💼")

                st.rerun()

            else:

                st.error("Invalid Username or Password")

    else:

        col1, col2 = st.columns([6,1])

        with col2:

            if st.button("Logout"):

                st.session_state.admin_logged = False

                st.rerun()

        admin_panel()



# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;
padding:20px;
color:gray;'>

<h3>🏥 MediSync Hospital</h3>

Doctor Appointment Booking System

📍 Tirupati, Andhra Pradesh

📧 nikhithareddylakkireddy@gmail.com

📞 +91 xxxxxxxxxxx

<br>

<b>Developed By</b>

👩‍💻 <span style="color:#0d6efd;"><b>Nikhitha</b></span>

Artificial Intelligence & Data Science

Version 1.0

<br><br>

© 2026 MediSync Hospital

</div>
""",
unsafe_allow_html=True
)