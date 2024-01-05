import sys

input = sys.stdin.readline

N = int(input())
child_line = list(map(int, input().split()))

child_line.insert(0, 0)

child_position = [0] * (N+1)
for i in range(1, N+1):
    child_position[child_line[i]] = i

cnt = 1
num = -1
for n in range(1, N):
    if child_position[n] < child_position[n+1]:
        cnt += 1
    else:
        num = max(num, cnt)
        cnt = 1

print(N-num if num != -1 else 0)
