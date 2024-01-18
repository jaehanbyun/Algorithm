import sys

input = sys.stdin.readline

N = int(input())
cost = [0]
for _ in range(N):
    red, green, blue = map(int, input().split())
    cost.append([red, green, blue])

for i in range(2, N+1):
    cost[i][0] += min(cost[i - 1][1], cost[i - 1][2])
    cost[i][1] += min(cost[i - 1][0], cost[i - 1][2])
    cost[i][2] += min(cost[i - 1][0], cost[i - 1][1])

print(min(*cost[-1]))