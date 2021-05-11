#Importamos las librerías necesarias
import serial
import pynmea2      #Se encarga de los mensajes NMEA
import string
import io
import arrow        #Se encarga de manejar el datetimestamp

#Globales
BAUDRATE = 9600
TIMEOUT = 1
usbCom = 0
datoLog = ""
noValidData = True

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

'''
Se encarga de recibir el dato NMEA para ser procesado
Obtiene los valores necesarios y los convierte a Strings
Construye un objeto del tipo arrow para cambiar el UTC a -6 GMT
Convierte el timestamp
Le da el formato necesario al timestamp
Construye el mensaje CSV y lo almacena en la variable global
'''
def GpsGetData(newLine):
    #Control de errores, salida en caso de haber error en el mensaje pynmea2
    try:
        #Validación del mensaje
        if (gpsNewMsg[0:6] == "$GPRMC"):
            #Proccess msg
            gpsDat = pynmea2.parse(gpsNewMsg)
            print(gpsDat)

            #Decode data and convert float to string only 6 decimals
            fecha = str(gpsDat.datestamp)
            hora = str(gpsDat.timestamp)
            lat = str('%.8f' % gpsDat.latitude)
            lon = str('%.8f' % gpsDat.longitude)

            #Control de errores, salida en caso de haber dato nulo en la fecha/hora
            try:
                #Construction arrow object to handle timestamp
                fechaHora = arrow.get(fecha + " " + hora, 'YYYY-MM-DD HH:mm:ss')
                #Convert to local GMT and formatting
                fechaHoraLocal = fechaHora.to('America/Mexico_City').format('DD-MM-YYYY,HH:mm:ss')

            except arrow.parser.ParserMatchError as e:
                #Cambio de estado de la bandera
                noValidData = True
                #Salida de la función
                return

            #Línea válida para el CSV
            datoLog = fechaHoraLocal + "," + lat + "," + lon

            #Cambio de estado de la bandera
            noValidData = False

            #Usr DEBUG
            print(datoLog)

    except pynmea2.ParseError as e:
        return

######### MAIN ###################################

#Iniciamos la UART
InitUart()

#Wrapper para el buffer a texto
usbWrp = io.TextIOWrapper(io.BufferedRWPair(usbCom, usbCom))

while True:
    #Control de errores
    try:
        #Feed hungry mounster
        gpsNewMsg = usbWrp.readline()

        #Get gps data
        GpsGetData(gpsNewMsg)

    except(KeyboardInterrupt):
        print(">> Interrupción del teclado...")
        break