import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp_asc = [1] * n
dp_des = [1] * n
dp = [0] * n

for a in range(1, n):
    for b in range(a):
        if A[a] > A[b]:
            dp_asc[a] = max(dp_asc[a], dp_asc[b] + 1)

A.reverse()

for a in range(1, n):
    for b in range(a):
        if A[a] > A[b]:
            dp_des[a] = max(dp_des[a], dp_des[b] + 1)

dp_des.reverse()
for i in range(n):
    dp[i] = dp_asc[i] + dp_des[i] - 1

print(max(dp))