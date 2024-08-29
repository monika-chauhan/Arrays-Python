# time = O(n^2)
def twoSum(a, target):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == target:
                print(a[i], a[j])


a = [2, 6, 5, 8, 11]
target = 14
print(twoSum(a, target))
