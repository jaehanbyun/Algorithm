import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for _ in range(n)]
start = [[1e9] * m for _ in range(n)]
end = [[1e9] * m for _ in range(n)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def oob(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return True
    return False

def bfs(x, y, cost, arr):
    queue = deque()
    queue.append((x, y, cost))
    visited[x][y] = True
    arr[x][y] = 1

    while queue:
        cx, cy, ncost = queue.popleft()

        for i in range(4):
            nx = cx + dir[i][0]
            ny = cy + dir[i][1]

            if oob(nx, ny) or visited[nx][ny]:
                continue

            arr[nx][ny] = min(arr[nx][ny], ncost + 1)

            if matrix[nx][ny] != 1:
                visited[nx][ny] = True
                queue.append((nx, ny, ncost+1))

visited = [[False] * m for _ in range(n)]
bfs(0, 0, 1, start)

visited = [[False] * m for _ in range(n)]
bfs(n-1, m-1, 1, end)

answer = start[n-1][m-1] if start[n-1][m-1] != 0 else 1e9

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1 and start[i][j] and end[i][j]:
            answer = min(answer, start[i][j] + end[i][j]-1)

if answer == 1e9:
    print(-1)
else:
    print(answer)