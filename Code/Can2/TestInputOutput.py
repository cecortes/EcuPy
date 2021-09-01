#Entrada estándar
#print("Esperando opciones de usuario: ")
#opt = input()
#Salida estándar
#print("Opción: ", opt)

#Entrada con argumentos
import sys

#Muestra los argumentos que pasan al programa
print(sys.argv)

if sys.argv[1] == "mostrar":
    texto = sys.argv[2]
    print("mostrar", texto)
else:
    print("El primer argumento no es mostrar")