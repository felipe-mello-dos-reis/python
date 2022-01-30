num = int(input("Digite um número inteiro: "))
dez = num%100
dez = (dez-(dez%10))//10
print("O dígito das dezenas é",dez)
