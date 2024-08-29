# Time complexity = O(n)
# space complexity = O(1)

def Sort0s1s2s(a):
    n = len(a)
    left = 0
    right = n - 1
    mid = 0
    while mid <= right:
        if a[mid] == 0:
            a[left], a[mid] = a[mid], a[left]
            left += 1
            mid += 1
        elif a[mid] == 2:
            a[right], a[mid] = a[mid], a[right]
            right -= 1
        else:
            mid += 1

    return a


a = [1, 0, 2, 1, 2, 0, 0]
print(Sort0s1s2s(a))
