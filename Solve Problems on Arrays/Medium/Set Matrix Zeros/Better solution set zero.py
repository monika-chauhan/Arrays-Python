# time = O(2*(N*M))
# Space = O(n)+O(m)
def SetZero(mat, n, m):
    row = [0] * n
    col = [0] * m

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                row[i] = 1
                col[j] = 1

    for i in range(n):
        for j in range(m):
            if row[i] == 1 or col[j] == 1:
                mat[i][j] = 0
    return mat


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
n = len(matrix)
m = len(matrix[0])
print(SetZero(matrix, n, m))
