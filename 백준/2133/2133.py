import sys

input = sys.stdin.readline

n = int(input())

if n % 2 == 1:
    print(0)
else:
    dp = [1] * (n+1)
    dp[2] = 3

    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * dp[2]
        for j in range(i-4, -1, -2):
            dp[i] += dp[j] * 2

    print(dp[n])