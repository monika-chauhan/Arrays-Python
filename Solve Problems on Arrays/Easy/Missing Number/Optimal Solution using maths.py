# Time complexity = O(n)
# space Complexity = O(1)
def Missing(a,n):
    sumArr = 0
    for i in range(len(a)): # O(n)
        sumArr += a[i]

    totalSum = n*(n+1)//2
    return totalSum - sumArr

a = [1,3]
n = 3
print(Missing(a,n))