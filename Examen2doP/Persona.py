class Persona:
    def __init__(self, AñoCurso, añoNacimiento, nombre, apellidoPaterno, apellidoMaterno, Carrera):
        self.AñoCurso = AñoCurso
        self.añoNacimiento = añoNacimiento
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.Carrera = Carrera
          
    def generarMatricula(self):
        matricula = str(self.AñoCurso) + str(self.añoNacimiento) + self.nombre[0:1] + self.apellidoPaterno[0:1] + self.apellidoMaterno[0:1] + self.Carrera[0:3]
        return matricula