#Crear un algoritmo que me cree una 
#calculadora de descuentos, pedira 
#el nombre del producto y su precio, 
#el descuento que se le aplicara sera 
#del 24%, mostrara por terminal el nombre 
#del producto su precio real y el 
#precio menos el descuento.


#Pedimos el nombre del producto y el precio

nombre = input("Coloca el nombre del producto: ")
precio = int(input("Coloca el precio del producto: s/."))

#Calculamos el descuento de 24%

descuento = precio * 0.24

#Mostramos el resultado

print(f"""
    El nombre del producto es: {nombre}
    El precio del producto es: s/.{precio}
    El precio con descuento es: s/.{descuento}
    """)