#Importamos las librerías necesarias
import can
from can import Message
from can import bus

#Globales
sendArrFrame = bytearray([2, 1, 47, 204, 204, 204, 204, 204])           #Los valores están convertidos de hex a int, 2F-47 CC-204
queryMsg = Message(is_extended_id=False, arbitration_id=2015, data=sendArrFrame)        #El Id broadcast es 7DF en hex y 2015 en int

#Configuración del bus, canal can0 y velocidad:1000000 para Mitsubishi y Audi
bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=1000000)

#Envío de mensaje CANBUS
bus.send(queryMsg)

#Detenemos el CANBUS
bus.shutdown()

#Mostramps el mensaje en pantalla
print(">>Send : " , queryMsg)