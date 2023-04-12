import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())

answer = 0
mat = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

for i in range(k):
    r, c = map(int, sys.stdin.readline().split())
    mat[r-1][c-1] = 1

def adj_pos(x, y):
    yield x-1, y
    yield x+1, y
    yield x, y-1
    yield x, y+1

def bfs(x, y, cnt):
    visited[x][y] = True

    dQ = deque([(x, y)])
    while dQ:
        nx, ny = dQ.popleft()

        for adj_x, adj_y in adj_pos(nx, ny):
            if not (0 <= adj_x < n and 0 <= adj_y < m):
                continue
            if mat[adj_x][adj_y]==1 and not visited[adj_x][adj_y]:
                visited[adj_x][adj_y] = True
                dQ.append((adj_x, adj_y))
                cnt += 1

    return cnt

for i in range(n):
    for j in range(m):
        if mat[i][j] == 1 and not visited[i][j]:
            tmp = bfs(i, j, 1)
            if tmp > answer:
                answer = tmp

print(answer)