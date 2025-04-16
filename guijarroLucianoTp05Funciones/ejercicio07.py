from utils import operacionesBasicas, pedirNumero

num1 = pedirNumero("por favor ingrese un primer numero: ")
num2 = pedirNumero("Por favor ingrese un segundo numero: ")

suma, resta, division , multiplicacion = operacionesBasicas(num1, num2)

print("Las operaciones basicas con esos numeros son las siguientes:")
print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multiplicacion}")
print(f"{num1} / {num2} = {division}")

