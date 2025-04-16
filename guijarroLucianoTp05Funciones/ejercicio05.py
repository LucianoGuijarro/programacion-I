from utils import segundosAHoras

segundos = int(input("Por favor ingrese una cantidad de segundos para saber cuantas horas son: "))
horas = segundosAHoras(segundos)

print(f"Esos segundos equivales a {horas} horas.")