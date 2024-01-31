import sys

input = sys.stdin.readline

L = int(input())
content = list(input().rstrip())
matrix = [['#'] * 101 for _ in range(101)]

x, y = 50, 50
matrix[x][y] = '.'
cur_d = 0
d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
for c in content:
    if c == 'R':
        cur_d = (cur_d+1)%4
    elif c == 'L':
        cur_d = (cur_d-1)%4
    else:
        x += d[cur_d][0]
        y += d[cur_d][1]
        matrix[x][y] = '.'

s_x, l_x = 50, 50
s_y, l_y = 50, 50
for i in range(101):
    for j in range(101):
        if matrix[i][j] != '#':
            s_x, s_y = min(s_x, i), min(s_y, j)
            l_x, l_y = max(l_x, i), max(l_y, j)

for i in range(s_x, l_x+1):
    print(''.join(matrix[i][s_y:l_y+1]))