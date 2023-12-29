import sys

N, M, x, y, K = map(int, sys.stdin.readline().split())
map_array = []
# 위, 북, 동, 서, 남, 아래
dice = [0] * 6

# 위 북 동 서 남 아래
# 1 2 3 4 5 6
# 동쪽으로
# 4 2 1 6 5 3
# 서쪽으로
# 3 2 6 1 5 4
# 북쪽으로
# 5 1 3 4 6 2
# 남쪽으로
# 2 6 3 4 1 5

for _ in range(N):
    map_array.append(list(map(int, sys.stdin.readline().split())))

# 위치 이동 = 1: 동, 2: 서, 3: 북, 4: 남
command = list(map(int, sys.stdin.readline().split()))
nx, ny = 0, 0
for c in command:
    if c == 1: # 동쪽으로
        nx = x
        ny = y + 1
    elif c == 2: # 서쪽으로
        nx = x
        ny = y - 1
    elif c == 3: # 북쪽으로
        nx = x - 1
        ny = y
    elif c == 4: # 남쪽으로
        nx = x + 1
        ny = y

    if (0 <= nx < N) and (0 <= ny < M):
        if c == 1:  # 동쪽으로
            dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
        elif c == 2:  # 서쪽으로
            dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
        elif c == 3:  # 북쪽으로
            dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
        elif c == 4:  # 남쪽으로
            dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

        if map_array[nx][ny] == 0:
            map_array[nx][ny] = dice[5]
        else:
            dice[5] = map_array[nx][ny]
            map_array[nx][ny] = 0

        x, y = nx, ny
        print(dice[0])