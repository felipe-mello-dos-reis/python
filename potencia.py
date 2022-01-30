def main():
	n = int(input())
	k = int(input())
	resultado = 1
	while k >= 1:
		resultado = resultado*n
		k = k-1
	print(resultado)

main()
