# Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error.

primerNum = int(input("Introduce el primer número:"))
segundoNum = int(input("Introduce el segundo número:"))

if (segundoNum == 0):
    print("ERROR, El divisor no puede ser 0")
else:
    division = primerNum / segundoNum
    print(division)

