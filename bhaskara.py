import math
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
delta = b**2 - 4*a*c

if delta > 0:
	raiz1 = (-b - math.sqrt(delta))/(2*a)
	raiz2 = (-b + math.sqrt(delta))/(2*a)
	print("as raízes da equação são", raiz1, "e", raiz2)
if delta == 0:
	raiz = -b/(2*a)
	print("a raiz dupla desta equação é", raiz)
if delta < 0:
#	real = -b/(2*a)
#	imaginaria = math.sqrt(-delta)/(2*a)
#	print("As raízes de", a, "x^2 +", b, "x +", c, "são:")
#	print("x1 =", real,"+",imaginaria,"i")
#	print("x2 =", real,"-",imaginaria,"i")
	print("esta equação não possui raízes reais")
