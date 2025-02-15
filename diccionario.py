persona = dict()
swiche: bool = True
def agregarValor (clave:str, valor:str):
    persona.update ({clave:valor})
def eliminarValor ():
    persona.popitem ()
while swiche:
    print ("Menu de operaciones")
    print ("Digite 1 para agregar persona")
    print ("Digite 2 para eliminar persona")
    print ("Digite 3 para ver lista")
    print ("Digite 4 para salir")
    opcion = int(input("#: "))
    if opcion == 1:
        clave = str(input("Digite clave: "))
        valor = str(input("Digite valor: "))
        agregarValor (clave, valor)
    elif opcion == 2:
        eliminarValor ()
    elif opcion == 3:
        print ("Lista", persona)
    elif opcion == 4:
        print ("Finalizando...")
        break
    else:
        print ("Elija un numero del 1 al 6")