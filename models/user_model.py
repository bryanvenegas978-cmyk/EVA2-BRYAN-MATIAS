from config.database import BaseDatos
from models.user import UsuarioModelo


class AccesoUsuario:
    @staticmethod
    def guardar(usr):
        con = BaseDatos().abrir_conexion()
        try:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO usuario(login, contraseña) VALUES(?, ?)",
                (usr.nombre_usuario, usr.clave)
            )
            con.commit()
            usr.codigo = cur.lastrowid
            return True
        except Exception as error:
            print("Error al guardar usuario en BD: " + str(error))
            return False
        finally:
            con.close()

    @staticmethod
    def listar_todos():
        con = BaseDatos().abrir_conexion()
        resultado = []
        try:
            cur = con.cursor()
            cur.execute("SELECT id_usuario, login, contraseña FROM usuario")
            registros = cur.fetchall()
            for reg in registros:
                resultado.append(UsuarioModelo(reg['id_usuario'], reg['login'], reg['contraseña']))
        except Exception as error:
            print("Error al listar usuarios: " + str(error))
        finally:
            con.close()
        return resultado