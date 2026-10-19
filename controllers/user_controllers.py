from argon2 import PasswordHasher
from models.user import UsuarioModelo
from models.user_model import AccesoUsuario
from views.user_view import VistaUsuario


class ControladorUsuario:
    def __init__(self):
        self.vista = VistaUsuario()
        self.cifrador = PasswordHasher()

    def iniciar(self):
        while True:
            eleccion = self.vista.desplegar_menu()
            if eleccion == 1:
                self.registrar_usuario()
            elif eleccion == 2:
                self.listar_usuarios()
            elif eleccion == 0:
                self.vista.avisar("Saliendo de la gestion de usuarios...")
                break
            else:
                self.vista.avisar("Opcion no valida.")

    def registrar_usuario(self):
        info = self.vista.pedir_datos_usuario()
        try:
            clave_cifrada = self.cifrador.hash(info['contrasena'])
            usr = UsuarioModelo(None, info['login'], clave_cifrada)
            resultado = AccesoUsuario.guardar(usr)

            if resultado:
                self.vista.avisar("Usuario agregado con exito (ID: " + str(usr.codigo) + ")")
            else:
                self.vista.avisar("Error interno al guardar en la base de datos.")
        except ValueError as error:
            self.vista.avisar("Error en los datos: " + str(error))

    def listar_usuarios(self):
        lista = AccesoUsuario.listar_todos()
        self.vista.imprimir_usuarios(lista)
        