#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva 
# el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el 
# perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
from utils import calcularAreaCirculo, calcularPerimetroCirculo

radio = int(input("Por favor indique el radio de un circulo para saber su permitro y su area: "))

area = calcularAreaCirculo(radio)
permimetro = calcularPerimetroCirculo(radio)

print(f"El area del circulo es de {area} y el perimetro es de {permimetro}")