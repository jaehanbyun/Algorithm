import sys

input = sys.stdin.readline

N = int(input())
dp = [1] * (N+1)
dp[1] = 0
for n in range(4, N+1):
    f = dp[n-1] + 1
    s = dp[n//3] + 1 if n%3 == 0 else int(1e9)
    t = dp[n//2] + 1 if n%2 == 0 else int(1e9)
    dp[n] = min(f, s, t)

print(dp[N])