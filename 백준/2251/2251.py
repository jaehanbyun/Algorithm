import sys
from collections import deque

A, B, C = map(int, sys.stdin.readline().split())
visited = [[False for _ in range(B+1)] for _ in range(A+1)]
queue = deque()
queue.append([0, 0, C])
answer = []

def bfs():
    while queue:
        x, y, z = queue.popleft()

        if visited[x][y] == 1:
            continue

        visited[x][y] = 1

        if x == 0:
            answer.append(z)

        # A -> B
        water = min(x, B-y)
        queue.append([x-water, y+water, z])

        # A -> C
        water = min(x, C-z)
        queue.append([x-water, y, z+water])

        # B -> A
        water = min(A-x, y)
        queue.append([x+water, y-water, z])

        # B -> C
        water = min(y, C-z)
        queue.append([x, y-water, z+water])

        # C -> A
        water = min(A-x, z)
        queue.append([x+water, y, z-water])

        # C -> B
        water = min(B-y, z)
        queue.append([x, y+water, z-water])

bfs()
print(*sorted(answer))