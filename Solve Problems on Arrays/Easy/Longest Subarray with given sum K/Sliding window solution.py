# Time = O(n)
# Space = O(1)
def LongestSubarray(a, K):
    left = right = 0
    maxLen = 0
    sum = 0
    while right < len(a): #O(n)
        sum += a[right]

        if left < right and sum > K:
            sum -= a[left]
            left += 1
        if sum == K:
            maxLen = max(maxLen, right - left + 1)

        right += 1

    return maxLen


a = [7, 1, 6, 0]
print(LongestSubarray(a, 7))
