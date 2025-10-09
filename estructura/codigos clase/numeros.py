numeros= list()
swiche: bool = True
def agregar (numero:int) -> None:
    numeros.append (numero)
def eliminar () -> None:    
    numeros.pop ()
while swiche:
    print ("Menu de operaciones")
    print ("Digite 1 para agregar numero: ")
    print ("Digite 2 para eliminar numero: ")
    print ("Digite 3 para ver lista de numeros: ")
    print ("Digite 4 para salir")
    opcion = int(input("#: "))
    if opcion == 1:
        numero= int(input("Digite el numero que desea agregar: "))
        agregar (numero)
    elif opcion == 2:
        numero= int(input("Digite el numero que desea eliminar: "))
        eliminar ()
    elif opcion == 3:
        print ("Lista de numeros: ",numeros)
    elif opcion == 4:
        print ("Finalizando...")
        break
        swiche=0
    else:
        print ("Debe elegir un numero del 1 al 4")
