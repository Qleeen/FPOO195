class contraseña:
    def __init__(self, longitud, mayusculas, caracteres_especiales):
        self.longitud = longitud
        self.mayusculas = mayusculas
        self.caracteres_especiales = caracteres_especiales

    def generar_contraseña(self):
        import random
        import string

        chars = string.ascii_lowercase
        if self.mayusculas:
            chars += string.ascii_uppercase
        if self.caracteres_especiales:
            chars += string.punctuation

        password = ''.join(random.choice(chars) for _ in range(self.longitud))
        return password

    def verificar_fortaleza(self, password):
        if len(password) >= 8:
            return "Fuerte"
        else:
            return "Débil"


