def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

def sumRecursive(arr):
    if len(arr) <= 1: return arr[0]
    return arr[0] + sumRecursive(arr[1:])

testList = [1, 2, 3, 4, 5]
print("sum: {}".format(sum(testList)))
print("recursive sum: {}".format(sumRecursive(testList)))