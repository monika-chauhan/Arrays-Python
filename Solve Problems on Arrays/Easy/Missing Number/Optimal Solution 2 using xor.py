# Time = O(n)
# Space = O(1)
def Missing(a, n):
    xor1 = 0
    xor2 = 0
    for i in range(1, n - 1):
        xor1 = xor1 ^ a[i]
        xor2 = xor2 ^ (i + 1)
    xor2 = xor2 ^ n
    return xor1 ^ xor2


a = [1, 2, 3, 5]
n = 5
print(Missing(a, n))
