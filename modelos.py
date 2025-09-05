from dataclasses import dataclass
from typing import List

@dataclass
class Producto:
    codigo: str
    nombre: str
    precio: float #$USD
    unidad: str 

print("Hellow word!")
@dataclass
class DetalleVenta:
    producto: Producto
    cantidad: float

    @property
    def subtotal(self) -> float:
        return self.cantidad * self.producto.precio
    

class Venta:
    _contador = 1

    def __init__(self, vendedor: str):
        self.id = Venta._contador
        Venta._contador += 1
        self.vendedor = vendedor
        self.detalles: List[DetalleVenta] = []

    def agregar_item(self, producto: Producto, cantidad: float) -> None:
        self.detalles.append(DetalleVenta(producto, cantidad))

    def total(self) -> float:
        return sum(d.subtotal for d in self.detalles)