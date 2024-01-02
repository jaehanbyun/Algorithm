import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * M for _ in range(N)]

def dfs(x, y, score, depth):
    global answer

    if depth == 4:
        answer = max(score, answer)
        return
    elif answer >= (score + (4-depth) * max_value):
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < M) and (visited[nx][ny] == False):
                visited[nx][ny] = True
                if depth == 2:
                    dfs(x, y, score + matrix[nx][ny], depth + 1)
                dfs(nx, ny, score + matrix[nx][ny], depth + 1)
                visited[nx][ny] = False

max_value = max(map(max, matrix))
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, matrix[i][j], 1)
        visited[i][j] = False

print(answer)