from views.utilities import pedir_entero
from models.departament import DepartamentoModelo


class VistaDepartamento:
    @staticmethod
    def desplegar_menu():
        print("\n" + "-" * 30)
        print("     GESTION DE DEPARTAMENTOS")
        print("-" * 30)
        print("1.   AGREGAR DEPARTAMENTO")
        print("2.   MOSTRAR TODOS LOS DEPARTAMENTOS")
        print("0.   VOLVER AL (MENU PRINCIPAL)")
        print("-" * 30)
        return pedir_entero("Seleccione una opcion.")

    @staticmethod
    def pedir_datos_departamento():
        print("\n--- AGREGAR NUEVO DEPARTAMENTO ---")
        titulo = input("Ingrese el nombre del departamento: ")
        encargado = input("Ingrese el nombre del gerente asociado: ")
        return {"nombre": titulo, "gerente_asociado": encargado}

    @staticmethod
    def imprimir_departamentos(lista):
        print("\n--- LISTA DE DEPARTAMENTOS ---")
        if not lista:
            print("No hay departamentos registrados.")
        else:
            for depto in lista:
                print("ID Departamento: " + str(depto.codigo) + " | Nombre: " + depto.titulo + " | Gerente: " + depto.encargado)
        print("-" * 30)

    @staticmethod
    def avisar(texto):
        print("[DEPARTAMENTOS] " + texto)
        