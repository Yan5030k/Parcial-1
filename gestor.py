#Este módulo gestiona las ventas registradas y proporciona métodos para registrar ventas, 
#calcular los ingresos por producto y generar reportes.

from collections import defaultdict
from typing import Iterable
from modelos import Venta, Producto

#Clase GestorVentas: Gestiona el proceso de ventas, cálculos y reportes.
class GestorVentas:
    def __init__(self, catalogo: dict[str, Producto]):
        self.catalogo= catalogo #Obtenemos el catalogo de procutos guardado en al clase catalogo.py
        self.ventas: list[Venta] = [] #Lista para almacenar las ventas

    # Método para registrar una venta con los productos y cantidades proporcionados.
    def registrar_venta(self, vendedor: str, items: Iterable[tuple[str, float]]) -> Venta:
        venta = Venta(vendedor)  # Crea una nueva venta.
        for codigo, cantidad in items:
            prod = self.catalogo.get(codigo.upper())
            if prod is None:
                raise ValueError(f"Código de producto inválido: {codigo}")
            if cantidad <= 0:
                raise ValueError(f"La cantidad debe ser mayor a 0 (recibido: {cantidad})")
            venta.agregar_item(prod, cantidad)  # Agrega el ítem (producto) a la venta.
        self.ventas.append(venta)  # Guarda la venta en la lista de ventas.
        return venta

    # Método que calcula los ingresos totales por producto (por ventas registradas).
    def ingresos_por_producto(self) -> list[dict]:
        resumen = defaultdict(lambda: {"producto": None, "cantidad": 0.0, "ingreso": 0.0})
        for v in self.ventas:
            for d in v.detalles:
                rec = resumen[d.producto.codigo]  # Obtiene el resumen del producto.
                rec["producto"] = d.producto
                rec["cantidad"] += d.cantidad  # Suma la cantidad vendida.
                rec["ingreso"] += d.subtotal  # Suma el ingreso del producto.
        return list(resumen.values())  # Retorna el resumen de los productos.

    # Método para calcular el total general de todas las ventas registradas.
    def total_general(self) -> float:
        return sum(v.total() for v in self.ventas)  # Suma el total de todas las ventas.
    
    #Metodo para ordenar los productos por "ingreso" o por "cantidad" de mayor a menor.
    def ordenar_resumen(self, por: str = "ingreso", descendente: bool = True) -> list[dict]:
        datos = self.ingresos_por_producto()
        clave = "ingreso" if por.lower() == "ingreso" else "cantidad"  # Define la clave de ordenamiento.
        return sorted(datos, key=lambda r: r[clave], reverse=descendente)  # Ordena los datos.