#Crear un algoritmo que pida tres numeros y me 
#muestre cual es el numero mayor


#Pedimos el primer numero

numero1 = int(input("Coloca tu primer numero: "))

#Pedimos el segundo numero

numero2 = int(input("Coloca tu segundo numero: "))

#Pedimos el tercer numero

numero3 = int(input("Coloca tu tercer numero: "))

#Realizamos la operacion

mayor = max(numero1, numero2, numero3)

#Mostramos el resultado

print(f"El resultado es: {mayor}")
