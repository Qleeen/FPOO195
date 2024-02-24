# el * es para todo
from Personaje import *
from Armas import *
#creamos el objeto de la clase personaje 
spartan = Personaje()
Arma = Armas()

#usamos los atributos Spartan
print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

#usamos los metodos del spartan
spartan.correr(False)
spartan.lanzarGranada()

#usamos los metodos del arma
Arma.seleccionarArma(spartan.nombre)
Arma.recargarArma(65)
