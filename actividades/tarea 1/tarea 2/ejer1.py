class Vehiculo:

    combustible:int
    marca:str
    tipo:str

    def __init__(self, marca:str, combustible:int, tipo:str) -> None:
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo

    def __str__(self) -> str:
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Combustible: {self.combustible} galones"

    def encender(self):
        if self.combustible < 10:
            return("El vehiculo tiene un nivel bajo de gasolina")
        else:
            return("El vehiculo tiene un nivel adecuado de gasolina")

    def arrancar(self):
        print(f"{self.marca}: Arrancando el vehículo...")

    def conducir(self, distancia):
        consumo = distancia * 0.05  
        self.combustible -= consumo
        if self.combustible <= 0:
            self.combustible = 0
            print(f"{self.marca}: Se ha agotado el combustible. Deteniendo el vehículo.")
        elif self.combustible < 10:
            print(f"{self.marca}: Necesita ir a la gasolinera. Nivel de combustible muy bajo.")
        else:
            print(f"{self.marca}: Conduciendo {distancia} km. Combustible restante: {self.combustible} galones.")

class Moto(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible, "Moto")

class Carro(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible, "Carro")

moto = Moto("Honda", 10)
carro = Carro("Toyota", 30)

print(moto)
moto.encender()
moto.conducir(50)
moto.conducir(30)
moto.conducir(20)

print(carro)
carro.encender()
carro.conducir(100)
carro.conducir(200)
carro.conducir(50)