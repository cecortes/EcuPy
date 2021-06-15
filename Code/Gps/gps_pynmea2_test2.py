#Importamos las librerías necesarias
import serial
import pynmea2
import string
import io

#Globales
BAUDRATE = 9600
TIMEOUT = 1
usbCom = 0

########### Funciones #############################
#Se encarga de inciar y configurar el UART
def InitUart():
    #Cada que se utiliza una variable global se debe indicar en la función que la llama
    global BAUDRATE, TIMEOUT, usbCom

    #Objetos
    usbCom = serial.Serial('COM3')      #Para el caso de Linux '/dev/ttyUSB0' or '/dev/ttyAMA0' or Zero '/dev/ttyS0'
    usbCom.baudrate = BAUDRATE
    usbCom.timeout = TIMEOUT

    #Flush
    usbCom.flushInput()

######### MAIN ###################################

#Iniciamos la comUART
InitUart()

#Wrapper para el buffer a texto
usbWrp = io.TextIOWrapper(io.BufferedRWPair(usbCom, usbCom))

while True:
    #Control de errores
    try:
        #Feed hungry mounster
        gpsNewMsg = usbWrp.readline()

        #print(gpsNewMsg[0:6])  DEBUG MESG

        #Validación del mensaje
        if (gpsNewMsg[0:6] == "$GPRMC"):
            #Proccess msg
            gpsDat = pynmea2.parse(gpsNewMsg)
            #Usr
            print(gpsDat)
            #Decode data and convert float to string only 6 decimals
            fecha = str(gpsDat.datestamp)
            hora = str(gpsDat.timestamp)
            lat = str('%.8f' % gpsDat.latitude)
            lon = str('%.8f' % gpsDat.longitude)
            #Usr
            print(">> Fecha: " + fecha)
            print(">> Hora: " + hora)
            print(">> Latitud: " + lat)
            print(">> Longuitud: " + lon)

    except pynmea2.ParseError as e:
        #print('Parse error: {}'.format(e)) DEBUG MESG
        continue

    except(KeyboardInterrupt):
        print(">> Interrupción del teclado...")
        break