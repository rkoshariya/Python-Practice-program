N = 4
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
print(mat)

mat_mod = [[0 for i in range(N)] for j in range(N)]
print(mat_mod)
l = 0
k = 0
for j in range(N-1 , -1, -1):
    for i in range(N):
        mat_mod[k][l]= mat[i][j]
        l = (l + 1) % N
    k = (k + 1) % N 
print(mat_mod)