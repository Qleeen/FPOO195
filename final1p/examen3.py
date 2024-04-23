#Ejercicio 3
pedido= input("Ingrese 10 números separados por comas y sin espacios: ").split(",")
while len(pedido) != 10:
    pedido = input("Introduce 10 números separados por comas y sin espacios: ").split(",")
print("Lista original:", pedido)
opcion = input("Elija una opción: 1. Imprimir lista invertida 2. Imprimir lista sin números repetidos 3. Ambas listas en una: ")
if opcion == "1":
    pedido.reverse()
    print("Lista invertida:", pedido)
elif opcion == "2":
    pedido = list(set(pedido))
    print("Lista sin números repetidos:", pedido)
elif opcion == "3":
    pedido.reverse()
    print("Lista invertida:", pedido)
    pedido = list(set(pedido))
    print("Lista sin números repetidos:", pedido)  
    
opcion = input("Elija una opción: 1. Imprimir lista invertida 2. Imprimir lista sin números repetidos 3. Ambas listas en una: ")
if opcion == "1":
    pedido.reverse()
    print("Lista invertida:", pedido)
elif opcion == "2":
    pedido = list(set(pedido))
    print("Lista sin números repetidos:", pedido)
elif opcion == "3":
    pedido.reverse()
    print("Lista invertida:", pedido)
    pedido = list(set(pedido))
    print("Lista sin números repetidos:", pedido)  