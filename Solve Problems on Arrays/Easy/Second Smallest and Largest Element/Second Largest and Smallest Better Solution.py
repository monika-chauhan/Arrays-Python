# Time complexity => O(n) + O(n) = O(2n)
def LargestSmallest(a):
    mini = secondMini = float('inf')
    maxi = secondMax = float('-inf')
    for i in range(len(a)):
        mini = min(mini,a[i])
        maxi = max(maxi,a[i])

    for i in range(len(a)):
        if a[i] < secondMini and a[i] != mini:
            secondMini = a[i]

        if a[i] > secondMax and a[i] != maxi:
            secondMax = a[i]
    return secondMax,secondMini

a = [1,2,3,4,5,6,7,8,9]
print(LargestSmallest(a))