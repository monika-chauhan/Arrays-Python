# Time complexity = O(n^2)
def majorityElement(a, n):
    ans = []
    for i in range(n):
        cnt = 0
        if len(ans) == 0 or ans[0] != a[i]:
            for j in range(n):
                if a[i] == a[j]:
                    cnt += 1

            if cnt > n // 3:
                ans.append(a[i])

        if len(ans) == 2: break
    return ans


a = [11, 33, 33, 11, 33, 11]
b = [1, 2, 2, 3, 2]
print(majorityElement(a, len(a)))
print(majorityElement(b, len(b)))
