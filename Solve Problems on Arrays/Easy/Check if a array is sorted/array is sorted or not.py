# time complexity = O(n)
def checkSortedArr(a):
    for i in range(len(a) - 1): #--- O(n)
        if a[i] > a[i + 1]:
            return False
    return True


a = [3, 4, 2, 1, 5]
print(checkSortedArr(a))
b = [1,2,3,4,5]
print(checkSortedArr(b))
