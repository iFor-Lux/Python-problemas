#Crea un algoritmo que solicite al 
#usuario ingresar la cantidad de kilómetros 
#recorridos por una motocicleta y la cantidad 
#de litros de combustible que consumió
#durante ese recorrido. Mostrar el consumo
#de combustible por kilómetro.


#Pedimos los datos

kilometros = int(input("Kilómetros recorridos: "))
litros = int(input("Litros de combustible consumidos: "))

#Calculamos el consumo

consumo = kilometros / litros

#Mostramos el resultado

print(f"Consumo de combustible por kilómetro: {consumo}")
