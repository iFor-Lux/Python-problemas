#Escribe un programa que pida al usuario que ingrese un mes (1-12) y luego imprima la temporada correspondiente ( verano - otoño - invierno - primavera )

mes = int(input("Ingresa un mes: "))

if mes == 1 or mes == 2 or mes == 12:
    print("El mes colocado es Invierno")
elif mes == 3 or mes == 4 or mes == 5:
    print("El mes colocado es Primavera")
elif mes == 6 or mes == 7 or mes == 8:
    print("El mes colocado es Verano")
elif mes == 9 or mes == 10 or mes == 11:
    print("El mes colocado es Otono")
else:
    print("El mes colocado es invalido")