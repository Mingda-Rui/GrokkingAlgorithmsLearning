def mergeSort(array):
    if len(array) <= 1: return array
    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])
    return merge(left, right) 

def merge(left, right):
    merged = []
    indexL = indexR = 0
    while indexL < len(left) and indexR < len(right):
        if left[indexL] < right[indexR]:
            merged.append(left[indexL])
            indexL += 1
        else:
            merged.append(right[indexR])
            indexR += 1

    tail = right[indexR:] if indexL == len(left) else left[indexL:]
    merged.extend(tail)
    return merged

list = [1, 3, 2, 5, 4, 8, 5, 9]
print(mergeSort(list))

list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(mergeSort(list))