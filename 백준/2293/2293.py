import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
dp_array = [0] * (k+1)
dp_array[0] = 1

for _ in range(n):
    coins.append(int(sys.stdin.readline()))

for coin in coins:
    for i in range(coin, k+1):
        dp_array[i] += dp_array[i-coin]

print(dp_array[k])