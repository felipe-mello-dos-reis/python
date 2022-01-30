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
    def semelhantes(self, other):
        t1 = []
        t2 = []
        t1.append(self.a)
        t1.append(self.b)
        t1.append(self.c)
        t1.sort()
        t2.append(other.a)
        t2.append(other.b)
        t2.append(other.c)
        t2.sort()
        if t1[0]/t2[0] == t1[1]/t2[1] and t1[1]/t2[1] == t1[2]/t2[2]:
            return True
        else:
            return False