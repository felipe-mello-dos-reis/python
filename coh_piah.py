import re

def le_assinatura():
    # '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos# '''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:\n")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    # '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento# '''
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

def separa_sentencas(texto):
    # '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto# '''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    # '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca# '''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    # '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase# '''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    # '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez# '''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    # '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas# '''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    # '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.# '''
    similaridade = 0
    for i in range(6):
        similaridade += abs(as_a[i] - as_b[i])
    return similaridade/6

def calcula_assinatura(texto):
    # '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.# '''
    wal = ttr = hlr = sal = sac = pal = n_palavras = n_char = 0
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        lista_frases = separa_frases(sentenca)
        sac += len(lista_frases)
        for frase in lista_frases:
            lista_palavras = separa_palavras(frase)
            ttr += n_palavras_diferentes(lista_palavras)
            hlr += n_palavras_unicas(lista_palavras)
            n_palavras += len(lista_palavras)
            for palavra in lista_palavras:
                n_char += len(palavra)
    wal = n_char / n_palavras
    ttr /= n_palavras
    hlr /= n_palavras
    sal = n_char / len(sentencas)
    pal = n_char / sac
    sac /= len(sentencas)

    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    # '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.# '''
    similaridade = []
    for texto in textos:
        similaridade.append(compara_assinatura(ass_cp, calcula_assinatura(texto)))
    infectado = 0
    for i in range(len(similaridade)):
        if similaridade[i] < similaridade[infectado]:
            infectado = i
    return infectado + 1
    


def main():
    ass_cp =le_assinatura()
    textos = le_textos()
    print("\nO autor do texto %d está infectado com COH-PIAH" %avalia_textos(textos, ass_cp))
main()
