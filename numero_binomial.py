def fat(n):
	fat = 1
	while n > 1:
		fat = fat*n
		n = n-1
	return fat

def main():
    n = int(input("Digite o valor de n: "))
    k = int(input("Digite o valor de k: "))
    print(int(fat(n)/(fat(n-k)*fat(k))))
main()