import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur_v):
    visited.append(cur_v)

    for next_v in graph[cur_v]:
        if next_v not in visited:
            dfs(next_v)

N, M = map(int, input().split())
graph = defaultdict(list)
visited = []

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1, N+1):
    if i not in visited:
        dfs(i)
        count += 1

print(count)