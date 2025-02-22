numeros=list()
cont = 0
cantidad = int(input("ingresa cantidad de numeros que va a digitar: "))
for n in range (cantidad):
    num = int(input("Ingrese el numero: "))
    numeros.append(num)
    cont += num
print("Lista de números ingresados:", numeros)
print("Suma total:", cont)