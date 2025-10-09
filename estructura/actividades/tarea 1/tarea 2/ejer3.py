class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
    
    def trabajar(self):
        pass

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, equipo=[]):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo
    
    def trabajar(self):
        return f"{self.nombre} está supervisando al equipo."
    
    def supervisarAEquipo(self):
        return f"{self.nombre} está supervisando a {len(self.equipo)} empleados."

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguajeDeProgramacion):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion
    
    def trabajar(self):
        return f"{self.nombre} está escribiendo código en {self.lenguajeDeProgramacion}."


class FiguraGeometrica:
    def calcularArea(self):
        pass

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        return (self.base * self.altura) / 2

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado
    
    def calcularArea(self):
        return self.lado ** 2


class Electrodomestico:
    def __init__(self, marca, modelo, consumoEnergetico):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergetico = consumoEnergetico
    
    def encender(self):
        return "Encendiendo el electrodoméstico."

class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, consumoEnergetico, capacidad):
        super().__init__(marca, modelo, consumoEnergetico)
        self.capacidad = capacidad
    
    def encender(self):
        return "Iniciando el ciclo de lavado."

class Refrigerador(Electrodomestico):
    def __init__(self, marca, modelo, consumoEnergetico, tieneCongelador):
        super().__init__(marca, modelo, consumoEnergetico)
        self.tieneCongelador = tieneCongelador
    
    def encender(self):
        return "Regulando la temperatura."

class Usuario:
    def __init__(self, nombreDeUsuario, contraseña):
        self.nombreDeUsuario = nombreDeUsuario
        self.contraseña = contraseña
    
    def iniciarSesion(self, usuario, clave):
        return usuario == self.nombreDeUsuario and clave == self.contraseña

class Administrador(Usuario):
    def gestionarUsuarios(self):
        return "Gestionando usuarios del sistema."

class Cliente(Usuario):
    def realizarCompra(self):
        return "Realizando una compra."

if __name__ == "__main__":
    dev = Desarrollador("Carlos", 5000, "IT", "Python")
    gerente = Gerente("Ana", 7000, "IT", [dev])
    print(dev.trabajar())
    print(gerente.trabajar())
    print(gerente.supervisarAEquipo())
    
    tri = Triangulo(10, 5)
    cuad = Cuadrado(4)
    print(f"Área del triángulo: {tri.calcularArea()}")
    print(f"Área del cuadrado: {cuad.calcularArea()}")
    
    lav = Lavadora("LG", "X200", "A++", 10)
    ref = Refrigerador("Samsung", "R300", "A+", True)
    print(lav.encender())
    print(ref.encender())
    
    admin = Administrador("admin", "1234")
    cliente = Cliente("juan", "abcd")
    print(f"Inicio de sesión admin: {admin.iniciarSesion('admin', '1234')}")
    print(f"Inicio de sesión cliente: {cliente.iniciarSesion('juan', 'abcd')}")
    print(admin.gestionarUsuarios())
    print(cliente.realizarCompra())
