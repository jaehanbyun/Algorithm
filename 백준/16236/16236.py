import sys
from collections import deque

input = sys.stdin.readline

def bfs(pos):
    queue = deque([(pos[0], pos[1], 0)])
    visited[pos[0]][pos[1]] = True

    while queue:
        cx, cy, cost = queue.popleft()

        for nx, ny in ([(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]):
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if 0 < space[nx][ny] < w:
                    fish.append([cost+1, nx, ny])
                    visited[nx][ny] = True
                if space[nx][ny] == 0 or space[nx][ny] == w:
                    queue.append((nx, ny, cost+1))
                    visited[nx][ny] = True

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
cur_pos = [0, 0]
w, eat_fish, t = 2, 0, 0

for x in range(n):
    for y in range(n):
        if space[x][y] == 9:
            space[x][y] = 0
            cur_pos = [x, y]

while True:
    fish = []
    visited = [[False] * n for _ in range(n)]
    bfs(cur_pos)

    if not fish:
        print(t)
        sys.exit(0)

    fish.sort()
    t += fish[0][0]
    cur_pos = fish[0][1:]
    space[cur_pos[0]][cur_pos[1]] = 0
    eat_fish += 1

    if w == eat_fish:
        w += 1
        eat_fish = 0