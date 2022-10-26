# Escribir un programa que muestre el eco de lo que el usuario introduzca hasta que el usuario escriba “salir”
# que terminará.

while True:
    texto = input("Introduce texto para que se muestre por pantalla o 'salir' para terminar: ")
    if texto == "salir":
        break
    print(texto)
