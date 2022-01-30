import math
def e_primo(x):
    aux = 2
    primo = True
    while aux <= math.sqrt(x) and primo:
        if x%aux == 0:
            primo = False
        else:
            aux+=1
    if primo:
        return True
    else:
        return False

def n_primos(n):
    cont = 0
    while n > 1:
        if e_primo(n):
            cont+=1
        n-=1
    return cont