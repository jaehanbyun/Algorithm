import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

mat = []
visited = [[False]*m for _ in range(n)]

for i in range(n):
    mat.append(list(map(int, sys.stdin.readline().strip())))

answer = 987654321

def adj_pos(x, y):
    yield x-1, y
    yield x+1, y
    yield x, y-1
    yield x, y+1

def bfs(x, y, cost):
    global answer
    visited[x][y] = True
    dQ = deque([(x, y, cost)])

    while dQ:
        nx, ny, ncost = dQ.popleft()

        for adj_x, adj_y in adj_pos(nx, ny):
            if not (0 <= adj_x < n and 0 <= adj_y < m):
                continue
            if not visited[adj_x][adj_y] and mat[adj_x][adj_y] == 1:
                visited[adj_x][adj_y] = True
                if adj_x == n-1 and adj_y == m-1:
                    if ncost+1 < answer:
                        answer = ncost+1
                else:
                    dQ.append((adj_x, adj_y, ncost+1))

bfs(0, 0, 1)
print(answer)