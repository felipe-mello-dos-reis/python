import random
def lista_grande(n):
    list = []
    for i in range(n):
        list.append(random.randrange(n))
    return list