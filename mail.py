#import pip
#pip.main(["install", "openpyxl"])

import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Email configuration
sender_email = "adithyanraj150@gmail.com"
sender_password = "wwln aqlf gcxn uszd"  # Replace with your email password
email_subject = "Summmary and minutes of meeting"
email_body = "Summary , Meeting Transcript is attached below"

# Excel file with email addresses
excel_file = "C:/Users/adith/Dropbox/PC/Pictures/INVIS/Project_2/sumarisegpt/email_addresses.xlsx"

# List of text files to send as attachments
text_files = [
    "C:/Users/adith/Dropbox/PC/Pictures/INVIS/Project_2/sumarisegpt/meeting_minutes.txt",
    "C:/Users/adith/Dropbox/PC/Pictures/INVIS/Project_2/sumarisegpt/combined_text.txt",
    "C:/Users/adith/Dropbox/PC/Pictures/INVIS/Project_2/sumarisegpt/summary.txt",
]

# Read email addresses from Excel
df = pd.read_excel(excel_file)
email_addresses = df["Email address"].tolist()

# Email server settings (for Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Iterate through email addresses and send the text files as attachments
for recipient_email in email_addresses:
    # Create message container
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = email_subject

    # Attach email body
    msg.attach(MIMEText(email_body, "plain"))

    # Attach text files as attachments
    for text_file in text_files:
        with open(text_file, "rb") as file:
            attachment = MIMEApplication(file.read())
        attachment.add_header("Content-Disposition", "attachment", filename=text_file)
        msg.attach(attachment)

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {str(e)}")
