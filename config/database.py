import sqlite3


class BaseDatos:
    _unica = None
    _archivo_bd = "EcoTECH.db"

    def __new__(cls):
        if cls._unica is None:
            cls._unica = super(BaseDatos, cls).__new__(cls)
        return cls._unica

    def abrir_conexion(self):
        con = sqlite3.connect(self._archivo_bd)
        con.row_factory = sqlite3.Row
        return con

    def crear_tablas(self):
        con = self.abrir_conexion()
        try:
            cur = con.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS usuario (
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    login TEXT NOT NULL,
                    contraseña TEXT NOT NULL
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS departamento (
                    id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    gerente_asociado TEXT NOT NULL
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS proyecto (
                    id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT NOT NULL,
                    fecha_inicio TEXT NOT NULL,
                    id_departamento INTEGER,
                    FOREIGN KEY (id_departamento)
                        REFERENCES departamento(id_departamento) ON DELETE SET NULL
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS empleado (
                    id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    correo TEXT NOT NULL,
                    fecha_inicio TEXT NOT NULL,
                    direccion TEXT NOT NULL,
                    telefono TEXT NOT NULL,
                    salario REAL NOT NULL,
                    id_departamento INTEGER,
                    id_proyecto INTEGER,
                    id_usuario INTEGER,
                    FOREIGN KEY (id_departamento)
                        REFERENCES departamento(id_departamento) ON DELETE SET NULL,
                    FOREIGN KEY (id_proyecto)
                        REFERENCES proyecto(id_proyecto) ON DELETE SET NULL,
                    FOREIGN KEY (id_usuario)
                        REFERENCES usuario(id_usuario) ON DELETE SET NULL
                )
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS registrotiempo (
                    id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha TEXT NOT NULL,
                    horas_trabajadas INTEGER NOT NULL,
                    descripcion TEXT NOT NULL,
                    id_empleado INTEGER,
                    id_proyecto INTEGER,
                    FOREIGN KEY (id_empleado)
                        REFERENCES empleado(id_empleado) ON DELETE SET NULL,
                    FOREIGN KEY (id_proyecto)
                        REFERENCES proyecto(id_proyecto) ON DELETE SET NULL
                )
            """)

            con.commit()
        except sqlite3.Error as error:
            print("Error al crear las tablas: " + str(error))
        finally:
            con.close()


if __name__ == "__main__":
    bd = BaseDatos()
    bd.crear_tablas()
    print("Tablas creadas correctamente.")