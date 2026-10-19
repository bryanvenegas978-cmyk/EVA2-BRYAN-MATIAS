from argon2 import PasswordHasher
from models.user import Usuario
from models.user_model import UsuarioDao
from views.user_view import UsuarioView


class ControladorUsuario:
    def __init__(self):
        self.vista = UsuarioView()
        self.cifrador = PasswordHasher()

    def iniciar(self):
        while True:
            eleccion = self.vista.mostrar_menu()
            if eleccion == 1:
                self.registrar_usuario()
            elif eleccion == 2:
                self.listar_usuarios()
            elif eleccion == 0:
                self.vista.mostrar_mensaje("Saliendo de la gestion de usuarios...")
                break
            else:
                self.vista.mostrar_mensaje("Opcion no valida.")

    def registrar_usuario(self):
        info = self.vista.formulario_nv_usuario()
        try:
            clave_cifrada = self.cifrador.hash(info['contrasena'])
            usr = Usuario(None, info['login'], clave_cifrada)
            resultado = UsuarioDao.crear(usr)

            if resultado:
                self.vista.mostrar_mensaje("Usuario agregado con exito (ID: " + str(usr.id_usuario) + ")")
            else:
                self.vista.mostrar_mensaje("Error interno al guardar en la base de datos.")
        except ValueError as error:
            self.vista.mostrar_mensaje("Error en los datos: " + str(error))

    def listar_usuarios(self):
        lista = UsuarioDao.obtener_datos()
        self.vista.mostrar_lista_usuarios(lista)