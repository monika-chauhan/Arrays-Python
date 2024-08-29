# using Kadane Algo -> time = O(n)
def maximumSum(a):
    Sum = 0
    max_sum = 0
    for i in range(len(a)):
        Sum += a[i]

        if Sum < 0:
            Sum = 0

        max_sum = max(max_sum, Sum)
    return max_sum


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximumSum(a))
