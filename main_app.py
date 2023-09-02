from email.message import EmailMessage
from key_code import password
import ssl
import smtplib

# Email Name and Passcode
email_sender = 'farazfayyazschool@gmail.com' # Your Email
email_password = password # Passcode from Gmail to bypass 2 factor check

subject = input('Enter the email Subject: ') # User inputs Email Subject

email_receiver = input("Enter someone's Email (johndoe@email.com): ") # User enters email to send to


body = input('Enter your message: ') # User enters a body message

# Email Structure gets input into email app
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

# Function fills in the information and sends email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())