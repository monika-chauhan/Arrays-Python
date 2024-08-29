# Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle
# We know the formala is nCr = fact(n) / fact(n-r) * fact(r)
# We will observe that fact(6)/fact(6-3)*fact(3) = 6*5*4*3*2*1/ 3*2*1 * 3*2*1 = 6*5*4/3*2*1
# if n = 6 and r = 3 ever time = (n/1 * (n-1)/2 * (n-3)/3.............(n-r)/r)
# if we iterate a loop till 0 to r then n/i+1 * (n-i)/(i+1) *(n-i)/(i+1)

# Time = O(n)
# Space = O(1)

def printRowColValInPascal(row, col):
    n = row - 1
    r = col - 1

    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res


row = 5
col = 3
print(printRowColValInPascal(row, col))
