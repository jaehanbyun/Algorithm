# 시간초과

import sys

N, M = map(int, sys.stdin.readline().split())
city_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_distance = float('inf')
house = []
chick = []

for i in range(N):
    for j in range(N):
        if city_map[i][j] == 1:
            house.append([i, j])
        if city_map[i][j] == 2:
            chick.append([i, j])

visited = [False] * len(chick)
def backtracking(index, count):
    global min_distance

    if count == M:
        total_distance = 0

        for x, y in house:
            distance = float('inf')
            for i in range(len(chick)):
                if visited[i]:
                    num = abs(x - chick[i][0]) + abs(y - chick[i][1])
                    distance = min(num, distance)
            total_distance += distance
            if total_distance >= min_distance:
                return

        min_distance = min(min_distance, total_distance)
        return

    for i in range(index, len(chick)):
        if not visited[i]:
            visited[i] = True
            backtracking(index+1, count+1)
            visited[i] = False

backtracking(0, 0)

print(min_distance)