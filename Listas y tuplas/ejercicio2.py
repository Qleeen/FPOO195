def lista_random():
    import random
    lista_num= []
    for i in range(30):
        lista_num.append(random.randint(1, 20))
    return lista_num

def val_repetidos(lista_num):
    return{n : lista_num.count(n) for n in lista_num if lista_num.count(n) > 1}

def eliminar_repetidos(lista_num):
    return list(set(lista_num))

def remplazar(lista_num):
    return [0 if lista_num.count(n) > 1 else n for n in lista_num]

def mostrar_menu():
    print("Menú funcional:")
    print("1. Generar lista aleatoria")
    print("2. Ver la lista")
    print("3. Ver valores repetidos")
    print("4. Eliminar valores repetidos")
    print("5. Remplazar valores repetidos con 0")
    print("0. Salir")
    
def main():
    lista = []
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            lista = lista_random()
        elif opcion == 2:
            print(lista)
        elif opcion == 3:
            print(val_repetidos(lista))
        elif opcion == 4:
            lista = eliminar_repetidos(lista)
        elif opcion == 5:
            lista = remplazar(lista)
        elif opcion == 0:
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()