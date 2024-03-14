import PyPDF2
import re
import smtplib
from email.message import EmailMessage

import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page in range(reader.numPages):
            text += reader.getPage(page).extractText()
        return text

def find_email_addresses(text):
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

email_addresses = ["exampleemail.com","exampleemail.com"]

def send_emails_with_attachments(email_addresses, subject, body, attachment_paths):
    sender_email = "youremail@email.com"
    sender_password = "yourpassword"

    with smtplib.SMTP_SSL('smtp.yourprovider.com', 465) as smtp:
        smtp.login(sender_email, sender_password)

        for email in email_addresses:
            # Create a multipart message
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = email

            # Add body to email
            msg.attach(MIMEText(body, 'plain'))

            # Process each attachment
            for attachment_path in attachment_paths:
                if attachment_path and os.path.isfile(attachment_path):
                    with open(attachment_path, "rb") as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())

                    # Encode file in ASCII characters to send by email
                    encoders.encode_base64(part)

                    # Add header as key/value pair to attachment part
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= {os.path.basename(attachment_path)}",
                    )

                    msg.attach(part)

            # Send the email
            smtp.send_message(msg)
            print(f"Email sent to {email}")


attachment_paths = ["example.pdf", "example.pdf"]

pdf_path = "path_to_your_pdf.pdf"
text = extract_text_from_pdf(pdf_path)
email_addresses = find_email_addresses(text)

subject = ""
body = """ """

send_emails_with_attachments(email_addresses, subject, body, attachment_paths)
