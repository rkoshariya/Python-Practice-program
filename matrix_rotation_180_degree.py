N = 4
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
print(mat)

for i in range(len(mat)):
    mat[i].reverse()

for i in range(int(len(mat)/2)):
    for j in range(len(mat)):
        mat[i][j], mat[N-i-1][j] = mat[N-i-1][j], mat[i][j]

print(mat)