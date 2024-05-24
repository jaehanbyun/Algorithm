import sys
from collections import deque

input = sys.stdin.readline

def bfs(n, d):
    queue = deque()
    queue.append(n)
    visited[n] = 1

    while queue:
        pos = queue.popleft()

        if pos == d:
            return

        for i, next_pos in enumerate([pos-1, pos+1, pos*2]):
            if next_pos < 0 or next_pos > 100000:
                continue

            if visited[next_pos] == 0:
                if i != 2:
                    cost[next_pos] = cost[pos] + 1
                else:
                    cost[next_pos] = cost[pos]

                queue.append(next_pos)
                visited[next_pos] = 1
            else:
                if i != 2:
                    cost[next_pos] = min(cost[next_pos], cost[pos] + 1)
                else:
                    cost[next_pos] = min(cost[next_pos], cost[pos])

n, k = map(int, input().split())
visited = [0] * 100001
cost = [0] * 100001

bfs(n, k)
print(cost[k])