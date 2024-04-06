import sys
from collections import deque

input = sys.stdin.readline

def oob(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return True
    return False

n = int(input())
k = int(input())
apple_pos = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
change_info = [input().split() for _ in range(l)]
change_info = [[int(x), c] for x, c in change_info]
change_info = deque(change_info)

board = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
tail = deque()
tail.append((0, 0))
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cur_dir = 0
time = 0
cx, cy = 0, 0
visited[cx][cy] = 1

for x, y in apple_pos:
    board[x-1][y-1] = 1

while True:
    time += 1
    cx += dir[cur_dir][0]
    cy += dir[cur_dir][1]

    if oob(cx, cy) or visited[cx][cy]:
        break

    if board[cx][cy] == 1:
        board[cx][cy] = 0
    else:
        tx, ty = tail.popleft()
        visited[tx][ty] = 0

    visited[cx][cy] = 1
    tail.append((cx, cy))

    if change_info and time == change_info[0][0]:
        command_time, command = change_info.popleft()
        if command == 'D':
            cur_dir = (cur_dir + 1) % 4
        else:
            cur_dir = (cur_dir - 1) % 4

print(time)