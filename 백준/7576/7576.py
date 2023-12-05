import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomato_box = []

for _ in range(N):
    tomato_box.append(list(map(int, sys.stdin.readline().split())))

direction = [[1, 0], [-1, 0], [0, -1], [0, 1]]
visited = [[False for _ in range(M)] for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if (0 <= nx < N) and (0 <= ny < M):
            if tomato_box[nx][ny] == 0:
                queue.append((nx, ny))
                tomato_box[nx][ny] = tomato_box[x][y] + 1

answer = 0
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 0:
            print(-1)
            exit()
    if answer < max(tomato_box[i]):
        answer = max(tomato_box[i])

print(answer-1)
