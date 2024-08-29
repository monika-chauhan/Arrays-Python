# time complexity = O(n)
# space complexity = O(1)
def MajorityElement(a):
    cnt = 0
    ele = None
    for i in range(len(a)):
        if cnt == 0:
            cnt = 1
            el = a[i]
        elif el == a[i]:
            cnt += 1
        else:
            cnt -= 1

    cnt1 = 0
    for i in range(len(a)):
        if a[i] == el:
            cnt1 += 1

    if cnt1 > (len(a) / 2):
        return el
    return -1


a = [2, 2, 1, 1, 1, 2, 2]
print(MajorityElement(a))
