#Librerías
import can
import time
from can import Message

'''
The functional PID query is sent to the vehicle on the CAN bus at ID 7DFh, using 8 data bytes. The bytes are:

                                                            Byte    
PID Type	        0	        1	                        2	                                        3	    4	    5	    6	    7
SAE Standard	Number of       Service                     PID code                                    not used (ISO 15765-2 suggests CCh)
                additional      01 = show current data;     (e.g.: 05 = Engine coolant temperature)	
                data bytes:     02 = freeze frame;
                2	
'''

'''Globales'''
#Los valores de la tabla de arriba están convertidos de hex a int
arryFuelFrame = bytearray([2, 1, 47, 204, 204, 204, 204, 204])

#El ID broascast es 7DF en hex y 2015 en int
queryFuelMsg = Message(is_extended_id=False, arbitration_id=2015, data=arryFuelFrame)

#Configuración del bus, canal can0 y velocidad 500KBaud
bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)

'''Funciones'''

'''
Se encarga de cosntruir el mensaje necesario para enviar la petición de
combustible a la computadora del auto, por medio del ID para broadcast =0x7DF y 
el dataframe 02,01,0x2F,0xCC,0xCC,0xCC,0xCC,0xCC de acuerdo al OBDII standard.
'''
def TxFuel():

    #Envío del request Fuel al CANBUS
    bus.send(queryFuelMsg)

    #Usuario
    print(">> Fuel Level request sended...")

'''MAIN'''

while True:

    #Control de errores
    try:

        #Request Fuel Level
        TxFuel()

        #5 Sec Delay
        time.sleep(5)

    except(KeyboardInterrupt):

        #Detenemos el CANBUS
        bus.shutdown()

        #Usuario
        print(">> Bus CAN0 detenido...")
        print(">> Programa terminado por el usuario...")
        break