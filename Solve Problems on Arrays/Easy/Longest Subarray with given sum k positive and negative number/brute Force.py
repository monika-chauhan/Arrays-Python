# time complexity = O(n)
# Space complexity = O(1)
def LongestSubarray(a, k):
    maxLen = sum = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            sum += a[j]

            if sum == k:
                maxLen = max(maxLen, j - i + 1)
    return maxLen


a = [-1, 1, 1]
print(LongestSubarray(a, 1))
