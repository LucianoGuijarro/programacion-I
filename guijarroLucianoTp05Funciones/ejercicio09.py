from utils import celsiusAFahrenheit

temperaturaCelsiu = float(input("Por favor indique la temperatura en grados Celsius: "))

temperaturaFahrenheit = celsiusAFahrenheit(temperaturaCelsiu)

print(f"Su temperatura convertida a Fahrenheit es de: {temperaturaFahrenheit} grados F")