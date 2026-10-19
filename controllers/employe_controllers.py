from models.employe import EmpleadoModelo
from models.employe_model import AccesoEmpleado
from views.employe_view import VistaEmpleado


class ControladorEmpleado:
    def __init__(self):
        self.vista = VistaEmpleado()

    def iniciar(self):
        while True:
            eleccion = self.vista.desplegar_menu()
            if eleccion == 1:
                self.registrar_empleado()
            elif eleccion == 2:
                self.listar_empleados()
            elif eleccion == 0:
                self.vista.avisar("Saliendo de la gestion de empleados.....")
                break
            else:
                self.vista.avisar("Opcion no valida.")

    def registrar_empleado(self):
        info = self.vista.pedir_datos_empleado()
        try:
            persona = EmpleadoModelo(None, info['nombre'], info['correo'], info['fecha_inicio'], info['direccion'], info['telefono'], info['salario'], info['id_departamento'], info['id_proyecto'], info['id_usuario'])
            resultado = AccesoEmpleado.guardar(persona)

            if resultado:
                self.vista.avisar("Empleado agregado con exito (ID: " + str(persona.codigo) + ")")
            else:
                self.vista.avisar("Error interno al guardar en la base de datos.")
        except ValueError as error:
            self.vista.avisar("Error en los datos: " + str(error))

    def listar_empleados(self):
        lista = AccesoEmpleado.listar_todos()
        self.vista.imprimir_empleados(lista)
        