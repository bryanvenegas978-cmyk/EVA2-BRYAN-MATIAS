from models.departament import DepartamentoModelo
from models.dep_model import AccesoDepartamento
from views.departament_view import VistaDepartamento


class ControladorDepartamento:
    def __init__(self):
        self.vista = VistaDepartamento()

    def iniciar(self):
        while True:
            eleccion = self.vista.desplegar_menu()
            if eleccion == 1:
                self.registrar_departamento()
            elif eleccion == 2:
                self.listar_departamentos()
            elif eleccion == 0:
                self.vista.avisar("Saliendo de la gestion de departamentos.")
                break
            else:
                self.vista.avisar("Opcion no valida.")

    def registrar_departamento(self):
        info = self.vista.pedir_datos_departamento()
        try:
            depto = DepartamentoModelo(None, info['nombre'], info['gerente_asociado'])
            resultado = AccesoDepartamento.guardar(depto)

            if resultado:
                self.vista.avisar("Departamento agregado con exito (ID: " + str(depto.codigo) + ")")
            else:
                self.vista.avisar("Error al intentar guardar en la base de datos.")
        except ValueError as error:
            self.vista.avisar("Error en los datos ingresados: " + str(error))

    def listar_departamentos(self):
        lista = AccesoDepartamento.listar_todos()
        self.vista.imprimir_departamentos(lista)
        