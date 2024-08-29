# Time complexity = O(n+m)
# Space Complexity = O(n+m)
def union(a1, a2):
    s = set()
    i = j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] == a2[j]:
            s.add(a1[i])
            i += 1
            j += 1

        s.add(a1[i])
        s.add(a2[i])
        i += 1
        j += 1
    return list(s)


a1 = [1, 2, 3, 4, 5]
a2 = [3, 4, 5, 6, 7]
print(union(a1, a2))
