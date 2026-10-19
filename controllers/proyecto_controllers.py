from models.proyect import ProyectoModelo
from models.proyect_model import AccesoProyecto
from views.proyect_view import VistaProyecto


class ControladorProyecto:
    def __init__(self):
        self.vista = VistaProyecto()

    def iniciar(self):
        while True:
            eleccion = self.vista.desplegar_menu()
            if eleccion == 1:
                self.registrar_proyecto()
            elif eleccion == 2:
                self.listar_proyectos()
            elif eleccion == 0:
                self.vista.avisar("Saliendo de la gestion de proyectos...")
                break
            else:
                self.vista.avisar("Opcion no valida.")

    def registrar_proyecto(self):
        info = self.vista.pedir_datos_proyecto()
        try:
            proy = ProyectoModelo(None, info['nombre'], info['descripcion'], info['fecha_inicio'], info['id_departamento'])
            resultado = AccesoProyecto.guardar(proy)

            if resultado:
                self.vista.avisar("Proyecto agregado con exito: (ID: " + str(proy.codigo) + ")")
            else:
                self.vista.avisar("Error interno al guardar en la base de datos.")
        except ValueError as error:
            self.vista.avisar("Error en la base de datos: " + str(error))

    def listar_proyectos(self):
        lista = AccesoProyecto.listar_todos()
        self.vista.imprimir_proyectos(lista)
        
        
        