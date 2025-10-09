import time
from collections import deque   # Usamos deque para manejar la cola FIFO

class SistemaArchivos:
    def __init__(self, tamano_disco=50):
        # El disco tiene 50 MB por defecto
        self.tamano_disco = tamano_disco
        self.disco = [None] * tamano_disco     # Cada posición representa 1 MB del disco
        self.cola = deque()                    # Cola FIFO para los archivos
        self.archivos = {}                     # Guarda nombre del archivo y su tamaño

    # Funciones internas del sistema
    
    def espacio_libre(self):
        # Cuenta cuántos MB del disco están libres.
        return self.disco.count(None)

    def crear_archivo(self, nombre, tamano):
        # Crea un archivo si hay espacio y no existe otro igual.
        if nombre in self.archivos:
            print(f"Ya existe un archivo llamado '{nombre}'.")
            return

        if tamano > self.espacio_libre():
            print(f"No hay suficiente espacio. Solo quedan {self.espacio_libre()} MB libres.")
            return

        # Asignar espacio en el disco
        ocupados = 0
        for i in range(len(self.disco)):
            if self.disco[i] is None:
                self.disco[i] = nombre
                ocupados += 1
                if ocupados == tamano:
                    break

        # Guardar el archivo en las estructuras
        self.archivos[nombre] = tamano
        self.cola.append(nombre)
        print(f"Archivo '{nombre}' creado ({tamano} MB). Espacio libre: {self.espacio_libre()} MB")

    def eliminar_mas_antiguo(self):
        # Elimina el archivo más antiguo (FIFO).
        if not self.cola:
            print("No hay archivos para eliminar.")
            return

        nombre = self.cola.popleft()
        self._liberar_espacio(nombre)
        print(f"Archivo '{nombre}' eliminado (más antiguo). Espacio libre: {self.espacio_libre()} MB")

    def eliminar_por_nombre(self, nombre):
        # Elimina un archivo específico por su nombre.
        if nombre not in self.archivos:
            print(f"No existe un archivo llamado '{nombre}'.")
            return

        if nombre in self.cola:
            self.cola.remove(nombre)
        self._liberar_espacio(nombre)
        print(f"Archivo '{nombre}' eliminado correctamente. Espacio libre: {self.espacio_libre()} MB")

    def _liberar_espacio(self, nombre):
        # Libera el espacio del disco ocupado por el archivo dado.
        for i in range(len(self.disco)):
            if self.disco[i] == nombre:
                self.disco[i] = None
        self.archivos.pop(nombre)

    # Funciones de visualización
    
    def mostrar_archivos(self):
        # Muestra todos los archivos guardados y su tamaño.
        print("\nArchivos almacenados:")
        if not self.archivos:
            print("   (No hay archivos guardados)")
        else:
            for i, (nombre, tamano) in enumerate(self.archivos.items(), start=1):
                print(f"   {i}. {nombre} - {tamano} MB")

    def mostrar_estado(self):
        # Muestra el estado general del disco.
        usados = self.tamano_disco - self.espacio_libre()
        print(f"\nEspacio usado: {usados}/{self.tamano_disco} MB  |  Libres: {self.espacio_libre()} MB\n")

    # Menú principal

    def menu(self):
        print("Simulador de Espacio en Disco\n")
        while True:
            self.mostrar_estado()
            print("1. Crear archivo")
            print("2. Eliminar archivo más antiguo")
            print("3. Eliminar archivo por nombre")
            print("4. Ver archivos guardados")
            print("5. Salir\n")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Nombre del archivo: ")
                try:
                    tamano = int(input("Tamaño en MB: "))
                    self.crear_archivo(nombre, tamano)
                except ValueError:
                    print("Ingrese un número válido.")
            elif opcion == "2":
                self.eliminar_mas_antiguo()
            elif opcion == "3":
                nombre = input("Nombre del archivo a eliminar: ")
                self.eliminar_por_nombre(nombre)
            elif opcion == "4":
                self.mostrar_archivos()
            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

            time.sleep(1)


if __name__ == "__main__":
    sistema = SistemaArchivos()
    sistema.menu()
