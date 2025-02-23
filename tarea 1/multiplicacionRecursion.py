def multiplicacion(a, b):
    if b == 0:
        return 0
    if b < 0:
        return -multiplicacion(a, -b)
    return a + multiplicacion(a, b - 1)

resultado = multiplicacion(5, 3)
print("El resultado es:", resultado)
