from abc import ABC, abstractmethod
 
# FACTORY METHOD 
class IProducto(ABC):

    @abstractmethod
    def obtener_descripcion(self) -> str:
        pass

    @abstractmethod
    def obtener_precio(self) -> float:
        pass

# Producto básico sin personalización.
class ProductoSimple(IProducto):
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio

    def obtener_descripcion(self) -> str:
        return f"Producto simple: {self.nombre}"

    def obtener_precio(self) -> float:
        return self.precio

# Producto que incluye costo adicional por personalización
class ProductoPersonalizable(IProducto):
    def __init__(self, nombre: str, precio_base: float, costo_extra: float) -> None:
        self.nombre = nombre
        self.precio_base = precio_base
        self.costo_extra = costo_extra

    def obtener_descripcion(self) -> str:
        return f"Producto personalizable: {self.nombre}"

    def obtener_precio(self) -> float:
        return self.precio_base + self.costo_extra

class FabricaDeProductos(ABC):
    # Clase abstracta que define la creación de productos.
    @abstractmethod
    def crear_producto(self, nombre: str, precio_base: float):
        pass

class FabricaProductoSimple(FabricaDeProductos):
    def crear_producto(self, nombre: str, precio_base: float):
        return ProductoSimple(nombre, precio_base)


class FabricaProductoPersonalizable(FabricaDeProductos):
    def crear_producto(self, nombre: str, precio_base: float, costo_extra: float):
        return ProductoPersonalizable(nombre, precio_base, costo_extra)


# DECORATOR
class IPedido(ABC):
    @abstractmethod
    def obtener_costo(self):
        pass

# Pedido base con un solo producto
class PedidoBase(IPedido):
    def __init__(self, producto: IPedido) -> None:
        self.producto = producto

    def obtener_costo(self) -> float:
        return self.producto.obtener_precio()

# Clase base para todos los decoradores
class DecoradorPedido(IPedido):
    def __init__(self, pedido: IPedido) -> None:
        self.pedido = pedido

    @abstractmethod
    def obtener_costo(self):
        pass


class DescuentoPorVolumen(DecoradorPedido):
    # Aplica un descuento al total
    def __init__(self, pedido: IPedido, porcentaje_descuento: float) -> None:
        super().__init__(pedido)
        self.porcentaje_descuento = porcentaje_descuento

    def obtener_costo(self) -> float:
        costo_original = self.pedido.obtener_costo()
        return costo_original * (1 - self.porcentaje_descuento / 100)


class ImpuestoDeLujo(DecoradorPedido):
    # Aplica un impuesto adicional al costo
    def __init__(self, pedido, porcentaje_impuesto: float) -> None:
        super().__init__(pedido)
        self.porcentaje_impuesto = porcentaje_impuesto

    def obtener_costo(self):
        costo_original = self.pedido.obtener_costo()
        return costo_original * (1 + self.porcentaje_impuesto / 100)

# STRATEGY

class EstrategiaDePago(ABC):
    @abstractmethod
    def pagar(self, monto) -> None:
        pass


class PagoConTarjeta(EstrategiaDePago):
    def pagar(self, monto: float) -> None:
        print(f"Pago con tarjeta por ${monto:,.0f} realizado.")


class PagoConPayPal(EstrategiaDePago):
    def pagar(self, monto: float) -> None:
        print(f"Pago con PayPal por ${monto:,.0f} realizado.")


# MOTOR DE PEDIDOS 
class MotorDePedidos:
    # Cliente que coordina las fábricas, decoradores y estrategias
    def __init__(self, estrategia_pago: EstrategiaDePago) -> None:
        self.estrategia_pago = estrategia_pago

    def procesar_pedido(self, pedido: IPedido) -> None:
        total = pedido.obtener_costo()
        print(f"Total del pedido: ${total:,.0f}")
        self.estrategia_pago.pagar(total)


if __name__ == "__main__":
    # Crear fábricas
    fabrica_simple = FabricaProductoSimple()
    fabrica_personalizada = FabricaProductoPersonalizable()

    # Crear productos
    producto1 = fabrica_simple.crear_producto("Mouse óptico", 50000)
    producto2 = fabrica_personalizada.crear_producto("Teclado mecánico", 150000, 30000)

    # Crear pedidos base
    pedido1 = PedidoBase(producto1)
    pedido2 = PedidoBase(producto2)

    # Aplicar decoradores
    pedido_con_descuento = DescuentoPorVolumen(pedido2, 10)
    pedido_con_impuesto = ImpuestoDeLujo(pedido_con_descuento, 5)

    # Configurar estrategia de pago
    estrategia = PagoConTarjeta()
    motor = MotorDePedidos(estrategia)

    # Procesar pedido
    motor.procesar_pedido(pedido_con_impuesto)
