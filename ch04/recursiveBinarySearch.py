# EXERCISES 4.4 
# Remember binary search from chapter 1? It's a divide-and-conquer
# algorithm, too. Can you come up with the base case and recursive
# case for binary search?
def recursiveBinarySearch(list, item):
    return findItemInRange(list, item, 0, len(list))

def findItemInRange(list, item, start, end):
    if start == end - 1: return start if list[start] == item else -1
    mid = (start + end) // 2
    if list[mid] == item: return mid
    elif list[mid] > item: end = mid
    elif list[mid] < item: start = mid
    return findItemInRange(list, item, start, end)

testList = [3, 4, 5, 6, 7, 8]
item = 1
print("find index of {} in the list: {}".format(item, recursiveBinarySearch(testList, item)))
item = 2
print("find index of {} in the list: {}".format(item, recursiveBinarySearch(testList, item)))
item = 3
print("find index of {} in the list: {}".format(item, recursiveBinarySearch(testList, item)))
item = 4
print("find index of {} in the list: {}".format(item, recursiveBinarySearch(testList, item)))
item = 5
print("find index of {} in the list: {}".format(item, recursiveBinarySearch(testList, item)))
item = 6
print("find index of {} in the list: {}".format(item, recursiveBinarySearch(testList, item)))
item = 7
print("find index of {} in the list: {}".format(item, recursiveBinarySearch(testList, item)))
item = 8
print("find index of {} in the list: {}".format(item, recursiveBinarySearch(testList, item)))
item = 9
print("find index of {} in the list: {}".format(item, recursiveBinarySearch(testList, item)))
item = 10
print("find index of {} in the list: {}".format(item, recursiveBinarySearch(testList, item)))
