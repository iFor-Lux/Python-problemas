#Crear un algoritmo que pida el precio de 
#dos productos multiplicarlos por 2 y 
#mostrar por terminal la suma de ambos


#Primero solitamos los precios de los 2 productos y lo almacenamos en producto1 y producto2

producto1 = int(input("precio del producto: s/."))
producto2 = int(input("precio del producto: s/."))

#Ahora lo que haremos sera multiplicar los datos almacenamos * 2 y lo almacanamos en multi1 y multi2

multi1 = producto1 * 2
multi2 = producto2 * 2

#Como ultimo sumamos los resultados obtenidos de multi1 y multi2 y usamos una variable con el nombre de suma

suma = multi1 + multi2

#Ahora solo mostramos los resultados en la terminal acompañando con una string para dar mas entendimiento al resultado y {} para mostrar las variables

print(f"""
      
      - Si multiplicamos ( s/.{producto1} * 2 ) nos da como resultado s/.{multi1}
      
      - De igual manera si multiplicamos ( s/.{producto2} * 2 ) nos da como resultado s/.{multi2}
      
      - Si a estos 2 resultados lo sumamos nos da como resultado s/.{suma}
      
      """)