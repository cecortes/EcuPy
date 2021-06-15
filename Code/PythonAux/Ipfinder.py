#Librerías
import socket
import urllib.request
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP

#Captura de Hostaname
hostname = socket.gethostname()

#Captura de la Ip privada
ipLocal = socket.gethostbyname(hostname)

#Captura de la ip pública
ipPub = urllib.request.urlopen('https://ident.me').read().decode('utf8')

#Salida de resultados a pantalla
print(f">> Nombre del Host: {hostname}")
print(f">> Dirección ip local: {ipLocal}")
print(f">> Dirección ip externa: {ipPub}")
print(">> Preparando mensaje...")

#Construcción del objeto para el mensaje
mensaje = MIMEMultipart("plain")
mensaje["From"]= "cesarlopezcortes@hotmail.com"
mensaje["To"]= "cesarlopezcortes@hotmail.com"
mensaje["Subject"]= "Hostname: " + hostname + "Local: " + ipLocal

#Construccioón del objeto SMTP
smtp = SMTP("smtp.live.com")
smtp.starttls()
smtp.login("cesarlopezcortes@hotmail.com", "LynyrdSkynyrd2878")
smtp.sendmail("cesarlopezcortes@hotmail.com", "cesarlopezcortes@hotmail.com", mensaje.as_string())
smtp.quit()

#Usuario
print(">> Mensaje enviado...")