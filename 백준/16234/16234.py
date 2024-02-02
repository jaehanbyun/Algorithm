import sys
from collections import deque

input = sys.stdin.readline

def OOB(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return True
    return False
def bfs(x, y):
    global flag

    total = lands[x][y]
    sets = [(x, y)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            next_x, next_y = cur_x + dxy[i][0], cur_y + dxy[i][1]

            if OOB(next_x, next_y) or visited[next_x][next_y]:
                continue

            if L <= abs(lands[cur_x][cur_y] - lands[next_x][next_y]) <= R:
                queue.append((next_x, next_y))
                sets.append((next_x, next_y))
                total += lands[next_x][next_y]
                visited[next_x][next_y] = True

    if total != lands[x][y]:
        p = int(total / len(sets))
        for a, b in sets:
            lands[a][b] = p
        flag = 1

    return

N, L, R = map(int, input().split())
lands = [list(map(int, input().split())) for _ in range(N)]
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
days = 0
flag = 0

while True:
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)

    if flag == 1:
        days += 1
        flag = 0
    else:
        break

print(days)