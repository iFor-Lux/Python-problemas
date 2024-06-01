#Crear un algoritmo que pida dos 
#números y compare si el primer 
#numero es mayor, el mensaje por 
#terminal será True o False según sea el caso

#Primero pedimos los 2 numeros
numero1=int(input("Numero 1 : "))
numero2=int(input("Numero 2 : "))

#Aqui comparamos ambos numeros si el primero es mayor que el segundo
resultado=numero1 > numero2

#Una vez obtenido los resultados lo mostramos
print(f"""
      -Entonces {numero1} es mayor que {numero2} ?
      
      -El resultado es : {resultado}
      """)

#True : Verdadero
#False : Falso