#Crea un algoritmo que pida un número 
#entero y que luego imprima un valor de 
#verdad dependiendo de si el número es par 
#o no. Recordar que un número es par si 
#el resto, al dividirlo por 2, es 0.


#Pedimos el numero
numero = int(input("Ingresa un numero: "))

#Calculamos si es par

par = numero % 2 == 0

#Mostramos el resultado

print(par)