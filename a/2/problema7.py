#Crear un algoritmo que solicite dos 
#números y los almacene en dos variables. 
#En otra variable, almacena el resultado 
#de la suma de esos dos números y luego 
#muestra ese resultado en pantalla.
#Luego el programa debe solicitar al 
#usuario que ingrese un tercer número, el 
#cual se debe almacenar en una nueva variable. 
#Por último, muestra en pantalla el resultado de la 
#multiplicación de este nuevo número por 
#el resultado de la suma anterior.

#**Ejemplo solución**

#Ingresa un número: 1
#Ingresa otro número: 2
#Suman: 3
#Ingresa un nuevo número: 3
#Multiplicación de la suma por el último número: 9


#Pedimos el primer numero

numero1 = int(input("Ingresa un número: "))

#Pedimos el segundo numero

numero2 = int(input("Ingresa otro número: "))

#Sumamos los dos numeros

suma = numero1 + numero2

#Mostramos el resultado de la suma

print(f"El resultado de la suma es: {suma}")

#Pedimos el tercer numero

numero3 = int(input("Ingresa un nuevo número: "))

#Multiplicamos la suma por el nuevo numero

multiplicacion = suma * numero3

#Mostramos el resultado de la multiplicacion

print(f"Multiplicación de la suma por el nuevo número es: {multiplicacion}")