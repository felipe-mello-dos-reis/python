import math
def main():
    x = int(input("Digite um número inteiro: "))
    aux = 2
    primo = True
    while aux <= math.sqrt(x) and primo:
        if x%aux == 0:
            primo = False
        else:
            aux+=1
    if primo:
        print("primo")
    else:
        print("não primo")
main()
