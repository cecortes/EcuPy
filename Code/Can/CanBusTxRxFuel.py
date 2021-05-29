#Librerías
import can
import time
from can import Message
from can import listener

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

#Filtros SETUP
ecuFilter = [{'can_id': 0x7E8, 'can_mask':0x21, 'extended': False}]

#Configuración del bus, canal can0 y velocidad 500KBaud
bus = can.interface.Bus(bustype='socketcan', channel='can0', can_filters=ecuFilter, bitrate=500000)

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

'''
Esta función la dispara el Listener y se encarga de mostrar cualquier mensaje que circule por la línea CANBUS ya que carece de filtros o máscaras para descriminar los datos.
Cumple con la función de un simple sniffer.
'''
def Sniffer():

    #Usuario
    print(canRx)

'''
Esta función se encarga de iniciar la variable global del bus.recv con un timeout de escucha de 1 seg, además de indicarle al objeto listener que función debe disparar cuando se cumpla la recepción de un mensaje CANBUS válido y que cumpla con el filtro y máscara configurado.
'''
def RxCan():

    #Global init
    global canRx, listener

    #Variable que recibe la respuesta de la ECU, parámetro timeout en secs
    canRx = bus.recv(timeout=1)

    #Listener que se encarga de disparar a la función declarada
    listener = GetFuel()

'''
Valida el PID del frame recibido para que sea 0x2F
'''
def GetFuel():

    #Arreglo local
    frame = bytearray(8)

    #Almacenamos el bus de datos en el arreglo
    frame = canRx.data

    #Variable cadena con el byte significativo
    strFrame = frame[2:3]

    #Usuario DEBUG <---------------------------
    print(strFrame.hex())

    if strFrame == 0x2F:
        print("Hit")


'''MAIN'''
#Iniciamos las variables y objetos que serán utilizados por el CANBUS en funciones posteriores.
canRx = bus.recv(timeout=1)
listener = Sniffer()

while True:

    #Control de errores
    try:

        #Request Fuel Level
        TxFuel()

        #Receive CanBus Message
        RxCan()

        #2 Sec Delay
        time.sleep(2)

    except(KeyboardInterrupt):

        #Detenemos el CANBUS
        bus.shutdown()

        #Usuario
        print(">> Bus CAN0 detenido...")
        print(">> Programa terminado por el usuario...")
        break