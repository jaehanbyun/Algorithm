import sys

input = sys.stdin.readline

N = int(input())
INF = int(1e9)
graph = []

for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = INF

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(N):
    for j in range(N):
        if graph[i][j] == INF:
            graph[i][j] = 0
        else:
            graph[i][j] = 1

for i in range(N):
    print(*graph[i])