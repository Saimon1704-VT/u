from typing import Optional

class Node:
    def __init__(self, data:int)-> None:
        self.data = data
        self.next: Optional["Node"] = None

class ListaEnlazada:
    def __init__ (self) -> None:
        self.cabeza: Optional["Node"] = None

    def agregar(self, data:int):
        nodo: Node = Node(data)
        if self.cabeza is None:
            self.cabeza = nodo
        else:
            nodoActual = self.cabeza
            self.cabeza = nodo
            while nodoActual.next is not None:
                nodoActual = nodoActual.next
            nodoActual.next = nodo
            print (ListaEnlazada())

lista = ListaEnlazada()
lista.agregar(5)
lista.agregar(10)
lista.agregar(15)
lista.agregar(20)