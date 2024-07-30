import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    file_size = list(map(int, input().split()))
    dp = [[0] * k for _ in range(k)]
    prefix_sum = [0] * (k + 1)

    for i in range(1, k + 1):
        prefix_sum[i] = prefix_sum[i - 1] + file_size[i - 1]

    for length in range(2, k + 1):
        for i in range(k - length + 1):
            j = i + length - 1
            dp[i][j] = 1e9
            for mid in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j] + prefix_sum[j + 1] - prefix_sum[i])

    print(dp[0][k - 1])
