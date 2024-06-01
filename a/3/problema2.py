#Crear un programa que permita al usuario elegir 
#un candidato por el cual votar. Las posibilidades 
#son: candidato A por el partido rojo, candidato B 
#por el partido verde, candidato C por el partido azul. 
#Según el candidato elegido (A, B ó C) se le debe imprimir 
#el mensaje “Usted ha votado por el partido [color que 
#corresponda al candidato elegido]”. Si el usuario ingresa 
#una opción que no corresponde a ninguno de los candidatos 
#disponibles, indicar “Opción errónea”.

A="rojo"
B="azul"
C="azul"

candidato=input("Por Que partido desea votar: ")

if(candidato == A):
    print(f"Usted ha votado por el partida {A}")
elif(candidato == B):
    print(f"Usted ha votado por el partida {B}")
elif(candidato == C):
    print(f"Usted ha votado por el partida {C}")
else:
    print("Opción errónea")