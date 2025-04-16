from utils import pedirNombre, pedirApellido, pedirEdad, pedirResidencia, informacionPersonal, saludar

nombre = pedirNombre("por favor indique su nombre: ")
apellido = pedirApellido("Por favor indique su apellido: ")
edad = pedirEdad("Por favor indique su edad: ")
residencia = pedirResidencia("Por favor diga su pais de Residencia: ")

datos = informacionPersonal(nombre, apellido, edad, residencia)

saludar(f"Hola {datos['nombre']} {datos['apellido']}!! de {datos['edad']} años y de residencia en {datos['residencia']}")