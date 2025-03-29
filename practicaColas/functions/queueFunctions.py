from model.ticket import Ticket
from controller.ticketController import TicketController

def add_queue(ticket: Ticket, ticketTypes: dict) -> dict:
    """
    Add a ticket to the queue, using the TicketController class to manage the queue.
    you need order the tickets by type and priority. (dudas, asesor, caja, otros)
    """
    opciones = {  # Definimos los tipos de tickets válidos.
        "duda",
        "caja",
        "asesor",
        "otros"
    }

    if ticket.type not in opciones:
        print(f"Error: Tipo de atención inválido '{ticket.type}'")  # Esto aparecerá en consola
        return {"error": "Tipo de atención inválido"}  # Esto se verá en Postman

    if ticket.type not in ticketTypes:
        print(f"Error: No existe una cola para el tipo de ticket '{ticket.type}'")  
        return {"error": f"No existe una cola para el tipo '{ticket.type}'"}

    ticketTypes[ticket.type].enqueue(ticket)
    return {"mensaje": f"Ticket de tipo '{ticket.type}' añadido correctamente"}





