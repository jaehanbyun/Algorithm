import sys

n, m = map(int, sys.stdin.readline().split())
x, y, head = map(int, sys.stdin.readline().split())
visit = [[0]*m for _ in range(n)]
room = []

for i in range(n):
    room.append(list(map(int, sys.stdin.readline().split())))

direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
cnt = 1
visit[x][y] = 1

while True:
    check = 0
    for i in range(4):
        next_x = x+direction[(head+3)%4][0]
        next_y = y+direction[(head+3)%4][1]
        head = (head+3)%4
        if 0 <= next_x <= n-1 and 0 <= next_y <= m-1 and room[next_x][next_y] == 0:
            if visit[next_x][next_y] == 0:
                visit[next_x][next_y] = 1
                x = next_x
                y = next_y
                cnt += 1
                check = 1
                break

    if check == 0:
        next_x = x - direction[head][0]
        next_y = y - direction[head][1]
        if room[next_x][next_y] == 1:
            break
        else:
            x = next_x
            y = next_y
print(cnt)