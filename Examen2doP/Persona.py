class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, añoNacimiento, Carrera, AñoCurso):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.añoNacimiento = añoNacimiento
        self.Carrera = Carrera
        self.AñoCurso = AñoCurso    
    def generarMatricula(self):
        matricula = self.nombre[0:1] + self.apellidoPaterno[0:1] + self.apellidoMaterno[0:1] + str(self.añoNacimiento) + self.Carrera[0:3]  + str(self.AñoCurso)
        return matricula