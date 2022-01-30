x = int(input("Digite um número inteiro: "))
anterior = x%10
x=x//10
logic = False
while x > 0 and not logic:
	if x%10 == anterior:
		logic = True
	else:
		anterior = x%10
		x = x//10
if logic:
	print("sim")
else:
	print("não")
