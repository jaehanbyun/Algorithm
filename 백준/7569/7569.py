import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

tomato_box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
queue = deque()
answer = 0
# 오른쪽, 뒤, 앞, 왼쪽
x_y_direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
# 위, 아래
z_direction = [1, -1]
raw_tomato = 0

for h in range(H):
    for x in range(N):
        for y in range(M):
            if tomato_box[h][x][y] == 1:
                queue.append([h, x, y])
            if tomato_box[h][x][y] == 0:
                raw_tomato += 1

if raw_tomato == 0:
    print(0)
    exit()

while queue:
    h, x, y = queue.popleft()

    for i in range(2):
        nh = h + z_direction[i]
        if (0<= nh < H):
            if tomato_box[nh][x][y] == 0:
                queue.append([nh, x, y])
                tomato_box[nh][x][y] = tomato_box[h][x][y] + 1

    for i in range(4):
        nx = x + x_y_direction[i][0]
        ny = y + x_y_direction[i][1]
        if (0<= nx < N) and (0<= ny < M):
            if tomato_box[h][nx][ny] == 0:
                queue.append([h, nx, ny])
                tomato_box[h][nx][ny] = tomato_box[h][x][y] + 1


for h in range(H):
    for x in range(N):
        for y in range(M):
            if tomato_box[h][x][y] == 0:
                print(-1)
                exit()
        if answer < max(tomato_box[h][x]):
            answer = max(tomato_box[h][x])

print(answer-1)
