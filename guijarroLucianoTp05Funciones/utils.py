def pedirNombre(mensaje):
    return input(mensaje)

def pedirApellido(mensaje):
    return input(mensaje)

def pedirEdad(mensaje):
    return input(mensaje)

def pedirResidencia(mensaje):
    return input(mensaje)

def informacionPersonal(nombre, apellido, edad, residencia):
    persona = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "residencia": residencia
    }
    return persona

def saludar(mensaje):
    return print(mensaje)

def calcularAreaCirculo(radio):
    return 3.14 * (radio * radio)

def calcularPerimetroCirculo(radio):
    return 2 * 3.14 * radio