#En esta clase sera donde manejaremos lo principal, lo cual es el Producto, detalleventa, y venta

from dataclasses import dataclass
from typing import List

#Clase de Producto con sus correspectivos campos
@dataclass
class Producto:
    codigo: str
    nombre: str
    precio: float #$USD
    unidad: str 

#Clase de Detalle ventas que obtiene productos + su precio y todos los detalles de la venta
@dataclass
class DetalleVenta:
    producto: Producto
    cantidad: float

    @property
    def subtotal(self) -> float:
        return self.cantidad * self.producto.precio
    

#Clase Venta en esa se ira enlistando para la clase detalle Ventas
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