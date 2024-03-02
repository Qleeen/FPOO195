class Personaje:
    
#atributo de personaje
#Declaramos el constructor para crear los objetos
    
    def __init__(self,esp,nom,alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
    
    #metodos del personaje
    def correr(self, estado):
        if(estado):
            print('el personaje' + self.__nombre+' esta corriendo')
        else:
            print('el personaje' + self.__nombre+' esta muerto')
    
    def lanzarGranada(self):
        print(self.__nombre+ 'Pego una granada')
        
    def __pensar(self, estado):
        print(self.__nombre +'Esta pensando')
  
            
#getters
    def getEspecie(self):
        return self.__especie
    
    def getNombre(self):
        return self.__nombre
    
    def getAltura(self):
        return self.__altura

#setters
    def setEspecie(self, esp):
        self.__especie= esp
    
    def setNombre(self, nom):
        self.__nombre= nom
    
    def setAltura(self, alt):
        self.__altura= alt

