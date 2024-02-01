import copy
import sys
from itertools import product

input = sys.stdin.readline

def watch(d, x, y):
    d %= 4
    while True:
        x += direction[d][0]
        y += direction[d][1]

        if x < 0 or x >= N or y < 0 or y >= M or office2[x][y] == 6:
            return

        if office2[x][y] != 0:
            continue

        office2[x][y] = 7

N, M = map(int, input().split())
office1 = [list(map(int, input().split())) for _ in range(N)]
cctvs = []

zn = 0
for i in range(N):
    for j in range(M):
        if office1[i][j] == 0:
            zn += 1
        if 0 < office1[i][j] < 6:
            cctvs.append([i, j, office1[i][j]])

possible_case = []
for i in product([0, 1, 2, 3], repeat=len(cctvs)):
    possible_case.append(i)

# 북, 동, 남, 서
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for p in possible_case:
    office2 = copy.deepcopy(office1)

    for i, v in enumerate(cctvs):
        x, y, t = v[0], v[1], v[2]
        if t == 1:
            watch(p[i], x, y)
        elif t == 2:
            watch(p[i], x, y)
            watch(p[i]+2, x, y)
        elif t == 3:
            watch(p[i], x, y)
            watch(p[i]+1, x, y)
        elif t == 4:
            watch(p[i], x, y)
            watch(p[i] + 1, x, y)
            watch(p[i] + 2, x, y)
        else:
            watch(p[i], x, y)
            watch(p[i] + 1, x, y)
            watch(p[i] + 2, x, y)
            watch(p[i] + 3, x, y)

    value = 0
    for i in range(N):
        for j in range(M):
            if office2[i][j] == 0:
                value += 1

    zn = min(zn, value)

print(zn)