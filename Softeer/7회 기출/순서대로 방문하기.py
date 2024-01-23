import sys

input = sys.stdin.readline

def backtracking(x, y, log):
    global count
    if x == final_x and y == final_y:
        if log == target:
            count += 1
            return

    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if visited[nx][ny] == False and matrix[nx][ny] == 0:
            visited[nx][ny] = True
            l = len(log)
            if (nx, ny) in target:
                log.append((nx, ny))
            backtracking(nx, ny, log)
            visited[nx][ny] = False
            del log[l:]

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

target = []
for _ in range(m):
    x, y = map(int, input().split())
    target.append((x-1, y-1))

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
visited = [[0] * n for _ in range(n)]
start_x, start_y = target.pop(0)
final_x, final_y = target.pop(-1)
visited[start_x][start_y] = 1
count = 0
backtracking(start_x, start_y, [])
print(count)