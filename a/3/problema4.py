#Escribir un programa que solicite al usuario una letra y, 
#si es una vocal, muestre el mensaje “es vocal”. Se debe validar 
#que el usuario ingrese sólo un carácter. Si ingresa un string de más 
#de un carácter, informarle que no se puede procesar el dato.

letra = input("Ingresa una letra: ")

if(len(letra) == 1):
    if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print("Es vocal")
    else:
        print("No es vocal")
else:
    print("No se puede procesar el dato")