import copy
import sys
from collections import deque

input = sys.stdin.readline

def bfs(k, g, flag=0):
    queue = deque(k)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue

            if g[nx][ny] == 0 and (flag == 0 or g[x][y]+1 < fire_zone[nx][ny] or fire_zone[nx][ny] == 0):
                g[nx][ny] = g[x][y] + 1
                queue.append([nx, ny])

R, C = map(int, input().split())
graph = []

for _ in range(R):
    graph.append(list(input().strip()))

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
jihoon = []
fire = []
fire_zone = [[0] * C for _ in range(R)]
jihoon_zone = copy.deepcopy(fire_zone)
for a in range(R):
    for b in range(C):
        if graph[a][b] == 'J':
            jihoon.append([a, b])
            jihoon_zone[a][b] = 1
        if graph[a][b] == 'F':
            fire.append([a, b])
            fire_zone[a][b] = 1
        if graph[a][b] == '#':
            jihoon_zone[a][b] = -1
            fire_zone[a][b] = -1

bfs(fire, fire_zone)
bfs(jihoon, jihoon_zone, flag=1)

answer = int(1e9)
for a in range(C):
    if jihoon_zone[0][a] != -1 and jihoon_zone[0][a] != 0:
        answer = min(answer, jihoon_zone[0][a])
    if jihoon_zone[R-1][a] != -1 and jihoon_zone[R-1][a] != 0:
        answer = min(answer, jihoon_zone[R-1][a])

for a in range(R):
    if jihoon_zone[a][0] != -1 and jihoon_zone[a][0] != 0:
        answer = min(answer, jihoon_zone[a][0])
    if jihoon_zone[a][C-1] != -1 and jihoon_zone[a][C-1] != 0:
        answer = min(answer, jihoon_zone[a][C-1])

print('IMPOSSIBLE' if answer == int(1e9) else answer)