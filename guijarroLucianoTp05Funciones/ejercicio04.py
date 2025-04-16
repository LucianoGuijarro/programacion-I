from utils import calcularAreaCirculo, calcularPerimetroCirculo

radio = int(input("Por favor indique el radio de un circulo para saber su permitro y su area: "))

area = calcularAreaCirculo(radio)
permimetro = calcularPerimetroCirculo(radio)

print(f"El area del circulo es de {area} y el perimetro es de {permimetro}")