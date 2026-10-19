from views.utilities import pedir_entero


class VistaPrincipal:
    @staticmethod
    def desplegar_menu():
        print("\n" + "-" * 30)
        print("     ECOTECH - MENU PRINCIPAL")
        print("-" * 30)
        print("1.   GESTION DE EMPLEADOS")
        print("2.   GESTION DE DEPARTAMENTOS")
        print("3.   GESTION DE PROYECTOS")
        print("4.   REGISTRO TIEMPO")
        print("5.   GESTION DE USUARIOS")
        print("0.   SALIR")
        print("-" * 30)
        return pedir_entero("Seleccione una opcion: ")

    @staticmethod
    def avisar(texto):
        print("\n [SISTEMA] " + texto)