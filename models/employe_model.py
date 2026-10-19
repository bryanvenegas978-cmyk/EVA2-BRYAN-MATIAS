from datetime import date
from config.database import BaseDatos
from models.employe import EmpleadoModelo


class AccesoEmpleado:
    @staticmethod
    def guardar(persona):
        con = BaseDatos().abrir_conexion()
        try:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO empleado (nombre, correo, fecha_inicio, direccion, telefono, salario, id_departamento, id_proyecto, id_usuario) VALUES (?,?,?,?,?,?,?,?,?)",
                (persona.nombre_completo, persona.email, persona.fecha_ingreso, persona.domicilio, persona.celular, persona.sueldo, persona.codigo_depto, persona.codigo_proyecto, persona.codigo_usuario)
            )
            con.commit()
            persona.codigo = cur.lastrowid
            return True
        except Exception as error:
            print("Error al guardar empleado en BD: " + str(error))
            return False
        finally:
            con.close()

    @staticmethod
    def listar_todos():
        con = BaseDatos().abrir_conexion()
        resultado = []
        try:
            cur = con.cursor()
            cur.execute("SELECT id_empleado, nombre, correo, fecha_inicio, direccion, telefono, salario, id_departamento, id_proyecto, id_usuario FROM empleado")
            registros = cur.fetchall()
            for reg in registros:
                fecha_convertida = date.fromisoformat(reg['fecha_inicio'])
                resultado.append(EmpleadoModelo(reg['id_empleado'], reg['nombre'], reg['correo'], fecha_convertida, reg['direccion'], reg['telefono'], reg['salario'], reg['id_departamento'], reg['id_proyecto'], reg['id_usuario']))
        except Exception as error:
            print("Error al listar empleados: " + str(error))
        finally:
            con.close()
        return resultado
    