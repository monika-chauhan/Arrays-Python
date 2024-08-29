# time complexity = O(nlogn)

def longestConSeq(a):
    a = sorted(a)

    lastSmall = float('-inf')
    longest = 0
    cnt = 0
    for i in range(len(a)):
        if a[i] - 1 == lastSmall:
            lastSmall = a[i]
            cnt += 1
        elif a[i] != lastSmall:
            cnt = 1
            lastSmall = a[i]

        longest = max(longest, cnt)
    return longest


a = [100, 1, 3, 2, 4]
print(longestConSeq(a))
