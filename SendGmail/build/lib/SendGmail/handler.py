import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(appEmail, appPassword, toAddress, subject, body):

    message = MIMEMultipart()
    message["To"] = toAddress
    message["From"] = appEmail
    message["Subject"] = subject
    messageText = MIMEText(body,'html')
    message.attach(messageText)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo('Gmail')
    server.starttls()
    server.login(appEmail,appPassword)
    server.sendmail(appEmail, toAddress, message.as_string())

    server.quit()