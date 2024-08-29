def SecondLargestSmallest(a):
    a = sorted(a)
    return a[1], a[-2]


a = [3, 4, 2, 1, 5, 7]
print(SecondLargestSmallest(a))
