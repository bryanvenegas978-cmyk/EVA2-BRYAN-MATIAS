from datetime import date


class ProyectoModelo:
    def __init__(self, codigo, titulo, detalle, fecha_arranque, codigo_depto):
        self.codigo = codigo
        self.titulo = titulo
        self.detalle = detalle
        self.fecha_arranque = fecha_arranque
        self.codigo_depto = codigo_depto

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
            raise ValueError("El campo no puede quedar vacio.")
        self._titulo = valor.strip()

    @property
    def detalle(self):
        return self._detalle

    @detalle.setter
    def detalle(self, valor):
        if not valor.strip():
            raise ValueError("El campo no puede quedar vacio.")
        self._detalle = valor.strip()

    @property
    def fecha_arranque(self):
        return self._fecha_arranque

    @fecha_arranque.setter
    def fecha_arranque(self, valor):
        if valor > date.today():
            raise ValueError("La fecha de inicio no puede ser mayor a la fecha actual.")
        self._fecha_arranque = valor

    @property
    def codigo_depto(self):
        return self._codigo_depto

    @codigo_depto.setter
    def codigo_depto(self, valor):
        if valor is not None and valor <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._codigo_depto = valor