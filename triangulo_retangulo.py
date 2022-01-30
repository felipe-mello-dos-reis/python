class Triangulo:
    def __init__(self,a,b,c):
        self.a = a 
        self.b  = b
        self.c  = c
    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return 'equilátero'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return 'isóceles'
        else:
            return 'escaleno'
    def perimetro(self):
        return self.a + self.b + self.c
    def retangulo(self):
        if (self.a**2 == self.b**2 + self.c**2) or (self.b**2 == self.c**2 + self.a**2) or (self.c**2 == self.a**2 + self.b**2):
            return True
        else:
            return False
