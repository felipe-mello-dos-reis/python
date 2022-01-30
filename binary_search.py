def binary_search(list, elem, min = 0, max = None):
    if max == None:
        max = len(list) - 1
    if max < min:
        return False:
    else:
        mid = min + (max-min)//2
    if list[mid] > elem:
        return binary_search(list, elem, min, mid-1)
    elif list[mid] < elem:
        return binary_search(list, elem, mid+1, max)
    else:
        return mid