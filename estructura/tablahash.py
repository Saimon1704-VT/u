class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar(self, nombre, telefono):
        self.contactos[nombre] = telefono
        print(f"\nContacto agregado: {nombre} → {telefono}")

    def buscar(self, nombre):
        if nombre in self.contactos:
            print(f"\n{nombre}: {self.contactos[nombre]}")
        else:
            print("\nContacto no encontrado.")

    def eliminar(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            print(f"\nContacto {nombre} eliminado.")
        else:
            print("\nContacto no encontrado.")

    def listar(self):
        if self.contactos:
            print("\nLista de contactos:")
            for nombre, telefono in self.contactos.items():
                print(f"   {nombre}: {telefono}")
        else:
            print("\nNo hay contactos guardados.")

agenda = Agenda()

while True:
    print("\n1) Agregar  2) Buscar  3) Eliminar  4) Listar  5) Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '5':
        print("Saliendo...")
        break
    elif opcion == '1':
        agenda.agregar(input("Nombre: "), input("Teléfono: "))
    elif opcion == '2':
        agenda.buscar(input("Nombre: "))
    elif opcion == '3':
        agenda.eliminar(input("Nombre: "))
    elif opcion == '4':
        agenda.listar()
    else:
        print("Opción no válida.")
