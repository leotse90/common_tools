#coding=utf-8

import smtplib

from email.mime.text import MIMEText

# constants

HOST_NAME = "leotse"
HOST_MAIL = "proleo@leotse.com"

MAIL_SERVER_HOST = "localhost"
MAIL_SERVER_USER = "****"
MAIL_SERVER_PWD = "****"


# methods for send mail

def send_text_mail(mail_to, subject, content):
    # mail content
    mail_from = HOST_NAME + "<" + HOST_MAIL + ">"
    mail_content = MIMEText(content, _subtype="plain", _charset="utf-8")
    mail_content["From"] = mail_from
    mail_content["To"] = ";".join(mail_to)
    mail_content["Subject"] = subject
    
    try:
        # server config
        mail_server = smtplib.SMTP()
        mail_server.connect(MAIL_SERVER_HOST)
#     mail_server.login(MAIL_SERVER_USER, MAIL_SERVER_PWD)
        mail_server.ehlo()
        mail_server.starttls()
        
        mail_server.sendmail(mail_from, mail_to, mail_content.as_string())
        mail_server.close()
        return True
    except Exception:
        return False
