#Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla.

dobles = []

def agregarDoble(num):
    dobles.append(num*2)

for i in range(3):
    num = int(input("Por favor indica el doble de que numero quieres agregar: "))
    agregarDoble(num)

print(dobles)
