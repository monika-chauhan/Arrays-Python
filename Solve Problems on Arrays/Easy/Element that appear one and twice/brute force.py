# time complexity = O(n^2)

def element(a):

    for i in range(len(a)):
        num = a[i]
        cnt = 0

        for j in range(len(a)):
            if a[j] == num:
                cnt += 1

        if cnt == 1:
            return a[i]
    return -1

a = [1,1,2,3,3,4,4]
print(element(a))