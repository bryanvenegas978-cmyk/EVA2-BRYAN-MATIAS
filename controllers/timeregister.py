from models.timeregister import RegistroTiempoModelo
from models.timeregister_model import AccesoRegistroTiempo
from views.timeregister_view import VistaRegistroTiempo


class ControladorRegistroTiempo:
    def __init__(self):
        self.vista = VistaRegistroTiempo()

    def iniciar(self):
        while True:
            eleccion = self.vista.desplegar_menu()
            if eleccion == 1:
                self.registrar_horas()
            elif eleccion == 2:
                self.listar_registros()
            elif eleccion == 0:
                self.vista.avisar("Saliendo de la gestion de registros...")
                break
            else:
                self.vista.avisar("Opcion no valida.")

    def registrar_horas(self):
        info = self.vista.pedi

            if resultado:
                self.vista.avisar("Registro agregado con exito (ID: " + str(reg.codigo) + ")")
            else:
                self.vista.avisar("Error interno al guardar en la base de datos.")
        except ValueError as error:
            self.vista.avisar("Error en los datos: " + str(error))

    def listar_registros(self):
        lista = AccesoRegistroTiempo.listar_todos()
        self.vista.imprimir_registros(lista)