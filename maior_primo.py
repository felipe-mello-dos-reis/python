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

def maior_primo(n):
    primo = i = 2
    while i <= n:
        if e_primo(i):
            primo = i
        i+=1
    return(primo)