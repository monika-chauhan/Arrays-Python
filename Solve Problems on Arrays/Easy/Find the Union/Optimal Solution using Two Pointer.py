# Time complexity = O(m+n)
# Space Complexity : O(m+n) {If Space of Union ArrayList is considered}
def unionOfArr(a1,a2):
    union = []
    i = j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            if len(union) == 0 or union[-1] != a1[i]:
                union.append(a1[i])
            i += 1
        else:
            if len(union) == 0  or union[-1] != a2[j]:
                union.append(a2[j])
            j += 1

    while i < len(a1):
        if union[-1] != a1[i]:
            union.append(a1[i])
        i += 1
    while j < len(a2):
        if union[-1] != a2[j]:
            union.append(a2[j])
        j += 1
    return union

a1 = [1,2,3,4,5]
a2 = [3,4,5,6,7]
print(unionOfArr(a1,a2))