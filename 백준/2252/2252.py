import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
in_degree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

answer = []
queue = deque()

for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    cur_student = queue.popleft()
    answer.append(cur_student)

    for adj_student in graph[cur_student]:
        in_degree[adj_student] -= 1
        if in_degree[adj_student] == 0:
            queue.append(adj_student)

print(*answer)