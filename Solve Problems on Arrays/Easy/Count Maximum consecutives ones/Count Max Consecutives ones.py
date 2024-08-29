# Time = O(n)
# Space = O(1)
def countMaxConsecutiveOne(a):
    count = 0
    max_count = 0
    for i in range(len(a)):
        if a[i] == 1:
            count += 1
        elif a[i] == 0:
            count = 0
        max_count = max(count, max_count)
    return max_count


a = [1, 1, 0, 0, 1]
print(countMaxConsecutiveOne(a))
