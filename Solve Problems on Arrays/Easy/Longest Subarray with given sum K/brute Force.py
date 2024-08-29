# Time = O(n^3)
def LongestSubarrayN3(a, K):
    length = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            sum = 0
            for k in range(i, j + 1):
                sum += a[k]

            if sum == K:
                length = max(length, j - i + 1)
    return length


a = [2, 3, 5, 1, 9]
k = 10
print(LongestSubarrayN3(a, k))


# Time = O(n^2)
def LongestSubarray(a, k):
    length = 0
    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]

            if sum == k:
                length = max(length, j - i + 1)
    return length


a = [2, 3, 5, 1, 9]
k = 10
print(LongestSubarray(a, k))
