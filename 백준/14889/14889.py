import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
mates = [x for x in range(N)]
S = [list(map(int, input().split())) for _ in range(N)]
rst = 1e9

for team in combinations(mates, N//2):
    value1 = 0
    value2 = 0

    for a in team:
        for b in team:
            value1 += S[a][b]

    other_team = []
    for y in mates:
        if y not in team:
            other_team.append(y)

    for a in other_team:
        for b in other_team:
            value2 += S[a][b]

    rst = min(rst, abs(value1 - value2))

print(rst)