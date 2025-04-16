def pedirNombre(mensaje):
    return input(mensaje)

def pedirApellido(mensaje):
    return input(mensaje)

def pedirEdad(mensaje):
    return input(mensaje)

def pedirResidencia(mensaje):
    return input(mensaje)

def pedirNumero(mensaje):
    return int(input(mensaje))

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

def segundosAHoras(segundos):
    return segundos / 3600

def tablaMultiplicar(num):
    for i in range(1, 11):
        resultado = i * num
        print(f"{i} * {num} = {resultado}")
    

def operacionesBasicas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    return suma, resta, division, multiplicacion

def calcularIMC(peso, altura):
    return peso / (altura * altura)

def celsiusAFahrenheit(temperaturaCelsius):
    return (temperaturaCelsius * 9/5) + 32