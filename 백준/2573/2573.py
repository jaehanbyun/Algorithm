import sys
from collections import deque

input = sys.stdin.readline

def get_split_cnt(sx, sy):
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = 1

    while queue:
        cx, cy = queue.popleft()

        for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nx, ny = cx + d[0], cy + d[1]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if matrix[nx][ny] > 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

def bfs(sx, sy):
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = 1

    while queue:
        cx, cy = queue.popleft()
        cnt = 0

        for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nx, ny = cx + d[0], cy + d[1]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if matrix[nx][ny] > 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                else:
                    cnt += 1

        if matrix[cx][cy] - cnt <= 0:
            matrix[cx][cy] = 0
        else:
            matrix[cx][cy] -= cnt

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = 0

while True:
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > 0 and not visited[i][j]:
                bfs(i, j)

    split_cnt = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > 0 and not visited[i][j]:
                get_split_cnt(i, j)
                split_cnt += 1

    answer += 1

    if split_cnt == 0:
        print(0)
        break
    elif split_cnt >= 2:
        print(answer)
        break