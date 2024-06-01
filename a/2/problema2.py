#Crear un algoritmo que me me 
#pida el nombre, precio y unidades 
#de 5 productos y me muestre por 
#terminal el total de la venta


#Pedimos los datos de los 5 productos

nombre1 = input("Nombre del producto: ")
precio1 = int(input("Precio del producto: s/."))
unidades1 = int(input("Unidades del producto: "))
total1 = precio1 * unidades1

print("-----------------------------") #Este print sirve para separar los productos

nombre2 = input("Nombre del producto: ")
precio2 = int(input("Precio del producto: s/."))
unidades2 = int(input("Unidades del producto: "))
total2 = precio2 * unidades2

print("-----------------------------")

nombre3 = input("Nombre del producto: ")
precio3 = int(input("Precio del producto: s/."))
unidades3 = int(input("Unidades del producto: "))
total3 = precio3 * unidades3

print("-----------------------------")

nombre4 = input("Nombre del producto: ")
precio4 = int(input("Precio del producto: s/."))
unidades4 = int(input("Unidades del producto: "))
total4 = precio4 * unidades4

print("-----------------------------")

nombre5 = input("Nombre del producto: ")
precio5 = int(input("Precio del producto: s/."))
unidades5 = int(input("Unidades del producto: "))
total5 = precio5 * unidades5

print("-----------------------------")

#Calculamos el total de la venta

total_de_venta = total1 + total2 + total3 + total4 + total5

#Mostramos el resultado usando f para que se vea mas bonito

print(f"""
    
    -----------------------------
        TABLA DE PRECIOS
    -----------------------------
    
    PRODUCTO   /    PRECIO    /   PRECIOS
    
    {nombre1}  ( s/.{precio1} )  UNIDADES: {unidades1} = ( s/.{total1} )
    
    {nombre2}  ( s/.{precio2} )  UNIDADES: {unidades2} = ( s/.{total2} )
    
    {nombre3}  ( s/.{precio3} )  UNIDADES: {unidades3} = ( s/.{total3} )
    
    {nombre4}  ( s/.{precio4} )  UNIDADES: {unidades4} = ( s/.{total4} )
    
    {nombre5}  ( s/.{precio5} )  UNIDADES: {unidades5} = ( s/.{total5} )
    
    -----------------------------
    
    TOTAL DE LA VENTA : s/.{total_de_venta}
    
    """)