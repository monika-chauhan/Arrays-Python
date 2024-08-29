def LongestSubarray(a, k):
    sum = maxLen = 0
    preSum = {}
    for i in range(len(a)):  # O(n) i we use unorder Map otherwise O(nlogn) # ordered map
        sum += a[i]

        rem = k - sum
        if rem in preSum:
            length = i - preSum[rem]
            maxLen = max(maxLen, length)

        if sum == k:
            maxLen = max(maxLen, i + 1)

        if sum not in preSum:
            preSum[sum] = i
    return maxLen


a = [-1, 1, 1]
k = 1
print(LongestSubarray(a, k))
