from models.proyect import Proyecto
from models.proyect_model import Proyecto_Dao
from views.proyect_view import ProyectoView


class ControladorProyecto:
    def __init__(self):
        self.vista = ProyectoView()

    def iniciar(self):
        while True:
            eleccion = self.vista.mostrar_menu()
            if eleccion == 1:
                self.registrar_proyecto()
            elif eleccion == 2:
                self.listar_proyectos()
            elif eleccion == 0:
                self.vista.mostrar_mensaje("Saliendo de la gestion de proyectos...")
                break
            else:
                self.vista.mostrar_mensaje("Opcion no valida.")

    def registrar_proyecto(self):
        info = self.vista.formulario_nv_proyecto()
        try:
            proy = Proyecto(None, info['nombre'], info['descripcion'], info['fecha_inicio'], info['id_departamento'])
            resultado = Proyecto_Dao.crear(proy)

            if resultado:
                self.vista.mostrar_mensaje("Proyecto agregado con exito: (ID: " + str(proy.id_proyecto) + ")")
            else:
                self.vista.mostrar_mensaje("Error interno al guardar en la base de datos.")
        except ValueError as error:
            self.vista.mostrar_mensaje("Error en la base de datos: " + str(error))

    def listar_proyectos(self):
        lista = Proyecto_Dao.obtener_datos()
        self.vista.mostrar_lista_proyectos(lista)