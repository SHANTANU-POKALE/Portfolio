import streamlit as st
import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "shantanupokale009@gmail.com"
    password = st.secrets["PASSWORD1"]

    receiver = "shantanupokale009@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
