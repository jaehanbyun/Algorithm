import sys

input = sys.stdin.readline

# 유저 수, 친구 수
N, M = map(int, input().split())
graph = [[int(1e9)] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

total_count = [int(1e9)] * (N+1)

for i in range(1, N+1):
    count = 0
    for j in range(1, N+1):
        if graph[i][j] != int(1e9):
            count += graph[i][j]
    total_count[i] = count

print(total_count.index(min(total_count)))