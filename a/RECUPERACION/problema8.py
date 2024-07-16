#Crear un algoritmo que pida dos numeros enteros y 
#me determine la diferencia de numeros que existe entre ellos

#Pedimos el primer numero

numero1 = int(input("Coloca tu primer numero: "))

#Pedimos el segundo numero

numero2 = int(input("Coloca tu segundo numero: "))

#Realizamos la operacion

diferencia = abs(numero1 - numero2)

#Mostramos el resultado

print(f"El resultado es: {diferencia}")