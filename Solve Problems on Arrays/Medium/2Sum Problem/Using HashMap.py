def twoSum(a, target):
    d = {}
    for i, val in enumerate(a): # O(n) and sometime O(nlogn)
        rem = target - val  # 12, 8, 9, 6
        if rem in d:
            return d[rem], i
        d[val] = i  # 2:0, 6:1, 5:2, 8:3,11:4


a = [2, 6, 5, 8, 11]
k = 14
print(twoSum(a, k))
