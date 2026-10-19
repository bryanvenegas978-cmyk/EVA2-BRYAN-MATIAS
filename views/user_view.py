from views.utilities import pedir_entero
from models.user import UsuarioModelo


class VistaUsuario:
    @staticmethod
    def desplegar_menu():
        print("\n" + "-" * 30)
        print("     GESTION DE USUARIOS")
        print("-" * 30)
        print("1.   AGREGAR USUARIO")
        print("2.   MOSTRAR TODOS LOS USUARIOS")
        print("0.   VOLVER AL (MENU PRINCIPAL)")
        print("-" * 30)
        return pedir_entero("Seleccione una opcion: ")

    @staticmethod
    def pedir_datos_usuario():
        print("\n--- AGREGAR NUEVO USUARIO ---")
        nombre_ingresado = input("Ingrese el nombre de usuario (login): ")
        clave_ingresada = input("Ingrese la contrasena: ")

        return {
            "login": nombre_ingresado,
            "contrasena": clave_ingresada
        }

    @staticmethod
    def imprimir_usuarios(lista):
        print("\n--- LISTA DE USUARIOS ---")
        if not lista:
            print("No hay usuarios registrados.")
        else:
            for usr in lista:
                print("ID Usuario: " + str(usr.codigo) + " | Login: " + usr.nombre_usuario + " | Contraseña: " + usr.clave[:15] + "...")
        print("-" * 30)

    @staticmethod
    def avisar(texto):
        print("[USUARIOS] " + texto)