x = int(input("Digite um número inteiro: "))
sum = 0
while x != 0:
	sum +=  x%10
	x = x//10
print(sum)
