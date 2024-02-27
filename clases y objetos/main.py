# el * es para todo
from Personaje import *
from Armas import *

#solicitar datos Spartan
nombreS= input('Escribe el nombre de tu Spartan')
especieS= input('Escribe la especie de tu Spartan')
alturaS= float(input('Escribe la altura de tu Spartan'))

#solicitar datos de Nemesis
nombreN= input('Escribe el nombre de tu Nemesis')
especieN= input('Escribe la especie del Nemesis')
alturaN= float(input('Escribe la altura del Nemesis'))


#creamos el objeto de la clase personaje 
Spartan = Personaje(especieS,nombreS,alturaS)
Nemesis = Personaje(especieN,nombreN,alturaN)
Arma= Armas()

#usamos los atributos Spartan
print(Spartan.nombre)
print(Spartan.especie)
print(Spartan.altura)

#usamos los metodos del spartan
Spartan.correr(False)
Spartan.lanzarGranada()

#usamos los metodos del arma
Arma.seleccionarArma(Spartan.nombre)
Arma.recargarArma(65)
