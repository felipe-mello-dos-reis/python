def harmonico_esquerda(n):
    i = 1
    harmonico = 0
    while i <= n:
        harmonico += 1/i
        i+=1
    print(harmonico)

def harmonico_direita(n):
    i = n
    harmonico = 0
    while i >= 1:
        harmonico += 1/i
        i-=1
    print(harmonico)
