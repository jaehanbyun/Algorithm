import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque([(0, 0)])
    cheese = []
    melt_cnt = 0
    visited[0][0] = 1

    while queue:
        cx, cy = queue.popleft()

        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cx + d[0], cy + d[1]

            if 0 <= nx < r_len and 0 <= ny < c_len and not visited[nx][ny]:
                visited[nx][ny] = 1
                if table[nx][ny] == 0:
                    queue.append((nx, ny))
                else:
                    cheese.append((nx, ny))

    for x, y in cheese:
        table[x][y] = 0
        melt_cnt += 1

    return melt_cnt

r_len, c_len = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(r_len)]
time, ccnt = 0, 0

for r in range(r_len):
    ccnt += sum(table[r])

while True:
    visited = [[0] * c_len for _ in range(r_len)]
    time += 1
    melt_cnt = bfs()
    ccnt -= melt_cnt

    if ccnt == 0:
        print(f'{time}\n{melt_cnt}')
        break