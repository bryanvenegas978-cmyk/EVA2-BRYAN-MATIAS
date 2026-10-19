from views.main_view import VistaPrincipal
from controllers.employe_controllers import ControladorEmpleado
from controllers.dep_controllers import ControladorDepartamento
from controllers.proyecto_controllers import ControladorProyecto
from controllers.timeregister import ControladorRegistroTiempo
from controllers.user_controllers import ControladorUsuario


class ControladorPrincipal:
    def __init__(self):


        self.vista = VistaPrincipal()
        self.ctrl_empleado = ControladorEmpleado()
        self.ctrl_departamento = ControladorDepartamento()
        self.ctrl_proyecto = ControladorProyecto()
        self.ctrl_registro = ControladorRegistroTiempo()
        self.ctrl_usuario = ControladorUsuario()

    def iniciar(self):
        while True:
            eleccion = self.vista.desplegar_menu()
            if eleccion == 1:
                self.ctrl_empleado.iniciar()
            elif eleccion == 2:
                self.ctrl_departamento.iniciar()
            elif eleccion == 3:
                self.ctrl_proyecto.iniciar()
            elif eleccion == 4:
                self.ctrl_registro.iniciar()
            elif eleccion == 5:
                self.ctrl_usuario.iniciar()
            elif eleccion == 0:
                self.vista.avisar("Gracias por usar el sistema ECOTECH. ¡Hasta pronto!")
                break
            else:
                self.vista.avisar("Opcion no valida. Por favor intente nuevamente.")