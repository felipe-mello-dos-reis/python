def primeiro_lex(lista):
    primeiro = lista[0]
    for frase in lista:
        if frase < primeiro:
            primeiro = frase
    return primeiro
        