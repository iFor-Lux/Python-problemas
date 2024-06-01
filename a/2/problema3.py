#Crear un algoritmo que pida un numero 
#entero y determina con un operador de 
#comparación si es múltiplo de 10, mostrar 
#por terminal  True de ser verdadero 
#y False si no es múltiplo.


#Pedimos el numero

numero = int(input("Coloca tu numero: "))

#Realizamos la operacion

multiplo = numero % 10 == 0  # % es el operador de residuo

#Mostramos el resultado

print(f"El resultado es: {multiplo}")