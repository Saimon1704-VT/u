from model.ticket import Ticket  # Importamos la clase Ticket desde el módulo model.
from model.node import Node  # Importamos la clase Node desde el módulo model.

class TicketController:
    def __init__(self) -> None:
        # Inicializamos la cola con la cabeza en None (vacía).
        self.head = None
    
    def is_empty(self) -> bool:
        # Verificamos si la cola está vacía.
        return self.head is None
    
    def enqueue(self, ticket: Ticket) -> None:
        # Si la prioridad del ticket no está definida, la establecemos en True si la edad es >= 60.
        if ticket.priority_attention is None:
            ticket.priority_attention = ticket.age >= 60

        # Creamos un nuevo nodo con el ticket y su prioridad.
        node = Node(ticket, ticket.priority_attention)
        
        # Si la cola está vacía, el nuevo nodo será la cabeza.
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            
            # Si el nuevo nodo tiene mayor prioridad, lo colocamos al inicio.
            if current.priority < node.priority:
                node.next = current
                self.head = node
            else:
                # Recorremos la cola para insertar el nodo en la posición correcta.
                while current.next is not None and current.next.priority > node.priority:
                    current = current.next
                node.next = current.next
                current.next = node
        
        # Imprimimos el mensaje de confirmación.
        print(f"Turno {ticket.name} agregado con prioridad {ticket.priority_attention}")
      
    def dequeue(self) -> Ticket:
        # Si la cola está vacía, retornamos None.
        if self.is_empty():
            return None
        else:
            # Extraemos el ticket de la cabeza y movemos la cabeza al siguiente nodo.
            ticket = self.head.data
            self.head = self.head.next
            return ticket
        
    def peek(self) -> Ticket:
        # Retornamos el primer ticket en la cola sin eliminarlo.
        return None if self.is_empty() else self.head.data
