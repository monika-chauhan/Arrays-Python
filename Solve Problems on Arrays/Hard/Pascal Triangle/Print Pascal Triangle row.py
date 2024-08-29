# for printing the every element of pascal use the previous method and for printing we use a loop and calling the same
# function till the row goes end
# Time complexity = O(n*r)

def ncr(row, col):
    n = row - 1
    r = col - 1
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res


def printPascalRow(row):
    ans = []
    for c in range(1, row + 1):
        ans.append(ncr(row, c))
    return ans


print(printPascalRow(5))
