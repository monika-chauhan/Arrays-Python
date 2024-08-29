def MajorityElement(a):
    for i in range(len(a)):
        cnt = 0
        for j in range(i + 1, len(a)):
            if a[j] == a[i]:
                cnt += 1

        if len(a) // 2 <= cnt:
            return a[i]
    return -1


a = [2, 2, 1, 1, 1, 2, 2]
print(MajorityElement(a))
