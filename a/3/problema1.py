#Requerir al usuario que ingrese un día de la 
#semana e imprimir un mensaje si es lunes, otro 
#mensaje diferente si es viernes, otro mensaje 
#diferente si es sábado o domingo. Si el día ingresado 
#no es ninguno de esos, imprimir otro mensaje.

lunes="Lunes que aburrido"
martes="Hola mundo"
miercoles="Hola mundo"
jueves="Hola mundo"
viernes="Viernes que bien"
sabado="Sabado de pelicula"
domingo="Domingo de Fiesta xD"

dia=input("Ingresa un dia de la semana : ")

if(dia == "lunes"):
    print(lunes)
elif(dia == "martes"):
    print(martes)
elif(dia == "miercoles"):
    print(miercoles)
elif(dia == "jueves"):
    print(jueves)
elif(dia == "viernes"):
    print(viernes)
elif(dia == "sabado"):
    print(sabado)
elif(dia == "domingo"):
    print(domingo)
else:
    print("No es ningun dia de la semana")