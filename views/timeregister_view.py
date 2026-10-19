from datetime import date
from views.utilities import pedir_entero
from models.timeregister import RegistroTiempoModelo


class VistaRegistroTiempo:
    @staticmethod
    def desplegar_menu():
        print("\n" + "-" * 30)
        print("     GESTION DE REGISTROS DE TIEMPO")
        print("-" * 30)
        print("1.   AGREGAR REGISTRO")
        print("2.   MOSTRAR TODOS LOS REGISTROS")
        print("0.   VOLVER AL (MENU PRINCIPAL)")
        print("-" * 30)
        return pedir_entero("Seleccione una opcion: ")

    @staticmethod
    def pedir_datos_registro():
        print("\n--- AGREGAR NUEVO REGISTRO ---")

        print("FECHA DEL REGISTRO:")
        anio = pedir_entero(" Año: ")
        mes = pedir_entero(" MES: ")
        dia = pedir_entero(" DIA: ")
        fecha_ingresada = date(anio, mes, dia)

        horas_ingresadas = pedir_entero("Horas trabajadas: ")

        detalle_ingresado = input("Descripcion de la tarea: ")
        empleado = pedir_entero("ID del Empleado: ")
        proyecto = pedir_entero("ID del Proyecto: ")
        return {"fecha": fecha_ingresada, "horas_trabajadas": horas_ingresadas, "descripcion": detalle_ingresado, "id_empleado": empleado, "id_proyecto": proyecto}

    @staticmethod
    def imprimir_registros(lista):
        print("\n--- LISTA DE REGISTROS ---")
        if not lista:
            print("No hay registros guardados.")
        else:
            for reg in lista:
                print("ID Registrotiempo: " + str(reg.codigo) + " | Fecha: " + str(reg.fecha_registro) + " | Horas Trabajadas: " + str(reg.horas) + " | ID Empleado: " + str(reg.codigo_empleado) + " | ID Proyecto: " + str(reg.codigo_proyecto))
        print("-" * 30)

    @staticmethod
    def avisar(texto):
        print("[REGISTROS] " + texto)