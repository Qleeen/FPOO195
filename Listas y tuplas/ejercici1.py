def capturar_numeros():
    numeros = []
    n= int(input("Ingrese la cantidad de números que desea capturar: "))
    for i in range(n):
        numero = int(input("Ingrese un número: "))
        numeros.append(numero)
    return tuple(numeros)

def sumatoria(numeros):
    return sum(numeros)

def numero_mayor(numeros):
    return max(numeros)

def numero_menor(numeros):
    return min(numeros)

def promedio(numeros):
    return sum(numeros) / len(numeros)

def moda(numeros):
    contador = {}
    for numero in numeros:
        if numero in contador:
            contador[numero] += 1
        else:
            contador[numero] = 1
    moda = max(contador, key=contador.get)
    return moda

def rango(numeros):
    return max(numeros) - min(numeros)

def mostrar_menu():
    print("Menú funcional:")
    print("1. Sumatoria de los elementos de la lista")
    print("2. Numero mayor de la lista")
    print("3. Numero menor de la lista")
    print("4. Promedio")
    print("5. Moda")
    print("6. Rango")
    print("0. Salir")

def main():
    numeros = capturar_numeros()
    opcion = None
    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            print("Sumatoria:", sumatoria(numeros))
        elif opcion == 2:
            print("Número mayor:", numero_mayor(numeros))
        elif opcion == 3:
            print("Número menor:", numero_menor(numeros))
        elif opcion == 4:
            print("Promedio:", promedio(numeros))
        elif opcion == 5:
            print("Moda:", moda(numeros))
        elif opcion == 6:
            print("Rango:", rango(numeros))
        elif opcion == 0:
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()