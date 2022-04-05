# matrix operations
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Matrix Addition
# output: [[2, 6, 10], [6, 10, 14], [10, 14, 18]]
matrix1[0][0] = matrix1[0][0] + matrix2[0][0]
matrix1[0][1] = matrix1[0][1] + matrix2[0][1]
matrix1[0][2] = matrix1[0][2] + matrix2[0][2]
matrix1[1][0] = matrix1[1][0] + matrix2[1][0]
matrix1[1][1] = matrix1[1][1] + matrix2[1][1]
matrix1[1][2] = matrix1[1][2] + matrix2[1][2]
matrix1[2][0] = matrix1[2][0] + matrix2[2][0]
matrix1[2][1] = matrix1[2][1] + matrix2[2][1]
matrix1[2][2] = matrix1[2][2] + matrix2[2][2]

print matrix1

# Matrix Trace
# output: 15
print matrix2[0][0] + matrix2[1][1] + matrix2[2][2]


# Matrix Transpose of matrix2
# output: True

matrix2_t2 = [[matrix2[2][0], matrix2[1][0], matrix2[0][0]],
                [matrix2[2][1], matrix2[1][1], matrix2[0][1]],
                [matrix2[2][2], matrix2[1][2], matrix2[0][2]]]


tmp0 = matrix2[0][0]
matrix2[0][0] = matrix2[2][0]
tmp2 = matrix2[0][1]
matrix2[0][1] = matrix2[1][0]
tmp3 = matrix2[0][2]
matrix2[0][2] = tmp0
tmp4 = matrix2[1][0]
matrix2[1][0] = matrix2[2][1]
tmp5 = matrix2[1][2]
matrix2[1][2] = tmp2
tmp6 = matrix2[2][0]
tmp7 = matrix2[2][2]
matrix2[2][0] = tmp7
matrix2[2][1] = tmp5
matrix2[2][2] = tmp3

print matrix2 == matrix2_t2
