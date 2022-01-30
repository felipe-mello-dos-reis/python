def inverte(lista):
    lista_invertida = []
    for i in range(len(lista)):
        lista_invertida.append(lista[-1-i])
    return lista_invertida

lista = []
x = int(input("Digite um número: "))
while x != 0:
    lista.append(x)
    x = int(input("Digite um número: "))
lista_invertida = inverte(lista)
for i in lista_invertida:
    print(i)
