#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.
from utils import operacionesBasicas, pedirNumero

num1 = pedirNumero("por favor ingrese un primer numero: ")
num2 = pedirNumero("Por favor ingrese un segundo numero: ")

suma, resta, division , multiplicacion = operacionesBasicas(num1, num2)

print("Las operaciones basicas con esos numeros son las siguientes:")
print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multiplicacion}")
print(f"{num1} / {num2} = {division}")

