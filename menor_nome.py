def menor_nome(lista):
    lista[0] = lista[0].strip()
    tamanho = len(lista[0])
    menor = lista[0]
    for nome in lista:
        nome = nome.strip()
        if len(nome) < tamanho:
            tamanho = len(nome)
            menor = nome
    return menor.capitalize()

