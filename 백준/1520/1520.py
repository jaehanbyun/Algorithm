import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if oob(nx, ny) and h[nx][ny] < h[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

def oob(x, y):
    return 0 <= x < m and 0 <= y < n

m, n = map(int, input().split())
h = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

print(dfs(0, 0))