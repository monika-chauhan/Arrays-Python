# Time = O(n^2)
def maximumSum(a):
    maxSum = 0
    for i in range(len(a)):
        Sum = 0
        for j in range(i, len(a)):
            Sum += a[j]
            maxSum = max(maxSum, Sum)
    return maxSum


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximumSum(a))
