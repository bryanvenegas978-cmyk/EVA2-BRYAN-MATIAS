from datetime import date


class EmpleadoModelo:
    def __init__(self, codigo, nombre_completo, email, fecha_ingreso, domicilio, celular, sueldo, codigo_depto, codigo_proyecto, codigo_usuario):
        self.codigo = codigo
        self.nombre_completo = nombre_completo
        self.email = email
        self.fecha_ingreso = fecha_ingreso
        self.domicilio = domicilio
        self.celular = celular
        self.sueldo = sueldo
        self.codigo_depto = codigo_depto
        self.codigo_proyecto = codigo_proyecto
        self.codigo_usuario = codigo_usuario

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is not None and valor <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._codigo = valor

    @property
    def nombre_completo(self):
        return self._nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, valor):
        if not valor.strip():
            raise ValueError("El campo no puede estar vacio.")
        self._nombre_completo = valor.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not valor.strip():
            raise ValueError("El campo no puede estar vacio.")
        self._email = valor.strip()

    @property
    def fecha_ingreso(self):
        return self._fecha_ingreso

    @fecha_ingreso.setter
    def fecha_ingreso(self, valor):
        if valor > date.today():
            raise ValueError("La fecha de inicio no puede ser mayor a la fecha actual.")
        self._fecha_ingreso = valor

    @property
    def domicilio(self):
        return self._domicilio

    @domicilio.setter
    def domicilio(self, valor):
        if not valor.strip():
            raise ValueError("El campo no puede estar vacio.")
        self._domicilio = valor.strip()

    @property
    def celular(self):
        return self._celular

    @celular.setter
    def celular(self, valor):
        if not valor.strip():
            raise ValueError("El campo no puede estar vacio.")
        if not valor.strip().replace("+", "").isdigit():
            raise ValueError("El numero solo puede contener numeros y es opcional el (+)")
        if len(valor.strip()) < 9:
            raise ValueError("El numero debe tener al menos 9 caracteres.")
        self._celular = valor.strip()

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, valor):
        if valor < 1 or valor > 999999999.99:
            raise ValueError("El salario debe estar entre 1 y 999.999.999.99")
        self._sueldo = valor

    @property
    def codigo_depto(self):
        return self._codigo_depto

    @codigo_depto.setter
    def codigo_depto(self, valor):
        if valor is not None and valor <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._codigo_depto = valor

    @property
    def codigo_proyecto(self):
        return self._codigo_proyecto

    @codigo_proyecto.setter
    def codigo_proyecto(self, valor):
        if valor <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._codigo_proyecto = valor

    @property
    def codigo_usuario(self):
        return self._codigo_usuario

    @codigo_usuario.setter
    def codigo_usuario(self, valor):
        if valor <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._codigo_usuario = valor
        