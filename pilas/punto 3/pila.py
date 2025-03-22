class Pila:
    def __init__(self):
        # Inicializa una lista vacía para representar la pila
        self.pila = []  

    def push(self, elemento:str): 
        # Agrega un elemento al final de la lista (cima de la pila)
        self.pila.append(elemento)
        print("Elemento agregado a la pila.")

    def pop(self): 
        # Elimina y muestra el último elemento agregado (LIFO)
        if self.pila:
            print("Elemento eliminado:", self.pila.pop())
        else:
            print("Error: La pila está vacía.")

    def peek(self): 
        # Muestra el elemento en la cima sin eliminarlo
        if self.pila:
            print("Elemento en la cima:", self.pila[-1])
        else:
            print("Error: La pila está vacía.")

    def is_empty(self): 
        # Verifica si la pila está vacía
        if not self.pila:
            print("La pila está vacía.")
        else:
            print("La pila NO está vacía.")


# Creación de una instancia de la clase Pila
pila = Pila()

# Menú interactivo para manejar la pila
while True:
    print("\n------ Menú de Pila ------")
    print("1. Insertar elemento (push)")
    print("2. Eliminar elemento (pop)")
    print("3. Ver elemento superior (peek)")
    print("4. Verificar si la pila está vacía (isEmpty)")
    print("5. Salir")
    
    # Solicita al usuario una opción
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Agrega un elemento ingresado por el usuario
        elemento = input("Ingrese el elemento a agregar: ")
        pila.push(elemento)
    elif opcion == "2":
        # Elimina el elemento en la cima de la pila
        pila.pop()
    elif opcion == "3":
        # Muestra el elemento en la cima de la pila sin eliminarlo
        pila.peek()
    elif opcion == "4":
        # Verifica si la pila está vacía
        pila.is_empty()
    elif opcion == "5":
        # Sale del programa
        print("Saliendo del programa...")
        break
    else:
        # Manejo de opción inválida
        print("Opción inválida, intente de nuevo.")
