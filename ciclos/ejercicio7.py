
base = int(input("Ingrese la cantidad de copoes que desea para su base: "))
z = base - 1
x = 1

while z >= 0:
    print(' ' * z + '*' * x + ' ' * z)
    x += 2
    z -= 1