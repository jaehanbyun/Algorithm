import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        next_node = queue.popleft()

        for idx, v in enumerate(graph[next_node]):
            if not visited[idx] and v == 1:
                queue.append(idx)
                visited[idx] = True

n = int(input())
m = int(input())
graph = []
visited = [False] * n

for _ in range(n):
    graph.append(list(map(int, input().split())))

plan = list(map(int, input().split()))

bfs(plan[0]-1)

flag = True
for p in plan:
    if not visited[p-1]:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')