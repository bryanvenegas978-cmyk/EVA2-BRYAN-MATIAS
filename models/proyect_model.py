from datetime import date
from config.database import BaseDatos
from models.proyect import ProyectoModelo


class AccesoProyecto:
    @staticmethod
    def guardar(proy):
        con = BaseDatos().abrir_conexion()
        try:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO proyecto (nombre, descripcion, fecha_inicio, id_departamento) VALUES(?, ?, ?, ?)",
                (proy.titulo, proy.detalle, proy.fecha_arranque, proy.codigo_depto)
            )
            con.commit()
            proy.codigo = cur.lastrowid
            return True
        except Exception as error:
            print("Error al guardar proyecto en BD: " + str(error))
            return False
        finally:
            con.close()

    @staticmethod
    def listar_todos():
        con = BaseDatos().abrir_conexion()
        resultado = []
        try:
            cur = con.cursor()
            cur.execute("SELECT id_proyecto, nombre, descripcion, fecha_inicio, id_departamento FROM proyecto")
            registros = cur.fetchall()
            for reg in registros:
                fecha_convertida = date.fromisoformat(reg['fecha_inicio'])
                resultado.append(ProyectoModelo(reg['id_proyecto'], reg['nombre'], reg['descripcion'], fecha_convertida, reg['id_departamento']))
        except Exception as error:
            print("Error al listar proyectos: " + str(error))
        finally:
            con.close()
        return resultado
    