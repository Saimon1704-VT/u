class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y soy {self.genero}."

class CuentaBancaria:
    def __init__(self, titular, saldo, numeroDeCuenta):
        self.titular = titular
        self.saldo = saldo
        self.numeroDeCuenta = numeroDeCuenta

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= cantidad

    def consultarSaldo(self):
        return f"Saldo actual: {self.saldo}"

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2

    def calcular_circunferencia(self):
        return 2 * 3.1416 * self.radio

class Libro:
    def __init__(self, titulo, autor, genero, anoDePublicacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anoDePublicacion = anoDePublicacion

    def mostrarDetalles(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Año: {self.anoDePublicacion}"

class Cancion:
    def __init__(self, titulo, artista, album, duracion):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion

    def reproducir(self):
        print(f"Reproduciendo: {self.titulo} - {self.artista}")

class Producto:
    def __init__(self, nombre, precio, cantidadDisponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidadDisponible = cantidadDisponible

    def calcularTotal(self, cantidad):
        return self.precio * cantidad

class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def calcular_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones) if self.calificaciones else 0

    def determinar_estado(self):
        return "Aprobado" if self.calcular_promedio() >= 6 else "Reprobado"
    
persona = Persona("Carlos", 30, "Masculino")
print(persona.presentarse())

cuenta = CuentaBancaria(persona, 1000, "123456")
cuenta.retirar(200)
print(cuenta.consultarSaldo())

rectangulo = Rectangulo(5, 10)
print("Área del rectángulo:", rectangulo.calcular_area())

circulo = Circulo(7)
print("Área del círculo:", circulo.calcular_area())

libro = Libro("1984", "George Orwell", "Distopía", 1949)
print(libro.mostrarDetalles())

cancion = Cancion("Bohemian Rhapsody", "Queen", "A Night at the Opera", 5.55)
cancion.reproducir()

producto = Producto("Laptop", 800, 10)
print("Total por 3 unidades:", producto.calcularTotal(3))

estudiante = Estudiante("Ana", 20, "Matemáticas")
estudiante.agregar_calificacion(8)
estudiante.agregar_calificacion(7)
estudiante.agregar_calificacion(9)
print("Promedio del estudiante:", estudiante.calcular_promedio())
print("Estado del estudiante:", estudiante.determinar_estado())