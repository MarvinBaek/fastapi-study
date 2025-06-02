import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_verification_email(email: str, token: str):
    sender = os.getenv("EMAIL_SENDER")
    app_password = os.getenv("EMAIL_PASSWORD")
    verification_url = f"http://localhost:8000/api/v1/auth/verify-email?token={token}"

    msg = MIMEText(f"이메일 인증을 위해 아래 링크를 클릭하세요:\n\n{verification_url}")
    msg["Subject"] = "이메일 인증 요청"
    msg["From"] = sender
    msg["To"] = email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, app_password)
        server.send_message(msg)
