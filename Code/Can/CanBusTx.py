#Importamos la librería
import can
from can import Message

#Globales
'''
The functional PID query is sent to the vehicle on the CAN bus at ID 7DFh, using 8 data bytes. The bytes are:

                                                            Byte    
PID Type	        0	        1	                        2	                                        3	    4	    5	    6	    7
SAE Standard	Number of       Service                     PID code                                    not used (ISO 15765-2 suggests CCh)
                additional      01 = show current data;     (e.g.: 05 = Engine coolant temperature)	
                data bytes:     02 = freeze frame;
                2	
'''
arryFuelFrame = bytearray([2, 1, 47, 204, 204, 204, 204, 204])                              #Los valores de la tabla de arriba están convertidos de hex a int
queryFuelMsg = Message(is_extended_id=False, arbitration_id=2015, data=arryFuelFrame)       #El ID broascast es 7DF en hex y 2015 en int

#Configuración del bus, canal can0 y velocidad 500KBaud
bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)

#Envío de mensaje CANBUS
bus.send(queryFuelMsg)

#Detenemos el CANBUS
bus.shutdown()

#Mostramos el mensaje en pantalla
print(queryFuelMsg)