# Los alumnos de Hogwarts se han dividido en dos casas, Gryffindor y Slytherin, de acuerdo al sexo y el nombre.
# Gryffindor está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N
# y Slytheryn por el resto. Escribir un programa que pregunte al usuario su nombre y sexo,
# y muestre por pantalla el grupo que le corresponde.

sexo = str(input("Introduce tu sexo (H/M)"))
nombre = str(input("Introduce tu nombre:"))

letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in letras:
    if sexo.upper() == "M" and nombre[0].upper() < letras[12]:
        print("Perteneces al grupo Gryffindor ")
        break
    if sexo.upper() == "H" and nombre[0].upper() > letras[12]:
        print("Perteneces al grupo Gryffindor ")
        break
    else:
        print("Perteneces al grupo Slytherin")
        break

