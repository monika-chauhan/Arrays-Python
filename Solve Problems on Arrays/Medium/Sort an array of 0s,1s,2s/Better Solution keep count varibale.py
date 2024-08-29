def Sort0s1s2s(a):
    c0 = c1 = c2 = 0
    for i in range(len(a)):
        if a[i] == 0:
            c0 += 1
        elif a[i] == 1:
            c1 += 1
        else:
            c2 += 1

    a = [0] * c0 + [1] * c1 + [2] * c2
    return a


a = [1, 0, 2, 1, 2, 0]
print(Sort0s1s2s(a))
