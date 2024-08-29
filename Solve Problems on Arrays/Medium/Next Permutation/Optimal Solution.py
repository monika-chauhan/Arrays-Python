# Time complexity = O(3*n) = O(n)

def next_permutation(a):
    # step1: Find the break Point (index) when a[i] < a[i+1] when iterate in reverse order
    breakPoint = -1
    for i in range(len(a) - 2, -1, -1):
        if a[i] < a[i + 1]:
            breakPoint = i
            break

    # Step2: If the breakPoint == -1 then the array sorted in decreasing order means it's last permuation and
    # answer  will the first one so just reverse the array
    if breakPoint == -1:
        return a[::-1]

    # Step3: If the break point exists then iterate the array in reverse order when we found the next greater element
    # than a[index] then swap with a[index] value

    for i in range(len(a) - 1, breakPoint, -1):
        if a[i] > a[breakPoint]:
            a[i], a[breakPoint] = a[breakPoint], a[i]
            break

    a[breakPoint + 1:] = reversed(a[breakPoint + 1:])
    return a


a = [2, 1, 5, 4, 3, 0, 0]
print(next_permutation(a))
