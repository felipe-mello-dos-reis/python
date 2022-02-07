def ordenada(list):
    prev = list[0]
    for item in list:
        if item < prev:
            return False
        else:
            prev = item
    return True
#ohana
