temperature = []
cont = 0
cantidad = int(input("ingresa cuantas temperaturas vas a registrar"))
for n in range (cantidad):
    temp = int(input("Ingrese la temperatura"))
    temperature.append(temp)
    cont += temp

prom = cont/cantidad
print(prom)
if prom < 20:
    print("Hacer revision")
elif prom > 30:
    print("Hacer revision")
else:
    print ("La temperatura es correcta")


