import sys
from collections import deque

input = sys.stdin.readline

def oob(x, y):
    return x < 0 or x >= n or y < 0 or y >= n

def bfs(x, y, l):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]

            if oob(nx, ny) or visited[nx][ny] or matrix[nx][ny] <= l:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = 1

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0
max_height = max(max(row) for row in matrix)

for limit in range(max_height + 1):
    visited = [[0] * n for _ in range(n)]
    tmp = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and matrix[i][j] > limit:
                bfs(i, j, limit)
                tmp += 1

    answer = max(tmp, answer)

print(answer)