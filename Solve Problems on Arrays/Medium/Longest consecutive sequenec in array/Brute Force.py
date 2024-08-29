# We are using Linear search for searching the number
# time = O(n^2)

def linearSearch(a, num):
    for i in range(len(a)):
        if a[i] == num:
            return True
    return False


def longestSubseq(a):
    n = len(a)
    longest = 1
    for i in range(n):
        x = a[i]
        cnt = 1

        while linearSearch(a, x + 1):
            x += 1
            cnt += 1

        longest = max(longest, cnt)
    return longest


a = [100, 200, 1, 3, 2, 4]
print(longestSubseq(a))
