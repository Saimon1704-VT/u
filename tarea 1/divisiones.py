def dividir(a, b)->float:
    if b == 0:
        return "Error"
    cociente = 0
    while a >= b:
        a = a-b
        cociente =cociente+ 1
    return cociente + a / b

print("Ingresa el dividendo: ")
a = int(input())
print("Ingresa el divisor: ")
b = int(input())

print("El resultado es:",round(dividir(a,b),3))