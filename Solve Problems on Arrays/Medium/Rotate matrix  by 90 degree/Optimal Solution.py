# Time = O(n*n)
# Spcae = O(1)

def rotateMatrixBy90(mat):
    # Transpose of matrix
    for i in range(len(mat)):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    # reverse all the row of matrix

    for i in range(len(mat)):
        mat[i].reverse()

    return mat


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotateMatrixBy90(a))
