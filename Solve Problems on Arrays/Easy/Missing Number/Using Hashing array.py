# time = O(n)
# Space = O(n)
def Missing(a, n):
    hashing = [i for i in range(1, n + 1)]
    for i in range(len(hashing)):
        if hashing[i] not in a:
            return hashing[i]
    return -1


a = [1, 3]
n = 3
print(Missing(a, n))
