import sys

input = sys.stdin.readline

# 피보나치 수 점화식 : f(n) = f(n-1) + f(n-2)
def solution(n):
    dp = [0] * (n+1)
    if n == 0:
        print(dp.count(0), dp.count(1))
        return
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[-2], dp[-1])
    return

T = int(input())

for _ in range(T):
    N = int(input())
    solution(N)