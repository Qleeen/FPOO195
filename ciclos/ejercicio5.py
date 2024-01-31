frase=input('Escriba una frase: ')
letra=input('Escriba una letra: ')
cuenta = 0
for i in frase:
    if i==letra:
        cuenta=cuenta+1

print('La letra',letra,'aparece',cuenta,'veces')