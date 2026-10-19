from models.departament import Departamento
from models.dep_model import DepartamentoDao
from views.departament_view import DepartamentoView


class ControladorDepartamento:
    def __init__(self):
        self.vista = DepartamentoView()

    def iniciar(self):
        while True:
            eleccion = self.vista.mostrar_menu()
            if eleccion == 1:
                self.registrar_departamento()
            elif eleccion == 2:
                self.listar_departamentos()
            elif eleccion == 0:
                self.vista.mostrar_mensaje("Saliendo de la gestion de departamentos.")
                break
            else:
                self.vista.mostrar_mensaje("Opcion no valida.")

    def registrar_departamento(self):
        info = self.vista.formaulario_nv_departamento()
        try:
            depto = Departamento(None, info['nombre'], info['gerente_asociado'])
            resultado = DepartamentoDao.crear(depto)

            if resultado:
                self.vista.mostrar_mensaje("Departamento agregado con exito (ID: " + str(depto.id_departamento) + ")")
            else:
                self.vista.mostrar_mensaje("Error al intentar guardar en la base de datos.")
        except ValueError as error:
            self.vista.mostrar_mensaje("Error en los datos ingresados: " + str(error))

    def listar_departamentos(self):
        lista = DepartamentoDao.obtener_datos()
        self.vista.mostrar_lista_departamentos(lista)