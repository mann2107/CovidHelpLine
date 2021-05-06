import email
import logging
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import EmailConfig

# logging.basicConfig(filename='app.log', filemode='a', level=# logging.debug, format='%(asctime)s - %(message)s',
#                     datefmt='%d-%b-%y %H:%M:%S')


def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)


def send_mail(receiver_email, message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = EmailConfig.username  # Enter your address
    # receiver_email = "manish.kumar2107@gmail.com"  # Enter receiver address
    password = EmailConfig.password
    # message = """\
    # Subject: Hi there

    # This message is sent from Python."""
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        return True
    except Exception as e:
        print(e)
        return False


def send_mail_reply(receiver_email, message, message_id, subject):
    # logging.debug('Replying to email')
    # logging.debug('Message Id is ')
    # logging.debug(message_id)
    # logging.debug('Subject is ')
    # logging.debug(subject)
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = EmailConfig.username  # Enter your address
    # receiver_email = "manish.kumar2107@gmail.com"  # Enter receiver address
    password = EmailConfig.password
    # message = """\
    # Subject: Hi there

    # This message is sent from Python."""
    new = MIMEMultipart("mixed")
    body = MIMEMultipart("alternative")
    body.attach(MIMEText(message, "plain"))
    # body.attach( MIMEText("<html>"+message+"</html>", "html") )
    new.attach(body)
    new.add_header('In-Reply-To', message_id)
    new.add_header('References', message_id)
    new.add_header('Subject', subject)
    new["Message-ID"] = email.utils.make_msgid()
    new["In-Reply-To"] = message_id
    new["References"] = message_id
    # new["Subject"] = "Re: "
    new["To"] = receiver_email
    new["From"] = sender_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, new.as_string())


def send_mail_reply_with_attachment(receiver_email, message, message_id, subject, filename):
    # logging.debug('Replying to email with attachment')
    # logging.debug('Message Id is ')
    # logging.debug(message_id)
    # logging.debug('Subject is ')
    # logging.debug(subject)
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = EmailConfig.username  # Enter your address
    # receiver_email = "manish.kumar2107@gmail.com"  # Enter receiver address
    password = EmailConfig.password
    # message = """\
    # Subject: Hi there

    # This message is sent from Python."""
    new = MIMEMultipart("mixed")
    body = MIMEMultipart("alternative")
    body.attach(MIMEText(message, "plain"))

    ########################
    # open the file to be sent  

    attachment = open(filename, "rb")

    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form 
    p.set_payload((attachment).read())

    # encode into base64 
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg' 
    new.attach(p)
    ########################
    # body.attach( MIMEText("<html>"+message+"</html>", "html") )
    new.attach(body)
    new.add_header('In-Reply-To', message_id)
    new.add_header('References', message_id)
    new.add_header('Subject', subject)
    new["Message-ID"] = email.utils.make_msgid()
    new["In-Reply-To"] = message_id
    new["References"] = message_id
    # new["Subject"] = "Re: "
    new["To"] = receiver_email
    new["From"] = sender_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, new.as_string())


