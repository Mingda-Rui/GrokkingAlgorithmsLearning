# EXERCISES 4.2 
# Write a recursive function to count the number of items in a list.
def count(arr):
    if len(arr) <= 1: return 1
    return 1 + count(arr[1:])

testList = [1, 2, 3, 4, 5]
print("count the lenth of list: {}".format(count(testList)))