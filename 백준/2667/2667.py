import sys

input = sys.stdin.readline

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().strip())))

visited = [[False] * N for _ in range(N)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def dfs(x, y, count):
    stack = []
    visited[x][y] = True
    stack.append((x, y))

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < N) and graph[nx][ny] == 1 \
                and visited[nx][ny] == False:
                visited[nx][ny] = True
                stack.append((nx, ny))
                count += 1

    return count

answer = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1 and visited[x][y] == False:
            count = dfs(x, y, 1)
            answer.append(count)

answer.sort()
print(len(answer))
print('\n'.join(map(str, answer)))