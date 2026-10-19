from models.timeregister import RegistroTiempo
from models.timeregister_model import Registrotiempo_Dao
from views.timeregister_view import RegistroTiempoView


class ControladorRegistroTiempo:
    def __init__(self):
        self.vista = RegistroTiempoView()

    def iniciar(self):
        while True:
            eleccion = self.vista.mostrar_menu()
            if eleccion == 1:
                self.registrar_horas()
            elif eleccion == 2:
                self.listar_registros()
            elif eleccion == 0:
                self.vista.mostrar_mensaje("Saliendo de la gestion de registros...")
                break
            else:
                self.vista.mostrar_mensaje("Opcion no valida.")

    def registrar_horas(self):
        info = self.vista.formulario_nv_registro()
        try:
            reg = RegistroTiempo(None, info['fecha'], info['horas_trabajadas'], info['descripcion'], info['id_empleado'], info['id_proyecto'])
            resultado = Registrotiempo_Dao.crear(reg)

            if resultado:
                self.vista.mostrar_mensaje("Registro agregado con exito (ID: " + str(reg.id_registrotiempo) + ")")
            else:
                self.vista.mostrar_mensaje("Error interno al guardar en la base de datos.")
        except ValueError as error:
            self.vista.mostrar_mensaje("Error en los datos: " + str(error))

    def listar_registros(self):
        lista = Registrotiempo_Dao.obtener_datos()
        self.vista.mostrar_lista_registros(lista)