import sys

input = sys.stdin.readline

N = int(input())
game_board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dp[0][0] = 1
visited[0][0] = 1
dir = [(0, 1), (1, 0)]

for x in range(N):
    for y in range(N):
        if visited[x][y] == 0 or (x == N-1 and y == N-1):
            continue

        jump_size = game_board[x][y]
        for dx, dy in dir:
            nx = x + jump_size * dx
            ny = y + jump_size * dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            dp[nx][ny] += dp[x][y]
            visited[nx][ny] = 1

print(dp[N-1][N-1])