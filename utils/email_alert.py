import os
import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, body, to_email):
    email_provider = os.getenv('EMAIL_PROVIDER', 'protonmail')  # 'protonmail' or 'sendgrid'
    
    if email_provider == 'protonmail':
        smtp_host = 'smtp.protonmail.com'
        smtp_port = 587
        smtp_user = os.getenv('EMAIL_USER')
        smtp_pass = os.getenv('EMAIL_PASS')
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = smtp_user
        msg['To'] = to_email

        try:
            server = smtplib.SMTP(smtp_host, smtp_port)
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.sendmail(smtp_user, [to_email], msg.as_string())
            server.quit()
            print("Alert email sent.")
        except Exception as e:
            print(f"Email send failed: {e}")
