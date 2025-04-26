from typing import Union
from fastapi import FastAPI
from model.ticket import Ticket # Cambio en la ruta de importación, antes era 'from model import Ticket'
from controller.ticketController import TicketController # Cambio en la ruta, antes era 'from controller import TicketController'
from functions.queueFunctions import add_queue # Cambio en la ruta, antes era 'from functions import add_queue'
from typing import List # Importamos List de typing para especificar que usamos una lista de objetos Ticket

app = FastAPI()

ticketTypes = {
    "duda": TicketController(),
    "asesor": TicketController(),
    "caja": TicketController(),
    "otros": TicketController()
}

#--------------------------------------------------------------------------------------------

# Nuevo endpoint agregado para permitir la creación de múltiples tickets a la vez
@app.post("/ticketCreateSome")
def crear_turnos_some(turnos: List[Ticket]):
    errores = []  # Lista para almacenar errores
    exitos = 0  # Contador de tickets agregados correctamente

    for turno in turnos:
        resultado = add_queue(turno, ticketTypes)  # Llamamos a la función add_queue
        if "error" in resultado:  # Si la función devuelve un error
            errores.append(resultado["error"])  # Guardamos el error en la lista
        else:
            exitos += 1  # Si no hubo error, contamos el ticket como exitoso

    return {
        "mensaje": f"{exitos} tickets agregados correctamente",
        "errores": errores if errores else "Ningún error"
    }

#--------------------------------------------------------------------------------------------

# Endpoint para obtener el siguiente turno
@app.get("/ticketNext")
def obtener_siguiente_turno(): # Eliminado parámetro 'tipo', ahora se selecciona automáticamente el de mayor prioridad
    highest_priority_ticket = None
    highest_priority_type = None

    for type, queue in ticketTypes.items():
        if not queue.is_empty():
            candidate_ticket = queue.peek() # Se obtiene el primer ticket de la cola sin eliminarlo
            if highest_priority_ticket is None or candidate_ticket.priority_attention: # Se priorizan los tickets urgentes
                highest_priority_ticket = candidate_ticket
                highest_priority_type = type

    if highest_priority_ticket is None:
        return {"mensaje": "No hay tickets en ninguna cola."}
    
    ticketTypes[highest_priority_type].dequeue() # Se elimina el ticket de la cola después de seleccionarlo

    
    return {
        "mensaje": "El siguiente turno es",
        "datos_turno": {
            "name": highest_priority_ticket.name, 
            "identity": highest_priority_ticket.identity,  
            "age": highest_priority_ticket.age,  
            "priority_attention": highest_priority_ticket.priority_attention
        }
    }

#--------------------------------------------------------------------------------------------

# Endpoint para listar los turnos en cola por el tipo de turno
@app.get("/ticketList")
def listar_turnos_cola(): # Eliminado parámetro 'tipo' para listar todas las colas juntas

    queue = []

    for type, queue_controller in ticketTypes.items():
        current = queue_controller.head # Se recorre la lista enlazada de cada cola
        while current:
            queue.append({
                "name": current.data.name,
                "identity": current.data.identity,
                "age": current.data.age,
                "priority_attention": current.priority, # Se incluye la prioridad en la respuesta
                "tipo": type  # Se añade el tipo de ticket para más claridad en la respuesta
            })
            current = current.next

    # Ordenamos la lista por prioridad (los tickets con 'priority_attention' en True van primero)
    queue.sort(key=lambda x: x["priority_attention"], reverse=True)

    return {"mensaje": "Lista de todos los turnos en cola ordenados por prioridad", "datos_turnos": queue if queue else "No hay turnos en cola"}

#--------------------------------------------------------------------------------------------

# Otros endpoints existentes
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
