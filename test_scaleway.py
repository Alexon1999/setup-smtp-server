import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(
    smtp_host, smtp_port, smtp_user, smtp_password, from_addr, to_addr, subject, body
):
    # Create a MIMEText object to represent the email
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = subject

    # Attach the email body to the MIMEText object
    msg.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()  # Enable TLS
        server.login(smtp_user, smtp_password)  # Login to the SMTP server
        server.send_message(msg)  # Send the email


# Email configuration
smtp_host = "smtp.tem.scw.cloud"
smtp_port = 587
smtp_user = "f29228ea-993a-47fa-b07a-88ac6b7db7a0"
smtp_password = "bfa76664-d603-42a7-83d6-2b974cb96228"
from_addr = "noreply@example.com"
to_addr = "john@example.com"
subject = "Test Email from Python"
body = "This is a test email sent from a Python script."

# Send the email
send_email(
    smtp_host, smtp_port, smtp_user, smtp_password, from_addr, to_addr, subject, body
)


# SCW09WD0VCZX5EZRRSRS
# bfa76664-d603-42a7-83d6-2b974cb96228
