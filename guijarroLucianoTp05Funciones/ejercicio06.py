#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.
from utils import tablaMultiplicar

num = int(input("Por favor indique un numero para mostrarte su tabla: "))

tablaMultiplicar(num)