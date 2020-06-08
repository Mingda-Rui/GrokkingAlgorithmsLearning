def quicksort(array):
    if len(array) <= 1: return array
    pivot = array[0]
    less = []
    greater = []
    for ele in array[1:]:
        if ele < pivot: less.append(ele)
        else: greater.append(ele)
    print("pivot: {}".format(pivot))
    print(less)
    print(greater)
    return quicksort(less) + [pivot] + quicksort(greater)

# def quicksort_notWorking(array):
#     if len(array) <= 1: return array
#     if len(array) == 2: return array if array[0] <= array[1] else [array[1], array[0]]
#     pivotIndex = 0
#     for i in range(1, len(array)):
#         if array[i] < array[pivotIndex]:
#             temp = array[pivotIndex]
#             array[pivotIndex] = array[i]
#             array[i] = array[pivotIndex + 1]
#             array[pivotIndex + 1] = array[pivotIndex]
#             pivotIndex += 1

#     less = quicksort(array[0:pivotIndex])
#     greater = quicksort(array[pivotIndex+1:])
#     print("pivot: {}".format(array[pivotIndex]))
#     print(less)
#     print(greater)
#     return less + [array[pivotIndex]] + greater

print( quicksort([10, 5, 2, 3]) )
