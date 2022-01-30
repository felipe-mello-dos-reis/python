import time
def bubble_sort(list):
    t0 = time.time()
    for i in range(len(list) - 1, 0, -1):
        trocou = False
        for j in range(i):
            if list[j] > list[j+1]:
                trocou = True
                list[j],list[j+1] = list[j+1],list[j]
                print(list)
        if not trocou:
            t1 = time.time()
         #   print("time =", t1-t0)
            return list
    t1 = time.time()
    return list
