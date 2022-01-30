class Buscador:
    def busca_sequencial(self, list, x):
        for i in range(len(list)):
            if list[i] == x:
                return i
        return -1

    def busca_binaria(self, list, x):
        first = 0
        last = len(list) - 1
        list.sort()
        while first <= last:
            m = (first + last)//2
            if x > list[m]:
                first = m + 1
            elif x < list[m]:
                last = m - 1
            else:
                return m
            return -1

