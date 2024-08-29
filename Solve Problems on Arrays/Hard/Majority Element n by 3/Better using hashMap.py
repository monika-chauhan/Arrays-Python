# time = O(n)
# Space = O(n)

def majorityElement(a, n):
    mp = {}
    for i in range(n):
        mp[a[i]] = mp.get(a[i], 0) + 1

    ans = []
    for key in mp.keys():
        if mp[key] > n // 3:
            ans.append(key)
    return ans


a = [1, 2, 2, 3, 2]
b = [11, 33, 33, 11, 33, 11]
print(majorityElement(b, len(b)))
print(majorityElement(a, len(a)))
