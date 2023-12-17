import copy
import sys
from itertools import combinations
from collections import deque

N, M = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
safe_zones = []
virus_zones = []
max_count = 0

for i in range(N):
    for j in range(M):
        if map[i][j] == 2:
            virus_zones.append([i, j])
        if map[i][j] == 0:
            safe_zones.append([i, j])

def bfs():
    global max_count
    count = 0
    copy_map = copy.deepcopy(map)
    queue = deque(virus_zones)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            if (0 <= nx < N) and (0 <= ny < M):
                if copy_map[nx][ny] == 0:
                    copy_map[nx][ny] = 2
                    queue.append([nx, ny])

    for i in range(N):
        count += copy_map[i].count(0)

    max_count = max(max_count, count)

# (1, 1), (2, 2), (3, 3) 좌표에 벽을 세우는 것과 (1, 1), (3, 3), (2, 2)에 벽을 세우는 것은 같은 경우
# 때문에, 아래 for문으로 벽을 세울 경우 중복되는 경우에도 bfs를 동작시키므로 시간초과
''' 
def make_wall(wall_count):
    if wall_count == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if map[i][j] == 0:
                map[i][j] = 1
                make_wall(wall_count + 1)
                map[i][j] = 0
'''
def make_walls():
    for walls in combinations(safe_zones, 3):
        first, second, third = walls

        map[first[0]][first[1]] = 1
        map[second[0]][second[1]] = 1
        map[third[0]][third[1]] = 1

        bfs()

        map[first[0]][first[1]] = 0
        map[second[0]][second[1]] = 0
        map[third[0]][third[1]] = 0

make_walls()
print(max_count)
