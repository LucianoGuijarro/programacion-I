#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
from utils import calcularIMC

peso = int(input("Por favor indique su peso en kg: "))
altura = float(input("Por favor indique su altura en metros: "))

imc = calcularIMC(peso, altura)

print(f"Su IMC es de: {imc}")