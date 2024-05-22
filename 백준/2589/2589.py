import sys
from collections import deque

input = sys.stdin.readline

def oob(x, y):
    return x < 0 or x >= r_len or y < 0 or y >= c_len
def bfs(x, y, cost):
    total_cost = 0
    queue = deque()
    queue.append((x, y, cost))
    visited[x][y] = True

    while queue:
        cx, cy, ccost = queue.popleft()
        total_cost = max(ccost, total_cost)

        for i in range(4):
            nx = cx + dir[i][0]
            ny = cy + dir[i][1]

            if oob(nx, ny) or visited[nx][ny] == True or matrix[nx][ny] == 'W':
                continue

            queue.append((nx, ny, ccost + 1))
            visited[nx][ny] = True

    return total_cost

r_len, c_len = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(r_len)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
answer = 0

for r in range(r_len):
    for c in range(c_len):
        if matrix[r][c] == 'L':
            visited = [[False] * c_len for _ in range(r_len)]
            answer = max(answer, bfs(r, c, 0))

print(answer)