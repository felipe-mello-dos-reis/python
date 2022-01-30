def busca(list, elem):
    for i in range(len(list)):
        if list[i] == elem:
            return i
    return False
