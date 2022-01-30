def ordena(list):
    for i in range(len(list) - 1):
        lowest = i
        j = i+1
        while j < len(list):
            if list[j] < list[lowest]:
                lowest = j
            j+=1
        list[i],list[lowest] = list[lowest],list[i]
    return list