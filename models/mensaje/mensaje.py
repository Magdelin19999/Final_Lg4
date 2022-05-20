
from smtplib import SMTP
from email.message import EmailMessage
from flask import url_for

from config import settings
username = settings.SMTP_EMAIL
password = settings.SMTP_PASSWORD
def mensaje(correoEmpresa,id,keyToken):
    
    url = url_for('activarEmpresa', token=keyToken, _external=True)
    
    mensaje=f'!Hola, {correoEmpresa}, Abre este link, para terminar el proceso de activacion: {url}'
    
    subject="Contirnuar con el registro"
    envio(mensaje, subject, correoEmpresa)

def solicituCambioContra(correoEmpresa,keyToken):
    print(correoEmpresa)
    
def envio(mensaje, subject, correoEmpresa):
    print(mensaje)
    msg = EmailMessage()
    msg.set_content(mensaje)
    msg['Subject']=subject
    msg['Form']=username
    msg['To']=correoEmpresa

    server = SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.send_message(msg)
    server.quit()
    
''' def mensaje(correoEmpresa,id,keyToken):
    # el correo del admin
    username = settings.SMTP_EMAIL
    password = settings.SMTP_PASSWORD
    
    msg = EmailMessage()
    url = url_for('activarEmpresa',token=keyToken, _external=True)
    msg.set_content(f'!Hola, {correoEmpresa}, Abre este link, para terminar el proceso de activacion: {url}')

    msg['Subject']='Asunto de prueba'
    msg['Form']=username
    msg['To']=correoEmpresa

    server = SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.send_message(msg)
    #code = server.rcpt(usuario)
    #print(code)
    server.quit() 
'''