from os import system as sys
from termcolor import colored
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email
import secrets
import smtplib
import ssl
import json


def _write_to_file(msg):
    with open('message.txt', 'w') as write_file:
        write_file.write(msg)
    return write_file


def _encrypt_message(msg, key):
    file = _write_to_file(msg)
    sys_string = 'python ../my_codex/k_obscurus.py --encrypt {} {}'.format(key, file.name)
    msg = sys(sys_string)
    if msg == 0:
        print(colored('success','green'))
    else:
        print(colored('error try again','red'))


def _send_email(recipient_email):
    msg = MIMEMultipart()
    msg["From"]= secrets.email
    msg["To"]=recipient_email
    msg["Sunbject"]="Super Secret message"
    msg.attach(MIMEText("secret message sent to you","plain"))
    attch_file = "message_out.json"
    with open(attch_file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attch_file}",
    )
    msg.attach(part)
    text = msg.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(secrets.email, secrets.password)
        server.sendmail(secrets.email, recipient_email, text)
    print(colored('success','green'))


def main():
    print('welcome to the encrypted mesaging.\n please enter the message')
    msg = input('message: ')
    key = input('password: ')
    _encrypt_message(msg, key)
    recipient_email = input('email of recipient: ')
    _send_email(recipient_email)


if __name__ == '__main__':
    main()
