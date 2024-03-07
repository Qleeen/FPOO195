class Humano:
    def __init__(self):
        self.__listaBD = []
        
    def Insertar(self, id, correo, Password):
        self.__listaBD.append({"Id": id, "corr": correo, "pass": Password})
        
    def validar(self, correo, Password):
        for usuario in self.__listaBD:
            if usuario["corr"] == correo and usuario["pass"] == Password:
                return True
        return False