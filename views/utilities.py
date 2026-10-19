def pedir_entero(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Error: Debe ingresar un numero entero valido.")


def preguntar_si_no(texto):
    while True:
        respuesta = input(texto + " (si/no):").strip().lower()
        if respuesta in ("si", "no"):
            return respuesta == "si"
        print("Respuesta no valida. por favor, ingrese 'si' o 'no'.")