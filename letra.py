letra= 0
palabra= str(input('Introduce una palabra'))
for i in range(len(palabra)):
    if palabra[i] == 'a' or palabra[i] == 'e' or palabra[i] == 'i' or palabra[i] == 'o' or palabra[i] == 'u':
        letra= letra+1
        
        