import passwordGenerator as pg
import smtplib
from email.message import EmailMessage
def emailSend(email):
    smtp_server = 'smtp.example.com'  # SMTP server address
    smtp_port = 587  # SMTP server port
    sender_email = 'your_email@example.com'  # Sender's email address
    sender_password = 'your_email_password'  # Sender's email password

    msg = EmailMessage()
    msg.set_content(f'Your OTP is: {"123"}')

    msg['Subject'] = 'OTP for Multi-factor Authentication'
    msg['From'] = sender_email
    msg['To'] = email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
    
emailSend("daniel.zlotnick5@gmail.com")