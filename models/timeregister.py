from datetime import date


class RegistroTiempoModelo:
    def __init__(self, codigo, fecha_registro, horas, detalle, codigo_empleado, codigo_proyecto):
        self.codigo = codigo
        self.fecha_registro = fecha_registro
        self.horas = horas
        self.detalle = detalle
        self.codigo_empleado = codigo_empleado
        self.codigo_proyecto = codigo_proyecto

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is not None and valor <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._codigo = valor

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, valor):
        if valor > date.today():
            raise ValueError("La fecha no puede ser mayor que la fecha actual.")
        self._fecha_registro = valor

    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self, valor):
        if valor <= 0:
            raise ValueError("Las horas trabajadas deben ser mayores a 0.")
        self._horas = valor

    @property
    def detalle(self):
        return self._detalle

    @detalle.setter
    def detalle(self, valor):
        if not valor.strip():
            raise ValueError("El campo no puede estar vacio.")
        self._detalle = valor.strip()

    @property
    def codigo_empleado(self):
        return self._codigo_empleado

    @codigo_empleado.setter
    def codigo_empleado(self, valor):
        if valor <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._codigo_empleado = valor

    @property
    def codigo_proyecto(self):
        return self._codigo_proyecto

    @codigo_proyecto.setter
    def codigo_proyecto(self, valor):
        if valor <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._codigo_proyecto = valor