"""
En El Salvador, los comerciantes de mercados locales desean llevar un
control organizado de sus ventas diarias. Cada venta incluye tipos variados
de productos con ciertas características y precios ya definidos. Sin un registro,
es difícil saber cuáles productos generan más ingresos y cómo planificar el
inventario de manera eficiente.
"""

#Este es el archivo principal donde se ejecuta la lógica del sistema.
# Aquí se presenta el menú al usuario y se orquestan las interacciones con los otros módulos.

from catalogo import catalogo_por_defecto, buscar_producto
from gestor import GestorVentas
from util import leer_opcion, leer_float_positivo, pausar

class App:
    def __init__(self):
        self.catalogo = catalogo_por_defecto()
        self.gestor = GestorVentas(self.catalogo)

#Menú unteractivo
    def ejecutar(self):
        while True:
            self._limpiar()
            print("-------Sistema de Ventas: Mercados de El Salvador (Hecho por Jhoan Ortega)-------")
            print("1) Ver catálogo")
            print("2) Registrar venta")
            print("3) Reporte: ordenar por INGRESO")
            print("4) Reporte: ordenar por CANTIDAD")
            print("5) Ver total general")
            print("0) Salir")
            opcion = leer_opcion("Elija una opción: ", {"0", "1", "2", "3", "4", "5"})

            if opcion =="1":
                self.mostrar_catalogo()
            elif opcion == "2":
                self.menu_registrar_venta()
            elif opcion == "3":
                self.mostrar_reporte(por="ingreso")
            elif opcion == "4":
                self.mostrar_reporte(por="cantidad")
            elif opcion == "5":
                self.mostrar_total_general()
            elif opcion == "0":
                print("¡Vuelva pronto!")
                break

    # ----------------- Menús / Acciones -----------------

    def mostrar_catalogo(self):
        self._limpiar()
        print("=== Catálogo de productos ===")
        print(f"{'COD':<4} {'Producto':<18} {'Precio(USD)':>11} {'Unidad':>8}")
        print("-"*45)
        for cod, p in self.catalogo.items():
            print(f"{cod:<4} {p.nombre:<18} {p.precio:>11.2f} {p.unidad:>8}")
        pausar()

    def menu_registrar_venta(self):
        self._limpiar()
        print("=== Registrar venta ===")
        vendedor = input("Nombre del vendedor/a: ").strip() or "N/D"
        items: list[tuple[str, float]] = []

        while True:
            print("\nIngresa un producto del catálogo (ej: TOM, CEB, ARR...).")
            cod = input("Código de producto (o ENTER para terminar): ").strip().upper()
            if cod == "":
                break
            prod = buscar_producto(self.catalogo, cod)
            if not prod:
                print("Código inválido. Revisa el catálogo (opción 1 del menú).")
                continue
            cantidad = leer_float_positivo(f"Cantidad en {prod.unidad} para {prod.nombre}: ")
            items.append((cod, cantidad))
            print(f"  + Agregado: {prod.nombre} x {cantidad} {prod.unidad}")

        if not items:
            print("No se agregaron productos. Venta cancelada.")
            pausar()
            return

        try:
            venta = self.gestor.registrar_venta(vendedor, items)
        except ValueError as e:
            print(f"Error al registrar venta: {e}")
            pausar()
            return

        # Resumen de la venta
        print("\n--- Venta registrada ---")
        print(f"ID Venta: {venta.id} | Vendedor: {venta.vendedor}")
        print(f"{'Producto':<18} {'Cant.':>8} {'PU':>8} {'Subtotal':>10}")
        print("-"*50)
        for d in venta.detalles:
            print(f"{d.producto.nombre:<18} {d.cantidad:>8.2f} {d.producto.precio:>8.2f} {d.subtotal:>10.2f}")
        print("-"*50)
        print(f"{'TOTAL':>42} {venta.total():>8.2f} USD")
        pausar()

    def mostrar_reporte(self, por: str):
        self._limpiar()
        if not self.gestor.ventas:
            print("Aún no hay ventas registradas.")
            pausar()
            return

        titulo = "INGRESO" if por == "ingreso" else "CANTIDAD"
        print(f"=== Reporte por {titulo} (desc) ===")
        datos = self.gestor.ordenar_resumen(por=por, descendente=True)

        print(f"{'Producto':<18} {'Cant.':>10} {'Ingreso(USD)':>14} {'PU':>8} {'Unidad':>8}")
        print("-"*65)
        for r in datos:
            p = r["producto"]
            print(f"{p.nombre:<18} {r['cantidad']:>10.2f} {r['ingreso']:>14.2f} {p.precio:>8.2f} {p.unidad:>8}")
        print("-"*65)
        print(f"TOTAL GENERAL: {self.gestor.total_general():.2f} USD")
        # Producto top
        top = datos[0]
        print(f"TOP por {titulo}: {top['producto'].nombre} (Cant: {top['cantidad']:.2f}, Ingreso: ${top['ingreso']:.2f})")
        pausar()

    def mostrar_total_general(self):
        self._limpiar()
        print("=== Total general ===")
        print(f"Monto total de ventas: ${self.gestor.total_general():.2f} USD")
        pausar()

    # ----------------- Utilidades -----------------
    def _limpiar(self):
        # Limpieza visual sencilla (no borra pantalla real, solo separa)
        print("\n" * 2)

if __name__ == "__main__":
    App().ejecutar()

