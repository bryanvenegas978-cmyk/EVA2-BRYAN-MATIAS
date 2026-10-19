from datetime import date
from views.utilities import pedir_entero
from models.employe import EmpleadoModelo


class VistaEmpleado:
    @staticmethod
    def desplegar_menu():
        print("\n" + "-" * 30)
        print("     GESTION DE EMPLEADOS")
        print("-" * 30)
        print("1.   AGREGAR EMPLEADO")
        print("2.   MOSTRAR TODOS LOS EMPLEADOS")
        print("0.   VOLVER AL (MENU PRINCIPAL)")
        print("-" * 30)
        return pedir_entero("Seleccione una opcion: ")

    @staticmethod
    def pedir_datos_empleado():
        print("\n--- AGREGAR NUEVO EMPLEADO ---")
        nombre_ingresado = input("Nombre: ")
        email_ingresado = input("Correo: ")

        print("FECHA DE INICIO: ")
        anio = pedir_entero(" Año: ")
        mes = pedir_entero(" Mes: ")
        dia = pedir_entero(" Día: ")
        fecha_ingresada = date(anio, mes, dia)

        domicilio_ingresado = input("Direccion: ")
        celular_ingresado = input("Telefono: ")

        while True:
            try:
                sueldo_ingresado = float(input("Salario: "))
                break
            except ValueError:
                print("Error: Ingrese un numero valido en salario.")

        depto = pedir_entero("ID del departamento asignado: ")
        proyecto = pedir_entero("ID del proyecto asignado: ")
        usuario = pedir_entero("ID del usuario del sistema: ")

        return {"nombre": nombre_ingresado, "correo": email_ingresado, "fecha_inicio": fecha_ingresada, "direccion": domicilio_ingresado, "telefono": celular_ingresado, "salario": sueldo_ingresado, "id_departamento": depto, "id_proyecto": proyecto, "id_usuario": usuario}

    @staticmethod
    def imprimir_empleados(lista):
        print("\n--- LISTA DE EMPLEADOS ---")
        if not lista:
            print("No hay empleados registrados.")
        else:
            for persona in lista:
                print("ID: " + str(persona.codigo) + " | Nombre: " + persona.nombre_completo + " | Correo: " + persona.email + " | Telefono: " + persona.celular)

        print("-" * 30)

    @staticmethod
    def avisar(texto):
        print("[EMPLEADOS] " + texto)