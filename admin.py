import streamlit as st
import pandas as pd
import plotly.express as px

from appointment import get_appointments


def admin_panel():

    st.title("🏥 Admin Dashboard")

    appointments = get_appointments()

    if not appointments:
        st.warning("No Appointments Found")
        return

    columns = [
        "ID",
        "Appointment ID",
        "Patient",
        "Age",
        "Gender",
        "Phone",
        "Email",
        "Symptom",
        "Department",
        "Doctor",
        "Date",
        "Time",
        "Status",
        "Created At"
    ]

    df = pd.DataFrame(appointments, columns=columns)

    # ==========================================
    # Dashboard Statistics
    # ==========================================

    total = len(df)

    pending = len(df[df["Status"] == "Pending"])

    completed = len(df[df["Status"] == "Completed"])

    cancelled = len(df[df["Status"] == "Cancelled"])

    st.subheader("📊 Dashboard Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📅 Total", total)

    with col2:
        st.metric("🟡 Pending", pending)

    with col3:
        st.metric("🟢 Completed", completed)

    with col4:
        st.metric("🔴 Cancelled", cancelled)

    st.divider()

    # ==========================================
    # Department Chart
    # ==========================================

    st.subheader("🏥 Department Wise Appointments")

    dept = (
        df["Department"]
        .value_counts()
        .reset_index()
    )

    dept.columns = [
        "Department",
        "Appointments"
    ]

    fig = px.bar(
        dept,
        x="Department",
        y="Appointments",
        color="Department",
        title="Appointments by Department"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # All Appointments
    # ==========================================

    st.subheader("📋 All Appointment Records")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # Pending Appointments
    # ==========================================

    st.subheader("🟡 Pending Appointments")

    pending_df = df[df["Status"] == "Pending"]

    if len(pending_df):

        st.dataframe(
            pending_df,
            use_container_width=True
        )

    else:

        st.success("No Pending Appointments")

    st.divider()

    # ==========================================
    # Completed Appointments
    # ==========================================

    st.subheader("🟢 Completed Appointments")

    completed_df = df[df["Status"] == "Completed"]

    if len(completed_df):

        st.dataframe(
            completed_df,
            use_container_width=True
        )

    else:

        st.info("No Completed Appointments")

    st.divider()

    # ==========================================
    # Cancelled Appointments
    # ==========================================

    st.subheader("🔴 Cancelled Appointments")

    cancelled_df = df[df["Status"] == "Cancelled"]

    if len(cancelled_df):

        st.dataframe(
            cancelled_df,
            use_container_width=True
        )

    else:

        st.success("No Cancelled Appointments")

    st.divider()

    # ==========================================
    # Download CSV
    # ==========================================

    csv = df.to_csv(index=False)

    st.download_button(
        label="📥 Download Appointment Report",
        data=csv,
        file_name="appointments.csv",
        mime="text/csv"
    )

    st.success("✅ Admin Dashboard Loaded Successfully")