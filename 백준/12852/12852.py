import copy
import sys

input = sys.stdin.readline

N = int(input())
matrix = [[int(1e9), 0] for _ in range(N+1)]
matrix[N][0] = 0

for i in range(N, 0, -1):
    if i % 3 == 0:
        if matrix[i//3][0] > matrix[i][0] + 1:
            matrix[i//3][0] = matrix[i][0] + 1
            matrix[i//3][1] = i

    if i % 2 == 0:
        if matrix[i // 2][0] > matrix[i][0] + 1:
            matrix[i // 2][0] = matrix[i][0] + 1
            matrix[i // 2][1] = i

    if matrix[i - 1][0] > matrix[i][0] + 1:
        matrix[i - 1][0] = matrix[i][0] + 1
        matrix[i - 1][1] = i

rst = [1]
cur_num = 1

for i in range(matrix[1][0]):
    rst.append(matrix[cur_num][1])
    cur_num = matrix[cur_num][1]

rst.reverse()

print(matrix[1][0])
print(*rst)