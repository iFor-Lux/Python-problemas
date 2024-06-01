#Crear un algoritmo que solicite al 
#usuario ingresar un número con decimales 
#y almacenarlo en una variable. A continuación, 
#el programa debe solicitar al usuario que ingrese 
#un número entero y guardarlo en otra variable. 
#En una tercera variable se deberá guardar el 
#resultado de la suma de los dos números 
#ingresados por el usuario. Por último, 
#se debe mostrar en pantalla el texto “El 
#resultado de la suma es [suma]”, donde 
#“[suma]” se reemplazará por 
#el resultado de la operación.


#Pedimos el primer numero decimales

numero1 = float(input("Ingresa un numero con decimales: ")) #float es para decimales

#Pedimos el segundo numero entero

numero2 = int(input("Ingresa un numero entero: ")) #int es para enteros

#Sumamos los dos numeros

suma = numero1 + numero2

#Mostramos el resultado de la suma

print(f"El resultado de la suma es {suma}")