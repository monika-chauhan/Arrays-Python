def SecondSmallest(a):
    small = secondSmall = float('inf')
    for i in range(len(a)):
        if a[i] < small:
            secondSmall = small
            small = a[i]
        elif a[i] < secondSmall and a[i] != small:
            secondSmall = a[i]
    return secondSmall


a = [1, 2, 3, 4, 5]
print(SecondSmallest(a))


def SecondLargest(a):
    maxi = secondMaxi = float('-inf')
    for i in range(len(a)):
        if a[i] > maxi:
            secondMaxi = maxi
            maxi = a[i]
        elif a[i] > secondMaxi and a[i] != maxi:
            secondMaxi = a[i]
    return secondMaxi


a = [1, 2, 3, 5, 6, 7]
print(SecondLargest(a))
