#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
from utils import segundosAHoras

segundos = int(input("Por favor ingrese una cantidad de segundos para saber cuantas horas son: "))
horas = segundosAHoras(segundos)

print(f"Esos segundos equivales a {horas} horas.")