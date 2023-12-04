import sys

N, K = map(int, sys.stdin.readline().split())

# k/n 1 2 3 4
# 1   1 1 1 1
# 2   2 3 4 5
# 3   3 6 10 15
# 4   4 10 20 35

# dp[k][n] = dp[k-1][n] + dp[k][n-1]

dp_array = [[0 for _ in range(N+1)] for _ in range(K+1)]

for k in range(1, K+1):
    dp_array[k][1] = k
    for n in range(2, N+1):
        dp_array[k][n] = dp_array[k-1][n] + dp_array[k][n-1]

print(dp_array[K][N]%1000000000)