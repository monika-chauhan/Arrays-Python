# Time = O(n^2)
# Space = O(1)

# using Two loop sum the values and compare with k and increase count is equal
def countSubarrayKSum(a,K):
    cnt = 0
    for i in range(len(a)):
        Sum = 0
        for j in range(i,len(a)):
            Sum += a[j]

            if Sum == K:
                cnt += 1
    return cnt

a =  [3, 1, 2, 4]
k = 6
print(countSubarrayKSum(a,k))