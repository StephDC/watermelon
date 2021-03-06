import flask
import mysql.connector as sql
import smtplib

from random import choice
from simplejson import dumps

from info import *

def connect_db():
    return sql.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        database=db_name
    )

# email
def send_email(sender, to, subject, body):
    with smtplib.SMTP_SSL(sender.get("smtp_server"), sender.get("port")) as conn:
        conn.login(sender.get("address"), sender.get("token"))
        conn.sendmail(
            sender.get("address"),
            to,
            bytes("Sender: %s\nTo: %s\nSubject: %s\nContent-Type: text/html\n\n%s" % (
                sender.get("address"),
                to,
                subject,
                body
            ), "utf8")
        )

# random
def rand_str(length):
    return "".join(choice("01234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM") for i in range(length))
