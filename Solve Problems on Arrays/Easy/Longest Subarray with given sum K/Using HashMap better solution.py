def LongestSubarray(a, K):
    preSum = {}
    maxLen = 0
    sum = 0
    for i in range(len(a)): # O(n)
        sum += a[i]
        if sum == K:
            maxLen = max(maxLen, i + 1)

        rem = K - sum
        if rem in preSum:
            length = i - preSum[rem]
            maxLen = max(maxLen, length)

        if sum not in preSum:
            preSum[sum] = i
    return maxLen


a = [2, 3, 5, 9, 1]
print(LongestSubarray(a, 10))
