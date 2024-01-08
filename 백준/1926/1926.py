import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    count = 1
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m) and map[nx][ny] == 1 and visited[nx][ny] == False:
                queue.append([nx, ny])
                visited[nx][ny] = True
                count += 1

    return count

paint_count = 0
max_area = 0
for x in range(n):
    for y in range(m):
        if map[x][y] == 1 and visited[x][y] == False:
            paint_count += 1
            area = bfs(x, y)
            max_area = max(max_area, area)

print(paint_count)
print(max_area)