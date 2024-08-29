# time = O(n*n)
# Space = O(n*n)
def rotateMatrix90(mat):
    n = len(mat)
    rotate = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotate[j][n-i-1] = mat[i][j]
    return rotate


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotateMatrix90(arr))