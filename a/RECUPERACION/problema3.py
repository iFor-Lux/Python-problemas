#Crear un algoritmo que pida tres numeros y 
#determine si uno de ello es multiplo de uno de los otros numeros


#Pedimos el primer numero

numero1 = int(input("Coloca tu primer numero: "))

#Pedimos el segundo numero

numero2 = int(input("Coloca tu segundo numero: "))

#Pedimos el tercer numero

numero3 = int(input("Coloca tu tercer numero: "))

#Realizamos la operacion

multiplo = (numero1 % numero2 == 0) or (numero1 % numero3 == 0) or (numero2 % numero3 == 0)

#Mostramos el resultado

print(f"El resultado es: {multiplo}")