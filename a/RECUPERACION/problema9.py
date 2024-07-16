#Crear un algoritmo que me pida dos 
#numeros enteros si la diferencia
#entre ambos numeros es par mostrar 
#la suma de ambos numeros


#Pedimos el primer numero

numero1 = int(input("Coloca tu primer numero: "))

#Pedimos el segundo numero

numero2 = int(input("Coloca tu segundo numero: "))

#Realizamos la operacion

diferencia = abs(numero1 - numero2)

#Mostramos el resultado

print(f"El resultado es: {diferencia}")
