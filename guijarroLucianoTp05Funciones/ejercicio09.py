#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.
from utils import celsiusAFahrenheit

temperaturaCelsiu = float(input("Por favor indique la temperatura en grados Celsius: "))

temperaturaFahrenheit = celsiusAFahrenheit(temperaturaCelsiu)

print(f"Su temperatura convertida a Fahrenheit es de: {temperaturaFahrenheit} grados F")