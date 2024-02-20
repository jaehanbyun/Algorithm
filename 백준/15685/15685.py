import sys

input = sys.stdin.readline

def make_dragon(x, y, d, g):
    stack = [(x, y)]

    if d == 0:
        stack.append((x, y+1))
    elif d == 1:
        stack.append((x-1, y))
    elif d == 2:
        stack.append((x, y-1))
    else:
        stack.append((x+1, y))

    for i in range(g):
        end_x, end_y = stack[-1][0], stack[-1][1]
        dir_trace = []
        for j in range(len(stack)-1, 0, -1):
            tmp_dir_x = stack[j-1][0] - stack[j][0]
            tmp_dir_y = stack[j-1][1] - stack[j][1]
            index = (dset.index((tmp_dir_x, tmp_dir_y))+1)%4
            dir_trace.append(dset[index])

        for dx, dy in dir_trace:
            end_x += dx
            end_y += dy
            stack.append((end_x, end_y))

    for a, b in stack:
        matrix[a][b] = 1

N = int(input())
matrix = [[0] * 101 for _ in range(101)]
dset = [(-1,0), (0,1), (1,0), (0,-1)]
rst = 0

for _ in range(N):
    x, y, d, g = map(int, input().split())
    make_dragon(y, x, d, g)

for i in range(100):
    for j in range(100):
        if matrix[i][j] and matrix[i][j+1] and matrix[i+1][j] and matrix[i+1][j+1]:
            rst += 1

print(rst)