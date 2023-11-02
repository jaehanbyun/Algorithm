import sys
from collections import deque

def bfs(n1, n2):
    visit = [False] * (N+1)
    visit[n1] = True
    q = deque()
    q.append((n1, 0))

    while q:
        cur_node, cur_len = q.popleft()

        if cur_node == n2:
            return cur_len

        for node, l in G[cur_node]:
            if visit[node] == False:
                visit[node] = True
                q.append((node, cur_len + l))

N, M = map(int, sys.stdin.readline().split())
G = [[] for _ in range(N+1)]

for _ in range(N-1):
    n1, n2, l = map(int, sys.stdin.readline().split())
    G[n1].append((n2, l))
    G[n2].append((n1, l))

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    print(bfs(n1, n2))