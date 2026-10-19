from models.employe import Empleado
from models.employe_model import EmpleadoDao
from views.employe_view import EmpleadoView


class ControladorEmpleado:
    def __init__(self):
        self.vista = EmpleadoView()

    def iniciar(self):
        while True:
            eleccion = self.vista.mostrar_menu()
            if eleccion == 1:
                self.registrar_empleado()
            elif eleccion == 2:
                self.listar_empleados()
            elif eleccion == 0:
                self.vista.mostrar_mensaje("Saliendo de la gestion de empleados.....")
                break
            else:
                self.vista.mostrar_mensaje("Opcion no valida.")

    def registrar_empleado(self):
        info = self.vista.formulario_nv_empleado()
        try:
            persona = Empleado(None, info['nombre'], info['correo'], info['fecha_inicio'], info['direccion'], info['telefono'], info['salario'], info['id_departamento'], info['id_proyecto'], info['id_usuario'])
            resultado = EmpleadoDao.crear(persona)

            if resultado:
                self.vista.mostrar_mensaje("Empleado agregado con exito (ID: " + str(persona.id_empleado) + ")")
            else:
                self.vista.mostrar_mensaje("Error interno al guardar en la base de datos.")
        except ValueError as error:
            self.vista.mostrar_mensaje("Error en los datos: " + str(error))

    def listar_empleados(self):
        lista = EmpleadoDao.obtener_datos()
        self.vista.mostrar_lista_empleados(lista)