# time = O(n^2)

def generate(row):
    ans = [1]
    res = 1
    for col in range(1, row):
        res = res * (row - col)
        res = res // col
        ans.append(res)
    return ans


def printNRows(n):
    result = []
    for row in range(1, n + 1):
        result.append(generate(row))
    return result


print(printNRows(5))
