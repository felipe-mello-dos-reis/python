def insertion_sort(list):
    if (len(list)) == 1:
        return list
    for i in range(1,len(list),1):
        j = i-1
        k = i
        while list[k] < list[j] and k >= 0 and j >= 0:
            list[k],list[j] = list[j],list[k]
            j-=1
            k-=1
    return list
