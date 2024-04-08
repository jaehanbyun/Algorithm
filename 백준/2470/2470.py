import sys

input = sys.stdin.readline

n = int(input())
sa = list(map(int, input().split()))

sa.sort()

gap = float('INF')
left, right = 0, n-1
answer = []

while left < right:
    tmp = sa[left] + sa[right]

    if abs(tmp) < gap:
        gap = abs(tmp)
        answer = [sa[left], sa[right]]

    if tmp < 0:
        left += 1
    else:
        right -= 1

print(*answer)