class Animal:
    # Representa un animal con nombre, edad y tipo
    def __init__(self, nombre: str, edad: int, tipoAnimal: str):
        self.nombre = nombre
        self.edad = edad
        self.tipoAnimal = tipoAnimal  
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Tipo de Animal: {self.tipoAnimal}"

class Node:
    def __init__(self, data: Animal) -> None:
        self.data = data
        self.next = None  # Apunta al siguiente nodo en la lista

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicio de la lista enlazada
        
    def agregar_animal(self, animal: Animal) -> None:
        nodo = Node(animal)
        if self.cabeza is None:
            self.cabeza = nodo  # Si la lista está vacía, el nuevo nodo es la cabeza
        else:
            actual = self.cabeza
            while actual.next:
                actual = actual.next
            actual.next = nodo  # Agregar al final de la lista

# Solicita los datos del animal al usuario
nombre = input("Ingrese el nombre del animal: ")
edad = int(input("Ingrese la edad del animal: "))
tipoAnimal = input("Ingrese el tipo de animal: ")

# Crea un objeto Animal con los datos ingresados
animal = Animal(nombre, edad, tipoAnimal)

# Muestra la información del animal
print(animal)
