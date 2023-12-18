# 정답

import sys
from itertools import combinations

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

for chick_array in combinations(chick, M):
    total_distance = 0
    for x, y in house:
        distance = float('inf')
        for each_chick in chick_array:
            temp_distance = abs(x - each_chick[0]) + abs(y - each_chick[1])
            distance = min(distance, temp_distance)
        total_distance += distance

    min_distance = min(min_distance, total_distance)

print(min_distance)
