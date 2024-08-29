# Time complexity = O(n)
# space Complexity = O(1)
def oneElement(a):
    xor = 0
    for i in a:
        xor = xor ^ i
    return xor
a = [1,1,2,2,4,4,5]
print(oneElement(a))