#Librerías
import can
import time
from can import Message


'''MAIN'''

while True:

    #Control de Errores
    try:

        #Reuest Fuel Level
        TxFuel()

        #5Seg Delay
        time.sleep(5)

    except(KeyboardInterrupt):

        #Detenemos el CANBUS
        bus.shutdown()

        #Usuario
        print(">> Bus CAN0 detenido...")
        print(">> Programa terminado por el usuario...")
        break