import sys

input = sys.stdin.readline

n = int(input())
lines = []
dp = [1] * n

for _ in range(n):
    a, b = map(int, input().split())
    lines.append([a, b])

lines.sort()

for i in range(1, n):
    for j in range(i):
        if lines[j][1] < lines[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))