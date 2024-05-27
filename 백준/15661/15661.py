import sys
from itertools import combinations

input = sys.stdin.readline

def cal(team):
    score = 0

    for i in team:
        for j in team:
            if i != j:
                score += matrix[i][j]

    return score

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9
all_team = set(range(n))

for i in range(1, (n//2) + 1):
    for team in combinations(range(n), i):
        start = set(team)
        link = all_team - start

        start_score = cal(start)
        link_score = cal(link)

        ans = min(ans, abs(start_score - link_score))

print(ans)