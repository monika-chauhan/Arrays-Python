# Time =  The loop will run at most N times. And sorting the array will take N*logN time complexity.

def twoSum(a, target):
    n = len(a)
    left = 0
    right = n - 1
    Sum = 0
    while left < right:
        if a[left] + a[right] == target:
            return a[left], a[right]

        if a[left] + a[right] < target:
            left += 1

        if a[left] + a[right] > target:
            right -= 1
    return [-1, -1]


a = [2, 6, 5, 8, 11]
k = 14
print(twoSum(a, k))
