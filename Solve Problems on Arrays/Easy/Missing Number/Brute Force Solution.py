# time = O(n^2)
def MissingNumber(a,n):
    for i in range(1,n+1): # O(n)
        flag = 0
        for j in range(len(a)): #o(n)
            if a[j] == i:
                flag = 1
                break
        if flag == 0:
            return i
    return -1
a = [1,3]
n = 3
print(MissingNumber(a,n))