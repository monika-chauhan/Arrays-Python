# time complexity - O(n) + O(nlogn) = O(nlogn)
def SecondLargest(a):
    maxi = max(a)
    mini = min(a)
    a = sorted(a)
    for i in range(len(a) - 1, -1, -1):
        if a[i] != maxi:
            secondMaxi = a[i]
            break
    for i in range(len(a)):
        if a[i] != mini:
            secondMini= a[i]
            break
    return secondMaxi,secondMini


a = [3, 4, 2, 5, 6, 9, 9, 9]

print(SecondLargest(a))
