import smtplib
import ssl
import streamlit as st

def send_email(message):
    port = 465  # SSL port
    try:
        password = st.secrets["PASSWORD"]
    except KeyError:
        st.error("Error: Missing 'PASSWORD' secrets. Please set it in secrets.toml.")
        return  # Exit the function if secret is missing

    username = "shantanupokale009@gmail.com"
    receiver = "shantanupokale009@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
