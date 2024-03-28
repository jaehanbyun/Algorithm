import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin_set = set()
dp = [10001] * (k+1)
dp[0] = 0

for _ in range(n):
    coin_value = int(input())
    coin_set.add(coin_value)

value_set = list(coin_set)

for coin in coin_set:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])