palabra = input('Ingrese una palabra: ')
contador_voc = 0
for letra in palabra:
    if letra.lower() in 'aeiou':
        contador_voc += 1
        print(f'La palabra {palabra} tiene {contador_voc} vocales')