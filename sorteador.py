import random

def sorteio_num():
    inf = int(input("Digite o limite inferior: ")) 
    sup = int(input("Digite o limite superior: ")) 
    print("O valor sorteado é: "+str(random.randrange(inf, sup)))

def sorteio_nomes(lista):
    for i in range(int(input("Quantos nomes deseja sortear? "))):
        if len(lista) == 1:
            print(lista.pop())
            return
        else:
            print(lista.pop(random.randrange(0,len(lista)-1)))

def main():
    print("SORTEADOR\n\nEscolha o sorteio:\n1. Sorteio de números\n2. Sorteio de nomes")
    cmd=int(input())
    if cmd == 1:
        sorteio_num()
    elif cmd == 2:
        lista=[]
        nome=input("Digite um nome da lista ou precione enter quando terminar: ")
        while nome != "":
            lista.append(nome)
            nome=input("Digite um nome da lista ou precione enter quando terminar: ")
        sorteio_nomes(lista)
    else:
        print("Entrada inválida")

if __name__ == "__main__":
    main()

