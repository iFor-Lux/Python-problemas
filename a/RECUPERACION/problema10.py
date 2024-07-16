#rear un algoritmo que pida dos numeros 
#enteros si la diferencia de ambos numeros 
#es un numero primo menor de 10 mostrar 
#por pantalla el producto de los dos numeros.


#Pedimos el primer numero

numero1 = int(input("Coloca tu primer numero: "))

#Pedimos el segundo numero

numero2 = int(input("Coloca tu segundo numero: "))

#Realizamos la operacion

diferencia = abs(numero1 - numero2)

#Mostramos el resultado

print(f"El resultado es: {diferencia}")
