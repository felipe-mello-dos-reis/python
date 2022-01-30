def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    cmd = int(input("2 - para jogar um campeonato "))
    #print()
    if cmd == 1:
        print("\nVoce escolheu uma partida!\n")
        #print()
        partida()
    else:
        print("\nVoce escolheu um campeonato!")
        #print()
        campeonato()

def computador_escolhe_jogada(n,m):
#pequenas, não chamam outras funções. Devolve numero de peças retiradas
    peças = 0
    i = 1
    while i < m and peças == 0:
        if (n-i)%(m+1) == 0:
            peças = i
        else:
            i+=1
    peças = i    
    if peças == 1:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou", peças,"peças")
    if n - peças == 0:
        return peças
    if n - peças == 1:
        print("Agora resta apenas uma peça no tabuleiro.\n")
    else:
        print("Agora restam",n-peças,"peças no tabuleiro.\n")
    return peças

def usuario_escolhe_jogada(n,m):
    peças = int(input("Quantas peças você vai tirar? "))
    while peças < 1 or peças > m:
        print("\nOops! Jogada inválida! Tente de novo.\n")
        peças = int(input("Quantas peças você vai tirar? "))
        print()
    if peças == 1:
        print("Você tirou uma peça.")
    else:
        print("Você tirou", peças,"peças")
    if n - peças == 0:
        return peças
    if n - peças == 1:
        print("Agora resta apenas uma peça no tabuleiro.\n")
    else:
        print("Agora restam",n-peças,"peças no tabuleiro.\n")
    return peças

def partida():
#pergunta n, m. Decide quem comeca, chama escolhe jogada alternadamente (laço). Altera valor de n. Identifica que o jogo acabou (n==0)
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n%(m+1) == 0:
        print("\nVoce começa!\n")
        while n > 0:
            n -= usuario_escolhe_jogada(n,m)
            if n == 0:
                print("Fim do jogo! Voce ganhou!")
                return False
            else:
                n -= computador_escolhe_jogada(n,m)
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return True
    else:
        print("\nComputador começa!\n")
        while n > 0:
            n -= computador_escolhe_jogada(n,m)
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return True
            else:
                n -= usuario_escolhe_jogada(n,m)
            if n == 0:
                print("Fim do jogo! Voce ganhou!")
                return False

def campeonato():
    vitorias_computador = vitorias_usuario = 0
    i = 1
    while i <= 3:
        print("\n**** Rodada", i, "****\n")
        if partida():
            vitorias_computador+=1
        else:
            vitorias_usuario+=1
        i+=1
    print("**** Final do campeonato! ****\n")
    print("Placar: Você", vitorias_usuario, "X", vitorias_computador, "Computador")

main()