import sys
from collections import deque

N = int(sys.stdin.readline())

f, s = 0, 0

arr = [[] for _ in range(N+1)]
score = []

while True:
    f, s = map(int, sys.stdin.readline().strip().split())
    if f == -1 and s == -1:
        break
    arr[f].append(s)
    arr[s].append(f)

def bfs(num, visited):
    dQ = deque([num])
    visited[num] = True

    while dQ:
        f = dQ.popleft()

        for i in arr[f]:
            if not visited[i]:
                dQ.append(i)
                visited[i] = True
                dist[i] = dist[f]+1

M = 99999

for i in range(1, N+1):
    visited = [False for _ in range(N + 1)]
    visited[i] = True
    dist = [0 for _ in range(N+1)]
    bfs(i, visited)
    cnt = max(dist)
    if cnt < M:
        score = [i]
        M = cnt
    elif cnt == M:
        score.append(i)

print(f'{M} {len(score)}')
for it in score:
    print(it, end=' ')