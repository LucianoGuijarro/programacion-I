from utils import calcularIMC

peso = int(input("Por favor indique su peso en kg: "))
altura = float(input("Por favor indique su altura en metros: "))

imc = calcularIMC(peso, altura)

print(f"Su IMC es de: {imc}")