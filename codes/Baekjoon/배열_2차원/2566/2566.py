# 2566 최댓값

mat = []
for _ in range(9):
    row = list(map(int, input().split()))
    mat.append(row)
#print(mat)

maxval = 0
maxrow = 0
maxcol = 0

for i in range(9):
    for j in range(9):
        if maxval <= mat[i][j]:
            maxval = mat[i][j]
            maxrow = i + 1
            maxcol = j + 1
print(maxval)
print(maxrow, maxcol, end= ' ')