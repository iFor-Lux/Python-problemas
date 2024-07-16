#Crear un algoritmo que pida un numero 
#entero y determine si es multiplo de 7


#Pedimos el numero

numero = int(input("Coloca tu numero: "))

#Realizamos la operacion

multiplo = numero % 7 == 0

#Mostramos el resultado

print(f"El resultado es: {multiplo}")
