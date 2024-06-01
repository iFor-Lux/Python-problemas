#Crea un algoritmo que pida el precio 
#de un producto y me muestre por 
#terminal el 18% del producto ingresado


#Pedimos el precio del producto
precio = int(input("Precio del producto: s/."))

#Calculamos el 18% del precio
porcentaje = int(precio * 0.18)

#Mostramos el resultado
print(f"""
      El 18% del precio del producto es de: s/.{porcentaje}
      """)
