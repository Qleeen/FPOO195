#ejercicio 5
lista = input("Ingresa números separados por comas y sin espacios: ").split(",")
while len(lista) < 1:
    lista = input("Ingreseanúmeros separados por comas y sin espacios: ").split(",")
pares = 0
impares = 0
for i in lista:
    if int(i) % 2 == 0:
        pares += int(i)
    else:
        impares += int(i)
print("Sumatoria de pares:", pares)
print("Sumatoria de impares:", impares)
