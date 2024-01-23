import sys
import bisect

input = sys.stdin.readline

N = int(input())
U = []
two_sum = []

for _ in range(N):
    U.append(int(input()))

U = list(set(U))
U.sort()

for i in range(N):
    for j in range(N):
        two_sum.append(U[i]+U[j])

two_sum.sort()
len_two_sum = len(two_sum)

for i in range(N-1, -1, -1):
    for j in range(i):
        num = U[i] - U[j]
        index = bisect.bisect_left(two_sum, num)
        if index < len_two_sum and two_sum[index] == num:
            print(U[i])
            exit()