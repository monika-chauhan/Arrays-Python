def MajorityElement(a):
    hash = {}
    for i in range(len(a)):
        if a[i] not in hash:
            hash[a[i]] = 1
        else:
            hash[a[i]] += 1

    for key in hash.keys():
        if hash[key] > len(a) // 2:
            return key
    return -1


a = [2, 2, 1, 1, 1, 2, 2]
print(MajorityElement(a))
