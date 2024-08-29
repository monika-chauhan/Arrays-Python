def rightRotate(a, d, n):
    d = d % n
    a1 = a[n-d:]
    a2 = a[:n-d]
    return a1 + a2


a = [1, 2, 3, 4, 5]
print(rightRotate(a, 3, len(a)))
