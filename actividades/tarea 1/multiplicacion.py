def multiplicar():
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    resultado = 0
    for i in range(b):
        resultado = resultado + a
    print("El resultado es:", resultado)

multiplicar()