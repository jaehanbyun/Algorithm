import sys
from collections import deque

input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
dl = [-1, 1]

while True:
    L, R, C = map(int, input().split())

    if L == 0 and R == 0 and C == 0:
        break

    building = []
    for i in range(L):
        floor = [list(input().strip()) for _ in range(R)]
        delimeter = input()

        building.append(floor)

    queue = deque()
    E_l, E_x, E_y = 0, 0, 0
    visited = [[[-1] * C for _ in range(R)] for _ in range(L)]
    for l in range(L):
        for x in range(R):
            for y in range(C):
                if building[l][x][y] == 'S':
                    queue.append([l, x, y])
                    visited[l][x][y] = 0
                if building[l][x][y] == 'E':
                    E_l, E_x, E_y = l, x, y

    while queue:
        l, x, y = queue.popleft()

        if visited[E_l][E_x][E_y] > 0:
            print(f'Escaped in {visited[E_l][E_x][E_y]} minute(s).')
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < R) and (0 <= ny < C) and building[l][nx][ny] != '#' and visited[l][nx][ny] == -1:
                queue.append([l, nx, ny])
                visited[l][nx][ny] = visited[l][x][y] + 1

        for i in range(2):
            nl = l + dl[i]

            if (0 <= nl < L) and building[nl][x][y] != '#' and visited[nl][x][y] == -1:
                queue.append([nl, x, y])
                visited[nl][x][y] = visited[l][x][y] + 1

    if visited[E_l][E_x][E_y] == -1:
        print('Trapped!')