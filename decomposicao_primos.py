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

def fator(n):
    primo = i = 2
    logic = False
    while i <= n and not logic:
        if e_primo(i) and n%i == 0:
            primo = i
            logic = True
        i+=1
    return(primo)

def multiplicidade(n, primo):
    i = 0
    while n > 1:
        if n%primo == 0:
            i+=1
            n/=primo
        else:
            break
    return i

n = int(input())
print(n,"=", end = " ")
while n > 1:
    print(fator(n), end = "")
    i = multiplicidade(n, fator(n))
    if i != 1:
        print("^%d" %i, end = "")
    while i >= 1:
        n = n/fator(n)
        i-=1
    if n != 1:
        print(" *", end = " ")

