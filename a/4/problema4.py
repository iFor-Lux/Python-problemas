#Escribe un programa que pida al usuario que ingrese las longitudes de los lados de un triangulo y ingrese las longitudes de los lados de un triangulo y luego imprima si es equilatero , ososceles o escaleno

lado1 = int(input("Coloque la longitud del lado 1: "))
lado2 = int(input("Coloque la longitud del lado 2: "))
lado3 = int(input("Coloque la longitud del lado 3: "))

if lado1 == lado2 == lado3:
    print("El triangulo Es equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triangulo Es isoceles")
else:
    print("El triangulo Es escaleno")