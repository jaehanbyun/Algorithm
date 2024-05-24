import sys
from itertools import combinations

input = sys.stdin.readline

def dfs(round):
    global rst

    if round == 15:
        rst = 1
        for item in record:
            if item.count(0) != 3:
                rst = 0
                break
        return

    g1, g2 = game[round]
    for x, y in ((2, 0), (1, 1), (0, 2)):
        if record[g1][x] > 0 and record[g2][y] > 0:
            record[g1][x] -= 1
            record[g2][y] -= 1
            dfs(round + 1)
            record[g1][x] += 1
            record[g2][y] += 1

game = list(combinations(range(6), 2))
answer = []

for i in range(4):
    record = list(map(int, input().split()))
    record = [record[i:i+3] for i in range(0, 16, 3)]
    rst = 0
    dfs(0)
    answer.append(rst)

print(*answer)