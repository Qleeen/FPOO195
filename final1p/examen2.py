#ejercicio 1
palabras = input("Introduce 6 palabras separadas por comas y sin espacios: ").split(",")
while len(palabras) != 6:
    palabras = input("Introduce 6 palabras separadas por comas y sin espacios: ").split(",")
print("Lista original:", palabras)
palabras.sort()
print("Lista ordenada:", palabras)


