import sys
from collections import deque

input = sys.stdin.readline

def solution(m, n, k):
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + d[i][0]
                ny = y + d[i][1]

                if (0 <= nx < m) and (0 <= ny < n) and visited[nx][ny] == False \
                    and matrix[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    matrix = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for _ in range(k):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    answer = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and visited[i][j] == False:
                bfs(i, j)
                answer += 1

    print(answer)
    return

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    solution(M, N, K)