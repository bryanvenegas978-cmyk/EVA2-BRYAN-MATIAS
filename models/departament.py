class DepartamentoModelo:
    def __init__(self, codigo, titulo, encargado):
        self.codigo = codigo
        self.titulo = titulo
        self.encargado = encargado

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is not None and valor <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._codigo = valor

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor.strip():
            raise ValueError("El campo no puede estar vacio.")
        self._titulo = valor.strip()

    @property
    def encargado(self):
        return self._encargado

    @encargado.setter
    def encargado(self, valor):
        if not valor.strip():
            raise ValueError("El campo no puede estar vacio.")
        self._encargado = valor.strip()
        