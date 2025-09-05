#Este módulo contiene funciones de utilidad para la entrada de datos por parte del usuario.

#Leemos la entrada del usuario:
def leer_opcion(mensaje: str, opciones_validas: set[str]) ->str:
    while True:
        valor = input(mensaje).strip()
        if valor in opciones_validas:
            return valor
        print(f"Opción inválida. Opciones: {', '.join(sorted(opciones_validas))}")

#Función para leer un número flotante positivo
def leer_float_positivo(mensaje: str) -> float:
    while True:
        try:
            v= float(input(mensaje).strip())
            if v >0:
                return v #Si el valor es positivo lo retorna, esto evita errores
            print("Debe ser un número mayor que 0.")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.") #Lo mismo evitar error, para que el usuario intente denuevo
        
def pausar():
    input("\nPresiona ENTER para continuar...")