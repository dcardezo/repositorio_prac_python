from clases import Empleado_fijo, Empleado_temporal

"""Funcion para un nuevo empleado."""


def new(empleado):
    nombre = str(input("Introduce el nombre del empleado: "))
    NIF = str(input("Introduce el NIF del empleado: "))
    fecha = str(input("Introduce la fecha de nacimiento del empleado: "))
    sueldo = float(input("Introduce el sueldo mensual: "))
    tipo = str(input("Indica si el empleado es fijo o temporal: "))
    if tipo == "fijo":
        complemento = float(input("Introduce el complemento correspondiente al empleado: "))
        alta = int(input("Introduce el año de alta en la empresa: "))
        empleado[NIF] = Empleado_fijo(nombre, NIF, fecha, sueldo, alta, complemento, tipo)
    elif tipo == "temporal":
        alta = str(input("Introduce la fecha de alta en la empresa: "))
        baja = str(input("Introduce la fecha de baja en la empresa: "))
        empleado[NIF] = Empleado_temporal(nombre, NIF, fecha, sueldo, alta, baja, tipo)


"""Funcion para eliminar un empleado."""


def del_empleado(empleado):
    NIF = str(input("Introduce el NIF del empleado que se desea eliminar: "))
    del empleado[NIF]


"""Funcion para listar todos empleados."""


def listar_empleados(empleado):
    for pwd in empleado:
        print(pwd, empleado[pwd].nombre, " ", empleado[pwd].tipo)


"""Funcion para obtener la ficha completa de un empleado."""


def ficha_empleado(empleado):
    NIF = str(input("Introduce el NIF del empleado deseado: "))
    print("Nombre:", empleado[NIF].nombre)
    print("NIF:", empleado[NIF].NIF)
    print("Fecha de nacimiento:", empleado[NIF].fecha)
    print("Tipo:", empleado[NIF].tipo)
    print("Sueldo fijo: ", empleado[NIF].sueldo)
    if empleado[NIF].tipo == "fijo":
        print("Año de alta: ", empleado[NIF].año_alta)
        print("Complemento anual: ", empleado[NIF].complemento)
        print("Sueldo mensual: ", "{:.2f}".format(empleado[NIF].calcular_sueldo_fijo()), "€")
    elif empleado[NIF].tipo == "temporal":
        print("Fecha de alta:", empleado[NIF].alta)
        print("Fecha de baja: ", empleado[NIF].baja)
        print(
            "Cantidad a cobrar: ",
            "{:.2f}".format(empleado[NIF].calcular_sueldo_temporal()),
            "€",
        )


"""Funcion detecta cumpleaños."""


def cumpleaños(empleado):
    intro_mes = int(input("Introduce un mes en numero:"))
    while intro_mes < 1 or intro_mes > 12:
        print("Error, no existe el mes introducido. Introdúcelo de nuevo (un numero entre 1 y 12).")
        intro_mes = int(input("Introduce un mes en numero:"))
    print("Estan de cumpleaños: ")
    for pwd in empleado:
        fecha = empleado[pwd].fecha.split("/")
        mes = int(fecha[1])
        if mes == intro_mes:
            print(empleado[pwd].nombre, " ", empleado[pwd].fecha)


"""Funcion que da todas las opciones que puede realizar el operarador."""


def options():
    print("Menú de opciones:")
    print("(1) Añadir empleado")
    print("(2) Borrar empleado")
    print("(3) Mostrar lista empleados")
    print("(4) Mostrar detalle de un empleado")
    print("(5) Mostrar empleados cumpleaños")
    print("(6) Terminar")
    option = int(input("Elige una opción: "))
    return option


if __name__ == "__main__":
    fin = 0
    empleado = {}
    while fin == 0:
        option = options()
        if option == 1:
            new(empleado)
        elif option == 2:
            del_empleado(empleado)
        elif option == 3:
            listar_empleados(empleado)
        elif option == 4:
            ficha_empleado(empleado)
        elif option == 5:
            cumpleaños(empleado)
        elif option == 6:
            fin = 1
        else:
            print("ERROR! Escoge un número del menú")
