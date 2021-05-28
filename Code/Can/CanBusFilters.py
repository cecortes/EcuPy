#Importamos la librería
import can
from can import listener

#Configuración de filtros
filtro = [{"can_id": 0x2F, "can_mask": 0x21, "extended": False}]

#Configuración del bus, canal can0 y velocidad 500KBaud
bus = can.interface.Bus(bustype='socketcan', channel='can0', can_filters=filtro, bitrate=500000)

#Función para imprimir el mensaje CANBUS en pantalla
def PrintMsg(msg):
    print(msg)

#Variable que recibe el mensaje para ser usada como argumento
msg = bus.recv()

#Listener, recibe como argumento el mensaje CANBUS
listener = PrintMsg(msg)

#listener.stop()

#Usuario
print(">> Done!!!")