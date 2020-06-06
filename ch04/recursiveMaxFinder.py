# EXERCISES 4.3
# Find the maximum number in a list
def findMax(arr):
    if len(arr) <= 1: return arr[0]
    maxInRest = findMax(arr[1:])
    return arr[0] if arr[0] > maxInRest else maxInRest

def max_answer(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list [0] > sub_max else sub_max

testList = [1, 2, 3, 4, 5]
print("max element: {}".format(findMax(testList)))
testList = [2, 3, 7, 9, 8]
print("max element: {}".format(findMax(testList)))