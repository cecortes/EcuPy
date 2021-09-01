#Librerías
import can
from can import Message
from can import bus

#Globales

#CAN

#Función principal de ejecución
from can.message import Message


def main():
    print("*******************************************************************")
    print("*****                                                         *****")
    print("*****        Programa CAN BUS para envío de QUERYs            *****")
    print("*****                                                         *****")
    print("*****                                                         *****")
    print("*****                                                         *****")
    print("*****                                                         *****")
    print("***** César López 2021                    Send Single Frame.  *****")
    print("*****                                                         *****")
    print("*******************************************************************")
    print()
    print(">>Elija el modo: ")
    print(">> 1 - Current data")
    print(">> 2 - Freeze data")
    #Variable para almacenar el modo
    modo = input()
    intModo = int(modo)
    print()

    print(">>Elija el PID para el Query: ")
    print(">> 03 - Fuel System Status")
    print(">> 04 - Engine load value")
    print(">> 05 - Engine coolant temperature")
    print(">> 0A - Fuel pressure")
    print(">> 0C - Engine rpm")
    print(">> 0D - Speed")
    print(">> 11 - Throttle position")
    print(">> 2F - Fuel Level Input")
    print(">> 46 - Ambient air temp")
    #Variable para almacenar el PID
    pid = input()
    print()

    #Coversión de string a hex a int
    pid = "0x" + pid
    intPid = int(pid, 16)

    #Construcción del array para el query
    queryArrFrame = bytearray([2, intModo, intPid, 204, 204, 204, 204, 204]) #Los valores están convertidos de hex a int

    #Construcción del mensaje
    queryMsg = Message(is_extended_id=False, arbitration_id=2015, data=queryArrFrame)   #El Id broadcast es 7DF en hex y 2015 en int

    #Configuración del bus, canal can0 y velocidad: 1000000 para Mitsubishi y Audi
    bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=1000000)

    #Envío del mensaje CANBUS
    bus.send(queryMsg)

    #Detenemos el CANBUS
    bus.shutdown()

    #User
    print(">> Query enviado: ", queryMsg)


#Ejecución de la función principal
if __name__ == "__main__":
    main()