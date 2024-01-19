import sys

input = sys.stdin.readline

def backtracking(x, y, count):
    global answer
    answer = max(answer, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and not board[nx][ny] in visited:
            visited.add(board[nx][ny])
            backtracking(nx, ny, count+1)
            visited.remove(board[nx][ny])

R, C = map(int, input().split())
board = []

for _ in range(R):
    board.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 1
visited = set()
visited.add(board[0][0])
backtracking(0, 0, 1)

print(answer)