# Time complexity = O(n)
# Current element = prevElement * (rowNumber - colIndex) / colIndex

def printPascalRow(row):
    ans = [1]
    res = 1
    for i in range(1, row):
        res = res * (row - i)  # the numerator is multiplied by the previous consecutive element,
        res = res // i  # the denominator is multiplied by the next consecutive element.
        ans.append(res)
    return ans


print(printPascalRow(5))
