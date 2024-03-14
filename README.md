# Email Automation

# Email Automation with Attachments

This project contains a Python script that automates the process of sending emails with attachments. It uses the `smtplib` library to handle the SMTP protocol and the `email` library to create and manage email messages and attachments.

## Features

- Send emails with subject and body
- Attach files to the email
- Scan PDF files for specific text (using PyPDF2)
- Email validation using regular expressions (using re)

## Prerequisites

Before running this script, you will need:

- Python 3.x installed on your system
- A valid email account from which to send the emails
- The recipient's email address
- Files to attach to the email (if any)

## Libraries Used

- `PyPDF2`: To read and search through PDF files.
- `re`: To validate email addresses.
- `smtplib`: To connect to the email server.
- `email`: To create email messages and manage attachments.
- `os`: To interact with the file system.

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/email-automation.git
