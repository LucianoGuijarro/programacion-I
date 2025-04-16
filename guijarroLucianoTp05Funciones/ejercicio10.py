#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.
from utils import calcularPromedioDeTresNumeros, pedirNumero

num1 = pedirNumero("Por favor ingrese su primera nota: ")
num2 = pedirNumero("por favor indique su segunda nota: ")
num3 = pedirNumero("Por favor indique su tercera nota: ")

promedio = calcularPromedioDeTresNumeros(num1, num2, num3)

print(f"Su promedio con esas tres notas es de: {promedio}")