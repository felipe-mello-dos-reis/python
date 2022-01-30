def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2

    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    return merge(left, right)

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    
    if left[0] <  right[0]:
        return [left[0]] + merge(left[1:], right)

    return [right[0]] + merge[lefft,right[1:]]