#Desarrollar un programa que calcula el 
#voltaje que cae en una resistencia cuando
#los valores de la intensidad y la resistencia son conocidos.
#La Ley de Ohm nos indica que voltaje = intensidad * resistencia
#Ejemplo: Para un valor de la intensidad igual a 3 
#amperios y un valor de la resistencia de 4 
#ohmios el valor del voltaje es de 12 voltios.


#Pedimos los datos

intensidad = int(input("Coloca la intensidad: "))
resistencia = int(input("Coloca la resistencia: "))

#Calculamos el voltaje usando la formula : voltaje = intensidad * resistencia

voltaje = intensidad * resistencia

#Mostramos el resultado en voltios

print(f"El voltaje es de {voltaje} voltios")