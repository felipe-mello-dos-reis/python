def remove_repetidos(lista):
    lista.sort()
    n = len(lista)
    i = 0
    while i < n - 1:
        if lista[i] == lista[i+1]:
            del(lista[i])
            n-=1
            i-=1
        i+=1
    return lista