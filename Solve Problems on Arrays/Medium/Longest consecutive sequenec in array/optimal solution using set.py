# time = O(n)
# Space = O(n)

def longestConSeq(a):
    s = set()
    n = len(a)
    longest = 0
    if n == 0: return 0

    for i in a:
        s.add(i)

    for val in s:
        if val - 1 not in s:
            cnt = 1
            x = val

            while x + 1 in s:
                x += 1
                cnt += 1

            longest = max(longest, cnt)
    return longest


a = [100, 1, 3, 4, 2]
print(longestConSeq(a))
