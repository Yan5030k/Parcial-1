from modelos import Producto

#En este modulo se crea el diccionario que servira como talago de los productos disponibles
def catalogo_por_defecto() -> dict[str, Producto]:
    return{
        "TOM": Producto("TOM", "Tomate", 0.50, "lb"),
        "CEB": Producto("CEB", "Cebolla", 0.60, "lb"),
        "MAI": Producto("MAI", "Maíz", 0.40, "lb"),
        "FRI": Producto("FRI", "Frijol", 1.10, "lb"),
        "ARR": Producto("ARR", "Arroz", 0.90, "lb"),
        "POL": Producto("POL", "Pollo", 2.20, "lb"),
        "RES": Producto("RES", "Carne de res", 3.50, "lb"),
        "PAN": Producto("PAN", "Pan francés", 0.12, "unidad"),
        "HUE": Producto("HUE", "Huevo", 0.18, "unidad"),
        "LEC": Producto("LEC", "Lechuga", 0.80, "unidad"),
    }

def buscar_producto(catalogo: dict[str, Producto], codigo: str) -> Producto | None:
    return catalogo.get(codigo.upper())