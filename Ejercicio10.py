# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


contraseña = "contraseña01"

for i in contraseña:
    contraseñaIntroducida = input("Introduce una contraseña")
    if contraseñaIntroducida == contraseña.lower():
        print("La contraseña es valida")
        break
    else:
        print("La contraseña no es valida")