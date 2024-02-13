def lista_random():
    import random
    lista_num= []
    for i in range(30):
        lista_num.append(random.randint(1, 20))
    return lista_num

def val_repetidos(lista_num):
    return{n : lista_num.count(n) for n in lista_num}

print(val_repetidos(lista_random()))