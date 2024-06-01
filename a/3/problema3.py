#Crear un algoritmo que pida un numero entero y 
#determina con un operador de comparación si es 
#múltiplo de 10, mostrar por terminal  True de ser 
#verdadero y False si no es múltiplo.

numero = int(input("Coloca tu numero: "))

multiplo = numero % 10 == 0

print(multiplo)