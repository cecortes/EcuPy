#Importamos la librería
import can

#Configuración del bus, canal can0 y velocidad 500KBaud
bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)

#Recibe los mensajes del buffer y los muestra en pantalla, de manera ciclíca el pprograma no sale hasta interrupt
for msg in bus:
    print(msg)