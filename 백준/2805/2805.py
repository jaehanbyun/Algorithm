import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)

while start <= end:
    sum = 0
    mid = (start + end) // 2

    for t in trees:
        if t > mid:
            sum += t - mid

    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)