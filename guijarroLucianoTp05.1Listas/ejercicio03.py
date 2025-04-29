#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
#ejemplo:

lista = []

for i in range(1, 3 + 1):
    palabraNueva = input("Por favor agrega un elemento a la lista: ")
    lista.append(palabraNueva)

print(lista)