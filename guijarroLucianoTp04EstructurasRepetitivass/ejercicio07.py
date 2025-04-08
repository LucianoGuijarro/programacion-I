#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

numero = int(input("Por favor ingrese un numero entero positivo: "))
suma = 0

for i in range(0, numero):
    suma = suma + i

print(f"La suma de los numeros comprendidos desde 0 hasta ese numero es de {suma}")