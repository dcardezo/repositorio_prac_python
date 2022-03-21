# prueba de cambio

"""Clase para empleado fijo."""


class Empleado_fijo:
    def __init__(self, nombre, NIF, fecha, sueldo, año_alta, complemento, tipo):
        self.nombre = nombre
        self.NIF = NIF
        self.fecha = fecha
        self.sueldo = sueldo
        self.año_alta = año_alta
        self.complemento = complemento
        self.tipo = tipo

    def calcular_sueldo_fijo(self):
        tiempo = 2022 - int(self.año_alta)
        comp = self.complemento * tiempo
        sueldo_mensual = self.sueldo + float(comp / 12)
        return sueldo_mensual


"""Clase para empleado temporal."""


class Empleado_temporal:
    def __init__(self, nombre, NIF, fecha, sueldo, alta, baja, tipo):
        self.nombre = nombre
        self.NIF = NIF
        self.fecha = fecha
        self.sueldo = sueldo
        self.alta = alta
        self.baja = baja
        self.tipo = tipo

    def calcular_sueldo_temporal(self):
        fecha_alta = self.alta.split("/")
        fecha_baja = self.baja.split("/")
        meses = int(fecha_baja[1]) - int(fecha_alta[1])
        sueldo_mensual = self.sueldo * meses
        return sueldo_mensual
