N = 4
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
print(mat)

for i in range(len(mat)):
    mat[i].reverse()

for i in range(len(mat)):
    for j in range(i, len(mat)):
        mat[i][j],mat[j][i]= mat[j][i], mat[i][j]

print(mat)