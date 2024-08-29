def leftRotate(a, d, n):
    d = d % n
    temp1 = a[:d]
    temp2 = a[d:]
    return temp2 + temp1


a = [1, 2, 3, 4, 5]
print(leftRotate(a, 3, len(a)))


def lRotate(a, d, n):
    d = d % n
    a1 = a[:d]
    a2 = a[d:]
    a = a1[::-1] + a2[::-1]
    return a[::-1]


a = [1, 2, 3, 4, 5]
print(lRotate(a, 3, len(a)))
