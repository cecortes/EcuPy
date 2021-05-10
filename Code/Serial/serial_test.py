#Importamos las librerías necesarias
import serial

#Variables Globales
comSer = serial.Serial('COM3')  #Para el caso de Linux '/dev/ttyUSB0' or '/

#Reset buffer
comSer.flushInput()

while True:
    try:
        ser_bytes = comSer.readline()
        print(ser_bytes)
    except:
        print("Interrupción del teclado")
        break
