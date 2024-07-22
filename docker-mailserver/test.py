import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr, make_msgid, formatdate
import time

# SMTP settings
smtp_server = "mail.example.com"
smtp_port = 587  # or 465 for SSL
username = "noreply@example.com"
password = "geGZ0uz8wNGn8ZM"

# IMAP settings
imap_server = "mail.example.com"
imap_port = 993
sent_folder = "Sent"  # Adjust if your sent folder has a different name

# Email content
# formataddr takes sender name and email :  you can replace the sender name by what you want or by default set to username
from_email = formataddr(("No Reply", username))
to_email = "john@example.com"
subject = "Test Email from Python"
body = "This is a test email sent from a Python script."

# Create MIME message
msg = MIMEMultipart()
msg["From"] = from_email
msg["To"] = to_email
msg["Subject"] = Header(subject, "utf-8")
msg["Message-ID"] = make_msgid(domain="example.com")
# Adding the Date header, this is a required header
msg["Date"] = formatdate(localtime=True)

msg.attach(MIMEText(body, "plain", "utf-8"))

# Send the email via SMTP
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Comment out if using SSL (port 465)
    server.login(username, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()
    print("Email sent successfully!")

    # (optional) Save a copy of the email in the 'Sent' folder via IMAP
    # Connect to the IMAP server and save the email to the 'Sent' folder
    with imaplib.IMAP4_SSL(imap_server, imap_port) as imap_server:
        imap_server.login(username, password)
        imap_server.append(
            sent_folder,
            "",
            imaplib.Time2Internaldate(time.time()),
            text.encode("utf-8"),
        )
        imap_server.logout()
        print("Copy saved in 'Sent' folder!")
except Exception as e:
    print(f"Error: {e}")
