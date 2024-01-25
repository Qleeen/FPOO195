
# Práctica2: Sintaxis Python

#1. Comentarios

#soy un comentario de 1 línea

'''
soy un comentario de varias líneas
'''
#2. Cadenas
print("soy una cadena")
print('soy otra cadena')
#COncatenar cadenas mediante variables
a= 'mi artista es /n favorito es'
b= "Dani Flow" 
print(a+b)
print(a,b)

#contar los caracteres
print(len(a))

print(b[2:5])
print(b[:5])
print(b[2:])

#3 variables.

X= int(3)
y=str('3')
z=float(3.2)

print(X)
print(y)
print(z)

import random 
numero= random.randrange(1,15)
print(numero)

#4 solicitud de datos

var1= input('introduce cualquier dato')

var2= str(input('introduce cadenas'))

var3= int(input('introduce solo enteros'))

var4= float(input('introduce numeros decimales'))

print(var1, var2, var3, var4)

#5 booleans, operadores de comparacion y lógicos

#Van a regresar un true o un false
print(10> 9) #mayor que
print(10== 9) #igual que
print(10 >= 9) #mayor o igual que
print(10 != 9) #diferente de
print(10 <= 9) #menor o igual que

x=1
print(x < 5 and x < 10) #Si cumple la primera y si cumple la segunda
print(x < 5 or x < 10) #Si uno cumple o no
print(not(x < 5 and x < 10)) #invierte el resultado 

# Operaciones binarias & | 