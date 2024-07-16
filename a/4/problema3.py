#Crea un programa que pida al usuario que ingrese la distancia en kilometros y luego imprima la distancia en metros y en millas

kilometros = int(input("Coloque la distancia en Kilometros: "))

metros = kilometros * 1000

millas = kilometros / 1,609

print(f"La distancia en Metros es: {metros} y La distancia en Millas es: {millas}")