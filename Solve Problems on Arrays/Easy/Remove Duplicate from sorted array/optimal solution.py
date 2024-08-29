# Two Pointer approach
def removeDuplicate(a):
    i = 0
    for j in range(i, len(a) - 1):
        if a[i] != a[j]:
            i += 1
            a[i] = a[j]
    return i + 1


def printArr(a):
    k = removeDuplicate(a)
    for i in range(k):
        print(a[i], end=' ')


a = [1, 1, 2, 2, 2, 3, 4]
printArr(a)
