def busca(list, x):
    first = 0
    last = len(list) - 1
    list.sort()
    while first <= last:
        m = (first + last)//2
        print(m)
        if x > list[m]:
            first = m + 1
        elif x < list[m]:
            last = m - 1
        else:
            return m
    return False

