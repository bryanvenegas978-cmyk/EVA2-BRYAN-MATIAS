from config.database import BaseDatos
from models.departament import Departamento


class AccesoDepartamento:
    @staticmethod
    def guardar(depto):
        con = BaseDatos().abrir_conexion()
        try:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO departamento (nombre, gerente_asociado) VALUES (?, ?)",
                (depto.nombre, depto.gerente_asociado)
            )
            con.commit()
            depto.id_departamento = cur.lastrowid
            return True
        except Exception as error:
            print("Error al guardar departamento en BD: " + str(error))
            return False
        finally:
            con.close()

    @staticmethod
    def listar_todos():
        con = BaseDatos().abrir_conexion()
        resultado = []
        try:
            cur = con.cursor()
            cur.execute("SELECT id_departamento, nombre, gerente_asociado FROM departamento")
            registros = cur.fetchall()
            for reg in registros:
                resultado.append(Departamento(reg['id_departamento'], reg['nombre'], reg['gerente_asociado']))
        except Exception as error:
            print("Error al listar departamentos: " + str(error))
        finally:
            con.close()
        return resultado