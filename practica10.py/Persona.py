class Persona:
    def __init__(self, nom, id, pat, mat, corr, cont):
        self.__id = id
        self.__nombre = nom
        self.__apellidoP = pat 
        self.__apellidoM = mat 
        self.__correo = corr 
        self.__contrasena = cont
    
    def agregar(self, nom, pat, mat, corr, cont):
        self.__id= id
        self.__nombre = nom
        self.__apellidoP = pat 
        self.__apellidoM = mat 
        self.__correo = corr 
        self.__contrasena = cont
        print('Se ha agregado un nuevo usuario')
    
    def consultar(self):
        print('ID:', self.__id)
        print('Nombre:', self.__nombre)
        print('Apellido Paterno:', self.__apellidoP)
        print('Apellido Materno:', self.__apellidoM)
        print('Correo:', self.__correo)
        print('Contrasena:', self.__contrasena)
    
    def modificar(self, nom, pat, mat, corr, cont):
        self.__id= id
        self.__nombre = nom
        self.__apellidoP = pat 
        self.__apellidoM = mat 
        self.__correo = corr 
        self.__contrasena = cont
        print('Se ha modificado el usuario')
    
    def eliminar(self):
        self.__id = ''
        self.__nombre = ''
        self.__apellidoP = ''
        self.__apellidoM = ''
        self.__correo = ''
        self.__contrasena = ''
        print('Se ha eliminado el usuario')
        
#getters
    def getId(self):
        return self.__id
    def getNombre(self, nom):
        return self.__nombre
    def getApellidoP(self):
        return self.__apellidoP
    def getApellidoM(self):
        return self.__apellidoM
    def getCorreo(self):
        return self.__correo
    def getContrasena(self):
        return self.__contrasena    
    
#Setters 
    def setId(self, id):
        self.__id = id     
    def setNombre(self, nom):
        self.__nombre = nom
    def seetApellidoP(self, pat):
        self.__apellidoP = pat
    def setApellidoM(self, mat):
        self.__apellidoM = mat
    def setCorreo(self, corr):
        self.__correo = corr
    def setContrasena(self, cont):
        self.__contrasena = cont