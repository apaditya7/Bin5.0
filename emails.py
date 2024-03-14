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
"""def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page in range(reader.numPages):
            text += reader.getPage(page).extractText()
        return text
"""
def find_email_addresses(text):
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

email_addresses = ["aditya034@e.ntu.edu.sg","apaditya.2005@gmail.com"]

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

# Example usage
attachment_paths = ["Academic_Transcript.pdf", "ap_aditya_resume.pdf"]
# Example usage
pdf_path = "path_to_your_pdf.pdf"
#text = extract_text_from_pdf(pdf_path)
#email_addresses = find_email_addresses(text)

subject = "Application for Internship"
body = """Dear Sir/Ma’am

My name is Anand Pramod Aditya, I’m currently a sophomore studying computer science at Nanyang Technological University. I’m writing to you to apply for an internship role at your company this summer. 


I understand you’re probably busy so I’ll keep this brief. My journey in computing began in 2019 and since then I’ve gained proficiency in several languages and frameworks most notably Python, Javascript and SQL. Through my experiences in internships, projects, hackathons and coursework, I’ve gained a huge passion and a decent skill set in the field of computing in specific AI, data analysis and software development and the practical applications.


While I may be inexperienced, I’m deeply passionate about computing and am just looking for an opportunity to learn in a practical environment. I apply to your company purely out of my passion to grow and learn in this field and not as an academic requirement, or any monetary gain and am open to working for any salary your company deems fit. I believe being able to work at a dynamic startup that utilizes technology to make a real world impact is the most suitable environment for me to grow and thus I hope you can consider my sincere application to your company.


I’ve attached my resume and academic transcript for more details on my experiences and skill set, kindly let me know if you’d require anything else. Looking forward to hearing back from you.


Regards """

send_emails_with_attachments(email_addresses, subject, body, attachment_paths)
