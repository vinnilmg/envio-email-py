from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from template import body_msg

email = 'email'
senha = 'senha'

msg = MIMEMultipart()
msg['from'] = 'Vinicius Lima'
msg['to'] = 'vini.delimagomes@gmail.com'
msg['subject'] = 'Email de Testes.'

body = MIMEText(body_msg, 'html')
msg.attach(body)

with open('luffy.jpg', 'rb') as pic:
    pic = MIMEImage(pic.read())
    msg.attach(pic)


with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, senha)
        smtp.send_message(msg)
        print('Email enviado com sucesso.')
    except Exception as e:
        print('Email não foi enviado.')
        print(e)
