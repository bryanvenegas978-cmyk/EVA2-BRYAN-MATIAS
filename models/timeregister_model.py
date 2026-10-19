from datetime import date
from config.database import BaseDatos
from models.timeregister import RegistroTiempoModelo


class AccesoRegistroTiempo:
    @staticmethod
    def guardar(reg):
        con = BaseDatos().abrir_conexion()
        try:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO registrotiempo(fecha, horas_trabajadas, descripcion, id_empleado, id_proyecto) VALUES(?, ?, ?, ?, ?)",
                (reg.fecha_registro, reg.horas, reg.detalle, reg.codigo_empleado, reg.codigo_proyecto)
            )
            con.commit()
            reg.codigo = cur.lastrowid
            return True
        except Exception as error:
            print("Error al guardar el registro de tiempo en BD: " + str(error))
            return False
        finally:
            con.close()

    @staticmethod
    def listar_todos():
        con = BaseDatos().abrir_conexion()
        resultado = []
        try:
            cur = con.cursor()
            cur.execute("SELECT id_registro, fecha, horas_trabajadas, descripcion, id_empleado, id_proyecto FROM registrotiempo")
            registros = cur.fetchall()
            for fila in registros:
                fecha_convertida = date.fromisoformat(fila['fecha'])
                resultado.append(RegistroTiempoModelo(fila['id_registro'], fecha_convertida, fila['horas_trabajadas'], fila['descripcion'], fila['id_empleado'], fila['id_proyecto']))
        except Exception as error:
            print("Error al listar registros de tiempo: " + str(error))
        finally:
            con.close()
        return resultado