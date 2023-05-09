# 파이썬의 기본 재귀 깊이 제한은 1000으로 설정되어 있다.
# 때문에 재귀로 문제를 풀 경우 해당 제한에 걸려 런타임 에러 메시지가 표출.
# 이를 방지하기 위한 sys.setrecursionlimit(10 ** 6) 숙지
import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())

arr = [[] for _ in range(N)]

for i in range(N):
    arr[i] = list(sys.stdin.readline().strip())

def adj_pos(x, y):
    yield x - 1, y
    yield x + 1, y
    yield x, y - 1
    yield x, y + 1

def dfs(flag, x, y):
    color = arr[x][y]

    for nx, ny in adj_pos(x, y):
        if not ( 0 <= nx < N and 0 <= ny < N):
            continue
        if flag == 1:
            if color == 'B':
                if not visited[nx][ny] and color == arr[nx][ny]:
                    visited[nx][ny] = True
                    dfs(1, nx, ny)
            else:
                if not visited[nx][ny] and arr[nx][ny] != 'B':
                    visited[nx][ny] = True
                    dfs(1, nx, ny)
        else:
            if not visited[nx][ny] and color == arr[nx][ny]:
                visited[nx][ny] = True
                dfs(0, nx, ny)

fcnt = 0
scnt = 0
visited = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(0, i, j)
            fcnt += 1

visited = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(1, i, j)
            scnt += 1

print(fcnt, scnt)