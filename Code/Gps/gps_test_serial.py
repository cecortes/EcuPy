#Importamos las librerías necesarias
import serial

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
    usbCom = serial.Serial('COM3')      #Para el caso de Linux '/dev/ttyUSB0' or '/dev/ttyAMA0'
    usbCom.baudrate = BAUDRATE
    usbCom.timeout = TIMEOUT

    #Flush
    usbCom.flushInput()

######### MAIN ###################################

#Iniciamos la comUART
InitUart()

while True:
    try:
        ser_bytes = usbCom.readline()
        print(ser_bytes)
    except:
        print("Interrupción del teclado")
        break