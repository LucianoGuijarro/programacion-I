from utils import calcularPromedioDetresNumeros, pedirNumero

num1 = pedirNumero("Por favor ingrese su primera nota: ")
num2 = pedirNumero("por favor indique su segunda nota: ")
num3 = pedirNumero("Por favor indique su tercera nota: ")

promedio = calcularPromedioDetresNumeros(num1, num2, num3)

print(f"Su promedio con esas tres notas es de: {promedio}")