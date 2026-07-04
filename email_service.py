import smtplib
from email.mime.text import MIMEText

EMAIL = "nikhithareddylakkireddy@gmail.com"
PASSWORD = "ernf btrp vljr ckgs"

def send_confirmation_email(
    recipient_email,
    patient,
    appointment_id,
    symptom,
    department,
    doctor,
    date,
    time
):
    try:

        subject = "Doctor Appointment Confirmation"

        body = f"""
Hello {patient},

Your appointment has been booked successfully.

Appointment ID: {appointment_id}

Symptom: {symptom}
Department: {department}
Doctor: {doctor}

Date: {date}
Time: {time}

Thank you for using our Doctor Appointment Booking System.
"""

        msg = MIMEText(body)

        msg["Subject"] = subject
        msg["From"] = EMAIL
        msg["To"] = recipient_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(EMAIL, PASSWORD)

        server.sendmail(
            EMAIL,
            recipient_email,
            msg.as_string()
        )

        server.quit()

        return True

    except Exception as e:
        print("EMAIL ERROR:", e)
        return False