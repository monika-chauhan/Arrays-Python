def printSubarray(a):
    start = 0
    ansStart = ansEnd = -1
    Sum = 0
    maxSum = float('-inf')
    for i in range(len(a)):
        if Sum == 0:
            start = i

        Sum += a[i]

        if Sum > maxSum:
            maxSum = Sum

            ansStart = start
            ansEnd = i

        if Sum < 0:
            Sum = 0

    return maxSum, a[ansStart:ansEnd + 1]


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(printSubarray(a))
