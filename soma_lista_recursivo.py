def soma_lista(lista):
    if len(lista)>1:
        lista[0]+=lista.pop()
        return soma_lista(lista)
    else:
        return lista[0]

print(soma_lista([0,1,2,3,4,5]))