# time = O(n^3)

def ncr(row, col):
    n = row - 1
    r = col - 1

    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return int(res)


def printNRow(n):
    ans = []
    for row in range(1, n + 1):
        tempLst = []
        for col in range(1, row + 1):
            tempLst.append(ncr(row, col))
        ans.append(tempLst)
    return ans


n = 5
print(printNRow(5))
