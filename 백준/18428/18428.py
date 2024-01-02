import sys
from itertools import combinations

N = int(sys.stdin.readline())
matrix = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
teacher_zones = []
obstacle_zones = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'T':
            teacher_zones.append([i, j])
        if matrix[i][j] == 'X':
            obstacle_zones.append([i, j])

def search():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    for t in teacher_zones:
        for i in range(4):
            nx, ny = t[0], t[1]

            while (0 <= nx < N) and (0 <= ny < N):
                if matrix[nx][ny] == 'O':
                    break
                if matrix[nx][ny] == 'S':
                    return False
                nx += dx[i]
                ny += dy[i]

    return True

# 모든 학생들을 감시로부터 피하도록 할 수 있는 경우가 존재하면 'YES' 출력 후 코드 종료,
# 어떤 경우에서도 감시로부터 피하도록 할 수 없다면 'NO' 출력
for obstacles in combinations(obstacle_zones, 3):
    for each_obstacle in obstacles:
        matrix[each_obstacle[0]][each_obstacle[1]] = 'O'
    if search():
        print('YES')
        exit()
    for each_obstacle in obstacles:
        matrix[each_obstacle[0]][each_obstacle[1]] = 'X'
print('NO')