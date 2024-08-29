# time = O9n) and sometime= O(nlogn)
# space = O(n)

def CountSubarrayKSum(a, k):
    cnt = 0
    preSum = {0:1}
    Sum = 0
    for i in range(len(a)):
        # add current element to prefix Sum:
        Sum += a[i]

        # Calculate x-k:
        rem = Sum - k

        if rem in preSum:
            # Add the number of subarrays to be removed:
            cnt += preSum[rem]

        # Update the count of prefix sum
        # in the map.
        preSum[Sum] = preSum.get(Sum,0)+1
    return cnt


a = [3, 1, 2, 4]
k = 6
print(CountSubarrayKSum(a, k))
