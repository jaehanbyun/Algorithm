import sys

input = sys.stdin.readline

h, w = map(int, input().split())
block_heights = list(map(int, input().split()))
answer = 0

for i in range(1, w-1):
    left = max(block_heights[:i])
    right = max(block_heights[i+1:])
    m = min(left, right)

    if m > block_heights[i]:
        answer += m - block_heights[i]

print(answer)