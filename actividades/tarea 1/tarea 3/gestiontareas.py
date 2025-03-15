class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        # Cada tarea tiene una descripción, una prioridad y una fecha de vencimiento
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.siguiente = None  # Apunta a la siguiente tarea en la lista

    def __str__(self):
        return f"{self.descripcion} - Prioridad: {self.prioridad} - Vence: {self.fecha_vencimiento}"

class ListaEnlazada:
    def __init__(self):
        # Inicializa la lista enlazada sin tareas
        self.cabeza = None  
    
    def agregar_tarea(self, descripcion, prioridad, fecha_vencimiento):
        # Agrega una tarea a la lista manteniendo el orden según la prioridad
        nueva = Tarea(descripcion, prioridad, fecha_vencimiento)
        if self.cabeza is None:
            self.cabeza = nueva  # Si la lista está vacía, la nueva tarea es la primera
        elif prioridad < self.cabeza.prioridad:
            nueva.siguiente = self.cabeza  # Inserta la tarea al inicio si tiene mayor prioridad
            self.cabeza = nueva
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva  # Inserta la tarea al final si no hay prioridad mayor
    
    def mostrar_tareas(self):
        # Muestra todas las tareas almacenadas en la lista enlazada
        actual = self.cabeza
        while actual:
            print(actual)
            actual = actual.siguiente
    
    def eliminar_tarea(self, descripcion):
        # Busca y elimina una tarea por su descripción
        actual = self.cabeza
        previo = None
        while actual:
            if actual.descripcion == descripcion:
                if previo:
                    previo.siguiente = actual.siguiente  # Salta la tarea eliminada
                else:
                    self.cabeza = actual.siguiente  # Si es la primera tarea, mueve la referencia
                del actual
                return
            previo = actual
            actual = actual.siguiente

# Menú interactivo para gestionar tareas
lista = ListaEnlazada()
while True:
    print("\nGestor de Tareas")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        # Solicita los datos de la nueva tarea al usuario
        descripcion = input("Ingrese la descripción de la tarea: ")
        prioridad = int(input("Ingrese la prioridad (1 alta, 3 baja): "))
        fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
        lista.agregar_tarea(descripcion, prioridad, fecha_vencimiento)
    elif opcion == "2":
        # Muestra todas las tareas almacenadas en la lista
        lista.mostrar_tareas()
    elif opcion == "3":
        # Elimina una tarea específica ingresada por el usuario
        descripcion = input("Ingrese la descripción de la tarea a eliminar: ")
        lista.eliminar_tarea(descripcion)
    elif opcion == "4":
        # Sale del programa
        print("Saliendo del programa.")
        break
    else:
        # Mensaje de error si la opción ingresada no es válida
        print("Opción no válida, intente de nuevo.")
