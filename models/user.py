class UsuarioModelo:
    def __init__(self, codigo, nombre_usuario, clave):
        self.codigo = codigo
        self.nombre_usuario = nombre_usuario
        self.clave = clave

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is not None and valor <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._codigo = valor

    @property
    def nombre_usuario(self):
        return self._nombre_usuario

    @nombre_usuario.setter
    def nombre_usuario(self, valor):
        if not valor.strip():
            raise ValueError("El campo no puede estar vacio.")
        self._nombre_usuario = valor.strip()

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, valor):
        if not valor.strip():
            raise ValueError("El campo no puede estar vacio.")
        self._clave = valor.strip()
        
        