import sys

input = sys.stdin.readline

def row_check(r, num):
    return row[r][num] != 1

def col_check(c, num):
    return col[c][num] != 1

def three_check(r, c, num):
    return three[(r // 3)*3 + (c // 3)][num] != 1
def dfs(depth):
    if depth == len(zero):
        for i in range(9):
            print(''.join(map(str, matrix[i])))
        exit()

    nr, nc = zero[depth]
    for i in range(1, 10):
        if row_check(nr, i) and col_check(nc, i) and three_check(nr, nc, i):
            matrix[nr][nc] = i
            row[nr][i] = 1
            col[nc][i] = 1
            three[(nr // 3)*3 + (nc // 3)][i] = 1
            dfs(depth + 1)
            matrix[nr][nc] = 0
            row[nr][i] = 0
            col[nc][i] = 0
            three[(nr // 3) * 3 + (nc // 3)][i] = 0

matrix = [list(map(int, input().rstrip())) for _ in range(9)]
zero = []
three = [[0] * 10 for _ in range(10)]
row = [[0] * 10 for _ in range(10)]
col = [[0] * 10 for _ in range(10)]

for i in range(9):
    for j in range(9):
        if matrix[i][j] != 0:
            three[(i // 3)*3 + (j // 3)][matrix[i][j]] = 1
            row[i][matrix[i][j]] = 1
            col[j][matrix[i][j]] = 1
        else:
            zero.append((i, j))

dfs(0)