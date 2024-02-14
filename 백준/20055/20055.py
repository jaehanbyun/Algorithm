import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
A = deque(list(map(int, input().split())))
robots = deque([0] * N)
stage = 0

while True:
    stage += 1

    # step 1
    A.rotate(1)
    robots[-1] = 0
    robots.rotate(1)
    robots[-1] = 0

    # step 2
    for i in range(N-2, -1, -1):
        if robots[i+1] == 0 and robots[i] == 1 and A[i+1] >= 1:
            robots[i+1] = 1
            robots[i] = 0
            A[i+1] -= 1

    robots[-1] = 0

    # step 3
    if A[0] != 0:
        robots[0] = 1
        A[0] -= 1

    # step 4
    if A.count(0) >= K:
        break

print(stage)