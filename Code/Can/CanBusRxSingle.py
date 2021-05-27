#Importamos la librería
import can

#Configuración del bus, canal can0 y velocidad 500KBaud
bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)

for msg in bus:
    print(msg)