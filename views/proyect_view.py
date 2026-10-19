from datetime import date
from views.utilities import pedir_entero
from models.proyect import ProyectoModelo


class VistaProyecto:
    @staticmethod
    def desplegar_menu():
        print("\n" + "-" * 30)
        print("     GESTION DE PROYECTOS")
        print("-" * 30)
        print("1.   AGREGAR PROYECTOS")
        print("2.   MOSTRAR TODOS LOS PROYECTOS")
        print("0.   VOLVER AL (MENU PRINCIPAL)")
        print("-" * 30)
        return pedir_entero("Seleccione una opcion: ")

    @staticmethod
    def pedir_datos_proyecto():
        print("\n--- AGREGAR NUEVO PROYECTO ---")
        titulo_ingresado = input("Nombre del proyecto: ")
        detalle_ingresado = input("Descripcion: ")

        print("FECHA DE INICIO: ")
        anio = pedir_entero(" Año: ")
        mes = pedir_entero(" Mes: ")
        dia = pedir_entero(" Día: ")
        fecha_ingresada = date(anio, mes, dia)

        depto = pedir_entero("Ingrese el (ID) del departamento a cargo: ")

        return {"nombre": titulo_ingresado, "descripcion": detalle_ingresado, "fecha_inicio": fecha_ingresada, "id_departamento": depto}

    @staticmethod
    def imprimir_proyectos(lista):
        print("\n--- LISTA DE PROYECTOS ---")
        if not lista:
            print("No hay proyectos registrados.")
        else:
            for proy in lista:
                print("ID: " + str(proy.codigo) + " | Nombre: " + proy.titulo + " | ID Departamento: " + str(proy.codigo_depto))
        print("-" * 30)

    @staticmethod
    def avisar(texto):
        print("[PROYECTO] " + texto)
        